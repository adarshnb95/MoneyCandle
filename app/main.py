from fastapi import FastAPI

from .routers import alerts  # adjust path if needed

app = FastAPI(
    title="MoneyCandle API",
    version="0.1.0",
    description="Stock alerts and volatility API",
)

app.include_router(alerts.router)


@app.get("/health")
def health():
    return {"status": "ok"}
