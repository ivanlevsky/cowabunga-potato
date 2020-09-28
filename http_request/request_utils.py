import requests,base64


def request_download_file_by_url(download_url, file_name):
    r = requests.get(download_url)
    with open(file_name, 'wb') as f:
        f.write(r.content)


def request_get_rss_news(rss_url):
    try:
        r = requests.get(rss_url)
        # print(r.encoding)
        print(r.text)
        return print('The scraping job succeeded: ', r.status_code)
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)

