import requests

response = requests.get("https://api.github.com/users/magbanum/repos")

json_output = response.json()

for data in json_output:
    print(data['name'],":",data["language"])