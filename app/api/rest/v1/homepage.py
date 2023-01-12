from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends

from app.api.rest.context import RequestContext
from app.common import responses
from app.common.errors import ServiceError
from app.common.responses import Success
from app.models.homepage import HomepageStats
from app.usecases import online
from app.usecases import score

router = APIRouter()


@router.get("/statistics/homepage", response_model=Success[HomepageStats])
async def get_homepage_statistics(
    ctx: RequestContext = Depends(),
):

    top_scores = []
    for mode in range(8):
        top_score_data = await score.fetch_one(ctx, mode)

        if isinstance(top_score_data, ServiceError):
            return responses.failure(
                top_score_data,
                "Failed to fetch top score.",
                status_code=200,
            )

        top_scores.append(top_score_data)

    online_history_data = await online.fetch_many(ctx)
    if isinstance(online_history_data, ServiceError):
        return responses.failure(
            online_history_data,
            "Failed to fetch online history.",
            status_code=200,
        )

    data = HomepageStats.from_mapping(
        {"online_history": online_history_data, "top_scores": top_scores},
    )
    return responses.success(data)
