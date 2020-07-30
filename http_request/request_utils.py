import requests


def request_download_file_by_url(download_url, file_name):
    r = requests.get(download_url)
    with open(file_name, 'wb') as f:
        f.write(r.content)
