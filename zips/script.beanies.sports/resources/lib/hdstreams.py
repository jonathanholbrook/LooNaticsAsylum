# -*- coding: utf-8 -*-

"""
HDStreams Scraper V-1.0.0
Date: Fri July 5, 2019
For Support contact: https://dreamcatcherit.com/
"""

try:
    import os
    import sys
    import requests
    from bs4 import BeautifulSoup
    import re
    from os.path import join
except:
	pass 
    #    print("Installing Dependencies")
    #    os.system("python2 -m pip install bs4 lxml requests ")
    #    print("Please re run the script")
    #    sys.exit(1)
    
import xbmc
chkV = (xbmc.getInfoLabel('System.BuildVersion')) 

if chkV.startswith('17'):
    myPath = sys.path[0] + '/resources/xml' 
else:
    myPath = os.path.dirname(__file__).replace('lib','xml')

outputFile = 'hdstreams.xml'
saveXML = 'no'


# clean old file (if any)

hdStreamList = []

if saveXML.lower () == 'yes':
    with open(join(myPath,outputFile), "w") as f:
        f.write("")

try:
    response = requests.get("http://hdstreams.club/")
    #       soup = BeautifulSoup(response.content, "lxml")
    soup = BeautifulSoup(response.content, "html.parser")
    parent_div = soup.find("div", {"class": "page-content"})
    p_tags = parent_div.find_all("p")

    if p_tags:
        for p_tag in p_tags:
            links = p_tag.find_all("a")
            time_list = re.findall("\d\d:\d\d", str(p_tag))
            titles = re.split("\d\d:\d\d", p_tag.text.encode("utf-8"))[1::]

            if links:
                for x, link in enumerate(links):
                    link = link["href"]
                    title = link.split("/")
                    channel = title[4].replace(".php", "")
                    title = "<title>{} {}</title>".format(time_list[x], titles[x])
                    game = str (titles[x])
                    for i in range(1, 8):
                        try:
                            r = requests.get(
                                "http://cdn{}.hdstreams.club/live/{}/index.m3u8".format(
                                    i, channel
                                ),
                                headers={
                                    "Referer": "http://hdstreams.club/page/{}.php".format(
                                        channel
                                    )
                                },
                            )
                            # print(r.status_code, r.url)
                            if r.status_code == 200:
                                m3u8_link = "http://cdn{}.hdstreams.club/live/{}/index.m3u8|Referer=http://hdstreams.club/page/{}.php".format(
                                    i, channel, channel
                                )
                                stream = m3u8_link
                                hdStreamList.append({'game':game,'stream':stream})               
                                m3u8_link = "<link>{}</link>".format(m3u8_link)
                                if saveXML.lower () == 'yes':
                                    with open(join(myPath,outputFile), "a") as f:
                                         f.write(
                                            "<item> \n {} \n {} \n <thumbnail></thumbnail> \n <fanart></fanart> \n </item>\n".format(
                                                title, m3u8_link
                                            )
                                    )
                                break
                        except:
                            pass
except Exception as e:
    print(e)
    pass

def startUp():
    return hdStreamList
