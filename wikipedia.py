
import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"


def get_wikipedia_results(search):
    PARAMS = {
        "action": "query",
        "generator": "search",
        "prop": "info",
        "inprop": "url",
        "gsrsearch": search,
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    entries = DATA['query']['pages']
    # print(entries)
    result = []
    for id in entries:
        # print(id)
        entry = entries[id]
        result.append({
        "title":entry['title'],
        "url":entry['fullurl']
        })
    return result

# test = get_wikipedia_results("lego")
# print(test)