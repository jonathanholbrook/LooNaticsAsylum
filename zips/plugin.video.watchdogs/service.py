# -*- coding: utf-8 -*-

import threading

from resources.lib.modules import control
from resources.lib.modules import log_utils
from resources.lib.modules import trakt

# check on adding while loop here with xbmc.Monitor().abortRequested() vs. inside the service function
control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

traktCredentials = trakt.getTraktCredentialsInfo()

try:
    AddonVersion = control.addon('plugin.video.watchdogs').getAddonInfo('version')
    RepoVersion = control.addon('repository.dedsec').getAddonInfo('version')
    log_utils.log('################### Watchdogs ######################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT Watchdogs VERSIONS REPORT ##########', log_utils.LOGNOTICE)
    log_utils.log('######## Watchdogs PLUGIN VERSION: %s ########' % str(AddonVersion), log_utils.LOGNOTICE)
    log_utils.log('#### DedSec REPOSITORY VERSION: %s ####' % str(RepoVersion), log_utils.LOGNOTICE)
    log_utils.log('################################################', log_utils.LOGNOTICE)

except:
    log_utils.log('############################# Watchdogs ############################', log_utils.LOGNOTICE)
    log_utils.log('################# CURRENT Watchdogs VERSIONS REPORT ################', log_utils.LOGNOTICE)
    log_utils.log('# ERROR GETTING Watchdogs VERSION - Missing Repo of failed Install #', log_utils.LOGNOTICE)
    log_utils.log('################################################################', log_utils.LOGNOTICE)


def syncTraktLibrary():
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.watchdogs/?action=tvshowsToLibrarySilent&url=traktcollection')
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.watchdogs/?action=moviesToLibrarySilent&url=traktcollection')


def syncTraktWatched():
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.watchdogs/?action=cachesyncTVShows')
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.watchdogs/?action=cachesyncMovies')
    # if control.setting('trakt.general.notifications') == 'true':
        # control.notification(title = 'default', message = 'Trakt Watched Status Sync Complete', icon='default', time=1, sound=False)


def check_for_addon_update():
    try:
        if control.setting('general.checkAddonUpdates') == 'false':
            return

        import re
        import requests
        repo_xml = requests.get('https://raw.githubusercontent.com/watchdogs36/dedsec/master/zips/addons.xml')
        if not repo_xml.status_code == 200:
            log_utils.log('Could not connect to repo XML, status: %s' % repo_xml.status_code, log_utils.LOGNOTICE)
            return
        repo_version = re.findall(r'<addon id=\"plugin.video.watchdogs\" version=\"(\d*.\d*.\d*)\"', repo_xml.text)[0]
        local_version = control.getWatchdogsVersion()

        if control.check_version_numbers(local_version, repo_version):
            while control.condVisibility('Library.IsScanningVideo'):
                control.sleep(10000)
            log_utils.log('A newer version of Watchdogs is available. Installed Version: v%s, Repo Version: v%s' % (local_version, repo_version), log_utils.LOGNOTICE)
            control.notification(title = 'default', message = control.lang(35523) % repo_version, icon = 'default', time=5000, sound=False)
    except:
        pass


if traktCredentials is True:
    syncTraktWatched()

if control.setting('autoTraktOnStart') == 'true':
    syncTraktLibrary()

if control.setting('general.checkAddonUpdates') == 'true':
    check_for_addon_update()

if int(control.setting('schedTraktTime')) > 0:
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
    log_utils.log('#################### STARTING TRAKT SCHEDULING ################', log_utils.LOGNOTICE)
    log_utils.log('#################### SCHEDULED TIME FRAME '+ control.setting('schedTraktTime')  + ' HOURS ###############', log_utils.LOGNOTICE)
    timeout = 3600 * int(control.setting('schedTraktTime'))
    schedTrakt = threading.Timer(timeout, syncTraktLibrary)
    schedTrakt.start()



