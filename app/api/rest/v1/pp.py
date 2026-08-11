from __future__ import annotations

import datetime

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response

from app.api.rest.context import RequestContext
from app.common import responses
from app.common.errors import ServiceError
from app.common.responses import Success
from app.models.pp import PPHistory
from app.usecases import pp
from app.usecases import user
from app.usecases import validation

router = APIRouter()


@router.get("/pp", response_model=Success[PPHistory])
async def get_profile_pp_history(
    user_id: int,
    mode: int,
    ctx: RequestContext = Depends(),
) -> Response:
    data = await pp.fetch_many(ctx, user_id, mode)
    user_data = await user.fetch_one(ctx, user_id, mode)

    if isinstance(user_data, ServiceError):
        return responses.failure(
            user_data,
            "Failed to fetch user data.",
            status_code=200,
        )

    if validation.is_restricted(user_data.privileges):
        return responses.failure(
            ServiceError.USERS_IS_RESTRICTED,
            "User is restricted.",
            status_code=200,
        )

    if validation.is_not_active(user_data.latest_pp_awarded):
        return responses.failure(
            ServiceError.USERS_IS_NOT_ACTIVE,
            "User is not active.",
            status_code=200,
        )

    # Only append live PP if there's no snapshot for today yet.
    # This avoids mixing data sources (MySQL live vs MySQL historical).
    today = datetime.date.today()
    has_today_snapshot = data.captures and data.captures[-1].captured_at.date() == today

    if not has_today_snapshot:
        current_pp_capture = await pp.fetch_current(ctx, user_id, mode)

        if current_pp_capture:
            data.captures.append(current_pp_capture)

    return responses.success(data)
