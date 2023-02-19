from sqlalchemy import Column, Sequence, Numeric
from sqlalchemy.dialects.postgresql import ENUM
from enum import Enum

from app.models.base_models import BaseOrmModel


class SensorTypesEnum(str, Enum):
    temperature = "temperature"
    vibration = "vibration"


class SensorModel(BaseOrmModel):
    __tablename__ = "sensor"
    __table_args__ = {"schema": "service_all"}

    id_seq = Sequence("sensor_id_seq")

    value = Column(Numeric(5, 2))
    alarm_max = Column(Numeric(5, 2))
    alarm_min = Column(Numeric(5, 2))
    warning_max = Column(Numeric(5, 2))
    warning_min = Column(Numeric(5, 2))
    type = Column(ENUM(SensorTypesEnum), nullable=False)
