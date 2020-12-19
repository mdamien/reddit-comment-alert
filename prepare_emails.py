import json
from collections import Counter

link_counter = Counter([link.strip() for link in open('data/links')])

for link, n in link_counter.most_common():
    if n == 2:
        print('======')
        print(link)
        print('======')

        for comment in open('data/comments.jsonl'):
            comment = json.loads(comment)
            if link in comment['body'].lower():
                print(comment['author'], ':', comment['body'], '(', comment['permalink'], ')')
                print('------------------')