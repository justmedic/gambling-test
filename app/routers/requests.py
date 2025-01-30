from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter()


@router.get("/requests", response_model=schemas.PaginatedResponse)
def get_requests(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    db: Session = Depends(get_db),  # noqa: FAST002, B008
):
    total = db.query(models.WalletRequest).count()
    requests = (
        db.query(models.WalletRequest)
        .order_by(models.WalletRequest.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {"items": requests, "total": total, "skip": skip, "limit": limit}
