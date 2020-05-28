import requests
from bs4 import BeautifulSoup
import re
from resources.lib import cfscrape

game_list = []
nhlToken = requests.get('https://bitbucket.org/threw/textfiles/raw/master/nhl.txt').content
nhl_auth = "|Cookie=Authorization=" + nhlToken

def get_games():
    scraper = cfscrape.create_scraper()
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    html = scraper.get(r"http://www.volokit.com/all-games/schedule/nhl.php",headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    anchor = soup.find_all('a',attrs={'class':"url hidden-xs-down summary"})
    for a in anchor:
        link = a['href']
        title = link.split('/')[-2]
        title = title.upper()
        game_list.append({'title':title.encode('ascii','ignore'),'link':link.encode('ascii','ignore')})
        
    return game_list

feeds = []
def get_feeds(link):
    scraper = cfscrape.create_scraper()
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    html = scraper.get(link,headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    test = soup.select(".feedsbtns")
    if test:
        test = test[0]
        button_list = test.find_all("button")
        if button_list:
            for button in button_list:
                feed_name = button.text.strip().encode("ascii")
                findings = re.compile("src='(.+?)'",re.DOTALL).findall(str(button))
                findings = findings[0]
                url = "http://www.volokit.com" + findings
                feeds.append({"name":feed_name,"feed":url})
            return feeds
        else:
            pass
    else:
        pass
   

stream = []
def get_stream(link):
    scraper = cfscrape.create_scraper()
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    html = scraper.get(link,headers={'user-agent':agent}).content
    soup = BeautifulSoup(html,'html.parser')
    m3u8 = re.compile('var data = {source:"(.+?)"',re.DOTALL).findall(str(soup.prettify))
    if m3u8:
        m3u8 = m3u8[0]
    stream.append({"stream":m3u8 + nhl_auth})
    return stream
