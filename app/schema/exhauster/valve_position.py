from decimal import Decimal
from typing import Optional
from pydantic import Field

from app.schema.base_schema_model import BaseModelWithId


class ValvePosition(BaseModelWithId):
    gas_valve_closed: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    gas_valve_open: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
    gas_valve_position: Optional[Decimal] = Field(max_digits = 6, decimal_places = 2)
