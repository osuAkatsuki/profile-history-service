from __future__ import annotations

from fastapi import APIRouter

from . import homepage
from . import pp
from . import rank


router = APIRouter(prefix="/api/v1")

router.include_router(rank.router, tags=["rank"])
router.include_router(pp.router, tags=["pp"])

router.include_router(homepage.router, tags=["homepage"])
