from __future__ import annotations

from typing import Any
from typing import Mapping

from pydantic import BaseModel


class UserInfo(BaseModel):
    privileges: int
    country: str

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> UserInfo:
        return cls(
            privileges=mapping["privileges"],
            country=mapping["country"],
        )
