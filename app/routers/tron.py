from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.dependencies import TronClient

router = APIRouter()


@router.post("/tron-info", response_model=schemas.TronInfoResponse)
async def get_tron_info(
    request: schemas.TronInfoRequest,
    db: Annotated[Session, Depends(get_db)],
    tron_client: Annotated[TronClient, Depends()],
):
    try:
        account_info = tron_client.get_account_info(request.address)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    crud.create_wallet_request(
        db,
        request.address,
        account_info["balance"],
        account_info["bandwidth"],
        account_info["energy"],
    )

    return {"address": request.address, **account_info}
