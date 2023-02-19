from decimal import Decimal
from typing import Optional
from pydantic import Field

from app.schema.base_schema_model import BaseModelWithId


class OilSystem(BaseModelWithId):
    oil_level: Optional[Decimal] = Field(max_digits=6, decimal_places=2)
    oil_pressure: Optional[Decimal] = Field(max_digits=6, decimal_places=2)
