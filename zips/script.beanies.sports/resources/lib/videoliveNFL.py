import requests
import re
from bs4 import BeautifulSoup

game_list = []

def get_games():
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    '''class="clean-grid-grid-post-title"'''
    html = requests.get(r'http://nflnetwork.club/category/nfl/',headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    games = soup.find_all('h3',attrs={'class':"clean-grid-grid-post-title"})
    for game in games:
        title = game.a.text.encode('ascii','ignore')
        link = game.a['href']
        game_list.append({'title':title,'link':link.encode('ascii','ignore')})
    return game_list


#print(get_games())

stream = []
def get_stream(link):
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    html = requests.get(link,headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    m3u8 = re.compile("source: '(.+?)'",re.DOTALL).findall(str(soup.prettify))
    if m3u8:
        m3u8 = m3u8[0]
        stream.append({'stream': (m3u8 + '|referer=' + link)})
        return stream
    else:
        return stream

#print(get_stream('http://nflnetwork.club/nfl-network-live/'))
        
    
