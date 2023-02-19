from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.exceptions import HTTPException, RequestValidationError

from app.views.root_router import root_router
from app.entrypoint.helpers import (
    use_route_names_as_operation_ids,
    http_exception_handler,
    validation_exception_handler,
    custom_http_exception_handler,
    HTTPExceptionCustom,
    api_error_responses,
)


def setup_router_and_exceptions(app: FastAPI, logging_dependency):
    app.include_router(
        root_router,
        responses=api_error_responses,
        dependencies=[Depends(logging_dependency)],
    )
    use_route_names_as_operation_ids(app)

    app.exception_handler(HTTPException)(http_exception_handler)
    app.exception_handler(HTTPExceptionCustom)(custom_http_exception_handler)
    app.exception_handler(RequestValidationError)(validation_exception_handler)
