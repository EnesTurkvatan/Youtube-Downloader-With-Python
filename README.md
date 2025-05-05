# YouTube Downloader With Python

A Python-based command-line tool to download YouTube videos and playlists in various formats (MP3, MP4, AAC, WAV, AVI) and qualities (720p, 192kbps, etc.). Featuring customizable save locations, progress tracking, and a user-friendly interface, this project is perfect for personal use and learning Python!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Features
- Download single YouTube videos or entire playlists.
- Support for multiple formats: MP3, MP4, AAC, WAV, AVI.
- Selectable quality: 720p, 480p, 360p, 192kbps, 128kbps, etc.
- Customizable save location or default folder (`~/Downloads/YT_Downloads`).
- Progress tracking with a visual progress bar.
- Robust error handling for invalid links or network issues.
- Built with `yt-dlp` for reliable and fast downloads.

## Installation

1. **Prerequisites**:
   - Ensure [Python 3.6+](https://www.python.org/downloads/) is installed.
   - Install [FFmpeg](https://ffmpeg.org/download.html) and add it to your system's PATH:
     - **Windows**: Download FFmpeg and add `ffmpeg.exe` to PATH.
     - **Mac**: Run `brew install ffmpeg`.
     - **Linux**: Run `sudo apt-get install ffmpeg`.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/youtube-downloader-with-python.git
   cd youtube-downloader-with-python
Install Dependencies:
bash

pip install -r requirements.txt
Usage
Run the script using Python and follow the prompts to enter the YouTube URL, desired format, quality, and save location.


python youtube_downloader.py
The tool will ask for:

Video/Playlist URL: A valid YouTube video or playlist link.
Format: Choose from mp3, mp4, aac, wav, or avi.
Quality: Specify quality (e.g., 720p, 480p, 192kbps, 128kbps).
Save Location: Press Enter for default (~/Downloads/YT_Downloads) or provide a custom path.
Examples
Download a Single Video as MP4 (720p)



Video/Playlist URL: https://www.youtube.com/watch?v=example
Format (mp3, mp4, aac, wav, avi): mp4
Quality (e.g., 720p, 480p, 192kbps, 128kbps): 720p
Save Location (default: ~/Downloads/YT_Downloads): 
Output:



Kopyala
Processing: Example Video Title
Downloading: 45.6%
Downloading: 89.2%
Download completed, processing file...
File saved: ~/Downloads/YT_Downloads
Download a Playlist as MP3 (192kbps)



Video/Playlist URL: https://www.youtube.com/playlist?list=example
Format (mp3, mp4, aac, wav, avi): mp3
Quality (e.g., 720p, 480p, 192kbps, 128kbps): 192kbps
Save Location (default: ~/Downloads/YT_Downloads): /path/to/custom/folder
Tip: Add a screenshot or GIF to showcase the tool in action! Create a screenshots folder and include it like this:


![Demo](screenshots/demo.gif)
Dependencies
yt-dlp: For downloading YouTube videos and playlists.
click: For creating the command-line interface.
tqdm: For displaying the progress bar.
FFmpeg: For audio/video format conversion.
Install them using:

pip install yt-dlp click tqdm
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.
Please ensure your code follows the project's style guidelines and includes appropriate tests.

License
This project is licensed under the MIT License. See the  file for details.

Disclaimer
This tool is for personal and educational use only. Downloading copyrighted content may violate YouTube's Terms of Service or local laws. Use responsibly and respect content creators' rights.
