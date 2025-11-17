from fastapi import FastAPI
from app.api.v1.stocks import router as stocks_router

app = FastAPI(title="MoneyCandle")

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(stocks_router, prefix="/api/v1/stocks", tags=["stocks"])
