from sqlalchemy import Column, Sequence, Numeric

from app.models.base_models import BaseOrmModel


class ValvePositionModel(BaseOrmModel):
    __tablename__ = "valve_position"
    __table_args__ = {"schema": "service_all"}

    id_seq = Sequence("valve_position_id_seq")

    gas_valve_closed = Column(Numeric(5, 2))
    gas_valve_open = Column(Numeric(5, 2))
    gas_valve_position = Column(Numeric(5, 2))
