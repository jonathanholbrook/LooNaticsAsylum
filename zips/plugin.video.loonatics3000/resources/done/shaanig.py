# -*- coding: utf-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# @shellc0de wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. - Muad'Dib
# ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Atreides
# Addon id: plugin.video.atreides
# Addon Provider: House Atreides

import urlparse

from resources.lib.modules import cfscrape, cleantitle, client, source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['shaanig.se']
        self.base_link = 'https://www.shaanig.se'
        self.search_link = '/%s-%s'
        self.search_tvlink = '/episode/%s'
        self.cfscraper = cfscrape.create_scraper()

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            title = cleantitle.geturl(title)
            url = urlparse.urljoin(self.base_link, (self.search_link % (title, year)))
            return url
        except Exception:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            title = cleantitle.geturl(tvshowtitle)
            url = urlparse.urljoin(self.base_link, (self.search_tvlink % (title)))
            return url
        except Exception:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            url = url + '-season-%s-episode-%s' % (season, episode)
            return url
        except Exception:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
            r = self.cfscraper.get(url).content
            give_me = client.parseDOM(r, "div", attrs={"id": "lnk list-downloads"})
            for url in give_me:

                some_links = client.parseDOM(url, 'a', ret='href')
                for url in some_links:

                    quality = source_utils.check_sd_url(url)
                    url = url.split('?s=')[1]
                    final = urlparse.urljoin('http:', url)
                    sources.append({'source': 'Direct', 'quality': quality, 'language': 'en', 'url': final, 'direct': True, 'debridonly': False})

            return sources
        except Exception:
            return sources

    def resolve(self, url):
        return url
