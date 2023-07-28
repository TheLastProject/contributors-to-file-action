import os
import requests
import sys
import time

def wait_until_api_allowed():
    while True:
        if requests.get('https://api.github.com/rate_limit').json()["rate"]["remaining"] != 0:
            return

        print("API limit reached, waiting 5 minutes...")
        time.sleep(300)

def get_name(contributor):
    if "url" in contributor:
        print(f"Resolving name of {contributor['login']}...")
        wait_until_api_allowed()
        contributor_data = requests.get(contributor["url"]).json()

        if "name" in contributor_data and contributor_data["name"]:
            return contributor_data["name"]

        return contributor_data["login"]

    return contributor["login"]

file_in_repo = sys.argv[1]

contributors = {}

print("Retrieving GitHub contributor list...")
contributors_url = f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}/contributors"
while True:
    wait_until_api_allowed()
    r = requests.get(contributors_url, params={'anon': 1})
    for contributor in r.json():
        name = get_name(contributor)
        
        if any(bot_string in name for bot_string in ["(bot)", "[bot]"]):
            print(f"Ignoring {name}, matches bot string")
            continue

        contributions = contributor["contributions"]

        if name in contributors:
            contributions += contributors[name]

        contributors[name] = contributions

        print(f"Set contribution count for {name} to {contributions}")

    if not 'next' in r.links:
        break

    contributors_url = r.links['next']['url']

print("Writing contributor list to file...")
with open(file_in_repo, "w") as output_file:
    for contributor in sorted(contributors.items(), key=lambda kv: kv[1], reverse=True):
        output_file.write(f"{contributor[0]}\n")
