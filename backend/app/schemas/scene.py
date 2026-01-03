from pydantic import BaseModel
from typing import List


class Scene(BaseModel):
    scene_id: int
    start_time: float
    end_time: float


class SceneDetectionResponse(BaseModel):
    job_id: str
    total_scenes: int
    scenes: List[Scene]
