# -*- coding: utf-8 -*-
"""
    OTB Music
    Copyright (C) 2018,
    Version 1.0.4
    OTB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    -------------------------------------------------------------

    Usage Examples:
 
    <dir>
    <title>OTB Music</title>
    <otb_music>all</otb_music>
    </dir>

    <dir>
    <title>Rock</title>
    <otb_music>genre|Rock_Bands|app2nf3mKUqrf67c0</otb_music>
    </dir>

    <dir>
    <title>Pop</title>
    <otb_music>genre|Pop_Bands|app6l5yniExppN9QP</otb_music>
    </dir>

    <dir>
    <title>Metal</title>
    <otb_music>genre|Metal_Bands|appVczmt7xvdifcr8</otb_music>
    </dir>

    <dir>
    <title>Country</title>
    <otb_music>genre|Country_Bands|appsQV4zX8poQ4y7M</otb_music>
    </dir>

    <dir>
    <title>Electronic</title>
    <otb_music>genre|Electronic_Bands|appY48NlVVE4SqvBw</otb_music>
    </dir>            

    --------------------------------------------------------------

"""



from __future__ import absolute_import
import requests
import re
import os
import xbmc
import xbmcaddon
import json
from koding import route
from ..plugin import Plugin
from resources.lib.external.airtable.airtable import Airtable
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from requests.exceptions import HTTPError
import time
from unidecode import unidecode

CACHE_TIME = 3600  # change to wanted cache time in seconds

addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
AddonName = xbmc.getInfoLabel('Container.PluginName')
AddonName = xbmcaddon.Addon(AddonName).getAddonInfo('id')

rock_keys = {'Concerts':'app97iqXbOkbFfVke',
            'Videos':'appnW82G1n9jTvruF',
            'Albums':'appZ6RDmvZaVORMId',
            'History':'appUESjBXYlu9vYPt',
            'Mp3':'appGiZLhh5gLmQRzs'}
pop_keys = {'Concerts':'apprE4OgCy2KhIWKJ',
            'Videos':'appGsBsrXAS2fFx6i',
            'Albums':'appfsMAIbMsTJ5g28',
            'History':'appL43J2ETCI36I0e',
            'Mp3':'app04qBDn5axmZueQ'}
metal_keys = {'Concerts':'appQyE3mSnE1jhDWJ',
            'Videos':'appEOYvvMwXVQcXNU',
            'Albums':'appUgh0nkcOmJQb6h',
            'History':'appkhwtJKRTg2xhqt',
            'Mp3':'appsbZQM1sMCwteJi'}
country_keys = {'Concerts':'appq2hGuxwi9VrmT7',
            'Videos':'appU5csDlbN6WBggN',
            'Albums':'appUoaDoaVGBB7EPb',
            'History':'appK2WHARQavhVkND',
            'Mp3':'appYmn54MvZI4Jnyj'}
electronic_keys = {'Concerts':'appdarvtCCqPObOHw',
            'Videos':'appq8Vom4rYRPKTlK',
            'Albums':'apptYBhQsxS73bBSj',
            'History':'appHNTX6e1M3uch1H',
            'Mp3':'appSSeja2mZslbjTR'}



