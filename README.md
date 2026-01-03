🎬 CineMind — Multimodal AI System for Movie Intelligence

CineMind is an end-to-end multimodal AI backend system that analyzes movies at the scene level by fusing video structure, audio emotion, and textual dialogue to compute engagement signals and identify impactful moments.

The project demonstrates real-world AI system design, focusing on data pipelines, feature engineering, and ML-ready architectures rather than isolated model training.

🚀 Why This Project Matters

Most student ML projects start with a dataset.
Real industry AI systems start by creating one.

CineMind solves this by converting raw, unstructured movie data into structured, scene-level intelligence suitable for analytics, ML training, and editorial workflows.

This mirrors how large companies (Netflix, YouTube, Amazon Prime) build internal AI services.

🧠 What CineMind Does

For an uploaded movie, CineMind:

Segments the movie into scenes

Extracts audio emotion signals

Extracts and parses subtitles

Performs NLP on dialogue (sentiment, intensity, keywords)

Fuses all modalities into numerical features

Computes an engagement score per scene

Each scene becomes a machine-readable data record.

🔄 Processing Pipeline
Movie Upload
   ↓
Scene Detection (Video)
   ↓
Audio Emotion Analysis
   ↓
Subtitle Extraction & NLP
   ↓
Multimodal Feature Fusion
   ↓
Scene-level Engagement Scoring

🧠 Core Engineering Highlights
Multimodal Feature Engineering

Scene-level temporal alignment across video, audio, and text

Emotion confidence aggregation

Dialogue density and sentiment intensity modeling

AI System Design

Weakly supervised engagement labeling (rule-based baseline)

ML-ready feature generation pipeline

Clear separation of ingestion, processing, fusion, and serving layers

Backend Architecture

Modular FastAPI service design

Clean API contracts and schemas

Database persistence using SQLAlchemy + PostgreSQL

📊 Example Output
{
  "scene_id": 2,
  "start_time": 18.5,
  "end_time": 34.2,
  "engagement_score": 76.4,
  "audio_confidence": 0.71,
  "text_sentiment": -0.58,
  "text_intensity": 0.82,
  "keywords": ["revenge", "threat"],
  "dialogue_count": 3
}

🏗️ Tech Stack
Backend & Data

FastAPI

Python 3.12

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

📁 Project Structure
backend/
 └── app/
     ├── api/          # FastAPI endpoints
     ├── services/     # Scene, audio, text, fusion logic
     ├── db/           # Database models & engine
     ├── schemas/      # API schemas
     └── main.py
data/
 ├── raw_movies/
 └── subtitles/

📌 Current Status
Component	Status
Backend architecture	✅ Complete
Scene detection	✅ Complete
Audio emotion analysis	✅ Complete
Text extraction & NLP	✅ Complete
Multimodal fusion	✅ Complete
Engagement scoring	✅ Complete (baseline)
Database persistence	✅ Implemented
ML model training	⏳ Planned
Frontend dashboard	⏳ Planned
