# Python program to get user data from GitHub api.
# import requests module
import requests
# provide GitHub username
username = input()
# Join the username at the end of api link
url = "https://api.github.com/users/" + username + "/repos"
# Get the response from url
response = requests.get(url)
# Convert the data into Json format
json_output = response.json()
# Loop through items in json to get key:value pairs

# print(json_output[0].keys())

# # top languages
# top_lang = dict()
# for item in json_output:
#     print(item['name'], item['language'])

#     top_lang[item['language']] = top_lang.get(item['language'], 0) + 1

# sorted_top_lang = dict(sorted(top_lang.items(), key=lambda item: item[1], reverse=True))
# print(top_lang)
# print(sorted_top_lang)

# # most starred
# most_starred = dict()
# for item in json_output:
#     print(item['name'], item['stargazers_count'])
#     most_starred[item['name']] = item['stargazers_count']

# sorted_most_starred = list(sorted(most_starred.items(), key=lambda item: item[1], reverse=True))
# sorted_most_starred = dict(sorted_most_starred[0:5])
# print(sorted_most_starred)

# stars per language
star_per_lang = {}
for item in json_output:
    star_per_lang[item['language']] = star_per_lang.get(item['language'], 0) + item['stargazers_count']
print(star_per_lang)





# for i in json_output:
#     for key, value in i.items():
#         print(key,":",value)