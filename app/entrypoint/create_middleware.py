from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware


ALLOW_ORIGINS = [
    "http://localhost:3000/",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8090",
    "*",
]


def create_middleware(app: FastAPI):
    app.add_middleware(GZipMiddleware, minimum_size=500)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )