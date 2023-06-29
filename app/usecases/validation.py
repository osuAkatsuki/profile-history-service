from __future__ import annotations

import time


def is_restricted(privileges: int) -> bool:
    return privileges & 1 == 0


def is_not_active(last_active: int) -> bool:

    delta_time = int(time.time()) - last_active
    days = delta_time / 60 / 60 / 24
    return days > 60
