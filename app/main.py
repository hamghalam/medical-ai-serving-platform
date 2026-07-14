from fastapi import FastAPI

from app.api.routers import health
from app.core.config import settings


def create_app() -> FastAPI:
    """
    Application factory.
    """

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.VERSION,
    )

    app.include_router(health.router)

    return app


app = create_app()