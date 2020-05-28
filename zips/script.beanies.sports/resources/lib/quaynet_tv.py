import requests
import re
from bs4 import BeautifulSoup
import base64
import xbmcgui

agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

game_list = []
#xbmcgui.Dialog().textviewer('Error', str(data))

def get_games():
    html = ''
    html += requests.get('http://123tvsports.com/', headers={'user-agent': agent}).content
    html += requests.get('http://123tvsports.com/page/2/', headers={'user-agent': agent}).content
    html += requests.get('http://123tvsports.com/page/3/', headers={'user-agent': agent}).content
    html += requests.get('http://123tvsports.com/page/4/', headers={'user-agent': agent}).content
    html += requests.get('http://123tvsports.com/page/5/', headers={'user-agent': agent}).content
    html += requests.get('http://123tvsports.com/page/6/', headers={'user-agent': agent}).content
    html += requests.get('http://123tvsports.com/page/7/', headers={'user-agent': agent}).content
    html += requests.get('http://123tvsports.com/page/8/', headers={'user-agent': agent}).content
    html += requests.get('http://123tvsports.com/page/9/', headers={'user-agent': agent}).content
    html += requests.get('http://123tvsports.com/page/10/', headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    event = soup.find_all('h2', attrs={'class': "post-title"})
    #xbmcgui.Dialog().textviewer('Error', str(event))
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
    #xbmcgui.Dialog().textviewer('Error', str(encrypt))
    if encrypt:
        encrypt = encrypt[0]
        encrypt = encrypt.replace("atob(", "").replace("')", "")
        decrypt = base64.b64decode(encrypt)
        #xbmcgui.Dialog().textviewer('Error', str(decrypt))
        stream.append({'title': '[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]','stream': decrypt + "|User-Agent=" + agent + "&Referer=" + link})
    else:
        pass

    return stream