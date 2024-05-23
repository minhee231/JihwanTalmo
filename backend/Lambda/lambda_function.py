import json
import requests

def lambda_handler(event, context):
    url = "https://indexp.jihwan-talmo.x-coll.com/add/talmo-gione"
    r = requests.get(url)
    return r.text