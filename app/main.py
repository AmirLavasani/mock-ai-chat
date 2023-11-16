"""
    Main script of Mock AI Chat.

    This script setups the API server using FastAPI.

"""

from fastapi import FastAPI
from routers import register_routers
from contextlib import asynccontextmanager

from version import VERSION

from app.schemas.message import Message


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting up the app...".upper())

    yield

    print("shutting down gracefully...".upper())


app = FastAPI(
    lifespan=lifespan,
    title="Mock AI Chat",
    version=VERSION
)

register_routers(app)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Mock AI Chat API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)