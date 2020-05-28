import requests
import re
import sys, os
import operator
import xbmc

from os.path import join

chkV = (xbmc.getInfoLabel('System.BuildVersion')) 

if chkV.startswith('17'):
    myPath = sys.path[0] + '/resources/xml' 
else:
    myPath = os.path.dirname(__file__).replace('lib','xml')

tempFile = 'site720Dump.xml'
saveXML = 'no'

print '\n' * 3
print ('........ Grabbing Data from Site .......')          

baseURL = 'http://www.720pstream.me'


nhlToken = requests.get('https://bitbucket.org/threw/textfiles/raw/master/nhl.txt').content
nhl_auth = "|Cookie=Authorization=" + nhlToken

mlbToken = requests.get('http://172.105.26.201/mlbs.txt').content
mlb_auth = "|Cookie=Authorization=" + mlbToken

#    wweToken = requests.get('http://www.retributionmedia.xyz/tokens/wwe.txt').content
wweToken = requests.get('http://www.theoracle.xyz/tokens/wwe.txt').content
wwe_auth = '|Cookie=' + wweToken

nfl_auth = "|Cookie=UNKNOWN_YET" 
nba_auth = "|Cookie=UNKNOWN_YET" 
mma_auth = "|Cookie=UNKNOWN_YET" 


fullsiteList = (
        '/nhl-stream',
        '/nfl-stream',
        '/mlb-stream',
        '/nba-stream',
        '/mma-stream',
        )
    
temp_siteList = (
        '/nhl-stream',
        '/mlb-stream',
        '/mma-stream',
        )
        

nhl720List = []
nfl720List = []
mlb720List = []
nba720List = []
mma720List = []

#        if saveXML.lower () == 'yes': f = open(join(myPath,tempFile),'w').close ()


def getStreams(siteList):
    site = siteList
    if site == '/nhl-stream': auth_token = nhl_auth
    if site == '/nfl-stream': auth_token = nfl_auth
    if site == '/mlb-stream': auth_token = mlb_auth
    if site == '/nba-stream': auth_token = nba_auth
    if site == '/mma-stream': auth_token = mma_auth
   
    url = baseURL + site
   
    html = requests.get(url).content
    match = re.compile('<a\stitle=\"(.+?)Stream\"\shref=\"(.+?)\">',re.DOTALL).findall(html)

    for name , link in match:
        name = name.replace ('   Live ',' Live').replace ('Live ',' Live') 
        if 'wwe' in link : auth_token = wwe_auth

        if "http" not in link:
            link = 'http://www.720pstream.me' + link
                   
        html2 = requests.get(link).content
        match2 = re.compile("videoURI\s=\s'(.+?)';",re.DOTALL).findall(html2)
        
        tempText = str (match2)
        rText = str (match2).split('/') [-1]
        bLink = str (match2).replace(rText,'').replace('[\'', '').strip() 
          
        #          if saveXML.lower () == 'yes': f = open(join(myPath,tempFile),'a')
        if match2:
            m3u8_response = requests.get(*match2)
            match_links = re.compile("\\n[^#].*?\.m3u8\\n").findall(m3u8_response.text)
            #        if saveXML.lower () == 'yes':
                #        f.write (('\n' + '.......... SITE = ' + str (site.replace('/','').upper ()) + '..........' + '\n'))
                #        f.write (('NAME = ' + name + '\n'))
                #        f.write("-------STREAMING URLS------" + "\n")
            for link in match_links:
                #        if saveXML.lower () == 'yes': f.write("\t" + bLink + link.strip("\n") + auth_token + "\n")
                
                if site == '/nhl-stream':
                    bitRate = int(link.split ('/')[-2].replace ('K','').replace ('k',''))
                    if saveXML.lower () == 'yes': f.write("\t" + 'BITRATE = '+ str (bitRate) + "\n")     
                    if bitRate >= 1800 : nhl720List.append({'game':name,'stream':bLink + link.strip("\n") + auth_token,'quality':bitRate})
                    
                if site == '/nfl-stream': 
                    if bitRate >= 1800 : nfl720List.append({'game':name,'stream':bLink + link.strip("\n") + auth_token})
                    
                if site == '/mlb-stream': 
                    bitRate = int(link.split ('/')[-2].replace ('K','').replace ('k',''))
                    link = link.replace ('complete','slide')
                    if saveXML.lower () == 'yes': f.write("\t" + 'BITRATE = '+ str (bitRate) + "\n")     
                    if bitRate >= 1800 : mlb720List.append({'game':name,'stream':bLink + link.strip("\n") + auth_token,'quality':bitRate})
                    
                if site == '/nba-stream':
                    if bitRate >= 1800 : nba720List.append({'game':name,'stream':bLink + link.strip("\n") + auth_token})
                    
                if site == '/mma-stream': 
                    bitRate = int(link.split ('/')[-2].replace ('K','').replace ('k',''))
                    if saveXML.lower () == 'yes': f.write("\t" + 'BITRATE = '+ str (bitRate) + "\n")     
                    if bitRate >= 1800 : mma720List.append({'game':name,'stream':bLink + link.strip("\n") + auth_token,'quality':bitRate})               
        else:
            pass
            
        #        nhl720List = sorted(nhl720List, key=lambda k: k['stream'])
        #        nfl720List = sorted(nfl720List, key=lambda k: k['stream'])
        #        mlb720List = sorted(mlb720List, key=lambda k: k['quality'])
        #        nba720List = sorted(nba720List, key=lambda k: k['stream'])
        #        mma720List = sorted(mma720List, key=lambda k: k['quality'])    
        nhl720List.sort(key = operator.itemgetter('game' , 'quality' ))
        nfl720List.sort(key = operator.itemgetter('game' ))
        mlb720List.sort(key = operator.itemgetter('game' , 'quality' ))
        nba720List.sort(key = operator.itemgetter('game' ))
        mma720List.sort(key = operator.itemgetter('game' , 'quality' ))
        
        if saveXML.lower () == 'yes': f.close ()

    #        if saveXML.lower () == 'yes':
        #        f = open(join(myPath,tempFile),'a')
        #        f.write (('....... FINISHED ......' + '\n'))
        #        f.close ()
               
    if site == '/nhl-stream': return nhl720List
    elif site == '/nfl-stream': return nfl720List
    elif site == '/mlb-stream': return mlb720List
    elif site == '/nba-stream': return nba720List
    elif site == '/mma-stream': return mma720List
    else : pass


