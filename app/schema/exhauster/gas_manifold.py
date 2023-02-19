from decimal import Decimal
from typing import Optional
from pydantic import Field

from app.schema.base_schema_model import BaseModelWithId


class GasManifold(BaseModelWithId):
    temperature_before: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    underpressure_before: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
   