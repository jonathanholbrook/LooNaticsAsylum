import requests
import re
from bs4 import BeautifulSoup
from resources.lib.modules import client
import xbmcgui

agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
u_link = 'https://sportsbay.org/sports/tv-channels'
game_list = []


def get_games():
    html = requests.get(u_link, headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    event = soup.find_all('a',attrs={'class':"url summary"})
    for game in event:
        title = game.text.encode('ascii','ignore')
        #xbmcgui.Dialog().textviewer('Error', str(title))
        link = game['href']
        if "http" not in link:
            link = "https://sportsbay.org" + link
        game_list.append({'title':title,'link':link})
    return game_list



stream = []


def get_stream(link):
    html = requests.get(link, headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    frame = soup.find('iframe')
    if frame:
        frame = frame['src']
        if "http" not in frame:
            frame = "https://sportsbay.org" + frame
            master = requests.get(frame, headers={'referer': link}).content
            soup = BeautifulSoup(master, 'html.parser')
            clapper = re.compile('new Clappr.Player', re.DOTALL).findall(str(soup.prettify))
            for m3u8 in clapper:
                m3u8 = re.compile("source: '(.+?)'",re.DOTALL).findall(str(soup.prettify))
                m3u8 = m3u8[0]
                m3u8 = m3u8 + '|User-Agent:' + agent + '&Referer=' + frame
        stream.append({'title': 'THIS', 'link': m3u8})
        pass
    else:
        pass

    return stream
