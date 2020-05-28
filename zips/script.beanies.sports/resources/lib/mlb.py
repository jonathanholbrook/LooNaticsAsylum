from bs4 import BeautifulSoup
import re
import requests
import operator
import xbmc
import os
import sys


chkV = (xbmc.getInfoLabel('System.BuildVersion')) 

if chkV.startswith('17'):
    myPath = sys.path[0] 
    myPath = myPath + '/resources/xml' 
else:
    myPath = os.path.dirname(__file__).replace('lib','xml')


outputFile = 'mlbstreams.xml'
saveXML = 'no'

mlb720List = []
mlb720Listt = []

def getSchedule():
    url = "http://www.720pstream.me/mlb-stream"
    mlbToken = requests.get("http://172.105.26.201/mlbs.txt").content
    mlbAuth = "|Cookie=Authorization=" + mlbToken
    html = requests.get(url).content
    soupObj = BeautifulSoup(html, 'html.parser')
    schedule_list = soupObj.find_all('div',attrs={'class':'gametime'})
    match = re.compile('<a\stitle=\"(.+?)Stream\"\shref=\"(.+?)\">',re.DOTALL).findall(html)
    i = 0
    for name, link in match:
        name = name.replace ('   Live ',' Live').replace ('Live ',' Live')
        if 'Network'  in name:
            schedule = "24 x 7"
        else:
            schedule = schedule_list[i].time.text
            i+=1
        mlb720Listt.append({'game':name, 'schedule':schedule})
    return mlb720Listt







def getStreams1():
    url = "http://www.720pstream.me/mlb-stream"
    mlbToken = requests.get("http://172.105.26.201/mlbs.txt").content
    mlbAuth = "|Cookie=Authorization=" + mlbToken
    html = requests.get(url).content
    soupObj = BeautifulSoup(html, 'html.parser')
    schedule_list = soupObj.find_all('div',attrs={'class':'gametime'})
    match = re.compile('<a\stitle=\"(.+?)Stream\"\shref=\"(.+?)\">',re.DOTALL).findall(html)
    i = 0
    for name, link in match:
        name = name.replace ('   Live ',' Live').replace ('Live ',' Live')
        if 'Network'  in name:
            schedule = "24 x 7"
        else:
            schedule = schedule_list[i].time.text
            i+=1
        mlb720Listt.append({'game':name, 'schedule':schedule})
        
        if "http" not in link:
            link = "http://www.720pstream.me" + link
        #print(name)
        #print(link)
        soup = BeautifulSoup(requests.get(link).content, 'html.parser')
        match2 = re.compile("videoURI\s=\s'(.+?)';",re.DOTALL).findall(str(soup.prettify))
        if len(match2) != 0:
            rText = str (match2[0]).split('/') [-1]
            #print(rText)
            bLink = str (match2[0]).replace(rText,'').strip()
            #print(bLink)
            m3u8_response = requests.get(*match2)
            #print(m3u8_response)
            match_links = re.compile("\\n[^#].*?\.m3u8\\n").findall(m3u8_response.text)
            #print(match_links)
            for link in match_links:
                bitRate = int(link.split ('/')[-2].replace ('K','').replace ('k',''))
                if bitRate >= 1800:
                    link = link.replace ('complete','slide')
                    mlb720List.append({'game':name,'stream':bLink + link.strip("\n") + mlbAuth,'quality':bitRate,'schedule':schedule})
                #if bitRate == 1800 or bitRate == 2500 or bitRate == 3500 or bitRate == 5600:
                #    mlb720List.append({'game':name,'stream':bLink + link.strip("\n") + mlbAuth,'quality':bitRate,'schedule':schedule})
        
        else:
            pass
            #    mlb720Listt.append({'game':name, 'schedule':schedule})
            #    print("[+] No live Streams So Far")

    mlb720List.sort(key = operator.itemgetter('game' , 'quality' ))

    return mlb720List #    , mlb720Listt

