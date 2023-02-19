from fastapi import Request
from fastapi.exceptions import RequestValidationError, HTTPException
from pydantic import BaseModel
from starlette.responses import JSONResponse


class HTTPExceptionCustom(HTTPException):
    """
    Переопределение HTTPException для поддержки своего формата вывода ошибок
    """
    def __init__(self, status_code, error_code, error_message):
        super().__init__(status_code=status_code)
        self.error_code = error_code
        self.error_message = error_message


def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": "some_problem",
            "error_message": exc.detail
        },
    )


def custom_http_exception_handler(request: Request, exc: HTTPExceptionCustom):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": exc.error_code,
            "error_message": exc.error_message
            },
        )


def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "error_code": "validation_error",
            "error_message": f"Неправильные параметры запроса: {exc}",
        },
    )


class ErrorMessage(BaseModel):
    error_code: str
    error_message: str

api_error_responses = {
    400: {"model": ErrorMessage},
    404: {"model": ErrorMessage},
    422: {"model": ErrorMessage},
}