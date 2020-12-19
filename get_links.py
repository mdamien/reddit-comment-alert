import json
import markdown
from urllib.parse import urlparse
import tqdm
from bs4 import BeautifulSoup


for comment in tqdm.tqdm(open('data/comments.jsonl')):
    comment = json.loads(comment)
    comment = BeautifulSoup(markdown.markdown(comment['body']), 'lxml')
    for a in comment.select('a'):
        if 'http' in a['href']:
            domain = urlparse(a['href']).netloc
            print(domain, sep='')
