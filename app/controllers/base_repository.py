from typing import Generic, Optional, TypeVar, List, Tuple
from fastapi import Query

from app.entrypoint.database import Base, SessionLocal
from app.schema.base_schema_model import BaseSchemaModel
from app.views.helpers.base_exceptions import ObjectAlreadyExistsError, ObjectNotFoundError


Model = TypeVar("Model", bound=Base)
Domain = TypeVar("Domain", bound=BaseSchemaModel)


class BaseRepository(Generic[Model, Domain]):
    def __init__(self, model: Model, domain: Domain):
        self._model = model
        self._domain = domain
        self._session = SessionLocal()

    def _to_domain(self, model: Model) -> Optional[Domain]:
        if model:
            return self._domain.from_orm(model)

    def get(self, **kwargs) -> Domain:
        query_model = self._model.query
        for attr, value in kwargs.items():
            query_model = query_model.filter(getattr(self._model, attr) == value)
        model = query_model.first()
        domain = self._to_domain(model)
        if domain:
            return domain
        raise ObjectNotFoundError

    def get_by_id(self, model_id: int) -> Domain:
        model = self._model.query.get(model_id)
        domain = self._to_domain(model)
        if domain:
            return domain
        self._session.close()
        raise ObjectNotFoundError

    def filter(self, **kwargs) -> Query:
        query_model = self._model.query
        for attr, value in kwargs.items():
            query_model = query_model.filter(getattr(self._model, attr) == value)
        return query_model

    def filter_by_list(self, **kwargs) -> Query:
        query_model = self._model.query
        for attr, value in kwargs.items():
            query_model = query_model.filter(getattr(self._model, attr).in_(value))
        return query_model
