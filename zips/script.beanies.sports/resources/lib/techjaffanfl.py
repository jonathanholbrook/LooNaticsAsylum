import requests
import re
import base64
from bs4 import BeautifulSoup


agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
u_link = 'http://crackstreams.com/nflstreams/'


game_list = []


def get_games():
    html = requests.get(u_link, headers={'user-agent': agent})
    soup = BeautifulSoup(html.content, 'html.parser')
    anchor = soup.find_all('a', class_={'btn btn-default btn-lg btn-block'})
    for a in anchor:
        link = a['href']
        title = a.find('h4', class_={'media-heading'}).text
        game_list.append({'title': title.encode('ascii'),
                          'link': link.encode("ascii")})
    return game_list


stream = []


def get_stream(link):
    html = requests.get(link, headers={'user-agent': agent}).content
    soup = BeautifulSoup(html, 'html.parser')
    iframe = re.compile('<iframe allowfullscreen="" frameborder="0" height="576" src="(.+?)" width="100%"',
                        re.DOTALL).findall(str(soup.prettify))
    if iframe:
        iframe = iframe[0]
        htmlContent = requests.get(
            iframe, headers={"user-agent": agent, "referer": link}).content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        content = str(soup.prettify)
        encrypt = re.compile("atob\(.+?\)", re.DOTALL).findall(content)
        if encrypt:
            encrypt = encrypt[0]
            encrypt = encrypt.replace("atob(", "").replace("')", "")
            decrypt = base64.b64decode(encrypt)
            stream.append({"title": "TITLE", "link": decrypt +
                           "|User-Agent=" + agent + "&Referer=" + iframe})
        else:
            pass
    else:
        pass
    return stream