########
def getStreams(tName):
    tName = tName.replace (' Live','')
    print ('recd tname - ' + str (tName))
    url = "http://www.720pstream.me/mlb-stream"
    mlbToken = requests.get("http://172.105.26.201/mlbs.txt").content
    mlbAuth = "|Cookie=Authorization=" + mlbToken
    html = requests.get(url).content
    soupObj = BeautifulSoup(html, 'html.parser')
    schedule_list = soupObj.find_all('div',attrs={'class':'gametime'})
    match = re.compile('<a\stitle=\"(.+?)Stream\"\shref=\"(.+?)\">',re.DOTALL).findall(html)
    i = 0
    for name, link in match:
        print ('searching name - ' + str (name))
        if tName.upper () in name.upper ():
            print ('found tname - ' + str (tName))
            name = name.replace ('   Live ',' Live').replace ('Live ',' Live')
            if 'Network'  in name:
                schedule = "24 x 7"
            else:
                schedule = schedule_list[i].time.text
                i+=1
            mlb720Listt.append({'game':name, 'schedule':schedule})
        
            if "http" not in link:
                link = "http://www.720pstream.me" + link
            #print(name)
            #print(link)
            soup = BeautifulSoup(requests.get(link).content, 'html.parser')
            match2 = re.compile("videoURI\s=\s'(.+?)';",re.DOTALL).findall(str(soup.prettify))
            if len(match2) != 0:
                rText = str (match2[0]).split('/') [-1]
                #print(rText)
                bLink = str (match2[0]).replace(rText,'').strip()
                #print(bLink)
                m3u8_response = requests.get(*match2)
                #print(m3u8_response)
                match_links = re.compile("\\n[^#].*?\.m3u8\\n").findall(m3u8_response.text)
                #print(match_links)
                for link in match_links:
                    bitRate = int(link.split ('/')[-2].replace ('K','').replace ('k',''))
                    if bitRate >= 1800:
                        link = link.replace ('complete','slide')
                        mlb720List.append({'game':name,'stream':bLink + link.strip("\n") + mlbAuth,'quality':bitRate,'schedule':schedule})
                    #if bitRate == 1800 or bitRate == 2500 or bitRate == 3500 or bitRate == 5600:
                    #    mlb720List.append({'game':name,'stream':bLink + link.strip("\n") + mlbAuth,'quality':bitRate,'schedule':schedule})
        
            else:
                pass
                #    mlb720Listt.append({'game':name, 'schedule':schedule})
                #    print("[+] No live Streams So Far")

        mlb720List.sort(key = operator.itemgetter('game' , 'quality' ))

    return mlb720List #    , mlb720Listt
    


   
#TESTING
#mlb720List, mlb720Listt = getStreams()
#print(mlb720Listt)

def getMLB():
    mlb720List,mlb720Listt = getStreams()
    #    mlb720List  = getStreams()
    if mlb720List:
        for items in mlb720List:
            game =items.get('game','Game Missing')
            stream =items.get('stream','Stream Missing')
            quality =items.get('quality','Quality Missing')
            #print '  ' + 'Game = '+ str (game)
            #print '  ' +  'BitRate = '+ str (quality) +'k'
            if saveXML.lower() == 'yes':
                with open(os.path.join(myPath, outputFile), "a") as file:
                    f.write("<item> \n {} \n {} \n {} \n <thumbnail></thumbnail> \n <fanart></fanart> \n </item>\n".format(
                        game, stream, quality))
    if mlb720Listt:
        for items in mlb720List:
            game =items.get('game','Game Missing')
            #stream =items.get('stream','Stream Missing')
            #quality =items.get('quality','Quality Missing')
            #print '  ' + 'Game = '+ str (game)
            #print '  ' +  'BitRate = '+ str (quality) +'k'
            if saveXML.lower() == 'yes':
                with open(os.path.join(myPath, outputFile), "a") as file:
                    f.write("<item> \n {} \n {} \n {} \n <thumbnail></thumbnail> \n <fanart></fanart> \n </item>\n".format(
                        game, '', ''))
        

    else:
        pass
    return mlb720List, mlb720Listt


'''
with open(r'C:\Users\NightmaRe\Documents\720pstream SOURCE\sample.html') as file:
    soup = BeautifulSoup(file,'html.parser')
    '''
'''
    print(soup.prettify)
    scripts = soup.find_all('script')
    print(scripts)
    for script in scripts:
        print(script)
        '''
'''
'''
'''        
    match2 = re.compile("videoURI\s=\s'(.+?)';",re.DOTALL).findall(str(soup.prettify))
    rText = str (match2[0]).split('/') [-1]
    print(rText)
    bLink = str (match2[0]).replace(rText,'').strip()
    print(bLink)
    m3u8_response = requests.get(*match2)
    print(m3u8_response)
    match_links = re.compile("\\n[^#].*?\.m3u8\\n").findall(m3u8_response.text)
    print(match_links)
    for link in match_links:
        bitRate = int(link.split ('/')[-2].replace ('K','').replace ('k',''))
        if bitRate == 1800 or bitRate == 2500 or bitRate == 3500 or bitRate == 5600:
            print(bitRate)
        #link = link.replace ('complete','slide')
        #if saveXML.lower () == 'yes': f.write("\t" + 'BITRATE = '+ str (bitRate) + "\n")
        #if bitRate >= 1800 : mlb720List.append({'game':name,'stream':bLink + link.strip("\n") + auth_token,'quality':bitRate})
    #print(mlb720List)
'''    