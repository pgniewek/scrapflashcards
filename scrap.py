import sys
import requests
import json

wiki_api = "https://en.wikipedia.org/w/api.php"

def getCategoryMembers(title, amount):
    requestsParams = {}
    requestsParams["action"] = "query"
    requestsParams["list"] = "categorymembers"
    requestsParams["format"] = "json"
    requestsParams["cmtitle"] = title
    requestsParams["cmlimit"] = str(amount)
    with requests.get(wiki_api, params=requestsParams) as r:
        contents = json.loads(r.text)
    return contents[requestsParams["action"]][requestsParams["list"]]
    

def main():
    requestedList = getCategoryMembers("Category:History_of_Poland_during_the_Piast_dynasty", 1)
    for page in requestedList:
        print(page["title"])

def init():
    if __name__ == '__main__':
        sys.exit(main())

init()
