import requests
import re
from bs4 import BeautifulSoup
import base64
import xbmcgui

agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

game_list = []


def get_games():
    html = ''
    html += requests.get('http://myustv.com/page/1/', headers={'user-agent': agent}).content
    html += requests.get('http://myustv.com/watch/category/united-states-usa-tv-channel/page/2/', headers={'user-agent': agent}).content
    html += requests.get('http://myustv.com/watch/category/united-states-usa-tv-channel/page/3/', headers={'user-agent': agent}).content
    html += requests.get('http://myustv.com/watch/category/united-states-usa-tv-channel/page/4/', headers={'user-agent': agent}).content
    html += requests.get('http://myustv.com/watch/category/united-states-usa-tv-channel/page/5/', headers={'user-agent': agent}).content
    html += requests.get('http://myustv.com/watch/category/united-states-usa-tv-channel/page/6/', headers={'user-agent': agent}).content
    html += requests.get('http://myustv.com/watch/category/united-states-usa-tv-channel/page/7/', headers={'user-agent': agent}).content
    html += requests.get('http://myustv.com/watch/category/united-states-usa-tv-channel/page/8/', headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    event = soup.find_all('h3', attrs={'class': "entry-title td-module-title"})
    for game in event:
        title = game.a.text.encode('ascii', 'ignore')
        link = game.a['href']
        game_list.append({'title': title, 'link': link})
    return game_list


stream = []


def get_stream(link):
    html = requests.get(link, headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    content = str(soup.prettify)
    encrypt = re.compile("atob\(.+?\)", re.DOTALL).findall(content)
    if encrypt:
        encrypt = encrypt[0]
        encrypt = encrypt.replace("atob(", "").replace("')", "")
        decrypt = base64.b64decode(encrypt)
        stream.append({'title': '[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]','stream': decrypt + "|User-Agent=" + agent + "&Referer=" + link})
    else:
        pass

    return stream