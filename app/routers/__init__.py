""" Routers Module.

    This module is responsible for registering different API routes.

"""

from fastapi import APIRouter
from .interactions_router import router as interactions_router
from .messages_router import router as messages_router

def register_routers(app: APIRouter):
    app.include_router(
        interactions_router,
        prefix="/interactions",
        tags=["interactions"]
    )
    app.include_router(
        messages_router,
        prefix="/messages",
        tags=["messages"]
    )