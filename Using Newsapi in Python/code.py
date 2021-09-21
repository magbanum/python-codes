# Python program to get news blogs from newsapi
import requests

response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=your-api-key")
result = response.json()

for blog in result['articles']:
    print(blog['title'])
