from fastapi import APIRouter, HTTPException
from backend.app.services.fusion_service import fuse_scene_features

router = APIRouter()


@router.get("/{job_id}")
def get_fusion(job_id: str):
    try:
        return {
            "job_id": job_id,
            "scenes": fuse_scene_features(job_id)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
