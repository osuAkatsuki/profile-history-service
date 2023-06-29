from __future__ import annotations

from enum import Enum


class ServiceError(str, Enum):
    USERS_NOT_FOUND = "users.not_found"
    USERS_IS_RESTRICTED = "users.is_restricted"
    USERS_IS_NOT_ACTIVE = "users.is_not_active"
    RANKS_NOT_FOUND = "ranks.not_found"
    PP_NOT_FOUND = "pp.not_found"
    ONLINE_NOT_FOUND = "online.not_found"
    TOP_SCORE_NOT_FOUND = "top_score.not_found"
    PEAK_RANK_NOT_FOUND = "peak_rank.not_found"
