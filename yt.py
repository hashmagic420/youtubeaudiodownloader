import requests

def get_video_info(video_id):
    api_key = 'YOUR_YOUTUBE_API_KEY'
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet,contentDetails,statistics'
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching video info")
        return None
    
    return response.json()

def download_video(video_info):
    formats = video_info.get('formats')
    if not formats:
        print("No formats available for this video")
        return
    
    for format in formats:
        if format['qualityLabel'] == '360p':
            download_url = format['url']
            response = requests.get(download_url, stream=True)
            if response.status_code == 200:
                with open(f'{video_info["title"]}.mp4', 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                print(f"Downloaded {video_info['title']}.mp4")
            else:
                print("Failed to download video")
            break

# Example usage
video_id = 'arj7oStGLkU'
video_info = get_video_info(video_id)
if video_info:
    download_video(video_info)
