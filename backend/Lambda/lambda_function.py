import json
import requests

def lambda_handler(event, context):
    with open("./key.json", "r", encoding='utf-8') as file:
        key_data = json.load(file)

    INDEX_PAGE_KEY = key_data["index_page"]
    url = f"https://indexp.jihwan-talmo.x-coll.com/add/talmo-gione?auth_key={INDEX_PAGE_KEY}"
    r = requests.get(url)
    return r.text