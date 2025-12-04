from fastapi import FastAPI

from app.db import init_db
from app.routers import alerts

app = FastAPI(
    title="MoneyCandle API",
    version="0.1.0",
    description="Stock alerts and volatility API",
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


app.include_router(alerts.router)


@app.get("/health")
def health():
    return {"status": "ok"}
