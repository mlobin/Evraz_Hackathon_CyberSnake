import json
from typing import Optional, List, Type
from pydantic import BaseModel, create_model
from pydantic.fields import ModelField


class BaseSchemaModel(BaseModel):
    class Config:
        use_enum_values = True
        orm_mode = True

    def json_response(self, by_alias=True, **kwargs):
        return json.loads(self.json(exclude_none=True, by_alias=by_alias, **kwargs))

    def to_dict(self, by_alias=True, **kwargs):
        return self.dict(exclude_none=False, by_alias=by_alias, **kwargs)

    @classmethod
    def create_request_body_model(cls, excluded_fields: List[str]):
        fields = cls.__fields__
        new_fields = {}
        for key, item in fields.items():
            if key not in excluded_fields:
                if issubclass(item.type_, BaseModel):
                    if (
                        hasattr(item.outer_type_, "_name")
                        and item.outer_type_._name == "List"
                    ):
                        new_fields[key + "_ids"] = (
                            Optional[List[int]],
                            ... if item.required else item.default,
                        )
                    else:
                        new_fields[key + "_id"] = (
                            Optional[int],
                            ... if item.required else item.default,
                        )
                else:
                    new_fields[key] = item.type_, ... if item.required else item.default

        return create_model(
            f"{cls.__name__}RequestBody", __base__=BaseSchemaModel, **new_fields
        )

class BaseModelWithId(BaseSchemaModel):
    id: int
