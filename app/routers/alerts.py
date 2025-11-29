# routers/alerts.py

from datetime import datetime
from itertools import count
from threading import Lock
from typing import Dict, List

from fastapi import APIRouter, HTTPException, status

from app.schemas.alerts import (
    Alert,
    AlertCreate,
    AlertCheckRequest,
    TriggeredAlert,
    AlertDirection,
)

router = APIRouter(prefix="/alerts", tags=["alerts"])


# In memory store for now. Later we can swap this out for a DB layer.
_alerts: Dict[int, Alert] = {}
_id_counter = count(1)
_lock = Lock()


@router.post(
    "",
    response_model=Alert,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new price alert",
)
def create_alert(payload: AlertCreate) -> Alert:
    alert_id = next(_id_counter)
    alert = Alert(
        id=alert_id,
        symbol=payload.symbol.upper(),
        target_price=payload.target_price,
        direction=payload.direction,
        created_at=datetime.utcnow(),
    )
    with _lock:
        _alerts[alert_id] = alert
    return alert


@router.get(
    "",
    response_model=List[Alert],
    summary="List all active alerts",
)
def list_alerts() -> List[Alert]:
    with _lock:
        return list(_alerts.values())


@router.delete(
    "/{alert_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an alert by id",
)
def delete_alert(alert_id: int) -> None:
    with _lock:
        if alert_id not in _alerts:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Alert {alert_id} not found",
            )
        del _alerts[alert_id]


@router.post(
    "/check",
    response_model=List[TriggeredAlert],
    summary="Check which alerts would trigger for given prices",
)
def check_alerts(payload: AlertCheckRequest) -> List[TriggeredAlert]:
    price_map = {p.symbol.upper(): p.price for p in payload.prices}
    triggered: List[TriggeredAlert] = []

    with _lock:
        for alert in _alerts.values():
            current_price = price_map.get(alert.symbol)
            if current_price is None:
                continue

            if alert.direction == AlertDirection.ABOVE and current_price >= alert.target_price:
                triggered.append(TriggeredAlert(alert=alert, current_price=current_price))
            elif alert.direction == AlertDirection.BELOW and current_price <= alert.target_price:
                triggered.append(TriggeredAlert(alert=alert, current_price=current_price))

    return triggered
