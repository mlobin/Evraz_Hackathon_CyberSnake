from decimal import Decimal
from typing import Optional
from pydantic import Field

from app.schema.base_schema_model import BaseModelWithId
from app.models.exhauster.sensor import SensorTypesEnum


class Sensor(BaseModelWithId):
    value: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    alarm_max: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    alarm_min: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    warning_max: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    warning_min: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    type: SensorTypesEnum