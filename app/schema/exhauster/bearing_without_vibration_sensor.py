from app.schema.base_schema_model import BaseModelWithId
from app.models.exhauster.bearing_with_vibration_sensor import SensorStatusesEnum
from app.schema.exhauster.sensor import Sensor


class BearingWithoutVibrationSensor(BaseModelWithId):
    temperature: Sensor
    number: int
    temperature_status: SensorStatusesEnum
    