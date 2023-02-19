from datetime import datetime
from typing import Optional

from app.schema.base_schema_model import BaseModelWithId
from app.schema.exhauster import (
    ExsgauterMetadata,
    MainDrive,
    Refrigerant,
    ValvePosition,
    OilSystem,
    GasManifold,
    BearingWithVibrationSensor,
    BearingWithoutVibrationSensor,
)


class Exhauster(BaseModelWithId):

    loaded_from_kafka_at: datetime
    is_active: int

    meta: ExsgauterMetadata
    refrigerant: Refrigerant
    gas_manifold: GasManifold
    valve_position: ValvePosition
    main_drive: MainDrive
    oil_system: OilSystem
    bearing_with_vibration_sensor_1: BearingWithVibrationSensor
    bearing_with_vibration_sensor_2: BearingWithVibrationSensor
    bearing_with_vibration_sensor_7: BearingWithVibrationSensor
    bearing_with_vibration_sensor_8: BearingWithVibrationSensor
    bearing_without_vibration_sensor_3: BearingWithoutVibrationSensor
    bearing_without_vibration_sensor_4: BearingWithoutVibrationSensor
    bearing_without_vibration_sensor_5: BearingWithoutVibrationSensor
    bearing_without_vibration_sensor_6: BearingWithoutVibrationSensor
    bearing_without_vibration_sensor_9: BearingWithoutVibrationSensor
