from __future__ import annotations

from typing import Any

from app.common.context import Context
from app.common.errors import ServiceError
from app.models.homepage import TopScore
from app.repositories.score import TopScoreRepo


async def fetch_one(
    ctx: Context,
    mode: int,
) -> dict[str, Any] | ServiceError:
    r_repo = TopScoreRepo(ctx)
    resp = await r_repo.fetch_one(mode)

    if resp is None:
        return ServiceError.TOP_SCORE_NOT_FOUND

    return resp
