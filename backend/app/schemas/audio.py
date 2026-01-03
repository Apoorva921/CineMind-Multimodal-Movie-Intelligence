from pydantic import BaseModel
from typing import List


class AudioEmotion(BaseModel):
    start_time: float
    end_time: float
    emotion: str
    confidence: float


class AudioEmotionResponse(BaseModel):
    job_id: str
    emotions: List[AudioEmotion]
