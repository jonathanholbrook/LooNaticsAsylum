import requests
import re
from bs4 import BeautifulSoup
import xbmcgui

agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
u_link = 'http://markky88.com/ligue-1/'

gameList = []
def get_games():
    html = requests.get(u_link,headers={"user-agent":agent}).content
    soup = BeautifulSoup(html,'html.parser')
    newerPostsURL = soup.select(".next.page-numbers")
    if newerPostsURL:
        url = newerPostsURL[0]['href'].encode("ascii")
        html = requests.get(url, headers={"user-agent":agent}).content
        soup = BeautifulSoup(html,'html.parser')
        links = soup.find_all("h2",attrs={"class":"entry-title"})
        for link in links:
            try:
                gameList.append({"title":link.text.strip().encode("ascii"),"link":link.a['href'].encode("ascii")})
            except:
                continue        
    else:
        links = soup.find_all("h2",attrs={"class":"entry-title"})
        for link in links:
            try:
                gameList.append({"title":link.text.strip().encode("ascii"),"link":link.a['href'].encode("ascii")})
            except:
                continue

    return gameList

stream = []
def get_stream(link):
    html = requests.get(link,headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    m3u8 = re.compile('source: "(.+?)"',re.DOTALL).findall(str(soup.prettify))
    if m3u8:
        m3u8 = m3u8[0]
        stream.append({'stream':m3u8 + '|User-Agent=' + agent + '&referer=' + link})
        return stream
    else:
        return stream