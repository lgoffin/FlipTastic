# FlipTastic

FlipTastic is a command-line tool that sorts video files in a folder based on their orientation (landscape, portrait, square).

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- Sorts videos into `landscape` and `portrait` subfolders based on their orientation.
- Supports the following video formats: `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv`, `.wmv`, `.webm`.
- Works recursively on subfolders if needed.

## Prerequisites
- Python 3.6 or higher
- The `moviepy` library to read video metadata.

You can install `moviepy` using the following command:
```bash
pip install moviepy
```

## Installation

Clone this repository to your local machine:
```bash
git clone <REPOSITORY_URL>
```

## Usage
To sort videos in a folder, use the following command:
```bash
python main.py -f <path_to_folder>
```

To sort videos recursively in all subfolders, add the -r option:
```bash
python main.py -f <path_to_folder> -r
```

## Project Structure
```
FlipTastic/
│
├── main.py                # Entry point of the program
├── video_utils.py         # Contains the `VideoSorter` class for sorting videos
└── README.md              # Project documentation
```

## Contributing
Contributions are welcome! Here's how you can contribute:

1. Fork this repository.
2. Create a branch for your feature (git checkout -b feature/my-new-feature).
3. Commit your changes (git commit -am 'Add a new feature').
4. Push to the branch (git push origin feature/my-new-feature).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
