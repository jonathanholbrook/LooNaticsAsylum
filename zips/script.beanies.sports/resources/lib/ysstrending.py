import requests
from bs4 import BeautifulSoup
from resources.lib import cfscrape
import re
import base64

game = []
def get_games():
    scraper = cfscrape.create_scraper()
    url = "http://yoursports.stream/games.js?x=1578846031"
    html = scraper.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    jsonList = re.compile("hawt=(.+?)];",re.DOTALL).findall(str(soup.prettify))
    jsonList = jsonList[0]
    jsonList = jsonList.replace("[","")
    titles = re.compile("chan:'(.+?)'",re.DOTALL).findall(jsonList)
    url = re.compile("url:'(.+?)'",re.DOTALL).findall(jsonList)
    prior = "http://yoursports.stream/live?v="
    index = len(titles)
    i = 0
    while (i < index):
        title = titles[i]
        link = prior + url[i]
        game.append({"title":title,"link":link})
        i += 1

    return game


stream = []
def get_stream(link):
    scraper = cfscrape.create_scraper()
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    htmlContent = scraper.get(link,headers={"user-agent":agent}).content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    iframe = re.compile('<iframe allowfullscreen="" allowtransparency="" frameborder="0" height="100%" scrolling="no" src="(.+?)"',re.DOTALL).findall(str(soup.prettify))
    if iframe:
        iframe = iframe[0]
        htmlContent = scraper.get(iframe,headers={"user-agent":agent,"referer":link}).content
        soup = BeautifulSoup(htmlContent,'html.parser')
        content = str(soup.prettify)
        encrypt = re.compile("atob\(.+?\)",re.DOTALL).findall(content)
        if encrypt:
            encrypt = encrypt[0]
            encrypt = encrypt.replace("atob('","").replace("')","")
            decrypt = base64.b64decode(encrypt)
            stream.append({"title":"[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]","link":decrypt + "|User-Agent=" + agent + "&Referer=" + iframe})
        else:
            pass
    else:
        pass

    return stream