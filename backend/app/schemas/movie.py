from pydantic import BaseModel
from datetime import datetime


class MovieUploadResponse(BaseModel):
    job_id: str
    filename: str
    status: str
    created_at: datetime
