from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.scenes import router as scene_router
from backend.app.api.health import router as health_router
from backend.app.api.movies import router as movie_router
from backend.app.api.audio import router as audio_router
from backend.app.api.engagement import router as engagement_router
from backend.app.api.fusion import router as fusion_router

from backend.app.db.database import engine
from backend.app.db import models

# -------------------------------------------------
# APP INITIALIZATION
# -------------------------------------------------
app = FastAPI(title="CineMind API")

# -------------------------------------------------
# CREATE DATABASE TABLES (PHASE 1 - MEMORY)
# -------------------------------------------------
models.Base.metadata.create_all(bind=engine)

# -------------------------------------------------
# CORS CONFIG
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# ROUTERS
# -------------------------------------------------
app.include_router(health_router, prefix="/health")
app.include_router(movie_router, prefix="/movies", tags=["Movies"])
app.include_router(scene_router, prefix="/scenes", tags=["Scenes"])
app.include_router(audio_router, prefix="/audio", tags=["Audio"])
app.include_router(engagement_router, prefix="/engagement", tags=["Engagement"])
app.include_router(fusion_router, prefix="/fusion", tags=["Fusion"])
