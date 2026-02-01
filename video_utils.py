from pathlib import Path
from moviepy import VideoFileClip
import shutil

VIDEO_EXT = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm'}

class VideoSorter:
    def get_video_orientation(self, video_path: Path) -> str:
        try:
            with VideoFileClip(str(video_path)) as clip:
                w, h = clip.size
                if w > h:
                    return "landscape"
                elif h > w:
                    return "portrait"
                else:
                    return "square"
        except Exception as e:
            print(f"Error processing {video_path}: {e}")
            return "undefined"

    def sort_videos_by_orientation(self, folder: Path):
        landscape_dir = folder / 'landscape'
        portrait_dir = folder / 'portrait'

        try:
            landscape_dir.mkdir(exist_ok=True)
        except Exception as e:
            print(f"Error creating landscape folder: {e}")

        try:
            portrait_dir.mkdir(exist_ok=True)
        except Exception as e:
            print(f"Error creating portrait folder: {e}")

        for file in folder.iterdir():
            if file.is_file() and file.suffix.lower() in VIDEO_EXT:
                orientation = self.get_video_orientation(file)
                if orientation == "landscape":
                    shutil.move(str(file), landscape_dir / file.name)
                elif orientation == "portrait":
                    shutil.move(str(file), portrait_dir / file.name)
                elif orientation == "square":
                    # don't move square videos
                    pass
                else:
                    print(f"Unknown orientation: {orientation}. Skipping.")