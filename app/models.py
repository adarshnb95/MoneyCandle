# app/models.py

from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum as SAEnum,
    Integer,
    Numeric,
    String,
)

from app.db import Base


class AlertDirection(str, Enum):
    ABOVE = "above"
    BELOW = "below"


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False, index=True)
    target_price = Column(Numeric(18, 4), nullable=False)
    direction = Column(SAEnum(AlertDirection, name="alert_direction"), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )
