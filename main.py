import argparse
from pathlib import Path
from moviepy import VideoFileClip
import shutil

def get_video_orientation(video_path):
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
        return None

def sort_videos_by_orientation(folder):
    folder = Path(folder)
    landscape_dir = folder / 'landscape'
    portrait_dir = folder / 'portrait'

    landscape_dir.mkdir(exist_ok=True)
    portrait_dir.mkdir(exist_ok=True)

    video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm'}

    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() in video_extensions:
            orientation = get_video_orientation(file)
            if orientation == 'landscape':
                shutil.move(str(file), landscape_dir / file.name)
            elif orientation == 'portrait':
                shutil.move(str(file), portrait_dir / file.name)
            elif orientation == 'square':
                # don't move square videos
                pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="FlipTastic",
        description="Sort video files according to their orientation."
    )
    parser.add_argument("-r", "--recursive", action="store_true", help="Look recursively for subfolders.")
    parser.add_argument("-f", "--folder", type=str, required=True, help="Folder in which to look for videos.")
    args = parser.parse_args()
    if args.recursive:
        # loop over subfolders
        for subfolder in Path(args.folder).iterdir():
            if subfolder.is_dir() and subfolder.name not in ['portrait', 'landscape', '..']:
                print(f"Processing folder: {subfolder} ...")
                sort_videos_by_orientation(subfolder)
                print(f"Done sorting videos in {subfolder} !")
    else:
        # process only current folder
        print(f"Processing folder: {args.folder} ...")
        sort_videos_by_orientation(args.folder)
        print(f"Done sorting videos in {args.folder} !")
