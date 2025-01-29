import os

import requests
from dotenv import load_dotenv


load_dotenv()

response = requests.get(
    url=os.getenv('ZABBIX_SERVER_URL'),
    data={
        'jsonrpc': '2.0',
        'method': 'apiinfo.version',
        'params': {},
        'id': 1
    },
    headers={
        'Content-Type': 'application/json-rpc'
    })

print(response)
