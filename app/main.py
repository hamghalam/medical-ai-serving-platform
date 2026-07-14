from fastapi import FastAPI

from app.api.routers import (
    health,
    inference,
    models,
)

from app.core.config import settings


def create_app() -> FastAPI:
    """
    Application Factory
    """

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.VERSION,
    )

    # Root endpoint
    @app.get("/", tags=["Root"])
    async def root():

        return {
            "service": settings.APP_NAME,
            "version": settings.VERSION,
            "docs": "/docs",
        }

    # Routers
    app.include_router(health.router)
    app.include_router(models.router)
    app.include_router(inference.router)

    return app


app = create_app()