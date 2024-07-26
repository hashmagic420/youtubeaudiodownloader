import streamlit as st
import yt_dlp

# Function to get video information
def get_video_info(video_url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        video_info = {
            "title": info.get("title"),
            "thumbnail": info.get("thumbnail"),
            "views": info.get("view_count"),
            "length": info.get("duration"),
            "rating": info.get("average_rating"),
            "url": video_url
        }
    return video_info

# Function to download video
def download_video(video_url):
    ydl_opts = {'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        st.success(f"Video downloaded from {video_url}")

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
