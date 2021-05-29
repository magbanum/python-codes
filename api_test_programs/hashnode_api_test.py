import os
import requests

headers = {
    "Authorization": os.environ['TOKEN']

}

def run_query(query, headers):
    response = requests.post(url="https://api.hashnode.com", json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}.".format(response.status_code))

query = """{{
    user(username: "{username}"){{
        username
        name
        tagline
        numFollowers
        publicationDomain
        publication{{
          posts(page:0){{
            title
            brief
            coverImage
            slug
          }}
        }}
    }}
}}""".format(username=input("Enter the Hashnode Username: "))

output = run_query(query,headers)
posts =  output["data"]["user"]["publication"]["posts"]
print("Recent 6 blog posts of {} are: ".format(output["data"]["user"]["name"]))
[print('-',post["title"]) for post in posts]


