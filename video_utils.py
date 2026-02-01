from pathlib import Path
from moviepy import VideoFileClip
import shutil


class VideoSorter:
    VIDEO_EXT = {".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"}
    def get_video_orientation(self, video_path: Path) -> str:
        """
        Gives the orientation of the video.
        :param video_path: Path to the video
        :return: a string with the orientation of the video
        """
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
        """
        Sort the videos by orientation in an appropriate folder.
        :param folder: Folder to sort videos
        :return:
        """
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
            if file.is_file() and file.suffix.lower() in self.VIDEO_EXT:
                orientation = self.get_video_orientation(file)
                if orientation == "landscape":
                    try:
                        shutil.move(str(file), landscape_dir / file.name)
                    except Exception as e:
                        print(f"Error moving landscape file: {e}. Skipping.")
                elif orientation == "portrait":
                    try:
                        shutil.move(str(file), portrait_dir / file.name)
                    except Exception as e:
                        print(f"Error moving portrait file: {e}. Skipping.")
                elif orientation == "square":
                    # don't move square videos
                    pass
                else:
                    print(f"Unknown orientation: {orientation}. Skipping.")
