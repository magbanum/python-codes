import requests

# response = requests.get("https://api.github.com/users/magbanum")
# response = requests.get("https://api.github.com/users/magbanum")
response = requests.get("https://api.github.com/users/magbanum/repos")
result = response.json()

# for item,data in result.items():
#     print(item,":",data)

# for item,data in result.items():
for data in result:
    print(data['name'],":",data["language"])