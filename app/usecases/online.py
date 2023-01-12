from __future__ import annotations

from app.common.context import Context
from app.common.errors import ServiceError
from app.repositories.online import OnlineHistoryRepo


async def fetch_many(
    ctx: Context,
) -> list[int] | ServiceError:
    r_repo = OnlineHistoryRepo(ctx)
    resp = await r_repo.fetch_many()

    if resp is None:
        return ServiceError.ONLINE_NOT_FOUND

    return resp
