from sqlalchemy import Column, Sequence, Integer, SmallInteger, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from app.models.base_models import BaseOrmModel


class ExhausterModel(BaseOrmModel):
    __tablename__ = "exhauster"
    __table_args__ = {"schema": "service_all"}

    id_seq = Sequence("exhauster_id_seq")

    meta_id = Column(
        Integer,
        ForeignKey("catalogs.exsgauter_metadata.id"),
        nullable=False,
    )
    refrigerant_id = Column(
        Integer,
        ForeignKey("service_all.refrigerant.id"),
        nullable=False,
    )
    gas_manifold_id = Column(
        Integer,
        ForeignKey("service_all.gas_manifold.id"),
        nullable=False,
    )
    valve_position_id = Column(
        Integer,
        ForeignKey("service_all.valve_position.id"),
        nullable=False,
    )
    main_drive_id = Column(
        Integer,
        ForeignKey("service_all.main_drive.id"),
        nullable=False,
    )
    oil_system_id = Column(
        Integer,
        ForeignKey("service_all.oil_system.id"),
        nullable=False,
    )
    bearing_with_vibration_sensor_1_id = Column(
        Integer,
        ForeignKey("service_all.bearing_with_vibration_sensor.id"),
        nullable=False,
    )
    bearing_with_vibration_sensor_2_id = Column(
        Integer,
        ForeignKey("service_all.bearing_with_vibration_sensor.id"),
        nullable=False,
    )
    bearing_with_vibration_sensor_7_id = Column(
        Integer,
        ForeignKey("service_all.bearing_with_vibration_sensor.id"),
        nullable=False,
    )
    bearing_with_vibration_sensor_8_id = Column(
        Integer,
        ForeignKey("service_all.bearing_with_vibration_sensor.id"),
        nullable=False,
    )
    bearing_without_vibration_sensor_3_id = Column(
        Integer,
        ForeignKey("service_all.bearing_without_vibration_sensor.id"),
        nullable=False,
    )
    bearing_without_vibration_sensor_4_id = Column(
        Integer,
        ForeignKey("service_all.bearing_without_vibration_sensor.id"),
        nullable=False,
    )
    bearing_without_vibration_sensor_5_id = Column(
        Integer,
        ForeignKey("service_all.bearing_without_vibration_sensor.id"),
        nullable=False,
    )
    bearing_without_vibration_sensor_6_id = Column(
        Integer,
        ForeignKey("service_all.bearing_without_vibration_sensor.id"),
        nullable=False,
    )
    bearing_without_vibration_sensor_9_id = Column(
        Integer,
        ForeignKey("service_all.bearing_without_vibration_sensor.id"),
        nullable=False,
    )
    loaded_from_kafka_at = Column(TIMESTAMP, nullable=False)
    is_active = Column(SmallInteger, nullable=False)

    meta = relationship("ExhausterMetadataModel")
    refrigerant = relationship("RefrigerantModel")
    gas_manifold = relationship("GasManifoldModel")
    valve_position = relationship("ValvePositionModel")
    main_drive = relationship("MainDriveModel")
    oil_system = relationship("OilSystemModel")
    bearing_with_vibration_sensor_1 = relationship(
        "BearingWithVibrationSensorModel",
        foreign_keys=[bearing_with_vibration_sensor_1_id],
    )
    bearing_with_vibration_sensor_2 = relationship(
        "BearingWithVibrationSensorModel",
        foreign_keys=[bearing_with_vibration_sensor_2_id],
    )
    bearing_with_vibration_sensor_7 = relationship(
        "BearingWithVibrationSensorModel",
        foreign_keys=[bearing_with_vibration_sensor_7_id],
    )
    bearing_with_vibration_sensor_8 = relationship(
        "BearingWithVibrationSensorModel",
        foreign_keys=[bearing_with_vibration_sensor_8_id],
    )
    bearing_without_vibration_sensor_3 = relationship(
        "BearingWithoutVibrationSensorModel",
        foreign_keys=[bearing_without_vibration_sensor_3_id],
    )
    bearing_without_vibration_sensor_4 = relationship(
        "BearingWithoutVibrationSensorModel",
        foreign_keys=[bearing_without_vibration_sensor_4_id],
    )
    bearing_without_vibration_sensor_5 = relationship(
        "BearingWithoutVibrationSensorModel",
        foreign_keys=[bearing_without_vibration_sensor_5_id],
    )
    bearing_without_vibration_sensor_6 = relationship(
        "BearingWithoutVibrationSensorModel",
        foreign_keys=[bearing_without_vibration_sensor_6_id],
    )
    bearing_without_vibration_sensor_9 = relationship(
        "BearingWithoutVibrationSensorModel",
        foreign_keys=[bearing_without_vibration_sensor_9_id],
    )
