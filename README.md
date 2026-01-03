🎬 CineMind — Multimodal Movie Intelligence Platform


AI-powered system for analyzing movies using video, audio, and text to extract scene-level engagement intelligence.

🌟 Overview

CineMind is a multimodal AI backend system that converts raw movie files into structured, scene-level intelligence.
It analyzes visual structure, audio emotion, and dialogue sentiment to estimate how engaging each scene is.

The project focuses on real-world AI system design — feature pipelines, multimodal fusion, and ML readiness — rather than toy model demos.

✨ Key Features

🎞 Scene Detection — Automatic segmentation of movies into timestamped scenes

🔊 Audio Emotion Analysis — Emotion confidence & intensity extracted from audio

💬 Text Intelligence (Subtitles) — Dialogue extraction, sentiment & keyword analysis

🧠 Multimodal Fusion — Combines video, audio, and text signals per scene

📊 Engagement Scoring — Scene-level engagement scores (baseline heuristic)

🗄 Database Persistence — Scene intelligence stored in PostgreSQL

⚙️ Production-Ready Backend — Modular FastAPI architecture

🧠 How CineMind Works
Movie Upload
   ↓
Scene Detection (Video)
   ↓
Audio Emotion Extraction
   ↓
Subtitle Parsing & NLP
   ↓
Multimodal Feature Fusion
   ↓
Scene-Level Engagement Scores


Each scene becomes a structured data record suitable for analytics or ML training.

📦 Example Output
{
  "scene_id": 3,
  "start_time": 42.1,
  "end_time": 58.9,
  "engagement_score": 81.6,
  "audio_confidence": 0.74,
  "text_sentiment": -0.62,
  "text_intensity": 0.85,
  "keywords": ["revenge", "threat"],
  "dialogue_count": 4
}

🛠 Tech Stack
Backend & Data

Python

FastAPI

SQLAlchemy

PostgreSQL

Media Processing

FFmpeg

PySceneDetect

MoviePy

OpenCV

NLP

NLTK

Rule-based sentiment & keyword extraction

🗂 Project Structure
backend/
 └── app/
     ├── api/          # REST endpoints
     ├── services/     # Scene, audio, text, fusion logic
     ├── db/           # Database models & engine
     ├── schemas/      # Pydantic schemas
     └── main.py
data/
 ├── raw_movies/
 └── subtitles/

📈 Project Status
Component	Status
Backend architecture	✅ Complete
Scene detection	✅ Complete
Audio emotion analysis	✅ Complete (baseline)
Text extraction & NLP	✅ Complete
Multimodal fusion	✅ Complete
Engagement scoring	✅ Complete (rule-based)
Database integration	✅ Complete
ML model training	⏳ Planned
Frontend dashboard	⏳ Planned
🤖 Machine Learning Note

CineMind currently uses rule-based heuristics to generate engagement scores.

This is intentional:

Enables weakly supervised learning

Produces labeled data for future ML models

Mirrors how real-world ML pipelines are bootstrapped

No pretrained ML model is used yet.

🚧 Limitations

Engagement scoring is heuristic (not learned)

Subtitle extraction depends on embedded subtitles

No frontend UI yet

Not optimized for large-scale production traffic

🔮 Future Improvements

ML-based engagement prediction models

Shot-level and pacing analysis

Speech-to-text (Whisper) integration

React-based analytics dashboard

Distributed processing & scaling

👤 Author

Apoorva Srivastava
B.Tech Computer Science
Focus: Backend Engineering, Multimodal AI Systems, ML Pipelines

📄 License

MIT License — for educational and research use.

🎯 Why This Project Matters

CineMind demonstrates how real AI systems are engineered — from raw data ingestion to structured intelligence — the same way teams at Netflix, Meta, or Google approach multimodal problems.
