from decimal import Decimal
from typing import Optional
from pydantic import Field

from app.schema.base_schema_model import BaseModelWithId


class MainDrive(BaseModelWithId):
    rotor_current: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    rotor_voltage: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    stator_current: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    stator_voltage: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
