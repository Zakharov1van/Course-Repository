import requests


def get_images(url, accept_header):
    payload = {}
    headers = {
        'Accept': accept_header
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.status_code
