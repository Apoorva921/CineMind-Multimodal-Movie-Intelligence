from fastapi import APIRouter, HTTPException
from backend.app.services.audio_service import extract_audio_emotions
from backend.app.schemas.audio import AudioEmotionResponse

router = APIRouter()


@router.get("/{job_id}", response_model=AudioEmotionResponse)
def get_audio_emotions(job_id: str):
    try:
        emotions = extract_audio_emotions(job_id)
        return {
            "job_id": job_id,
            "emotions": emotions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
