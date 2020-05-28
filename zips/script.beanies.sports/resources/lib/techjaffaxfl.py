import requests
import re
import base64
from bs4 import BeautifulSoup
#import xbmcgui


agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
u_link = 'http://crackstreams.com/xflstreams/'


game_list = []


def get_games():
    html = requests.get(u_link, headers={'user-agent': agent})
    soup = BeautifulSoup(html.content, 'html.parser')
    games = soup.select(".btn.btn-default.btn-lg.btn-block")
    for game in games:
        game_list.append({"title": game.text.strip().encode(
            "ascii"), "link": game['href'].encode("ascii")})

    return game_list

# print(get_games())


stream = []


def get_stream(link):
    html = requests.get(link, headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify)
    iframe = re.compile('<iframe allowfullscreen="" frameborder="0" height="576" src="(.+?)" width="100%"',
                        re.DOTALL).findall(str(soup.prettify))
    # print(iframe)
    if iframe:
        iframe = iframe[0]
        htmlContent = requests.get(
            iframe, headers={"user-agent": agent, "referer": link}).content
        # print(htmlContent)
        soup = BeautifulSoup(htmlContent, 'html.parser')
        content = str(soup.prettify)
        #content = content.replace("atob('","")
        # print(content)
        encrypt = re.compile("atob\(.+?\)", re.DOTALL).findall(content)
        # print(encrypt)
        if encrypt:
            encrypt = encrypt[0]
            encrypt = encrypt.replace("atob(", "").replace("')", "")
            #xbmcgui.Dialog().textviewer('Error', str(encrypt))
            #atobI = encrypt.find("window.atob")
            #encrypt = encrypt[:atobI]
            # print(encrypt)
            decrypt = base64.b64decode(encrypt)
            #xbmcgui.Dialog().textviewer('Error', str(decrypt))
            # print(decrypt)
            stream.append({"title": '[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                           "link": decrypt + "|User-Agent=" + agent + "&Referer=" + iframe})
        else:
            pass
    else:
        pass
    return stream

# print(get_stream('http://nbastreams.xyz/live/1/'))
