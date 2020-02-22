# -*- coding: utf-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
#  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. - Muad'Dib
# ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Atreides
# Addon id: plugin.video.atreides
# Addon Provider: House Atreides

'''
2019/4/16: Updated to use CFScrape - Still using single request
2019/5/26: Added quality check. Adj iframe to pull fembed links again
as they are now playable.
'''

import re

from resources.lib.modules import cfscrape, client, source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['hackimdb.com']
        self.base_link = 'https://hackimdb.com'
        # this still works too '/title/&%s'
        self.search_link = '/title/%s'
        self.cfscraper = cfscrape.create_scraper()

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = self.base_link + self.search_link % imdb
            return url
        except Exception:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
            r = self.cfscraper.get(url, headers=headers).content
            quality_bitches = re.compile('<strong>Quality:\s+</strong>\s+<span class="quality">(.+?)</span>', re.DOTALL).findall(r)

            for quality in quality_bitches:

                if 'HD' in quality:
                    quality = '720p'
                elif 'CAM' in quality:
                    quality = 'CAM'
                else:
                    quality = 'SD'

            match = re.compile('<iframe.+?src="(.+?)"').findall(r)
            for url in match:
                if 'youtube' in url:
                    continue
                valid, hoster = source_utils.is_host_valid(url, hostDict)
                if not valid:
                    continue
                sources.append({'source': hoster, 'quality': quality, 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})

            return sources
        except Exception:
            return sources

    def resolve(self, url):
        return url
