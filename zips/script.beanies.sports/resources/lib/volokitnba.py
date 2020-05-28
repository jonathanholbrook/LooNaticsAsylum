import requests
from bs4 import BeautifulSoup
import re
from resources.lib import cfscrape

game_list = []

def get_games():
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    scraper = cfscrape.create_scraper()
    html = scraper.get(r"http://www.volokit.com//all-games/schedule/nba.php",headers={'user-agent':agent}).content
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
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    scraper = cfscrape.create_scraper()
    html = scraper.get(link,headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    frame = soup.find('iframe',{'id':'volokit-feed'})
    frame = frame['src']
    frame = 'http://www.volokit.com' + frame
    master = scraper.get(frame,headers={'user-agent':agent}).content
    soup = BeautifulSoup(master,'html.parser')
    m3u8 = re.compile('var data = {source:"(.+?)"',re.DOTALL).findall(str(soup.prettify))
    m3u8 = m3u8[0]
    stream.append({"stream":m3u8})
    return stream
