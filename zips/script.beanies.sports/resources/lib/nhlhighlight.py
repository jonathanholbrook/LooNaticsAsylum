import requests
from bs4 import BeautifulSoup
import re

result = []
def get_highlight(date_year):
    year,month = date_year.split()
    #print(month)
    #print(year)
    data = requests.get(r"https://sbstp.ca/nhl/2018-2019/").content
    soup = BeautifulSoup(data,'html.parser')

    date_list = re.compile('<hr/>(.+?)<table border="0" cellpadding="5">',re.DOTALL).findall(str(soup.prettify))


    for date in date_list:
        date = date.replace('\\n','').strip()
        #date = re.sub('\n','',date).strip()
        #print(date)
        #break
        if month.lower() in date.lower() and year.strip() in date:
            #print(date)
            #break
            #print('inside if')
            
            tr = re.compile(date + "(.+?)<hr/>",re.DOTALL).findall(str(soup.prettify))
            new_soup = BeautifulSoup(tr[0],'html.parser')
            new_tr = new_soup.select("table > tr")
            index = 1
            title = ''
            while index < len(new_tr):
                text = new_tr[index].text.split()
                for t in text:
                    if 'link' not in t.strip():
                        title = title + ' ' + t.strip()
                    else:
                        pass
                    
                links = re.compile('<th><a href="(.+?)"',re.DOTALL).findall(str(new_tr[index]))
                if len(links) > 1:
                    link = links[1]
                result.append({'date':date,'title':title,'link':link})
                index += 1

            
        else:
            #print('inside else')
            #break
            continue
    #print(result)
    return result
    

#print(get_highlight('2019 June'))
