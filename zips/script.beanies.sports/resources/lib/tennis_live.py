import requests
import re
from bs4 import BeautifulSoup

agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
u_link = 'https://live-tennis.stream/'
game_list = []


def get_games():
    html = requests.get(u_link, headers={'user-agent': agent}).content
    soup = BeautifulSoup(html,'html.parser')
    data = soup.find_all('td',attrs={'class':'time'})
    for d in data:
        title = d.find(itemprop="name")
        link = d.find(itemprop="url")
        time = d.find(attrs={'class': "timegmt"}).text
        #print(title['content'])
        #print(link['content'])
        game_list.append({'time':time,'title':title['content'],'link':link['content']})

    return game_list
#print(get_games())


stream = []


def get_stream(link):
    html = requests.get(link, headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    frame = soup.find('iframe')
    if frame:
        frame = frame['src']
        master = requests.get(frame, headers={'referer': link}).content
        soup = BeautifulSoup(master, 'html.parser')
        clapper = re.compile('Clappr.Player', re.DOTALL).findall(
            str(soup.prettify))
        for m3u8 in clapper:
            m3u8 = re.compile("source: '(.+?)'",
                              re.DOTALL).findall(str(soup.prettify))
            m3u8 = m3u8[0]
            m3u8 = m3u8 + '|User-Agent:' + agent + '&Referer=' + frame
        stream.append({'title': 'THIS', 'link': m3u8})
        pass
    else:
        pass

    return stream
# print(get_stream('FINALLY'))
