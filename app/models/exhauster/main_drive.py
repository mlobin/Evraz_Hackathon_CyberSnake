from sqlalchemy import Column, Sequence, Numeric

from app.models.base_models import BaseOrmModel


class MainDriveModel(BaseOrmModel):
    __tablename__ = "main_drive"
    __table_args__ = {"schema": "service_all"}

    id_seq = Sequence("main_drive_id_seq")

    rotor_current = Column(Numeric(6, 2))
    rotor_voltage = Column(Numeric(6, 2))
    stator_current = Column(Numeric(6, 2))
    stator_voltage = Column(Numeric(6, 2))