# add different defs to return correct list
def getNHL ():
    thisSite = ('/nhl-stream')
    nhl720List = getStreams(thisSite)
    if nhl720List:
        tFile = 'nhlFile.xml'
        print '\n' +  'NHL Streams Found'
        if saveXML.lower () == 'yes': f = open(join(myPath,tFile),'w').close ()
        for items in nhl720List:
            game =items.get('game','Game Missing')
            stream =items.get('stream','Stream Missing')
            quality =items.get('quality','Quality Missing')
            print '  ' + 'Game = '+ str (game)
            print '  ' +  'BitRate = '+ str (quality) +'k'
            if saveXML.lower () == 'yes':
                f = open(join(myPath,tFile),'a')
                f.write ('Game = '+ str (game) +'(' + str (quality) +'k)') #  + '\n')
                f.write (' - Stream = '+ str (stream)+ '\n')
                f.close ()
    else:
        print  '\n' +  'No NHL Streams Found'
        
    return nhl720List

def getNFL ():
    thisSite = ('/nfl-stream')
    #    nfl720List = getStreams(thisSite)
    if nfl720List:
        print '\n' +  'NFL Streams Found'
    else:
        print  '\n' +  'NFL Section Under Construction'
        
    return nfl720List

def getMLB ():
    thisSite = ('/mlb-stream')
    mlb720List = getStreams(thisSite)
    if mlb720List:
        tFile = 'mlbFile.xml'
        print '\n' +  'MLB Streams Found'
        if saveXML.lower () == 'yes': f = open(join(myPath,tFile),'w').close ()
        for items in mlb720List:
            game =items.get('game','Game Missing')
            stream =items.get('stream','Stream Missing')
            quality =items.get('quality','Quality Missing')
            print '  ' + 'Game = '+ str (game)
            print '  ' +  'BitRate = '+ str (quality) +'k'
            if saveXML.lower () == 'yes':
                f = open(join(myPath,tFile),'a')
                f.write ('Game = '+ str (game) +'(' + str (quality) +'k)') #  + '\n')
                f.write (' - Stream = '+ str (stream)+ '\n')
                f.close ()
    else:
        print  '\n' +  'No MLB Streams Found'
        
    return mlb720List

def getNBA ():
    thisSite = ('/nba-stream')
    #    nba720List = getStreams(thisSite)
    if nba720List:
        print '\n' +  'NBA Streams Found'
    else:
        print  '\n' +  'NBA Section Under Construction'
        
    return nba720List
    
def getMMA ():
    thisSite = ('/mma-stream')
    mma720List = getStreams(thisSite)
    if mma720List:
        tFile = 'mmaFile.xml'
        print '\n' + 'MMA Streams Found'
        if saveXML.lower () == 'yes': f = open(join(myPath,tFile),'w').close ()
        for items in mma720List:
            game =items.get('game','Game Missing')
            stream =items.get('stream','Stream Missing')
            quality =items.get('quality','Quality Missing')
            print '  ' + 'Game = '+ str (game)
            print '  ' +  'BitRate = '+ str (quality) +'k'
            if saveXML.lower () == 'yes':
                f = open(join(myPath,tFile),'a')
                f.write ('Game = '+ str (game) +'(' + str (quality) +'k)') #  + '\n')
                f.write (' - Stream = '+ str (stream)+ '\n')
                f.close ()
    else:
        print  '\n' +  'No MMA Streams Found'
        
    return mma720List

# end of defs

# TESTING ONLY BELOW
#    getNHL ()
#####    getNFL ()
#    getMLB ()
#####    getNBA ()
#    getMMA ()
     