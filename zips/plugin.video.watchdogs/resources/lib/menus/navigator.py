# -*- coding: utf-8 -*-

import sys

from resources.lib.modules import control
from resources.lib.modules import log_utils
from resources.lib.modules import trakt

try:
    sysaddon = sys.argv[0]
    syshandle = int(sys.argv[1])
except:
    sysaddon = ''
    syshandle = '1'
    pass

artPath = control.artPath()
imdbCredentials = False if control.setting('imdb.user') == '' else True
tmdbSessionID = False if control.setting('tmdb.session_id') == '' else True
traktCredentials = trakt.getTraktCredentialsInfo()
traktIndicators = trakt.getTraktIndicatorsInfo()
indexLabels = False if control.setting('index.labels') == 'false' else True
iconLogos = False if control.setting('icon.logos') == 'Traditional' else True
notificationSound = False if control.setting('notification.sound') == 'false' else True


class Navigator:
    def root(self):
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')

        if control.getMenuEnabled('mylists.widget'):
            self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.png','DefaultVideoPlaylists.png')
            self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')

        if control.setting('newmovies.widget') != '0':
            indexer = 32478
            indexer_icon = 'imdb.png'
            setting = control.setting('newmovies.widget')
            if setting == '2':
                indexer = 32479
                indexer_icon = 'trakt.png'
            self.addDirectoryItem(indexer if indexLabels else 32477, 'newMovies', indexer_icon if iconLogos else 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')

        if (traktCredentials and control.setting('tv.widget.alt') != '0') or (not traktCredentials and control.setting('tv.widget') != '0'):
            indexer = 32481
            indexer_icon = 'tvmaze.png'
            setting = control.setting('tv.widget.alt')
            if setting == '2' or setting == '3':
                indexer = 32482
                indexer_icon = 'trakt.png'
            self.addDirectoryItem(indexer if indexLabels else 32480, 'tvWidget', indexer_icon if iconLogos else 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png')
            #self.addDirectoryItem(32484 if indexLabels else 32483, 'calendar&url=added', 'tvmaze.png' if iconLogos else 'latest-episodes.png', 'DefaultTVShows.png', queue=True)

        if control.getMenuEnabled('navi.main.userlists'):
            self.addDirectoryItem(30829, 'userListsNavigator', 'userlist.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.main.ustvgo'):
            self.addDirectoryItem(30827, 'ustvgoNavigator', 'blank.png', 'DefaultTVShows.png') # ustvgo.png need to make icon

        if control.getMenuEnabled('navi.main.streamlive'):
            self.addDirectoryItem(30828, 'streamliveNavigator', 'streamlive.png', 'DefaultTVShows.png')

        if control.getMenuEnabled('navi.main.swiftstreams'):
            self.addDirectoryItem(30802, 'swift', 'swiftstreamz.png', 'DefaultTVShows.png')

        if control.getMenuEnabled('navi.main.tvtap'):
            self.addDirectoryItem(30803, 'tvtap', 'tvtap.png', 'DefaultTVShows.png')

        if control.getMenuEnabled('navi.main.watchdogslive'):
            self.addDirectoryItem(30804, 'watchdogslive', 'm3ulist.png', 'DefaultTVShows.png')

        #if control.getMenuEnabled('navi.main.foreign'):
            #self.addDirectoryItem(30831, 'foreignNavigator', 'foreign.png', 'DefaultTVShows.png')

        if control.getMenuEnabled('navi.main.collections'):
            self.addDirectoryItem(32000, 'collectionsNavigator', 'boxsets.png', 'DefaultSets.png')

        if control.getMenuEnabled('navi.originals'):
            self.addDirectoryItem(30790 if control.setting('index.labels') == 'false' else 30800, 'originals', 'netamahul.png' if control.setting('icon.logos') == 'Traditional' else 'tvmaze.png', 'DefaultNetwork.png')

        if control.getMenuEnabled('navi.anime'):
            self.addDirectoryItem(30801, 'animeNavigator', 'anime.png', 'DefaultFolder.png')

        if control.getMenuEnabled('navi.main.cartoons'):
            self.addDirectoryItem(30808, 'tvshows&url=https://api.trakt.tv/users/sg0/lists/sg0-s-toontv/items', 'cartoons.png', 'DefaultTVShows.png')

        adultcartoons = True if control.setting('adultcartoons_pw') == 'drowssap' else False
        if adultcartoons == True:
            self.addDirectoryItem(30817, 'tvshows&url=https://api.trakt.tv/users/sirmax/lists/bad-toontv/items', 'adultcartoons.png', 'DefaultTVShows.png')

        porn = True if control.setting('porn_pw') == 'drowssap' else False
        if porn == True:
            self.addDirectoryItem(30819, 'porn', 'porno.png', 'DefaultTVShows.png')

        if control.getMenuEnabled('navi.main.music'):
            self.addDirectoryItem(30809, 'music', 'music.png', 'DefaultTVShows.png')

        if control.getMenuEnabled('navi.main.radio'):
            self.addDirectoryItem(30821, 'radioNavigator', 'radio.png', 'DefaultVideoPlaylists.png')

        if control.getMenuEnabled('navi.main.standup'):
            self.addDirectoryItem(30810, 'movies&url=https://api.trakt.tv/users/giladg/lists/stand-up-comedy/items', 'standup.png', 'DefaultMovies.png')

        #if control.getMenuEnabled('navi.main.skycinema'): # <setting id="navi.main.skycinema" type="bool" label="32000" default="true" />
            #self.addDirectoryItem(30807, 'channels', 'skycinema.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.main.1click'):
            self.addDirectoryItem(30805, 'oneclick', '1click.png', 'DefaultTVShows.png')

        if control.getMenuEnabled('navi.youtube'):
            self.addDirectoryItem('You Tube Videos & Music', 'youtube', 'youtube.png', 'youtube.png')

        if control.getMenuEnabled('navi.main.docs'):
            self.addDirectoryItem(30814, 'docuHeaven', 'documentaries.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.main.randmovie'):
            self.addDirectoryItem(30815, 'randmovie', 'randmovie.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.main.randtv'):
            self.addDirectoryItem(30816, 'randtv', 'randtv.png', 'DefaultMovies.png')

        if control.setting('furk.api') != '':
            self.addDirectoryItem('Furk.net', 'furkNavigator', 'movies.png',  'DefaultMovies.png')

        self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultAddonsSearch.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonService.png')

        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        if control.getMenuEnabled('navi.main.changelog'):
            self.addDirectoryItem(30823, 'ShowChangelog', 'icon.png', 'DefaultAddonsUpdates.png', isFolder=False)

        if control.getMenuEnabled('navi.main.news'):
            self.addDirectoryItem(30822, 'ShowNews', 'icon.png', 'DefaultAddonHelper.png', isFolder=False)

        self.endDirectory()


    def furk(self):
        self.addDirectoryItem('User Files', 'furkUserFiles', 'mytvnavigator.png', 'mytvnavigator.png')
        self.addDirectoryItem('Search', 'furkSearch', 'search.png', 'search.png')
        self.endDirectory()


    def movies(self, lite=False):

        if control.getMenuEnabled('navi.movie.newmovies'):
            self.addDirectoryItem(32478 if indexLabels else 32477, 'newMovies', 'imdb.png' if iconLogos else 'movies.png', 'DefaultRecentlyAddedMovies.png')

        if control.getMenuEnabled('navi.movie.most') == True:
            self.addDirectoryItem('Most Played / Collected / Watched', 'movieMosts', 'people-watching.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.reviews') == True:
            self.addDirectoryItem('Trailers / Reviews', 'movieReviews', 'reviews.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.imdb.intheater'):
            self.addDirectoryItem(32421 if indexLabels else 32420, 'movies&url=theaters', 'imdb.png' if iconLogos else 'in-theaters.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.tmdb.nowplaying'):
            self.addDirectoryItem(32423 if indexLabels else 32422, 'tmdbmovies&url=tmdb_nowplaying', 'tmdb.png' if iconLogos else 'in-theaters.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.trakt.anticipated'):
            self.addDirectoryItem(32425 if indexLabels else 32424, 'movies&url=traktanticipated', 'trakt.png' if iconLogos else 'in-theaters.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.tmdb.upcoming'):
            self.addDirectoryItem(32427 if indexLabels else 32426, 'tmdbmovies&url=tmdb_upcoming', 'tmdb.png' if iconLogos else 'in-theaters.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.imdb.popular'):
            self.addDirectoryItem(32429 if indexLabels else 32428, 'movies&url=mostpopular', 'imdb.png' if iconLogos else 'most-popular.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.tmdb.popular'):
            self.addDirectoryItem(32431 if indexLabels else 32430, 'tmdbmovies&url=tmdb_popular', 'tmdb.png' if iconLogos else 'most-popular.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.trakt.popular'):
            self.addDirectoryItem(32433 if indexLabels else 32432, 'movies&url=traktpopular', 'trakt.png' if iconLogos else 'most-popular.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.imdb.boxoffice'):
            self.addDirectoryItem(32435 if indexLabels else 32434, 'movies&url=imdbboxoffice', 'imdb.png' if iconLogos else 'box-office.png', 'DefaultMovies.png')
        if control.getMenuEnabled('navi.movie.tmdb.boxoffice'):
            self.addDirectoryItem(32436 if indexLabels else 32434, 'tmdbmovies&url=tmdb_boxoffice', 'tmdb.png' if iconLogos else 'box-office.png', 'DefaultMovies.png')
        if control.getMenuEnabled('navi.movie.trakt.boxoffice'):
            self.addDirectoryItem(32437 if indexLabels else 32434, 'movies&url=traktboxoffice', 'trakt.png' if iconLogos else 'box-office.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.imdb.mostvoted'):
            self.addDirectoryItem(32439 if indexLabels else 32438, 'movies&url=mostvoted', 'imdb.png' if iconLogos else 'most-voted.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.tmdb.toprated'):
            self.addDirectoryItem(32441 if indexLabels else 32440, 'tmdbmovies&url=tmdb_toprated', 'tmdb.png' if iconLogos else 'most-voted.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.trakt.trending'):
            self.addDirectoryItem(32443 if indexLabels else 32442, 'movies&url=trakttrending', 'trakt.png' if iconLogos else 'trending.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.trakt.recommended'):
            self.addDirectoryItem(32445 if indexLabels else 32444, 'movies&url=traktrecommendations', 'trakt.png' if iconLogos else 'highly-rated.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.imdb.featured'):
            self.addDirectoryItem(32447 if indexLabels else 32446, 'movies&url=featured', 'imdb.png' if iconLogos else 'movies.png', 'DefaultMovies.png')

        #if control.getMenuEnabled('navi.movie.collections'):
            #self.addDirectoryItem(32000, 'collectionsNavigator', 'boxsets.png', 'DefaultSets.png')

        if control.getMenuEnabled('navi.movie.imdb.oscars'):
            self.addDirectoryItem(32452 if indexLabels else 32451, 'movies&url=oscars', 'imdb.png' if iconLogos else 'oscar-winners.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.imdb.oscarsnominees'):
            self.addDirectoryItem(32454 if indexLabels else 32453, 'movies&url=oscarsnominees', 'imdb.png' if iconLogos else 'oscar-winners.png', 'DefaultMovies.png')

        if control.getMenuEnabled('navi.movie.imdb.genres'):
            self.addDirectoryItem(32456 if indexLabels else 32455, 'movieGenres', 'imdb.png' if iconLogos else 'genres.png', 'DefaultGenre.png')

        if control.getMenuEnabled('navi.movie.imdb.years'):
            self.addDirectoryItem(32458 if indexLabels else 32457, 'movieYears', 'imdb.png' if iconLogos else 'years.png', 'DefaultYear.png')

        if control.getMenuEnabled('navi.movie.imdb.persons'):
            self.addDirectoryItem(32460 if indexLabels else 32459, 'moviePersons', 'imdb.png' if iconLogos else 'people.png', 'DefaultActor.png')

        if control.getMenuEnabled('navi.movie.imdb.languages'):
            self.addDirectoryItem(32462 if indexLabels else 32461, 'movieLanguages', 'imdb.png' if iconLogos else 'languages.png', 'DefaultAddonLanguage.png')

        if control.getMenuEnabled('navi.movie.imdb.certificates'):
            self.addDirectoryItem(32464 if indexLabels else 32463, 'movieCertificates', 'imdb.png' if iconLogos else 'certificates.png', 'DefaultMovies.png')

        if not lite:
            if control.getMenuEnabled('mylists.widget'):
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultAddonsSearch.png')
            self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonService.png')
            #self.addDirectoryItem(32029, 'moviePerson', 'imdb.png' if iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
            #self.addDirectoryItem(32010, 'movieSearch', 'trakt.png' if iconLogos else 'search.png', 'DefaultAddonsSearch.png')
        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()
        self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'DefaultVideoPlaylists.png')

        if traktCredentials and imdbCredentials:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection&list_name=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist&list_name=traktwatchlist'))

            if traktIndicators:
                #self.addDirectoryItem(32468, 'moviesUnfinished&url=traktonDeck', 'trakt.png', 'DefaultYear.png')
                #self.addDirectoryItem(35308, 'moviesUnfinished&url=traktunfinished', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                #self.addDirectoryItem(32037, 'movies&url=progress', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                self.addDirectoryItem(32033, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultVideoPlaylists.png', queue=True)

        elif traktCredentials:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection&list_name=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist&list_name=traktwatchlist'))

            if traktIndicators:
                #self.addDirectoryItem(32468, 'moviesUnfinished&url=traktonDeck', 'trakt.png', 'DefaultYear.png')
                #self.addDirectoryItem(35308, 'moviesUnfinished&url=traktunfinished', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                #self.addDirectoryItem(32037, 'movies&url=progress', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)

        elif imdbCredentials:
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultVideoPlaylists.png', queue=True)

        # if control.setting('tmdb.session_id') != '':
            # self.addDirectoryItem(32033, 'tmdbmovieUserlists', 'tmdb.png', 'DefaultVideoPlaylists.png', queue=True)

        if not lite:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
            self.addDirectoryItem(32029, 'moviePerson', 'imdb.png' if iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png' if iconLogos else 'search.png', 'DefaultAddonsSearch.png')
        self.endDirectory()

    def randmovie(self, lite=False):
        self.addDirectoryItem('[COLORmagenta]Be Patient! It may take a minute to load...[/COLOR]', '', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Action', 'random&rtype=movie&url=genreaction', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Adventure', 'random&rtype=movie&url=genreadventure', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Animation', 'random&rtype=movie&url=genreanimation', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Anime', 'random&rtype=movie&url=genreanime', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Biography', 'random&rtype=movie&url=genrebiography', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Comedy', 'random&rtype=movie&url=genrecomedy', 'genres.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('Crime', 'random&rtype=movie&url=genrecrime', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Documentary', 'random&rtype=movie&url=genredocumentary', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Drama', 'random&rtype=movie&url=genredrama', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Family', 'random&rtype=movie&url=genrefamily', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Fantasy', 'random&rtype=movie&url=genrefantasy', 'genres.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('History', 'random&rtype=movie&url=genrehistory', 'genres.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('Horror', 'random&rtype=movie&url=genrehorror', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Music ', 'random&rtype=movie&url=genremusic', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Musical', 'random&rtype=movie&url=genremusical', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Mystery', 'random&rtype=movie&url=genremystery', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Romance', 'random&rtype=movie&url=genreromance', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Science Fiction', 'random&rtype=movie&url=genrescifi', 'genres.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('Sport', 'random&rtype=movie&url=genresport', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Thriller', 'random&rtype=movie&url=genrethriller', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('War', 'random&rtype=movie&url=genrewar', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Western', 'random&rtype=movie&url=genrewestern', 'genres.png', 'DefaultMovies.png')
        self.endDirectory()

    def movieMosts(self, lite=False):
        self.addDirectoryItem('Most Played This Week', 'movies&url=played1', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Played This Month', 'movies&url=played2', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Played This Year', 'movies&url=played3', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Played All Time', 'movies&url=played4', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Collected This Week', 'movies&url=collected1', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Collected This Month', 'movies&url=collected2', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Collected This Year', 'movies&url=collected3', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Collected All Time', 'movies&url=collected4', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Watched This Week', 'movies&url=watched1', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Watched This Month', 'movies&url=watched2', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Watched This Year', 'movies&url=watched3', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('Most Watched All Time', 'movies&url=watched4', 'most-popular.png', 'DefaultMovies.png')
        self.endDirectory()

    def tvshows(self, lite=False):
        if control.getMenuEnabled('navi.tv.most'):
            self.addDirectoryItem('Most Played / Collected / Watched', 'showMosts', 'people-watching.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.reviews'):
            self.addDirectoryItem('Trailers / Reviews', 'tvReviews', 'reviews.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.trakt.anticipated'):
            self.addDirectoryItem('Anticipated', 'tvshows&url=traktanticipated', 'tvshows.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.imdb.popular'):
            self.addDirectoryItem(32429 if indexLabels else 32428, 'tvshows&url=popular', 'imdb.png' if iconLogos else 'most-popular.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.tmdb.popular'):
            self.addDirectoryItem(32431 if indexLabels else 32430, 'tmdbTvshows&url=tmdb_popular', 'tmdb.png' if iconLogos else 'most-popular.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.trakt.popular'):
            self.addDirectoryItem(32433 if indexLabels else 32432, 'tvshows&url=traktpopular', 'trakt.png' if iconLogos else 'most-popular.png', 'DefaultTVShows.png', queue=True)
        if control.getMenuEnabled('navi.tv.imdb.mostvoted'):
            self.addDirectoryItem(32439 if indexLabels else 32438, 'tvshows&url=views', 'imdb.png' if iconLogos else 'most-voted.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.tmdb.toprated'):
            self.addDirectoryItem(32441 if indexLabels else 32440, 'tmdbTvshows&url=tmdb_toprated', 'tmdb.png' if iconLogos else 'most-voted.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.trakt.trending'):
            self.addDirectoryItem(32443 if indexLabels else 32442, 'tvshows&url=trakttrending', 'trakt.png' if iconLogos else 'trending.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.imdb.highlyrated'):
            self.addDirectoryItem(32449 if indexLabels else 32448, 'tvshows&url=rating', 'imdb.png' if iconLogos else 'highly-rated.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.trakt.recommended'):
            self.addDirectoryItem(32445 if indexLabels else 32444, 'tvshows&url=traktrecommendations', 'trakt.png' if iconLogos else 'highly-rated.png', 'DefaultTVShows.png', queue=True)
        if control.getMenuEnabled('navi.tv.imdb.genres'):
            self.addDirectoryItem(32456 if indexLabels else 32455, 'tvGenres', 'imdb.png' if iconLogos else 'genres.png', 'DefaultGenre.png')
        if control.getMenuEnabled('navi.tv.tvmaze.networks'):
            self.addDirectoryItem(32470 if indexLabels else 32469, 'tvNetworks', 'tvmaze.png' if iconLogos else 'networks.png', 'DefaultNetwork.png')
        if control.getMenuEnabled('navi.tv.imdb.languages'):
            self.addDirectoryItem(32462 if indexLabels else 32461, 'tvLanguages', 'imdb.png' if iconLogos else 'languages.png', 'DefaultAddonLanguage.png')
        if control.getMenuEnabled('navi.tv.imdb.certificates'):
            self.addDirectoryItem(32464 if indexLabels else 32463, 'tvCertificates', 'imdb.png' if iconLogos else 'certificates.png', 'DefaultTVShows.png')
        if control.getMenuEnabled('navi.tv.tmdb.airingtoday'):
            self.addDirectoryItem(32467 if indexLabels else 32465, 'tmdbTvshows&url=tmdb_airingtoday', 'tmdb.png' if iconLogos else 'airing-today.png', 'DefaultRecentlyAddedEpisodes.png')
        if control.getMenuEnabled('navi.tv.imdb.airingtoday'):
            self.addDirectoryItem(32466 if indexLabels else 32465, 'tvshows&url=airing', 'imdb.png' if iconLogos else 'airing-today.png', 'DefaultRecentlyAddedEpisodes.png')
        if control.getMenuEnabled('navi.tv.tmdb.ontv'):
            self.addDirectoryItem(32472 if indexLabels else 32471, 'tmdbTvshows&url=tmdb_ontheair', 'tmdb.png' if iconLogos else 'new-tvshows.png', 'DefaultRecentlyAddedEpisodes.png')
        if control.getMenuEnabled('navi.tv.imdb.returning'):
            self.addDirectoryItem(32474 if indexLabels else 32473, 'tvshows&url=active', 'imdb.png' if iconLogos else 'returning-tvshows.png', 'DefaultRecentlyAddedEpisodes.png')
        if control.getMenuEnabled('navi.tv.imdb.premiere'):
            self.addDirectoryItem(32476 if indexLabels else 32475, 'tvshows&url=premiere', 'imdb.png' if iconLogos else 'new-tvshows.png', 'DefaultRecentlyAddedEpisodes.png')
        if control.getMenuEnabled('navi.tv.tvmaze.calendar'):
            self.addDirectoryItem(32450 if indexLabels else 32027, 'calendars', 'tvmaze.png' if iconLogos else 'calendar.png', 'DefaultYear.png')

        #if (traktCredentials and control.setting('tv.widget.alt') != '0') or (not traktCredentials and control.setting('tv.widget') != '0'):
        indexer = 32481
        indexer_icon = 'tvmaze.png'
            #setting = control.setting('tv.widget.alt')
            #if setting == '2' or setting == '3':
                #indexer = 32482
                #indexer_icon = 'trakt.png'
        #self.addDirectoryItem(32480 if control.setting('index.labels') == 'false' else indexer, 'tvWidget', 'latest-episodes.png' if control.setting('icon.logos') == 'Traditional' else indexer_icon, 'DefaultRecentlyAddedEpisodes.png')
        if control.getMenuEnabled('navi.tv.tvmaze.newepisodes'):
            self.addDirectoryItem(32480 if control.setting('index.labels') == 'false' else 32481, 'calendar&url=added', 'latest-episodes.png' if control.setting('icon.logos') == 'Traditional' else 'tvmaze.png', 'DefaultTVShows.png', queue=True)
        #self.addDirectoryItem(32483 if control.setting('index.labels') == 'false' else 32481, 'calendar&url=added', 'latest-episodes.png' if control.setting('icon.logos') == 'Traditional' else 'tvmaze.png', 'DefaultTVShows.png', queue=True)

        #if (traktIndicators is True and not control.setting('tv.widget.alt') == '0') or (traktIndicators is False and not control.setting('tv.widget') == '0'):
            #self.addDirectoryItem(32006, 'tvWidget', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png')

        if lite is False:
            if control.getMenuEnabled('mylists.widget'):
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultAddonsSearch.png')
            self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonService.png')
            #self.addDirectoryItem(32030, 'tvPerson', 'imdb.png' if iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
            #self.addDirectoryItem(32010, 'tvSearch', 'trakt.png' if iconLogos else 'search.png', 'DefaultAddonsSearch.png')
        self.endDirectory()


    def mytvshows(self, lite=False):
        self.accountCheck()
        self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'DefaultVideoPlaylists.png')
        if traktCredentials and imdbCredentials:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultVideoPlaylists.png', context=(32551, 'tvshowsToLibrary&url=traktcollection&list_name=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultVideoPlaylists.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist&list_name=traktwatchlist'))
            self.addDirectoryItem(32041, 'episodesUserlists', 'userlists.png', 'DefaultVideoPlaylists.png')

            if traktIndicators:
                #self.addDirectoryItem(32468, 'episodesUnfinished&url=traktonDeck', 'trakt.png', 'DefaultYear.png')
                #self.addDirectoryItem(35308, 'episodesUnfinished&url=traktunfinished', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                self.addDirectoryItem(32027, 'calendar&url=mycalendar', 'trakt.png', 'DefaultYear.png', queue=True)
                self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultVideoPlaylists.png')

        elif traktCredentials:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultVideoPlaylists.png', context=(32551, 'tvshowsToLibrary&url=traktcollection&list_name=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultVideoPlaylists.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist&list_name=traktwatchlist'))
            self.addDirectoryItem(32041, 'episodesUserlists', 'trakt.png', 'DefaultVideoPlaylists.png')

            if traktIndicators:
                #self.addDirectoryItem(32468, 'episodesUnfinished&url=traktonDeck', 'trakt.png', 'DefaultYear.png')
                #self.addDirectoryItem(35308, 'episodesUnfinished&url=traktunfinished', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultVideoPlaylists.png', queue=True)
                self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultVideoPlaylists.png.png', queue=True)
                self.addDirectoryItem(32027, 'calendar&url=mycalendar', 'trakt.png', 'DefaultYear.png', queue=True)

        elif imdbCredentials:
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultVideoPlaylists.png')

        if not lite:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32030, 'tvPerson', 'imdb.png' if iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
            self.addDirectoryItem(32010, 'tvSearch', 'trakt.png' if iconLogos else 'search.png', 'DefaultAddonsSearch.png')
        self.endDirectory()

    def userlists(self, lite=False):
        self.addDirectoryItem('WolfGirl', 'U53R1nav', 'wolfgirl.png', 'DefaultMovies.png')
        self.addDirectoryItem('ShadowHawk', 'U53R2nav', 'shadowhawk.png', 'DefaultMovies.png')
        self.addDirectoryItem('DocOctyl', 'U53R3nav', 'dococtyl.png', 'DefaultMovies.png')
        #self.addDirectoryItem('U53R4', 'U53R4nav', 'icon.png', 'DefaultMovies.png')
        #self.addDirectoryItem('U53R5', 'U53R5nav', 'icon.png', 'DefaultMovies.png')
        self.endDirectory()

    def wolfgirl(self, lite=False):
        self.addDirectoryItem('Action', 'wolfgirlMovies&url=wgaction', 'wolfgirl.png', 'DefaultMovies.png')
        self.addDirectoryItem('Apocolypse', 'wolfgirlMovies&url=wgapocolypse', 'wolfgirl.png', 'DefaultMovies.png')
        self.addDirectoryItem('Comedy', 'wolfgirlMovies&url=wgcomedy', 'wolfgirl.png', 'DefaultMovies.png')
        self.addDirectoryItem('Documentaries', 'wolfgirlMovies&url=wgdocs', 'wolfgirl.png', 'DefaultMovies.png')
        self.addDirectoryItem('Monster', 'wolfgirlMovies&url=wgmonster', 'wolfgirl.png', 'DefaultMovies.png')
        self.addDirectoryItem('Paranormal', 'wolfgirlMovies&url=wgparanormal', 'wolfgirl.png', 'DefaultMovies.png')
        self.addDirectoryItem('Vault', 'wolfgirlMovies&url=wgvault', 'wolfgirl.png', 'DefaultMovies.png')
        self.endDirectory()

    def shadowhawks(self, lite=False):
        self.addDirectoryItem('Jay & Silent Bob', 'movies&url=shjaysilentbob', 'shadowhawk.png', 'DefaultMovies.png')
        self.addDirectoryItem('Stoner Movies', 'movies&url=shstonermovies', 'shadowhawk.png', 'DefaultMovies.png')
        self.addDirectoryItem('Monty Python', 'movies&url=shmontypython', 'shadowhawk.png', 'DefaultMovies.png')
        self.addDirectoryItem('Chech & Chong', 'movies&url=shchechchong', 'shadowhawk.png', 'DefaultMovies.png')
        self.addDirectoryItem('Stoner Tv Shows', 'tvshows&url=shstonertvshows', 'shadowhawk.png', 'DefaultTVShows.png')
        self.endDirectory()

    def dococtyl(self, lite=False):
        self.addDirectoryItem('70s Sci-fi', 'movies&url=dosyfy', 'dococtyl.png', 'DefaultMovies.png')
        self.addDirectoryItem('At the Drive-in', 'movies&url=dodrivein', 'dococtyl.png', 'DefaultMovies.png')
        self.addDirectoryItem('Parallel Universe', 'movies&url=douniverse', 'dococtyl.png', 'DefaultMovies.png')
        self.addDirectoryItem('Planet of the Apes', 'movies&url=dopota', 'dococtyl.png', 'DefaultMovies.png')
        self.addDirectoryItem('Time Travel', 'movies&url=dotimetravel', 'dococtyl.png', 'DefaultMovies.png')
        self.endDirectory()

    def userName4(self, lite=False):
        self.addDirectoryItem('U53R4 Movie List Name', 'movies&url=U53R4name', 'icon.png', 'DefaultMovies.png')
        self.endDirectory()

    def userName5(self, lite=False):
        self.addDirectoryItem('U53R5 Movie List Name', 'movies&url=U53R5name', 'icon.png', 'DefaultMovies.png')
        self.endDirectory()

    def anime(self, lite=False):
        self.addDirectoryItem(32001, 'animeMovies&url=anime', 'animemovie.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'animeTVshows&url=anime', 'animetv.png', 'DefaultTVShows.png')
        self.endDirectory()

    def randtv(self, lite=False):
        self.addDirectoryItem('[COLORmagenta]Be Patient! It may take a minute to load...[/COLOR]', '', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Action', 'random&rtype=show&url=genreaction', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Adventure', 'random&rtype=show&url=genreadventure', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Animation', 'random&rtype=show&url=genreAnimation', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Anime', 'random&rtype=show&url=genreAnime', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Biography', 'random&rtype=show&url=genreBiography', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Comedy', 'random&rtype=show&url=genreComedy', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Crime', 'random&rtype=show&url=genreCrime', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Documentary', 'random&rtype=show&url=genreDocumentary', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Drama', 'random&rtype=show&url=genreDrama', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Family', 'random&rtype=show&url=genreFamily', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Fantasy', 'random&rtype=show&url=genreFantasy', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('History', 'random&rtype=show&url=genreHistory', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Horror', 'random&rtype=show&url=genreHorror', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Music', 'random&rtype=show&url=genreMusic', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Musical', 'random&rtype=show&url=genreMusical', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Mystery', 'random&rtype=show&url=genreMystery', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('News', 'random&rtype=show&url=genrenews', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Reality-TV', 'random&rtype=show&url=genrereality', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Romance', 'random&rtype=show&url=genreRomance', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Science Fiction', 'random&rtype=show&url=genrescifi', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Sport', 'random&rtype=show&url=genreSport', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Talk-Show', 'random&rtype=show&url=genretalk', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Thriller', 'random&rtype=show&url=genreThriller', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('War', 'random&rtype=show&url=genreWar', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Western', 'random&rtype=show&url=genreWestern', 'genres.png', 'DefaultTVShows.png')
        self.endDirectory()

    def showMosts(self, lite=False):
        self.addDirectoryItem('Most Played This Week', 'tvshows&url=played1', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Played This Month', 'tvshows&url=played2', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Played This Year', 'tvshows&url=played3', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Played All Time', 'tvshows&url=played4', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Collected This Week', 'tvshows&url=collected1', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Collected This Month', 'tvshows&url=collected2', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Collected This Year', 'tvshows&url=collected3', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Collected All Time', 'tvshows&url=collected4', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Watched This Week', 'tvshows&url=watched1', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Watched This Month', 'tvshows&url=watched2', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Watched This Year', 'tvshows&url=watched3', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Most Watched All Time', 'tvshows&url=watched4', 'most-popular.png', 'DefaultTVShows.png')
        self.endDirectory()

    def tools(self):
        self.addDirectoryItem(32510, 'cfNavigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
        self.addDirectoryItem(32609, 'urlResolver', 'urlresolver.png', 'DefaultAddonService.png', isFolder=False)
        self.addDirectoryItem(32504, 'clearResolveURLcache', 'urlresolver.png', 'DefaultAddonProgram.png', isFolder=False)
        if control.condVisibility('System.HasAddon(service.upnext)'):
            self.addDirectoryItem(32505, 'UpNextSettings', 'UpNext.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32506, 'contextWatchdogsSettings', 'icon.png', 'DefaultAddonProgram.png', isFolder=False)
        #-- Providers - 5
        self.addDirectoryItem(32651, 'openscrapersSettings', 'OpenScrapers.png', 'DefaultAddonService.png', isFolder=False)
        self.addDirectoryItem(32083, 'cleanSettings', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        #-- General - 0
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        #-- Navigation - 1
        self.addDirectoryItem(32362, 'openSettings&query=1.1', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        #-- Playback - 4
        self.addDirectoryItem(32045, 'openSettings&query=4.1', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        #-- Api-keys - 9
        self.addDirectoryItem(32044, 'openSettings&query=9.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        #-- Downloads - 11
        self.addDirectoryItem(32048, 'openSettings&query=11.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        #-- Subtitles - 12
        self.addDirectoryItem(32046, 'openSettings&query=12.0', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.png', 'DefaultAddonService.png', isFolder=True)
        self.addDirectoryItem(32361, 'resetViewTypes', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        self.addDirectoryItem(32073, 'authTrakt&opensettings=false', 'trakt.png', 'DefaultAddonService.png', isFolder=False)
        self.endDirectory()


    def cf(self):
        self.addDirectoryItem(32610, 'clearAllCache&opensettings=false', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        self.addDirectoryItem(32611, 'clearSources&opensettings=false', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        self.addDirectoryItem(32612, 'clearMetaCache&opensettings=false', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        self.addDirectoryItem(32613, 'clearCache&opensettings=false', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        self.addDirectoryItem(32614, 'clearCacheSearch&opensettings=false', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        self.addDirectoryItem(32615, 'clearBookmarks&opensettings=false', 'tools.png', 'DefaultAddonService.png', isFolder=False)
        self.endDirectory()


    def library(self):
    # -- Library - 10
        self.addDirectoryItem(32557, 'openSettings&query=10.0', 'tools.png', 'DefaultAddonProgram.png', isFolder=False)
        self.addDirectoryItem(32558, 'updateLibrary', 'library_update.png', 'DefaultAddonLibrary.png', isFolder=False)
        self.addDirectoryItem(32676, 'cleanLibrary', 'library_update.png', 'DefaultAddonLibrary.png', isFolder=False)

        self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.png', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        if traktCredentials:
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection&list_name=traktcollection', 'trakt.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist&list_name=traktwatchlist', 'trakt.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem(32672, 'moviesListToLibrary&url=traktlists', 'trakt.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem(32673, 'moviesListToLibrary&url=traktlikedlists', 'trakt.png', 'DefaultMovies.png', isFolder=False)

        if tmdbSessionID:
            self.addDirectoryItem('TMDb: Import Movie Watchlist...', 'moviesToLibrary&url=tmdb_watchlist&list_name=tmdb_watchlist', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem('TMDb: Import Movie Favorites...', 'moviesToLibrary&url=tmdb_favorites&list_name=tmdb_favorites', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem('TMDb: Import Movie User list...', 'moviesListToLibrary&url=tmdb_userlists', 'tmdb.png', 'DefaultMovies.png', isFolder=False)

        if traktCredentials:
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection&list_name=traktcollection', 'trakt.png', 'DefaultTVShows.png', isFolder=False)
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist&list_name=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', isFolder=False)
            self.addDirectoryItem(32674, 'tvshowsListToLibrary&url=traktlists', 'trakt.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem(32675, 'tvshowsListToLibrary&url=traktlikedlists', 'trakt.png', 'DefaultMovies.png', isFolder=False)

        if tmdbSessionID:
            self.addDirectoryItem('TMDb: Import TV Watchlist...', 'tvshowsToLibrary&url=tmdb_watchlist&list_name=tmdb_watchlist', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem('TMDb: Import TV Favorites...', 'tvshowsToLibrary&url=tmdb_favorites&list_name=tmdb_favorites', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
            self.addDirectoryItem('TMDb: Import TV User list...', 'tvshowsListToLibrary&url=tmdb_userlists', 'tmdb.png', 'DefaultMovies.png', isFolder=False)
        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')
        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)
        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'trakt.png' if iconLogos else 'search.png', 'DefaultAddonsSearch.png')
        self.addDirectoryItem(32002, 'tvSearch', 'trakt.png' if iconLogos else 'search.png', 'DefaultAddonsSearch.png')
        self.addDirectoryItem(32029, 'moviePerson', 'imdb.png' if iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
        self.addDirectoryItem(32030, 'tvPerson', 'imdb.png' if iconLogos else 'people-search.png', 'DefaultAddonsSearch.png')
        self.endDirectory()


    def views(self):
        try:
            control.hide()
            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'),
                            (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1:
                return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')

            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'fanart': fanart, 'banner': banner})
            item.setProperty('IsPlayable', 'false')

            control.addItem(handle = int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import views
            views.setView(content, {})
        except:
            log_utils.error()
            return


    def accountCheck(self):
        if not traktCredentials and not imdbCredentials:
            control.hide()
            control.notification(title='default', message=32042, icon='WARNING', sound = notificationSound)
            sys.exit()


    def infoCheck(self, version):
        try:
            control.notification(title='default', message=32074, icon='WARNING',  time=5000, sound = notificationSound)
            return '1'
        except:
            return '1'


    def clearCacheAll(self):
        control.hide()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')

        if not yes:
            return

        try:
            from resources.lib.modules import cache
            cache.cache_clear_all()
            control.notification(title='default', message='All Cache Successfully Cleared!', icon='default', sound = notificationSound)
        except:
            log_utils.error()
            pass


    def clearCacheProviders(self):
        control.hide()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')

        if not yes:
            return

        try:
            from resources.lib.modules import cache
            cache.cache_clear_providers()
            control.notification(title='default', message='Provider Cache Successfully Cleared!', icon='default', sound = notificationSound)
        except:
            log_utils.error()
            pass


    def clearCacheMeta(self):
        control.hide()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')

        if not yes:
            return

        try:
            from resources.lib.modules import cache
            cache.cache_clear_meta()
            control.notification(title = 'default', message = 'Metadata Cache Successfully Cleared!', icon = 'default', sound = notificationSound)
        except:
            log_utils.error()
            pass


    def clearCache(self):
        control.hide()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')

        if not yes:
            return

        try:
            from resources.lib.modules import cache
            cache.cache_clear()
            control.notification(title = 'default', message = 'Cache Successfully Cleared!', icon = 'default', sound = notificationSound)
        except:
            log_utils.error()
            pass


    def clearCacheSearch(self):
        control.hide()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')

        if not yes:
            return

        try:
            from resources.lib.modules import cache
            cache.cache_clear_search()
            control.notification(title = 'default', message = 'Search History Successfully Cleared!', icon = 'default', sound = notificationSound)
        except:
            log_utils.error()
            pass


    def clearCacheSearchPhrase(self, table, name):
        control.hide()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')

        if not yes:
            return

        try:
            from resources.lib.modules import cache
            cache.cache_clear_SearchPhrase(table, name)
            control.notification(title = 'default', message = 'Search Phrase Successfully Cleared!', icon = 'default', sound = notificationSound)
        except:
            log_utils.error()
            pass

    def clearBookmarks(self):
        control.hide()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')

        if not yes:
            return

        try:
            from resources.lib.modules import cache
            cache.cache_clear_bookmarks()
            control.notification(title = 'default', message = 'Bookmarks Successfully Cleared!', icon = 'default', sound = notificationSound)
        except:
            log_utils.error()
            pass


    def clearBookmark(self, name, year):
        control.hide()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes:
            return
        try:
            from resources.lib.modules import cache
            cache.cache_clear_bookmark(name, year)
            control.notification(title = name, message = 'Bookmark Successfully Cleared!', icon = 'default', sound = notificationSound)
        except:
            log_utils.error()
            pass

    def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True, isPlayable=False, isSearch=False, table=''):
        try:
            if type(name) is str or type(name) is unicode:
                name = str(name)
            if type(name) is int:
                name = control.lang(name).encode('utf-8')
        except:
            log_utils.error()

        url = '%s?action=%s' % (sysaddon, query) if isAction else query

        thumb = control.joinPath(artPath, thumb) if artPath else icon

        if not icon.startswith('Default'):
             icon = control.joinPath(artPath, icon)

        cm = []
        queueMenu = control.lang(32065).encode('utf-8')

        if queue:
            cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))

        if context:
            cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))

        if isSearch:
            cm.append(('Clear Search Phrase', 'RunPlugin(%s?action=clearSearchPhrase&table=%s&name=%s)' % (sysaddon, table, name)))

        cm.append((control.lang(32610).encode('utf-8'), 'RunPlugin(%s?action=clearAllCache&opensettings=false)' % sysaddon))
        cm.append(('[COLOR magenta]Watchdogs Settings[/COLOR]', 'RunPlugin(%s?action=openSettings)' % sysaddon))

        item = control.item(label=name)
        item.addContextMenuItems(cm)

        if isPlayable:
            item.setProperty('IsPlayable', 'true')
        else:
            item.setProperty('IsPlayable', 'false')
        item.setArt({'icon': icon, 'poster': thumb, 'thumb': thumb, 'fanart': control.addonFanart(), 'banner': thumb})
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder= isFolder)


    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)
