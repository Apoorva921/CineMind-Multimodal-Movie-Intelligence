from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from backend.app.db.database import Base


class SceneEngagement(Base):
    __tablename__ = "scene_engagements"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True)
    scene_id = Column(Integer)

    start_time = Column(Float)
    end_time = Column(Float)

    dominant_emotion = Column(String)
    avg_confidence = Column(Float)
    engagement_score = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)