class OTB_Music(Plugin):
    name = "otb_music"

    def process_item(self, item_xml):
        if "<otb_music>" in item_xml:
            item = JenItem(item_xml)              
            if item.get("otb_music", "") == "all":
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_the_main_music_page",
                    'url': "",
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item              
            elif "genre|" in item.get("otb_music", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_the_main_genre_page",
                    'url': item.get("otb_music", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item 
            elif "cat|" in item.get("otb_music", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_the_band_Category_page",
                    'url': item.get("otb_music", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item
            elif "open|" in item.get("otb_music", ""):
                       
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_chosen_category_page",
                    'url': item.get("otb_music", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item
            elif "songs|" in item.get("otb_music", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_the_band_songs_page",
                    'url': item.get("otb_music", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item


@route(mode='open_the_main_music_page')
def open_table():
    xml = ""
    at = Airtable('appn8GRJzxzmi6Xph', 'music_genre', api_key='keyikW1exArRfNAWj')
    match = at.get_all(maxRecords=1200, view='Grid view') 
    for field in match:
        try:
            res = field['fields']   
            name = res['Name']
            name = remove_non_ascii(name)
            thumbnail = res['thumbnail']
            fanart = res['fanart']
            link = res['link']
            summary = res['Summary']                        
            xml +=  "<item>"\
                    "<title>%s</title>"\
                    "<thumbnail>%s</thumbnail>"\
                    "<fanart>%s</fanart>"\
                    "<summary>%s</summary>"\
                    "<link>"\
                    "<otb_music>genre|%s</otb_music>"\
                    "</link>"\
                    "</item>" % (name,thumbnail,fanart,summary,link)                                          

        except:
            pass                                                                     
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

@route(mode='open_the_main_genre_page',args=["url"])
def open_table(url):
    xml = ""
    table = url.split("|")[-2]
    key = url.split("|")[-1]
    at = Airtable(key, table, api_key='keyikW1exArRfNAWj')
    match = at.get_all(maxRecords=1200, view='Grid view') 
    for field in match:
        try:
            res = field['fields']   
            name = res['Name']
            name = remove_non_ascii(name)
            thumbnail = res['thumbnail']
            fanart = res['fanart']
            link = res['link']                        
            xml +=  "<item>"\
                    "<title>%s</title>"\
                    "<thumbnail>%s</thumbnail>"\
                    "<fanart>%s</fanart>"\
                    "<link>"\
                    "<otb_music>cat|%s|%s</otb_music>"\
                    "</link>"\
                    "</item>" % (name,thumbnail,fanart,name,link)                                          

        except:
            pass                                                                     
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

@route(mode='open_the_band_Category_page',args=["url"])
def open_table(url):
    xml = ""
    band = url.split("|")[1]
    gen = url.split("|")[2]
    table = url.split("|")[3]
    at = Airtable('appP8lvtpGOO2KPn7', 'Categories', api_key='keyikW1exArRfNAWj')
    match = at.get_all(maxRecords=1200, view='Grid view') 
    for field in match:
        try:
            res = field['fields']   
            name = res['Name']
            name = remove_non_ascii(name)
            thumbnail = res['thumbnail']
            fanart = res['fanart']
            link = res['link']
            title = band+" "+name                        
            xml +=  "<item>"\
                    "<title>%s</title>"\
                    "<thumbnail>%s</thumbnail>"\
                    "<fanart>%s</fanart>"\
                    "<link>"\
                    "<otb_music>open|%s|%s|%s|%s</otb_music>"\
                    "</link>"\
                    "</item>" % (title,thumbnail,fanart,name,band,gen,table)                                          

        except:
            pass                                                                     
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

@route(mode='open_chosen_category_page',args=["url"])
def open_table(url):
    xml = ""
    cat2 = url.split("|")[1]
    band = url.split("|")[2]
    gen = url.split("|")[3]
    table = url.split("|")[4]
    airtab = gen+"_"+cat2
    if gen == "Rock":
        table = rock_keys
    elif gen == "Pop":
        table = pop_keys
    elif gen == "Metal":
        table = metal_keys
    elif gen == "Country":
        table = country_keys
    elif gen == "Electronic":
        table = electronic_keys                             
    key = table[cat2]
    at = Airtable(key, airtab, api_key='keyikW1exArRfNAWj')
    match = at.search('category', band ,view='Grid view') 
    for field in match:
        try:
            res = field['fields']   
            name = res['Name']
            name = remove_non_ascii(name)
            thumbnail = res['thumbnail']
            fanart = res['fanart']
            summary = res['summary']
            summary = remove_non_ascii(summary)
            link1 = res['link1']
            link2 = res['link2']
            link3 = res['link3']
            link4 = res['link4']
            link5 = res['link5']                                    
            if link2 == "-":
                xml +=  "<item>"\
                        "<title>%s</title>"\
                        "<thumbnail>%s</thumbnail>"\
                        "<fanart>%s</fanart>"\
                        "<summary>%s</summary>"\
                        "<link>"\
                        "<sublink>%s</sublink>"\
                        "</link>"\
                        "</item>" % (name,thumbnail,fanart,summary,link1)                                          
            elif link3 == "-":
                xml +=  "<item>"\
                        "<title>%s</title>"\
                        "<thumbnail>%s</thumbnail>"\
                        "<fanart>%s</fanart>"\
                        "<summary>%s</summary>"\
                        "<link>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "</link>"\
                        "</item>" % (name,thumbnail,fanart,summary,link1,link2)
            elif link4 == "-":
                xml +=  "<item>"\
                        "<title>%s</title>"\
                        "<thumbnail>%s</thumbnail>"\
                        "<fanart>%s</fanart>"\
                        "<summary>%s</summary>"\
                        "<link>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "</link>"\
                        "</item>" % (name,thumbnail,fanart,summary,link1,link2,link3)
            elif link5 == "-":
                xml +=  "<item>"\
                        "<title>%s</title>"\
                        "<thumbnail>%s</thumbnail>"\
                        "<fanart>%s</fanart>"\
                        "<summary>%s</summary>"\
                        "<link>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "</link>"\
                        "</item>" % (name,thumbnail,fanart,summary,link1,link2,link3,link4)
            else:                
                xml +=  "<item>"\
                        "<title>%s</title>"\
                        "<thumbnail>%s</thumbnail>"\
                        "<fanart>%s</fanart>"\
                        "<summary>%s</summary>"\
                        "<link>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "<sublink>%s</sublink>"\
                        "</link>"\
                        "</item>" % (name,thumbnail,fanart,summary,link1,link2,link3,link4,link5)                                                                  

        except:
            pass                                                                     
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())



def remove_non_ascii(text):
    return unidecode(text)
