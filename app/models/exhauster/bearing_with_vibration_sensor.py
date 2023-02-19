from sqlalchemy import Column, Sequence, Integer, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM
from enum import Enum

from app.models.base_models import BaseOrmModel


class SensorStatusesEnum(str, Enum):
    ok = "ok"
    warning = "warning"
    alert = "alert"
    no_data = "no_data"


class BearingWithVibrationSensorModel(BaseOrmModel):
    __tablename__ = "bearing_with_vibration_sensor"
    __table_args__ = {"schema": "service_all"}

    id_seq = Sequence("bearing_with_vibration_sensor_id_seq")

    temperature_id = Column(
        Integer, ForeignKey("service_all.sensor.id"), nullable=False
    )
    axial_vibration_id = Column(
        Integer, ForeignKey("service_all.sensor.id"), nullable=False
    )
    horizontal_vibration_id = Column(
        Integer, ForeignKey("service_all.sensor.id"), nullable=False
    )
    vertical_vibration_id = Column(
        Integer, ForeignKey("service_all.sensor.id"), nullable=False
    )
    number = Column(SmallInteger, nullable=False)
    temperature_status = Column(ENUM(SensorStatusesEnum), nullable=False)
    vibration_status = Column(ENUM(SensorStatusesEnum), nullable=False)

    temperature = relationship("SensorModel", foreign_keys=[temperature_id])
    axial_vibration = relationship("SensorModel", foreign_keys=[axial_vibration_id])
    horizontal_vibration = relationship(
        "SensorModel", foreign_keys=[horizontal_vibration_id]
    )
    vertical_vibration = relationship(
        "SensorModel", foreign_keys=[vertical_vibration_id]
    )
