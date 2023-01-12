from __future__ import annotations

from typing import Union

from app.common.context import Context
from app.common.errors import ServiceError
from app.models.user import UserInfo
from app.repositories.user import UsersRepo


async def fetch_one(
    ctx: Context,
    user_id: int,
) -> Union[UserInfo, ServiceError]:
    r_repo = UsersRepo(ctx)
    resp = await r_repo.fetch_one(user_id)

    if resp is None:
        return ServiceError.USERS_NOT_FOUND

    return UserInfo.from_mapping(resp)
