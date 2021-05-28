#!/usr/bin/env python3

import requests
import datetime
import json
import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.environ['USERNAME']
# コンテストサイトのリソースIDをカンマ区切りで記述
RESOURCE_IDS="1,93"
API_KEY = os.environ['API_KEY']

headers = {'content-type': 'application/json'}

payload = {}
payload['resource_id__in'] = RESOURCE_IDS
payload['username'] = USERNAME
payload['api_key'] = API_KEY
payload['order_by'] = "start"

dt_now = datetime.datetime.now(datetime.timezone.utc)
start_date=dt_now.isoformat()[:19]

payload['start__gt'] = start_date

api_url = "https://clist.by/api/v2/contest/"

response = requests.get(api_url, params=payload, headers=headers).json()

print("contest information")
print("---")

for object in response['objects']:
    dt = datetime.datetime.fromisoformat(object['start']) + datetime.timedelta(hours=9)
    print(dt.isoformat()[5:-3] + " [" + dt.strftime('%a') + "] ", end="")
    print(object['event'], end="")
    print(f"|href={object['href']}")