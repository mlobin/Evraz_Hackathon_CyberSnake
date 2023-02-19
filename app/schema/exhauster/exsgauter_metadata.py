from datetime import date

from app.schema.base_schema_model import BaseModelWithId


class ExsgauterMetadata(BaseModelWithId):
    exhauster_name: str
    rotor_instalation: date
    rotor_number: int
    sinter_machine_name: str
