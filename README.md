# youtubeaudiodownloader
python-based web application via streamlit/rapidapi ran app to extract youtube audio 
# YouTube Video Downloader

This project is a Python-based YouTube video downloader that fetches video information using the YouTube Data API and downloads the video in the specified format (360p in this example).

## Features

- Fetch video information using the YouTube Data API.
- Download video in 360p format.
- Save the downloaded video locally.

## Prerequisites

- Python 3.x
- A YouTube Data API key
- A RapidAPI key

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Replace `YOUR_YOUTUBE_API_KEY` and `YOUR_RAPIDAPI_KEY` in the script with your actual YouTube Data API key and RapidAPI key.

## Usage

1. To get video information:
    ```python
    video_id = 'arj7oStGLkU'
    video_info = get_video_info(video_id)
    if video_info:
        print(video_info)
    ```

2. To download a video:
    ```python
    video_id = 'arj7oStGLkU'
    video_info = get_video_info(video_id)
    if video_info:
        download_video(video_info)
    ```

3. The video will be downloaded and saved as `title.mp4` in the current directory.

## Functions

- `get_video_info(video_id)`: Fetches video information using the YouTube Data API.
- `download_video(video_info)`: Downloads the video in the specified format and saves it locally.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
