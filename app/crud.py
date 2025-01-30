from sqlalchemy.orm import Session

from . import models


def create_wallet_request(db: Session, address: str, balance: float, bandwidth: int, energy: int):
    db_request = models.WalletRequest(
        address=address, balance=balance, bandwidth=bandwidth, energy=energy
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request
