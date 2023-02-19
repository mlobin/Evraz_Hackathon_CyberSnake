import logging
from pythonjsonlogger import jsonlogger
from starlette.requests import Request


def init_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    log_handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)

    def logging_dependency(request: Request):
        logger.info("%s %s", request.method, request.url, extra=request.path_params)

    return logging_dependency
