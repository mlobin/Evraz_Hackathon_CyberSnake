from app.schema.base_schema_model import BaseModelWithId
from app.models.exhauster.bearing_with_vibration_sensor import SensorStatusesEnum
from app.schema.exhauster.sensor import Sensor


class BearingWithVibrationSensor(BaseModelWithId):
    temperature: Sensor
    axial_vibration: Sensor
    horizontal_vibration: Sensor
    vertical_vibration: Sensor
    number: int
    temperature_status: SensorStatusesEnum
    vibration_status: SensorStatusesEnum