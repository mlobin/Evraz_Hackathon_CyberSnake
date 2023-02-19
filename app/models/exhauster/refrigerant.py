from sqlalchemy import Column, Sequence, Numeric

from app.models.base_models import BaseOrmModel


class RefrigerantModel(BaseOrmModel):
    __tablename__ = "refrigerant"
    __table_args__ = {"schema": "service_all"}

    id_seq = Sequence("refrigerant_id_seq")

    water_temperature_after = Column(Numeric(5, 2))
    water_temperature_before = Column(Numeric(5, 2))
    oil_temperature_after = Column(Numeric(5, 2))
    oil_temperature_before = Column(Numeric(5, 2))
