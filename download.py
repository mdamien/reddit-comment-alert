import json
import requests
from datetime import datetime

before = None

writer = open('data/comments.jsonl', 'w')

while True:
    url = "https://api.pushshift.io/reddit/search/comment/?q=&size=1000&subreddit=france" \
        + (f"&before={before}" if before else '')
    print(url)
    resp = requests.get(url).json()
    for comment in resp['data']:
        writer.write(json.dumps(comment)+'\n')
        before = comment['created_utc']
    print(datetime.fromtimestamp(before))