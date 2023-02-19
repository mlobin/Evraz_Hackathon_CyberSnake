from fastapi import APIRouter
from app.views.exhauster import exhauster_router

root_router = APIRouter()

root_router.include_router(
    exhauster_router, prefix="/exhauster", tags=["Exhauster"]
)