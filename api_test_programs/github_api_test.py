# Python program to get user data from GitHub api.
# import requests module
import requests
# provide GitHub username
username = input()
# Join the username at the end of api link
url = "https://api.github.com/users/" + username
# Get the response from url
response = requests.get(url)
# Convert the data into Json format
json_output = response.json()
# Loop through items in json to get key:value pairs
for key, value in json_output.items():
    print(key,":",value)