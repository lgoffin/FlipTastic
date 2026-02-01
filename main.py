import argparse
import os
from pathlib import Path
from video_utils import VideoSorter


def get_subfolder(folder: Path, excluded_folders: list[str], include_subfolders: bool = False) -> list[Path]:
    """
    Returns a list of subfolders within a folder.
    :param folder: root folder path
    :param excluded_folders: list of subfolders to exclude
    :param include_subfolders: whether to include subfolders
    :return:
    """
    if include_subfolders:
        return [folder] + [Path(r) for r, d, files in os.walk(folder) if not any(excl in Path(r).parts for excl in excluded_folders)]
    else:
        return [folder] + [Path(f) for f in os.scandir(folder) if f.is_dir() and f.name not in excluded_folders]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="FlipTastic",
        description="Sort video files according to their orientation."
    )
    parser.add_argument("-r", "--recursive", action="store_true", help="look recursively for subfolders")
    parser.add_argument("-f", "--folder", type=str, required=True, help="folder in which to look for videos")
    args = parser.parse_args()
    sorter = VideoSorter()
    if args.recursive:
        # list all folders to process
        subfolders = get_subfolder(Path(args.folder), excluded_folders=["..", "portrait", "landscape"], include_subfolders=True)
        print(f"Found {len(subfolders)} subfolders to process in {args.folder}.")
        # loop over subfolders
        for subfolder in subfolders:
            print(f"Processing folder: {subfolder} ...")
            sorter.sort_videos_by_orientation(subfolder)
            print(f"Done sorting videos in {subfolder} !")
    else:
        # process only current folder
        print(f"Processing folder: {args.folder} ...")
        sorter.sort_videos_by_orientation(args.folder)
        print(f"Done sorting videos in {args.folder} !")
