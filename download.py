import json
import requests
import tqdm
from datetime import datetime

before = None

for comment in tqdm.tqdm(open('data/comments.jsonl')):
    comment = json.loads(comment)
    before = comment['created_utc']

writer = open('data/comments.jsonl', 'a')

while True:
    url = "https://api.pushshift.io/reddit/search/comment/?q=&size=1000&subreddit=france" \
        + (f"&before={before}" if before else '')
    print(url)
    try:
        resp = requests.get(url)
        resp = resp.json()
    except:
        print(resp.text)
        break
    for comment in resp['data']:
        writer.write(json.dumps(comment)+'\n')
        before = comment['created_utc']
    print(datetime.fromtimestamp(before))