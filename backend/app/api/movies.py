from fastapi import APIRouter, UploadFile, File
from backend.app.services.ingestion_service import ingest_movie
from backend.app.schemas.movie import MovieUploadResponse

router = APIRouter()

@router.post("/upload", response_model=MovieUploadResponse)
def upload_movie(file: UploadFile = File(...)):
    return ingest_movie(file)
