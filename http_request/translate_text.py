import requests,re,json,time
from html.parser import HTMLParser

# https://curl.trillworks.com/#
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 ' \
             'Safari/537.36 Edge/18.18362 '

get_header = {
           'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN',
           'Cache-Control': 'max-age=0',
           'DNT': '1',
           'Host': 'cn.bing.com',
           'Upgrade-Insecure-Requests': '1',
           'User_Agent': user_agent,
           }

post_header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN',
    'Cache-Control': 'max-age=0',
    'Content-type': 'application/x-www-form-urlencoded',
    'DNT': '1',
    'Host': 'cn.bing.com',
    'Origin': 'https://cn.bing.com',
    'Referer': 'https://cn.bing.com/translator/',
    'User_Agent': user_agent,
}


get_url = 'https://cn.bing.com/translator/'
session = requests.Session()
get_response = session.get(url=get_url)

htmltext = repr(get_response.text)

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if(data.startswith(r'//<![CDATA[\n_G=')):
            self.data = data  #.replace(r'//<![CDATA[\n_G=','')
        if(data.startswith(r'//<![CDATA[\nvar TranslatorWebTelemetry')):
            self.id_data = data #.replace(r'//<![CDATA[\nvar TranslatorWebTelemetry','')

parser = MyHTMLParser()
parser.feed(htmltext)
parser.close()
IG = parser.data
IG = IG[IG.index('IG:"')+4:IG.index('",Even')]
MUID = parser.id_data
MUID = (MUID[MUID.index('muid":"')+7:MUID.index('","f":')])
current_time = time.time()
post_url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG='+ IG +'&IID=translator.5028.1'
datas = {'fromLang': 'en',  'to': 'zh-Hans', 'text': 'jack'}

session = requests.session()
get_response = session.post(url=post_url, headers= post_header, data=datas)
print(get_response.json())