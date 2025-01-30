from datetime import datetime

from pydantic import BaseModel


class TronInfoRequest(BaseModel):
    address: str


class TronInfoResponse(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance: float


class WalletRequestResponse(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance: float
    created_at: datetime

    class Config:
        orm_mode = True


class PaginatedResponse(BaseModel):
    items: list[WalletRequestResponse]
    total: int
    skip: int
    limit: int
