from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import crud

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def test_create_wallet_request(test_db, client):
    db = TestingSessionLocal()

    request_data = {
        "address": "TXYZopYRdj2D9XRtbG411X9RuRxWQk8y3C",
        "balance": 100.5,
        "bandwidth": 1500,
        "energy": 300,
    }

    db_request = crud.create_wallet_request(db, **request_data)

    assert db_request.address == request_data["address"]
    assert db_request.balance == request_data["balance"]
    assert db_request.bandwidth == request_data["bandwidth"]
    assert db_request.energy == request_data["energy"]
