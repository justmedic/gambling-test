from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from .database import Base


class WalletRequest(Base):
    __tablename__ = "wallet_requests"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    balance = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
