from decimal import Decimal
from typing import Optional
from pydantic import Field

from app.schema.base_schema_model import BaseModelWithId


class Refrigerant(BaseModelWithId):
    water_temperature_after: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    water_temperature_before: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    oil_temperature_after: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    oil_temperature_before: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
