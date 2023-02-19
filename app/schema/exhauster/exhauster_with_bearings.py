from datetime import datetime
from typing import Optional

from app.schema.base_schema_model import BaseModelWithId
from app.schema.exhauster import (
    ExsgauterMetadata,
    BearingWithVibrationSensor,
    BearingWithoutVibrationSensor,
)


class ExhausterWithBearings(BaseModelWithId):

    loaded_from_kafka_at: datetime
    is_active: int
    
    meta: ExsgauterMetadata
    bearing_with_vibration_sensor_1: BearingWithVibrationSensor
    bearing_with_vibration_sensor_2: BearingWithVibrationSensor
    bearing_with_vibration_sensor_7: BearingWithVibrationSensor
    bearing_with_vibration_sensor_8: BearingWithVibrationSensor
    bearing_without_vibration_sensor_3: Optional[BearingWithoutVibrationSensor]
    bearing_without_vibration_sensor_4: Optional[BearingWithoutVibrationSensor]
    bearing_without_vibration_sensor_5: Optional[BearingWithoutVibrationSensor]
    bearing_without_vibration_sensor_6: Optional[BearingWithoutVibrationSensor]
    bearing_without_vibration_sensor_9: Optional[BearingWithoutVibrationSensor]
