# Python program to get channel details using Youtube API
import os
from googleapiclient.discovery import build

api_key = os.environ['YOUTUBE_API_KEY']

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(part='statistics',
                                  id='UCMcNODogjrOfsls-0bfw-4g')

response = request.execute()

print(response)
