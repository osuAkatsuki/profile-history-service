from __future__ import annotations

from typing import Any

import orjson

from app.common.context import Context

redis_map = {
    0: ("vn", "std"),
    1: ("vn", "taiko"),
    2: ("vn", "ctb"),
    3: ("vn", "mania"),
    4: ("rx", "std"),
    5: ("rx", "taiko"),
    6: ("rx", "ctb"),
    7: ("ap", "std"),
}


class TopScoreRepo:

    REDIS_KEY = "statistik:cache:top:{}:{}"

    def __init__(self, ctx: Context) -> None:
        self.ctx = ctx

    async def fetch_one(self, mode: int) -> dict[str, Any] | None:

        (c_mode_name, mode_name) = redis_map[mode]
        key = self.REDIS_KEY.format(c_mode_name, mode_name)

        raw_data = await self.ctx.redis.get(key)

        if raw_data is None:
            return None

        return orjson.loads(raw_data)
