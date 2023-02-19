from fastapi import FastAPI

from app.entrypoint.helpers import WrappedResponse
from .config import Settings


def create_app(settings: Settings):
    _app = FastAPI(
        title="Сервис мониторинга и ремонта эксгаустеров",
        description=f"Current environment: {settings.APP_ENV}",
        docs_url="/docs",
        version=settings.VERSION,
        default_response_class=WrappedResponse,
        root_path=settings.ROOT_PATH,
    )
    return _app
