from pydantic import BaseModel
from typing import List


class SceneEngagement(BaseModel):
    scene_id: int
    start_time: float
    end_time: float
    engagement_score: float
    dominant_emotion: str


class EngagementResponse(BaseModel):
    job_id: str
    highlights: List[SceneEngagement]
