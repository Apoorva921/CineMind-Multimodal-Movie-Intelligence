import os
import subprocess
import pysrt

RAW_VIDEO_DIR = "data/raw_movies"
SUBTITLE_DIR = "data/subtitles"

os.makedirs(SUBTITLE_DIR, exist_ok=True)


def extract_subtitles(job_id: str):
    video_file = None

    for file in os.listdir(RAW_VIDEO_DIR):
        if file.startswith(job_id):
            video_file = os.path.join(RAW_VIDEO_DIR, file)
            break

    if not video_file:
        raise FileNotFoundError("Video not found for subtitle extraction")

    subtitle_path = os.path.join(SUBTITLE_DIR, f"{job_id}.srt")

    command = [
        "ffmpeg",
        "-y",
        "-i", video_file,
        subtitle_path
    ]

    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if not os.path.exists(subtitle_path):
        return None

    return subtitle_path


def parse_subtitles(job_id: str):
    subtitle_path = os.path.join(SUBTITLE_DIR, f"{job_id}.srt")

    if not os.path.exists(subtitle_path):
        return []

    subs = pysrt.open(subtitle_path)

    parsed = []

    for sub in subs:
        start_time = (
            sub.start.hours * 3600 +
            sub.start.minutes * 60 +
            sub.start.seconds +
            sub.start.milliseconds / 1000
        )

        end_time = (
            sub.end.hours * 3600 +
            sub.end.minutes * 60 +
            sub.end.seconds +
            sub.end.milliseconds / 1000
        )

        parsed.append({
            "start_time": round(start_time, 2),
            "end_time": round(end_time, 2),
            "text": sub.text.replace("\n", " ").strip()
        })

    return parsed

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def analyze_text_emotion(dialogue: list):
    """
    dialogue: list of strings (scene dialogue)
    returns: sentiment_score, intensity_score
    """

    if not dialogue:
        return 0.0, 0.0

    sentiment_scores = []
    intensity_score = 0.0

    for line in dialogue:
        scores = analyzer.polarity_scores(line)
        sentiment_scores.append(scores["compound"])

        # intensity proxy: emotional strength + punctuation
        intensity_score += abs(scores["compound"]) * (
            1 + line.count("!") + line.count("?")
        )

    sentiment = sum(sentiment_scores) / len(sentiment_scores)
    intensity = intensity_score / len(dialogue)

    return round(sentiment, 3), round(intensity, 3)

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOPWORDS = set(stopwords.words("english"))


def extract_keywords(dialogue: list, top_k: int = 5):
    """
    dialogue: list of dialogue strings
    returns: list of top keywords
    """

    if not dialogue:
        return []

    text = " ".join(dialogue).lower()

    # remove punctuation
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    tokens = word_tokenize(text)

    tokens = [
        t for t in tokens
        if t not in STOPWORDS and len(t) > 2
    ]

    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1

    keywords = sorted(freq, key=freq.get, reverse=True)

    return keywords[:top_k]
