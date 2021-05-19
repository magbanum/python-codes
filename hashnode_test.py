import requests

headers = {
    "Authorization": "9e46f81b-f1b9-416b-bd76-bf2d3ec680a3"
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
    }}
}}""".format(username=input())

result = run_query(query,headers)
print(result["data"]["user"]["tagline"])

