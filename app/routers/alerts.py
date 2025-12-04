# app/routers/alerts.py

from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app import models
from app.schemas import alerts as alert_schemas

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.post(
    "",
    response_model=alert_schemas.Alert,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new price alert",
)
def create_alert(
    payload: alert_schemas.AlertCreate,
    db: Session = Depends(get_db),
) -> alert_schemas.Alert:
    alert = models.Alert(
        symbol=payload.symbol.upper(),
        target_price=payload.target_price,
        direction=payload.direction,  # same values as models.AlertDirection
    )
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert


@router.get(
    "",
    response_model=List[alert_schemas.Alert],
    summary="List all active alerts",
)
def list_alerts(
    db: Session = Depends(get_db),
) -> List[alert_schemas.Alert]:
    alerts = (
        db.query(models.Alert)
        .filter(models.Alert.is_active.is_(True))
        .order_by(models.Alert.created_at.desc())
        .all()
    )
    return alerts


@router.get(
    "/{alert_id}",
    response_model=alert_schemas.Alert,
    summary="Get a single alert by id",
)
def get_alert(
    alert_id: int,
    db: Session = Depends(get_db),
) -> alert_schemas.Alert:
    alert = db.query(models.Alert).filter(models.Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Alert {alert_id} not found",
        )
    return alert


@router.delete(
    "/{alert_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an alert by id",
)
def delete_alert(
    alert_id: int,
    db: Session = Depends(get_db),
) -> None:
    alert = db.query(models.Alert).filter(models.Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Alert {alert_id} not found",
        )
    db.delete(alert)
    db.commit()


@router.post(
    "/check",
    response_model=List[alert_schemas.TriggeredAlert],
    summary="Check which alerts would trigger for given prices",
)
def check_alerts(
    payload: alert_schemas.AlertCheckRequest,
    db: Session = Depends(get_db),
) -> List[alert_schemas.TriggeredAlert]:
    # Map of SYMBOL -> current price coming from the client
    price_map: Dict[str, float] = {
        p.symbol.upper(): p.price for p in payload.prices
    }

    alerts = (
        db.query(models.Alert)
        .filter(models.Alert.is_active.is_(True))
        .all()
    )

    triggered: List[alert_schemas.TriggeredAlert] = []

    for alert in alerts:
        current_price = price_map.get(alert.symbol)
        if current_price is None:
            continue

        target_price = float(alert.target_price)

        if (
            alert.direction == models.AlertDirection.ABOVE
            and current_price >= target_price
        ):
            triggered.append(
                alert_schemas.TriggeredAlert(
                    alert=alert,
                    current_price=current_price,
                )
            )
        elif (
            alert.direction == models.AlertDirection.BELOW
            and current_price <= target_price
        ):
            triggered.append(
                alert_schemas.TriggeredAlert(
                    alert=alert,
                    current_price=current_price,
                )
            )

    return triggered
