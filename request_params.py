import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('ZABBIX_SERVER_API_TOKEN')

delta = timedelta(days=5)
end_date = datetime.now()
start_date = end_date - delta

end_date = str(end_date.timestamp()).split('.')[0]
start_date = str(start_date.timestamp()).split('.')[0]

URL = os.getenv('ZABBIX_SERVER_URL')
DATA = {
    "jsonrpc": "2.0",
    "method": "event.get",
    "params": {
        "tags": [
                    {
                        "tag": "service",
                        "value": "АИС паспорт",
                        "operator": "1"
                    },
                    {
                        "tag": "service",
                        "value": "Адаптер МВД",
                        "operator": "1"
                    },
                    {
                        "tag": "service",
                        "value": "Регистр населения",
                        "operator": "1"
                    }
                ],
        "time_from": start_date,
        "time_till": end_date,
        "output": [
            "eventid",
            "clock",
            "name",
            "r_eventid"
        ],
        "selectTags": ["value"],
        "sortorder": "desc"
    },
    "id": 1
}
HEADERS = {
    "Authorization": f"bearer {TOKEN}"
}
