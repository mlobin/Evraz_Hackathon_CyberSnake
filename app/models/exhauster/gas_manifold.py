from sqlalchemy import Column, Sequence, Numeric

from app.models.base_models import BaseOrmModel


class GasManifoldModel(BaseOrmModel):
    __tablename__ = "gas_manifold"
    __table_args__ = {"schema": "service_all"}

    id_seq = Sequence("gas_manifold_id_seq")

    temperature_before = Column(Numeric(5, 2))
    underpressure_before = Column(Numeric(5, 2))
