from __future__ import annotations

from app.common.context import Context


class OnlineHistoryRepo:

    REDIS_KEY = "statistik:online:history"

    def __init__(self, ctx: Context) -> None:
        self.ctx = ctx

    async def fetch_many(
        self,
    ) -> list[int] | None:

        counts = await self.ctx.redis.lrange(self.REDIS_KEY, 0, -1)

        if counts is None:
            return None

        return [int(count) for count in counts]
