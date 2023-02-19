from sqlalchemy import Column, Sequence, Numeric

from app.models.base_models import BaseOrmModel


class OilSystemModel(BaseOrmModel):
    __tablename__ = "oil_system"
    __table_args__ = {"schema": "service_all"}

    id_seq = Sequence("oil_system_id_seq")

    oil_level = Column(Numeric(5, 2))
    oil_pressure = Column(Numeric(5, 2))
