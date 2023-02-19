from sqlalchemy import Column, Sequence, String, Date, Integer

from app.models.base_models import BaseOrmModel


class ExhausterMetadataModel(BaseOrmModel):
    __tablename__ = "exsgauter_metadata"
    __table_args__ = {"schema": "catalogs"}

    id_seq = Sequence("exsgauter_metadata_id_seq")

    exhauster_name = Column(String(50), nullable=False)
    rotor_instalation = Column(Date, nullable=False)
    rotor_number = Column(Integer, nullable=False)
    sinter_machine_name = Column(String(20), nullable=False)
