import os
import cv2
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector


RAW_VIDEO_DIR = "data/raw_movies"


def get_video_duration(video_path: str) -> float:
    """Get video duration in seconds using OpenCV (stable)."""
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise RuntimeError("Cannot open video file")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.release()

    if fps <= 0:
        raise RuntimeError("Invalid FPS value")

    return frame_count / fps


def detect_scenes(job_id: str):
    # --------------------------------------------------
    # 1. Ensure directory exists
    # --------------------------------------------------
    if not os.path.exists(RAW_VIDEO_DIR):
        raise FileNotFoundError("Raw video directory does not exist")

    # --------------------------------------------------
    # 2. Find uploaded video
    # --------------------------------------------------
    video_file = None
    for file in os.listdir(RAW_VIDEO_DIR):
        if file.startswith(job_id):
            video_file = os.path.join(RAW_VIDEO_DIR, file)
            break

    if not video_file:
        raise FileNotFoundError("Video not found for given job_id")

    # --------------------------------------------------
    # 3. Scene detection (PySceneDetect)
    # --------------------------------------------------
    video_manager = VideoManager([video_file])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=15.0))

    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    scene_list = scene_manager.get_scene_list()
    video_manager.release()

    # --------------------------------------------------
    # 4. Prepare scenes
    # --------------------------------------------------
    scenes = []

    if not scene_list:
        # ✅ Fallback: full video as one scene
        duration = get_video_duration(video_file)

        scenes.append({
            "scene_id": 0,
            "start_time": 0.0,
            "end_time": round(duration, 2)
        })
    else:
        for idx, scene in enumerate(scene_list):
            scenes.append({
                "scene_id": idx,
                "start_time": scene[0].get_seconds(),
                "end_time": scene[1].get_seconds()
            })

    return scenes
