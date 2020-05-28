import requests
from bs4 import BeautifulSoup
import re
gameList = []
def get_games():
    url = "http://60fps.live/league/boxing-mma-ufc-live-stream/"
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    htmlContent = requests.get(url,headers={"user-agent":agent}).content
    soup = BeautifulSoup(htmlContent,'html.parser')
    newerPostsURL = soup.select(".next.page-numbers")
    if newerPostsURL:
        url = newerPostsURL[0]['href'].encode("ascii")
        htmlContent = requests.get(url, headers={"user-agent":agent}).content
        soup = BeautifulSoup(htmlContent,'html.parser')
        links = soup.find_all("h3",attrs={"class":"rapidwp-fp05-post-title"})
        for link in links:
            try:
                gameList.append({"title":link.text.strip().encode("ascii"),"link":link.a['href'].encode("ascii")})
            except:
                continue        
    else:
        links = soup.find_all("h3",attrs={"class":"rapidwp-fp05-post-title"})
        for link in links:
            try:
                gameList.append({"title":link.text.strip().encode("ascii"),"link":link.a['href'].encode("ascii")})
            except:
                continue

    return gameList


streamList = []

def get_stream(url):
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    htmlContent = requests.get(url,headers={"user-agent":agent}).content
    soup = BeautifulSoup(htmlContent,"html.parser")
    master = re.compile("var hanturl='(.+?)'",re.DOTALL).findall(str(soup.prettify))
    
    if master:
        master = master[0].encode("ascii")
        master = master + "|referer=" + url
        streamList.append({"title":"[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]","url":master})
    else:
        streamURL = soup.select(".title")[0]['href']
        htmlContent = requests.get(streamURL,headers={"user-agent":agent}).content
        soup = BeautifulSoup(htmlContent,"html.parser")
        master = re.compile("var hanturl='(.+?)'",re.DOTALL).findall(str(soup.prettify))
        if master:
            master = master[0].encode("ascii")
            master = master + "|referer=" + url
            streamList.append({"title":"[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]","url":master})

    return streamList

