from fastapi import FastAPI

from app.database import Base, engine
from app.routers import requests, tron

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(tron.router)
app.include_router(requests.router)


@app.get("/")
def read_root():
    return {"message": "Tron Info Service"}
