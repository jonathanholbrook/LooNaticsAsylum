import requests
import re
from bs4 import BeautifulSoup
import base64

agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
u_link = 'http://quaynet.us/category/nfl-streams/'
game_list = []


def get_games():
    html = requests.get(u_link, headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    event = soup.find_all('h2',attrs={'class':"post-title"})
    for game in event:
        title = game.a.text.encode('ascii','ignore')
        link = game.a['href']
        game_list.append({'title':title,'link':link})
    return game_list

stream = []
def get_stream(link):
    html = requests.get(link,headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    content = str(soup.prettify)
    encrypt = re.compile("atob\(.+?\)",re.DOTALL).findall(content)
    if encrypt:
        encrypt = encrypt[0]
        encrypt = encrypt.replace("atob(","").replace("')","")
        decrypt = base64.b64decode(encrypt)
        stream.append({'title': '[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                       'stream': decrypt + "|User-Agent=" + agent + "&Referer=" + link})
    else:
        pass

    return stream
