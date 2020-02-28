# -*- coding: utf-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# As long as you retain this notice you can do whatever you want with
# this stuff. If we meet some day, and you think this stuff is worth it,
# you can buy me a beer in return. - Muad'Dib
# ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Atreides
# Addon id: plugin.video.atreides
# Addon Provider: House Atreides

'''
2019/04/17: Readded this one, fix by SC
2019/07/06: Minor code updates
'''

import re
import urlparse

from resources.lib.modules import client, cleantitle, source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['coolmoviezone.online', 'coolmoviezone.co']
        self.base_link = 'https://coolmoviezone.io'
        self.search_link = '/%s-%s'
        # self.scraper = cfscrape.create_scraper()

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            title = cleantitle.geturl(title)
            url = urlparse.urljoin(self.base_link, (self.search_link % (title, year)))
            return url
        except Exception:
            return

    def sources(self, url, hostDict, hostprDict):
        hostDict = hostprDict + hostDict
        try:
            sources = []
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

            r = client.request(url, headers=headers)
            if r is None:
                return sources
            match = re.findall('<td align="center"><strong><a href="(.+?)"', r, re.DOTALL)
            for url in match:
                quality = source_utils.check_sd_url(url)
                valid, host = source_utils.is_host_valid(url, hostDict)
                if not valid:
                    continue
                sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})
        except Exception:
            return
        return sources

    def resolve(self, url):
        return url
