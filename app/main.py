# app/main.py
import logging

from fastapi import FastAPI

from app.api.v1.routes_demo import router as demo_router
from app.core.logging import configure_logging
from app.core.middleware import RequestIdMiddleware

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Hinsight Dashboard API", version="0.1.0")

app.add_middleware(RequestIdMiddleware)

@app.get("/healthz", tags=["health"])
def healthz() -> dict:
    logger.info("health_check", extra={"event": "health_check"})
    return {"status": "ok"}

@app.get("/hinsight", tags=["health"])
def hinsight() -> dict:
    logger.info("hinsight_check", extra={"event": "hinsight_check"})
    return {"status": "ok"}

app.include_router(demo_router)

