from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("YOUR_API_KEY")

# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=api_key)

# Search for videos
request = youtube.search().list(
    part="snippet",
    q="web scraping tutorial",  # Search query
    type="video",
    maxResults=5
)
response = request.execute()

# Print video details
for item in response["items"]:
    print(f"Title: {item['snippet']['title']}")
    print(f"Video ID: {item['id']['videoId']}")
    print(f"Channel: {item['snippet']['channelTitle']}")
    print()
