import requests
from bs4 import BeautifulSoup
import re
from resources.lib import cfscrape

game_list = []

def get_games():
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    scraper = cfscrape.create_scraper()
    html = scraper.get(r"http://www.volokit.com/all-games/schedule/mlb.php",headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    anchor = soup.find_all('a',attrs={'class':"url hidden-xs-down summary"})
    for a in anchor:
        link = a['href']
        title = link.split('/')[-2]
        title = title.upper()
        game_list.append({'title':title.encode('ascii','ignore'),'link':link.encode('ascii','ignore')})
        
    return game_list

stream = []
def get_stream(link):
    scraper = cfscrape.create_scraper()
    token = scraper.get("http://172.105.26.201/mlbs.txt").content
    auth =  "|Cookie=Authorization=" + token
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    html = scraper.get(link,headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    frame = soup.find('iframe',{'id':'volokit-feed'})
    frame = frame['src']
    frame = 'http://www.volokit.com' + frame
    master = scraper.get(frame,headers={'user-agent':agent}).content
    soup = BeautifulSoup(master,'html.parser')
    m3u8 = re.compile('var data = {source:"(.+?)"',re.DOTALL).findall(str(soup.prettify))
    m3u8 = m3u8[0]
    var_one = str(m3u8).split('/')[-1]
    fetch = str(m3u8).replace(var_one,'').strip()
    data = requests.get(m3u8)
    rates = re.compile("\\n[^#].*?\.m3u8\\n").findall(data.text)
    for link in rates:
        bitRate = int(link.split ('/')[-2].replace ('K','').replace ('k',''))
        if bitRate >= 1800:
            link = link.replace('complete','slide')
            url = fetch + link.strip('\n') + auth
            stream.append({"stream":url.encode('ascii','ignore'), 'quality':bitRate})
    return stream




#print(get_stream("http://www.volokit.com/volostream/mlb-games/braves-vs-phillies/"))
#print(get_games())
