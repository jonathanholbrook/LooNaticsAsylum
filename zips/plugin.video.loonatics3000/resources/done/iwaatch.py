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
2019/07/06: Minor tweaks
2019/07/17: Rewritten to use api system
'''

import re
import urllib
import urlparse
import requests

from resources.lib.modules import cfscrape, cleantitle


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['iwaatch.com']
        self.base_link = 'https://iwaatch.com'
        self.search_link = '/api/api.php'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except Exception:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url is None:
                return sources

            scraper = cfscrape.create_scraper()

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            title = data['title']
            year = data['year']

            search_id = cleantitle.getsearch(title.lower())
            url = urlparse.urljoin(self.base_link, self.search_link)
            params = {'page': 'moviesearch', 'q': search_id}
            r = scraper.get(url, params=params).content
            movie_scrape = re.findall('<a href="(.+?)">\s+<img src=.+?>\n\s+(.+)\s+<span class=\'result-year\'>(.+?)<\/span>', r, re.DOTALL)

            for movie_url, movie_title, movie_year in movie_scrape:
                if year not in str(movie_year):
                    continue

                if cleantitle.getsearch(title).lower() == cleantitle.getsearch(movie_title).lower():
                    r = scraper.get(movie_url).content
                    links = re.findall(r"<a href='(.+?)'>(\d+)p<\/a>", r)
                    for link, quality in links:
                        if '1080' in quality:
                            quality = '1080p'
                        elif '720' in quality:
                            quality = '720p'
                        elif '480' in quality:
                            quality = 'SD'
                        else:
                            quality = 'SD'
                        link = link+'|Referer=' + movie_url
                        sources.append({'source': 'Direct', 'quality': quality, 'language': 'en', 'url': link, 'direct': True, 'debridonly': False})
            return sources
        except Exception:
            return sources

    def resolve(self, url):
        return url
