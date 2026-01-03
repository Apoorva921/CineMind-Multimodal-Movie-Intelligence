import os
import uuid
from datetime import datetime
from fastapi import UploadFile


UPLOAD_DIR = "data/raw_movies"


def ingest_movie(file: UploadFile):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    job_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{job_id}_{file.filename}")

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return {
        "job_id": job_id,
        "filename": file.filename,
        "status": "uploaded",
        "created_at": datetime.utcnow()
    }
