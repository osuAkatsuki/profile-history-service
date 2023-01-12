from __future__ import annotations

import datetime
from typing import Any
from typing import Mapping

from pydantic import BaseModel


class HomepageStats(BaseModel):
    online_history: list[int]
    top_scores: list[TopScore]

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> HomepageStats:

        return cls(
            online_history=mapping["online_history"],
            top_scores=[
                TopScore.from_mapping(score) for score in mapping["top_scores"]
            ],
        )


class TopScore(BaseModel):
    user_id: int
    username: str
    pp_val: int
    time: datetime.datetime
    beatmap_id: int
    beatmapset_id: int

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> TopScore:

        return cls(
            user_id=mapping["user_id"],
            username=mapping["username"],
            pp_val=mapping["pp_val"],
            time=datetime.datetime.fromtimestamp(int(mapping["time"])),
            beatmap_id=mapping["beatmap_id"],
            beatmapset_id=mapping["beatmapset_id"],
        )


# Stupid hack.
HomepageStats.update_forward_refs()
