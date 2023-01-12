from __future__ import annotations


def is_restricted(privileges: int) -> bool:
    return privileges & 1 == 0
