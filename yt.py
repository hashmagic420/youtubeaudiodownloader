import streamlit as st
import requests
from pytube import YouTube

# Function to get video information
def get_video_info(video_url):
    try:
        yt = YouTube(video_url)
        video_info = {
            "title": yt.title,
            "thumbnail": yt.thumbnail_url,
            "views": yt.views,
            "length": yt.length,
            "rating": yt.rating,
            "url": video_url
        }
        return video_info
    except Exception as e:
        st.error(f"Error fetching video info: {e}")
        return None

# Function to download video
def download_video(video_url):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(file_extension='mp4', res="360p").first()
        stream.download()
        st.success(f"Video downloaded: {yt.title}.mp4")
    except Exception as e:
        st.error(f"Error downloading video: {e}")

st.set_page_config(page_title="YouTube Video Downloader", layout="centered")

# Sidebar
st.sidebar.title("YouTube Video Downloader")
video_url = st.sidebar.text_input("Enter YouTube Video URL")
if st.sidebar.button("Get Video Info"):
    if video_url:
        video_info = get_video_info(video_url)
        if video_info:
            st.sidebar.image(video_info['thumbnail'], width=200)
            st.sidebar.write(f"**Title:** {video_info['title']}")
            st.sidebar.write(f"**Views:** {video_info['views']}")
            st.sidebar.write(f"**Length:** {video_info['length']} seconds")
            st.sidebar.write(f"**Rating:** {video_info['rating']}")
    else:
        st.sidebar.error("Please enter a valid YouTube URL")

if st.sidebar.button("Download Video"):
    if video_url:
        download_video(video_url)
    else:
        st.sidebar.error("Please enter a valid YouTube URL")

# Main
st.title("YouTube Video Downloader")
st.write("""
    This app allows you to download YouTube videos in 360p format.
    Enter the YouTube video URL in the sidebar to get started.
""")

# Custom HTML/CSS/JS
st.markdown("""
    <link rel="stylesheet" href="static/style.css">
    <script src="static/scripts.js"></script>
""", unsafe_allow_html=True)
