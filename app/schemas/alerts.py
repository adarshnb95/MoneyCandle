# app/schemas/alerts.py

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict

class AlertDirection(str, Enum):
    ABOVE = "above"
    BELOW = "below"


class AlertCreate(BaseModel):
    symbol: str = Field(..., description="Ticker symbol, for example AAPL")
    target_price: float = Field(..., gt=0, description="Target price for the alert")
    direction: AlertDirection = Field(..., description="above or below")


class Alert(BaseModel):
    id: int
    symbol: str
    target_price: float
    direction: AlertDirection
    created_at: datetime

    # Pydantic v2 style – replaces orm_mode = True
    model_config = ConfigDict(from_attributes=True)

class PriceSnapshot(BaseModel):
    symbol: str
    price: float


class AlertCheckRequest(BaseModel):
    prices: list[PriceSnapshot]


class TriggeredAlert(BaseModel):
    alert: Alert
    current_price: float
