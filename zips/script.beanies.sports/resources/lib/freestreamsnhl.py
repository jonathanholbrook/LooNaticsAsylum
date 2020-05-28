import requests
from bs4 import BeautifulSoup
import re

game_list = []
def get_games():
    url = "http://freestreams-live1.com/nhl-live-stream/"
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    htmlContent = requests.get(url,headers={"user-agent":agent}).content
    soup = BeautifulSoup(htmlContent,'html.parser')
    feeds = soup.select(".button")
    for f in feeds:
        title = f["href"].split("/")[-2].replace("-"," ").upper() + "  " +  f.text
        url = f["href"]
        game_list.append({"title":title.encode("ascii"),"link":url.encode("ascii")})
    return game_list



stream = []
def get_stream(link):
    nhlToken = requests.get('https://bitbucket.org/threw/textfiles/raw/master/nhl.txt').content
    nhl_auth = "|Cookie=Authorization=" + nhlToken
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    htmlContent = requests.get(link,headers={"user-agent":agent}).content
    soup = BeautifulSoup(htmlContent,'html.parser')
    iframe = soup.find_all("iframe")
    for frame in iframe:
        if "php" in frame['src']:
            newURL = frame['src']
            data = requests.get(newURL,headers={"user-agent":agent}).content
            soup = BeautifulSoup(data,'html.parser')
            master = re.compile(' var strm = "(.+?)"',re.DOTALL).findall(str(soup.prettify))
            if master:
                master = master[0]
                stream.append({"title":"Stream","link":master.encode("ascii") + nhl_auth})
                '''
                tempText = str (master)
                rText = str (master).split('/') [-1]
                bLink = str (master).replace(rText,'').replace('[\'', '').strip() 
                m3u8_response = requests.get(master)
                match_links = re.compile("\\n[^#].*?\.m3u8\\n").findall(m3u8_response.text)
                for link in match_links:
                    bitRate = int(link.split ('/')[-2].replace ('K','').replace ('k',''))
                    url = bLink + link.strip("\n")
                    url = url.encode("ascii") + nhl_auth
                    url = url.encode("ascii")
                    if bitRate >= 1800 : stream.append({'title':str(bitRate) + "k",'link':url})
                '''
            else:
                pass
            
            #stream.append({"title":"stream","link":master.replace("wired","complete") + nhl_auth})
    return stream

#print(get_stream('http://nhl.freestreams-live1.com/detroit-red-wings-live-stream/'))
