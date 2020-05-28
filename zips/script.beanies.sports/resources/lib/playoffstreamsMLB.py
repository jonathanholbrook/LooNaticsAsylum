from bs4 import BeautifulSoup
import requests
import re
import os
'''
import xbmc
import sys

chkV = (xbmc.getInfoLabel('System.BuildVersion')) 

if chkV.startswith('17'):
    myPath = sys.path[0] + '/resources/xml' 
else:
    myPath = os.path.dirname(__file__).replace('lib','xml')

'''
#This method will scrape the GamesList
playOffStreamMLBPlayList = []
gameList =[]
def getMLBList():
    url = r"http://playoffsstream.live/reddit-mlb-streams"
    http_request = requests.get(url)
    http_response = http_request.content
    soup = BeautifulSoup(http_response, 'html.parser')
    mlb_list = soup.find_all('a',attrs={'class':'btn btn-info btn-block'})
    for game in mlb_list:
        #print(game['title'])
        try:
            title = game['title']
            time = game.findChild().text
            #print(game.findChild().text)
        except:
            time = ''
            print('')
        gameList.append({'title': title.encode('ascii','ignore'), 'time':time})
    return gameList    
        
#This method only check for the stream if user click on that specific name
def getStream(name):
    url = r"http://playoffsstream.live/reddit-mlb-streams"
    http_request = requests.get(url)
    http_response = http_request.content
    soup = BeautifulSoup(http_response, 'html.parser')
    mlb_list = soup.find_all('a',attrs={'class':'btn btn-info btn-block'})
    for game in mlb_list:
        #print(game['title'])
        title = game['title']
        title = title.encode('ascii','ignore')
        if name in str(title):
            #print('inside if')
            link = "http://www.playoffstream.com" + game['href']
            token = requests.get("http://172.105.26.201/mlbs.txt").content
            auth = "|Cookie=Authorization=" + token
            streamRequest = requests.get(link).content
            #print(streamRequest)
            soup = BeautifulSoup(streamRequest, 'html.parser')
            m3u8_URI = re.compile('\s=\s"(.+?)";', re.DOTALL).findall(str(soup.prettify))
            #print(m3u8_URI)
            
            if len(m3u8_URI) > 1:
                m3u8_name = str(m3u8_URI[1]).split('/')[-1]
                #print(m3u8_name)
                bitRateLink = str(m3u8_URI[1]).replace(m3u8_name,'').strip()
                #print(bitRateLink)
                URI_response = requests.get(m3u8_URI[1])
                bitrates = re.compile("\\n[^#].*?\.m3u8\\n").findall(URI_response.text)
                #print(bitrates)
                #return
                for bitrate in bitrates:
                    bitRate = int(bitrate.split('/')[-2].replace('K','').replace('k',''))
                    #print(bitRate)
                    if bitRate >= 1800:
                        bitrate = bitrate.replace('complete','slide')
                        playOffStreamMLBPlayList.append({'title':title, 'stream':bitRateLink + bitrate.strip("\n") + auth, 'quality':bitRate})

            elif len(m3u8_URI) == 1:
                m3u8_name = str(m3u8_URI[0]).split('/')[-1]
                #print(m3u8_name)
                bitRateLink = str(m3u8_URI[0]).replace(m3u8_name,'').strip()
                #print(bitRateLink)
                URI_response = requests.get(m3u8_URI[0])
                bitrates = re.compile("\\n[^#].*?\.m3u8\\n").findall(URI_response.text)
                #print(bitrates)
                #return
                for bitrate in bitrates:
                    bitRate = int(bitrate.split('/')[-2].replace('K','').replace('k',''))
                    #print(bitRate)
                    if bitRate >= 1800:
                        bitrate = bitrate.replace('complete','slide')
                        playOffStreamMLBPlayList.append({'title':title, 'stream':bitRateLink + bitrate.strip("\n") + auth, 'quality':bitRate})

                
                        #print(bitrate)
        else:
            continue
        return playOffStreamMLBPlayList
#print(getMLBList())
#print(getStream("MLB Network Live Stream"))
