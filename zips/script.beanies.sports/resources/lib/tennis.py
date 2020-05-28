from bs4 import BeautifulSoup
import requests
import re
game_list = []
def get_game():
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    html = requests.get(r"https://live-tennis.stream/",headers=headers).content
    soup = BeautifulSoup(html,'html.parser')
    data = soup.find_all('td',attrs={'class':'time'})
    for d in data:
        name = d.find(itemprop="name")
        url = d.find(itemprop="url")
        print(name['content'])
        print(url['content'])
        game_list.append({'title':name['content'],'link':url['content']})

    return game_list

m3u8 = ''
def get_stream(link):
    html = requests.get(link,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}).content
    soup = BeautifulSoup(html, 'html.parser')
    frame = soup.find('iframe',{'class':'embed-responsive-item'})
    iframe = frame['src']
    if iframe:
        iframe = "https://live-tennis.stream/" + iframe
        data = requests.get(iframe,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}).content
        soup2 = BeautifulSoup(data,'html.parser')
        source = re.compile("source: '(.+?)',",re.DOTALL).findall(str(soup2.prettify))
        if source:
            m3u8 = source[0]
            m3u8 = m3u8 + '|referer=' + iframe
            #print(m3u8)
    else:
        pass
    return m3u8

def readtennis() :
    import httplib2, re 
    #import arrow
    #utcZone = 'UTC'
    url = 'https://live-tennis.stream/free-matches-online-6'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    http = httplib2.Http() 

    game_list = [] 
    response = http.request(url) 
    webContent = str(response) 
    regex1 = 'class="theevent">(.+?)<\/tr>' 
    regex2 = 'content="(.+?)".+?"url" content="(.+?)".+?"startDate" content="(.+?)".+?"image" content="(.+?)"'
    match1 = re.compile(regex1,re.DOTALL).findall(webContent)
    
    for events in match1 : 
        evCheck = str(events). replace('\\r', ''). replace('\\n', ''). replace('\\', ''). strip()   
        match2 = re.compile(regex2,re.DOTALL).findall(evCheck)
      
        #.  print('event in match1 is - -' + evCheck + '\n')     #    .encode('ascii','ignore'))        
        for a, b, c, d in match2:
            #sched1 = arrow.get(c, 'YYYY-MM-DDTHH:mm')
                                            #        2019-08-31T23:30+00:00
            #sched = sched1.replace(tzinfo=utcZone)
            #    gTime = sched.to(addonZone)
            print '' 
            print('a - ' + str(a)) # + '\n')
            #    print('b - ' + str(b)) # + '\n')
            #    print('c - ' + gTime.strftime('%d-%b %H:%M (%Z) ') ) # + '\n')
            #    print('d - ' + str(d)) # + '\n')
        
        game_list.append({'game':a,'stream':b,'schedule':sched,'art':d})       
        
    return game_list



