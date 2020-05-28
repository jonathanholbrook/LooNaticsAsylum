import requests
import re
from bs4 import BeautifulSoup
import xbmcgui

agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
u_link = 'http://acesportz.jdevcloud.com/'
game_list = []


def get_games():
    html = requests.get(u_link, headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    event = soup.find_all('div',attrs={'class':"innerpage_news_title"})
    for game in event:
        title = game.a.text.encode('ascii','ignore')
        link = game.a['href']
        game_list.append({'title':title,'link':link})
    return game_list


stream = []
def get_stream(link):
    html = requests.get(link,headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    m3u8 = re.compile("source: '(.+?)'",re.DOTALL).findall(str(soup.prettify))
    if m3u8:
        m3u8 = m3u8[0]
        stream.append({'stream':m3u8 + '|User-Agent=' + agent + '&referer=' + link})
        return stream
    else:
        return stream