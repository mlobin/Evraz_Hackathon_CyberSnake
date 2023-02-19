import asyncio

import uvicorn

from app.entrypoint.config import resolve_settings
from app.entrypoint.database import init_engines
from app.entrypoint.create_app import create_app
from app.entrypoint.init_logger import init_logger
from app.entrypoint.create_middleware import create_middleware
from app.entrypoint.setup_router_and_exceptions import setup_router_and_exceptions
from app.services.kafka_consumer_service import KafkaConsumerService

settings = resolve_settings()
logging_dependency = init_logger()
app = create_app(settings)
create_middleware(app)
setup_router_and_exceptions(app, logging_dependency)
init_engines(settings)
#loop = asyncio.get_event_loop()
global consumer_task
#loop.run_in_executor(None, KafkaConsumerService.parse_data)

# if __name__ == '__main__':
#     uvicorn.run("main:app", reload=True)