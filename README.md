# 🎬 CineMind — Multimodal AI for Movie Intelligence

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=flat-square&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=flat-square&logo=postgresql)
![Status](https://img.shields.io/badge/Status-Active_Development-yellow?style=flat-square)

**AI-powered backend system for scene-level movie analysis using video, audio, and text**

</div>

---

## 🌟 Overview

CineMind is a **multimodal AI backend platform** that analyzes full-length movies to extract **scene-level engagement intelligence**.

It processes **video, audio, and subtitles** to generate structured, ML-ready data that highlights emotionally intense and high-impact scenes.  
The project mirrors real-world content intelligence systems used in **media, streaming, and entertainment analytics**.

CineMind is designed as a **production-style system**, focusing on clean architecture, data pipelines, and extensibility for machine learning.

---

## ✨ Key Features

- **🎞 Scene Detection (Video Intelligence)**  
  Automatically segments movies into timestamped scenes using content-based detection.

- **🎧 Audio Emotion Analysis**  
  Extracts emotional confidence and intensity from audio tracks.

- **📝 Subtitle Parsing & NLP**  
  Parses embedded subtitles and performs sentiment and keyword analysis.

- **🧠 Multimodal Feature Fusion**  
  Aligns video, audio, and text signals at scene level.

- **📊 Engagement Scoring**  
  Computes interpretable engagement scores for each scene.

- **🗄 Database Persistence**  
  Stores scene-level features in PostgreSQL for analytics and ML training.

---

## 🔄 How CineMind Works

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
Scene-Level Engagement Scoring
↓
PostgreSQL Storage


Each scene is converted into a **structured data record** that can be queried, analyzed, or used for ML model training.

---

## 📦 Example Output

```json
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


## ⚙️ Tech Stack

Backend & Data
Python
FastAPI
SQLAlchemy
PostgreSQL
Video & Audio Processing
FFmpeg
PySceneDetect
MoviePy
OpenCV
NLP
NLTK
Rule-based sentiment analysis
Keyword extraction


## 🗂️ Project Structure

backend/
├── app/
│   ├── api/            # REST endpoints
│   ├── services/       # Scene, audio, text, fusion logic
│   ├── db/             # Database models & engine
│   ├── schemas/        # Pydantic schemas
│   └── main.py         # FastAPI entry point
data/
├── raw_movies/
├── subtitles/


## 📊 Project Status

Component	Status
Backend Architecture	✅ Complete
Scene Detection	✅ Complete
Audio Emotion Analysis	✅ Complete (V1)
Text Extraction & NLP	✅ Complete (Baseline)
Multimodal Fusion	✅ Complete
Engagement Scoring	✅ Complete (Rule-based)
Database Integration	✅ Complete
Machine Learning Training	⏳ Planned
Frontend Dashboard	⏳ Planned


<div align="center">

Built to demonstrate real-world AI system design, not just model training

**⭐ Star this repository if you find it useful! **

</div> ```

