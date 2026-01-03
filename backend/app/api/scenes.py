from fastapi import APIRouter, HTTPException
from backend.app.services.scene_service import detect_scenes
from backend.app.schemas.scene import SceneDetectionResponse

router = APIRouter()


@router.get("/{job_id}", response_model=SceneDetectionResponse)
def get_scenes(job_id: str):
    try:
        scenes = detect_scenes(job_id)
        return {
            "job_id": job_id,
            "total_scenes": len(scenes),
            "scenes": scenes
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Video not found")
