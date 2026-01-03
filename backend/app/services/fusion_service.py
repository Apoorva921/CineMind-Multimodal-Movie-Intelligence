from backend.app.services.scene_service import detect_scenes
from backend.app.services.audio_service import extract_audio_emotions
from backend.app.services.text_service import (
    parse_subtitles,
    analyze_text_emotion,
    extract_keywords,
)


# --------------------------------------------------
# STEP 1: ALIGN TEXT WITH SCENES
# --------------------------------------------------
def align_text_with_scenes(job_id: str):
    scenes = detect_scenes(job_id)
    subtitles = parse_subtitles(job_id)

    aligned = []

    for scene in scenes:
        s_start = float(scene["start_time"])
        s_end = float(scene["end_time"])

        scene_dialogue = [
            sub["text"]
            for sub in subtitles
            if sub["start_time"] >= s_start and sub["end_time"] <= s_end
        ]

        aligned.append({
            "scene_id": int(scene["scene_id"]),
            "start_time": s_start,
            "end_time": s_end,
            "dialogue": scene_dialogue,
        })

    return aligned


# --------------------------------------------------
# STEP 2: MULTIMODAL FUSION (FINAL FEATURES)
# --------------------------------------------------
def fuse_scene_features(job_id: str):
    scenes = detect_scenes(job_id)
    emotions = extract_audio_emotions(job_id)
    text_alignment = align_text_with_scenes(job_id)

    fused_scenes = []

    for scene in scenes:
        s_id = int(scene["scene_id"])
        s_start = float(scene["start_time"])
        s_end = float(scene["end_time"])
        duration = max(s_end - s_start, 1.0)

        # ---------- AUDIO SIGNAL ----------
        scene_emotions = [
            e for e in emotions
            if e["start_time"] >= s_start and e["end_time"] <= s_end
        ]

        if scene_emotions:
            avg_audio_conf = float(
                sum(float(e["confidence"]) for e in scene_emotions)
                / len(scene_emotions)
            )
        else:
            avg_audio_conf = 0.0

        # ---------- TEXT SIGNAL ----------
        scene_text = next(
            item for item in text_alignment if item["scene_id"] == s_id
        )["dialogue"]

        sentiment, intensity = analyze_text_emotion(scene_text)
        sentiment = float(sentiment)
        intensity = float(intensity)

        keywords = extract_keywords(scene_text)
        dialogue_density = float(len(scene_text)) / duration

        # ---------- ENGAGEMENT SCORE (RULE-BASED V1) ----------
        engagement_score = float(
            0.4 * avg_audio_conf * 100 +
            0.3 * intensity * 100 +
            0.2 * abs(sentiment) * 100 +
            0.1 * dialogue_density * 10
        )

        fused_scenes.append({
            "scene_id": s_id,
            "start_time": s_start,
            "end_time": s_end,
            "engagement_score": round(engagement_score, 2),
            "audio_confidence": round(avg_audio_conf, 3),
            "text_sentiment": sentiment,
            "text_intensity": intensity,
            "keywords": keywords,
            "dialogue_count": int(len(scene_text)),
        })

    fused_scenes.sort(
        key=lambda x: x["engagement_score"],
        reverse=True,
    )

    return fused_scenes
