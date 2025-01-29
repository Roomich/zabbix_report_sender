import requests
from dotenv import load_dotenv

import request_params


load_dotenv()

params = (
    request_params.URL,
    request_params.DATA or None,
    request_params.HEADERS or None
)


def get_responce_from_server(params):
    url, data, headers = params
    response = requests.get(
        url=url,
        data=data,
        headers=headers
    )
    return response


print(get_responce_from_server(params).status_code)
