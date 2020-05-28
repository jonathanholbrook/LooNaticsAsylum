import requests
from bs4 import BeautifulSoup
import re
import base64
from resources.lib import cfscrape
game = []

def get_games():
    scraper = cfscrape.create_scraper()
    url = "http://yoursports.stream/"
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    htmlContent = scraper.get(url,headers={"user-agent":agent}).content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    nhl = soup.select("#nhl")
    if nhl:
        divs = nhl[0].select(".w3-center")
        for div in divs:
            title = div.select(".w3-medium")[0].text
            links = div.select(".w3-button.w3-bar-item.w3-hover-blue-gray.w3-black.w3-padding-small.w3-tiny.w3-border.w3-border-blue-gray")
            for link in links:
                Title = title + "  "  + link['title']
                url = link['href']

                if "http" not in url:
                    url = "http://yoursports.stream/" + url
                else:
                    pass
                game.append({"title":Title.encode("ascii"),"link":url.encode("ascii")})
        
        
    else:
        pass

    return game

stream = []
def get_stream(link):
    nhlToken = requests.get('https://bitbucket.org/threw/textfiles/raw/master/nhl.txt').content
    nhl_auth = "|Cookie=Authorization=" + nhlToken
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
        iframe = soup.select("#player")
        if iframe:
            iframe = iframe[0]['src']
            if "http" not in iframe:
                iframe = "http://yoursports.stream/" + iframe
            htmlContent = scraper.get(iframe,headers={"user-agent":agent,"referer":link}).content
            soup = BeautifulSoup(htmlContent,'html.parser')
            content = str(soup.prettify)
            encrypt = re.compile("atob\(.+?\)",re.DOTALL).findall(content)
            if encrypt:
                encrypt = encrypt[0]
                encrypt = encrypt.replace("atob('","").replace("')","")
                decrypt = base64.b64decode(encrypt)
                decrypt = decrypt.encode("ascii")
                decrypt = decrypt + nhl_auth
                stream.append({"title":"[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]","link":decrypt.encode("ascii")})
            else:
                pass
                
        else:
            pass
        

    return stream
