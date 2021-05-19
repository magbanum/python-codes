# import requests
# import json

# response = requests.get('https://www.googleapis.com/youtube/v3/videos')

# print(response.json())

# for data in response.json()['items']:
#     print(data['title'])
#     print()

#from http.client import responses
from googleapiclient.discovery import build

api_key = 'AIzaSyAwubYCnvbmwJDpSyVvUE6ArSdHahBJMHU'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    id='UCMcNODogjrOfsls-0bfw-4g'
)

response = request.execute()

print(response)
