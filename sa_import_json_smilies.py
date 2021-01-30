# Coded by DerVerrater#1769 ~=Bad Games Crew=~ 
# Use at your own risk!! -- No support at all...
# Variables in CAPITAL_LETTERS have to be changed to your values.  Don't be a dork!

import collections
import json
import os
import pprint
import itertools

def breakdown(l, size):
    for i in range(0, len(l), size):
        yield list(itertools.islice(l, i, i + size))

with open('./NAME_OF_FILE_GOES_HERE.json', 'r') as f:
    i = json.loads(f.read())

od = []

for tt_class in i['ul']:
    for emote in tt_class['li']:
        name = emote['div']['#text']
        url = emote['img']['@src']
        od.append({
            'name': name,
            'url': url
        })


bd = list(breakdown(od, 29))

fc = 0
for down in bd:
    oud = collections.OrderedDict()
    oud.update({'name': 'NAME OF YOUR LIST GOES HERE'})
    oud.update({'author': 'YOUR STUPID NAME GOES HERE'})
    oud.update({'emotes': []})
    for emote in down:
        # print(emote)
        oud['emotes'].append({
            'name': emote['name'],
            'url': emote['url']
        })
    print(oud)
    with open('OUTPUTNAMEGOESHERE'+str(fc)+'.json', 'w+') as f:
        json.dump(oud, f, indent=4)
    fc = fc+1