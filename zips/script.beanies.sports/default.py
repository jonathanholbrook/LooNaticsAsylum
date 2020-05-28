import sys
import os
from os.path import join
import urllib
import urllib2
import re
import webbrowser
import arrow

# use std kodi modules
import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui
from xbmcplugin import endOfDirectory, addDirectoryItem
import koding
from koding import Add_Dir

# import my stuff
from resources.lib._addon import *
from resources.lib._common import *
from resources.lib import clean_name

import resolveurl as RESOLVE

chkV = (xbmc.getInfoLabel('System.BuildVersion'))
if chkV.startswith('17'):
    myPath = sys.path[0]
else:
    myPath = os.path.dirname(__file__)

##### global Time variables #####

tFormat = 'YYYY-MM-DD HH:mm ZZZ'

utcNow = arrow.utcnow()
defaultTime = arrow.utcnow()
localDateTime = arrow.now()

utcZone = 'UTC'
#   siteZone = 'EST'
#   sdZone = 'PST'

siteZone = 'US/Eastern'
sdZone = 'US/Pacific'
myZone = 'Europe/London'
#addonZone = sdZone

addonZone = setting('zoneInfo')

localDateTime.format(tFormat)
siteTime = defaultTime.to(siteZone)
sdTime = defaultTime.to(sdZone)
myTime = defaultTime.to(myZone)

# Get the plugin url in plugin:// notation.
#    pluginUrl = sys.argv[0]
# Get the plugin handle as an integer number.
#    pluginHandle = int(sys.argv[1])

# default artwork setup - un hash to use std addon artwork
#      myIcon= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.jpg'))
#      myThumb= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.jpg'))
#      myWall = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))

# default artwork setup
#    addonPath = sys.path[0]
#    addonPath1 = join('special://home/addons',addon_id)
#            artPath = join('special://home/addons/' + addon_id,'resources/art')
artPath = join(myPath, 'resources/art')
ICON = 'live.png'       # used in menus
ICON2 = 'live.png'     # used in playlinks
ICON3 = 'nfl.png'
ICON4 = 'nhl.png'
ICON5 = 'nba.png'
ICON6 = 'ncaaf.png'
ICON7 = 'wwe.png'
ICON8 = 'mma.png'
ICON9 = 'mlb.png'
ICON10 = 'fifa.png'
ICON11 = 'pga.png'
ICON12 = 'tennis.png'
ICON13 = 'boxing.png'
ICON14 = 'ncaa-basketball.png'
ICON15 = 'xfl.png'
ICON16 = 'cricket.png'
ICON17 = 'volleyball.png'
ICON18 = 'nascar.png'
ICON19 = 'tabletennis.png'
ICON20 = 'handball.png'

WALL = 'wall.jpg'

myIcon = join(artPath, ICON)
myIcon2 = join(artPath, ICON2)
myIcon3 = join(artPath, ICON3)
myIcon4 = join(artPath, ICON4)
myIcon5 = join(artPath, ICON5)
myIcon6 = join(artPath, ICON6)
myIcon7 = join(artPath, ICON7)
myIcon8 = join(artPath, ICON8)
myIcon9 = join(artPath, ICON9)
myIcon10 = join(artPath, ICON10)
myIcon11 = join(artPath, ICON11)
myIcon12 = join(artPath, ICON12)
myIcon13 = join(artPath, ICON13)
myIcon14 = join(artPath, ICON14)
myIcon15 = join(artPath, ICON15)
myIcon16 = join(artPath, ICON16)
myIcon17 = join(artPath, ICON17)
myIcon18 = join(artPath, ICON18)
myIcon19 = join(artPath, ICON19)
myIcon20 = join(artPath, ICON20)

myThumb = join(artPath, ICON)
myWall = join(artPath, WALL)


def index():
    print ('Index mode')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]TESTING[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 152
    Menu(title, '', mode, myIcon12, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 2000
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]XFL[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 3000
    Menu(title, '', mode, myIcon15, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 1000
    Menu(title, '', mode, myIcon5, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]MLB[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 4000
    Menu(title, '', mode, myIcon9, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NHL[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 5000
    Menu(title, '', mode, myIcon4, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA-F[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 6000
    Menu(title, '', mode, myIcon6, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA-B[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 8000
    Menu(title, '', mode, myIcon14, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]UFC[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 7000
    Menu(title, '', mode, myIcon8, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]BOXING[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 9000
    Menu(title, '', mode, myIcon13, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]FIFA-SOCCER[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 10000
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]TENNIS[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 11000
    Menu(title, '', mode, myIcon12, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NASCAR[/COLOR] [COLOR orchid](NL)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 126
    Menu(title, '', mode, myIcon18, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]FORMULA 1[/COLOR] [COLOR orchid](QA)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 144
    Menu(title, '', mode, myIcon, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]FORMULA 1[/COLOR] [COLOR orchid](SN)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 206
    Menu(title, '', mode, myIcon, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]CRICKET[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 114
    Menu(title, '', mode, myIcon16, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]VOLLEY BALL[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 118
    Menu(title, '', mode, myIcon17, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]E SPORTS[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 116
    Menu(title, '', mode, myIcon, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]TABLE TENNIS[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 128
    Menu(title, '', mode, myIcon19, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]HANDBALL[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 130
    Menu(title, '', mode, myIcon20, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]VARIOUS SPORTS[/COLOR] [COLOR orchid]LIVE[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 12000
    Menu(title, '', mode, myIcon2, myWall, '', '', '')


def nba():
    print ('Index mode')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA LIVE[/COLOR] [COLOR orchid](60)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 70
    Menu(title, '', mode, myIcon5, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA LIVE[/COLOR] [COLOR orchid](7S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 76
    Menu(title, '', mode, myIcon5, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA LIVE[/COLOR] [COLOR orchid](AS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 134
    Menu(title, '', mode, myIcon5, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA LIVE[/COLOR] [COLOR orchid](CS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 60
    Menu(title, '', mode, myIcon5, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA LIVE[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 104
    Menu(title, '', mode, myIcon5, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA LIVE[/COLOR] [COLOR orchid](QA)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 136
    Menu(title, '', mode, myIcon5, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA LIVE[/COLOR] [COLOR orchid](YSS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 88
    Menu(title, '', mode, myIcon5, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA LIVE[/COLOR] [COLOR orchid](6S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 156
    Menu(title, '', mode, myIcon5, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NBA LIVE[/COLOR] [COLOR orchid](SN)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 200
    Menu(title, '', mode, myIcon5, myWall, '', '', '')


def nfl():
    print ('Index mode')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL LIVE[/COLOR] [COLOR orchid](60)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 72
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

    #title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL LIVE[/COLOR] [COLOR orchid](7S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    #mode = 74
    # Menu(title,'',mode,myIcon3,myWall,'','','')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL LIVE[/COLOR] [COLOR orchid](CS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 42
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL LIVE[/COLOR] [COLOR orchid](VK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 48
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL LIVE[/COLOR] [COLOR orchid](VL)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 64
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL LIVE[/COLOR] [COLOR orchid](YSS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 90
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL LIVE[/COLOR] [COLOR orchid](6S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 160
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL LIVE[/COLOR] [COLOR orchid](SN)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 202
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NFL LIVE[/COLOR] [COLOR orchid](CW)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 210
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

def xfl():
    print ('Index mode')
    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]XFL LIVE[/COLOR] [COLOR orchid](AS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 132
    Menu(title, '', mode, myIcon15, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]XFL LIVE[/COLOR] [COLOR orchid](CS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 124
    Menu(title, '', mode, myIcon15, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]XFL LIVE[/COLOR] [COLOR orchid](QA)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 148
    Menu(title, '', mode, myIcon3, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]XFL LIVE[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 120
    Menu(title, '', mode, myIcon15, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]XFL LIVE[/COLOR] [COLOR orchid](VK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 76
    Menu(title, '', mode, myIcon15, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]XFL LIVE[/COLOR] [COLOR orchid](YSS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 96
    Menu(title, '', mode, myIcon15, myWall, '', '', '')


def mlb():
    print ('Index mode')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]MLB LIVE[/COLOR] [COLOR orchid](7S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 13
    Menu(title, '', mode, myIcon9, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]MLB LIVE[/COLOR] [COLOR orchid](PS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 10
    Menu(title, '', mode, myIcon9, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]MLB LIVE[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 122
    Menu(title, '', mode, myIcon9, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]MLB LIVE[/COLOR] [COLOR orchid](VK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 52
    Menu(title, '', mode, myIcon9, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]MLB LIVE[/COLOR] [COLOR orchid](YS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 32
    Menu(title, '', mode, myIcon9, myWall, '', '', '')


def nhl():
    print ('Index mode')
    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NHL LIVE[/COLOR] [COLOR orchid](7S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 8
    Menu(title, '', mode, myIcon4, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NHL LIVE[/COLOR] [COLOR orchid](FN)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 68
    Menu(title, '', mode, myIcon4, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NHL LIVE[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 110
    Menu(title, '', mode, myIcon4, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NHL LIVE[/COLOR] [COLOR orchid](QA)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 140
    Menu(title, '', mode, myIcon4, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NHL LIVE[/COLOR] [COLOR orchid](VK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 54
    Menu(title, '', mode, myIcon4, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NHL LIVE[/COLOR] [COLOR orchid](YSS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 92
    Menu(title, '', mode, myIcon4, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NHL LIVE[/COLOR] [COLOR orchid](6S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 158
    Menu(title, '', mode, myIcon4, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NHL REPLAYS[/COLOR][/B][COLOR orchid]*[/COLOR]'
    mode = 26
    Menu(title, '', mode, myIcon4, myWall, '', '', '')


def ncaa():
    print ('Index Mode')
    #title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA FOOTBALL[/COLOR] [COLOR orchid](YS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    #mode = 30
    # Menu(title,'',mode,myIcon6,myWall,'','','')
    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA FOOTBALL[/COLOR] [COLOR orchid](CS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 44
    Menu(title, '', mode, myIcon6, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA FOOTBALL[/COLOR] [COLOR orchid](QA)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 138
    Menu(title, '', mode, myIcon6, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA FOOTBALL[/COLOR] [COLOR orchid](VL)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 66
    Menu(title, '', mode, myIcon6, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA FOOTBALL[/COLOR] [COLOR orchid](VK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 56
    Menu(title, '', mode, myIcon6, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA FOOTBALL[/COLOR] [COLOR orchid](6S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 162
    Menu(title, '', mode, myIcon6, myWall, '', '', '')


def ncaab():
    print ('Index Mode')
    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA MENS BASEKETBALL LIVE[/COLOR] [COLOR orchid](7S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 78
    Menu(title, '', mode, myIcon14, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA MENS BASEKETBALL LIVE[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 106
    Menu(title, '', mode, myIcon14, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA MENS BASEKETBALL LIVE[/COLOR] [COLOR orchid](YSS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 86
    Menu(title, '', mode, myIcon14, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]NCAA MENS BASEKETBALL LIVE[/COLOR] [COLOR orchid](6S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 164
    Menu(title, '', mode, myIcon14, myWall, '', '', '')


def ufc():
    print ('Index Mode')
    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]UFC LIVE[/COLOR] [COLOR orchid](60)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 84
    Menu(title, '', mode, myIcon8, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]UFC LIVE[/COLOR] [COLOR orchid](CS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 40
    Menu(title, '', mode, myIcon8, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]UFC LIVE[/COLOR] [COLOR orchid](VK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 62
    Menu(title, '', mode, myIcon8, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]UFC LIVE[/COLOR] [COLOR orchid](QA)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 146
    Menu(title, '', mode, myIcon8, myWall, '', '', '')


def boxing():
    print ('Index Mode')
    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]BOXING LIVE[/COLOR] [COLOR orchid](CS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 58
    Menu(title, '', mode, myIcon13, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]BOXING LIVE[/COLOR] [COLOR orchid](QA)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 142
    Menu(title, '', mode, myIcon13, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]BOXING LIVE[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 102
    Menu(title, '', mode, myIcon13, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]BOXING LIVE[/COLOR] [COLOR orchid](6S)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 154
    Menu(title, '', mode, myIcon13, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]BOXING LIVE[/COLOR] [COLOR orchid](CW)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 208
    Menu(title, '', mode, myIcon13, myWall, '', '', '')


def fifa():
    print ('Index Mode')
    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]SOCCER FROM ALL OVER[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 112
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]MAJOR LEAGUE SOCCER[/COLOR] [COLOR orchid](MLS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 20
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]EUROPEAN SOCCER[/COLOR] [COLOR orchid](60)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 80
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]EUROPEAN SOCCER[/COLOR] [COLOR orchid](SN)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 204
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]EUROPEAN SOCCER[/COLOR] [COLOR orchid](CW)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 212
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]BUNDESLIGA SOCCER[/COLOR] [COLOR orchid](MK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 228
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]CHAMPIONS LEAGUE SOCCER[/COLOR] [COLOR orchid](MK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 230
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]LA LIGA SOCCER[/COLOR] [COLOR orchid](MK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 232
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]LIGUE 1 SOCCER[/COLOR] [COLOR orchid](MK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 234
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]PREMIER LEAGUE SOCCER[/COLOR] [COLOR orchid](MK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 236
    Menu(title, '', mode, myIcon10, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]SERIE A SOCCER[/COLOR] [COLOR orchid](MK)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 238
    Menu(title, '', mode, myIcon10, myWall, '', '', '')


def tennis():
    print ('Index Mode')
    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]TENNIS LIVE[/COLOR] [COLOR orchid](SE)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 108
    Menu(title, '', mode, myIcon12, myWall, '', '', '')


    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]TENNIS LIVE[/COLOR] [COLOR orchid](TL)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 152
    Menu(title, '', mode, myIcon12, myWall, '', '', '')



def various():
    print ('Index Mode')
    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]VARIOUS SPORTS[/COLOR] [COLOR orchid](HS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 15
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]LIVE VARIOUS CHANNELS[/COLOR] [COLOR orchid](YSS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 82
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]TRENDING CHANNELS[/COLOR] [COLOR orchid](YSS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 94
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]LIVE TV CHANNELS[/COLOR] [COLOR orchid](WS)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 214
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]LIVE TV CHANNELS[/COLOR] [COLOR orchid](S24)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 218
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]LIVE TV CHANNELS[/COLOR] [COLOR orchid](QN)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 216
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]ARCONAI SHOWS[/COLOR] [COLOR orchid](AR)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 220
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]ARCONAI MOVIES[/COLOR] [COLOR orchid](AR)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 222
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]ARCONAI CABLE[/COLOR] [COLOR orchid](AR)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 224
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

    title = '[COLOR orchid]*[/COLOR] [B][COLOR white]LIVE TV CHANNELS[/COLOR] [COLOR orchid](SB)[/COLOR][/B] [COLOR orchid]*[/COLOR]'
    mode = 226
    Menu(title, '', mode, myIcon2, myWall, '', '', '')

# FUNCTIONS FROM HERE
######################
def main():
    return
######################


def streamNHL720():
    from resources.lib import stream720
    nhl720List = stream720.getNHL()
    if not nhl720List:
        print 'No NHL Games Available'
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n' + \
            '[COLOR orchid]'+'                                   ' + \
            'Click OK to quit[/I][/COLOR]'
        koding.OK_Dialog(title='NHL Games not available....', message=thisMess)
        nhl()
    for items in nhl720List:
        game = items.get('game', 'Game Missing')
        stream = items.get('stream', 'Stream Missing')
        quality = items.get('quality', 'Quality Missing')

        cName = '[COLOR orchid]' + \
            str(game) + '[/COLOR] [COLOR orchid][I](' + \
            str(quality) + 'k)' + '[/I][/COLOR]'
        cLink = stream
        icon = myIcon4

        Play(cName, cLink, 3, icon, myWall, '', '', '')

    return

######################


def playOffStreamMLBSchedule():
    games_list = []
    from resources.lib import playoffstreamsMLB
    games_list = playoffstreamsMLB.getMLBList()
    for game in games_list:
        title = game.get('title', 'Title Missing')
        time = game.get('time', 'Time Missing')

        if 'MLB NETWORK' in title. upper():
            cName = '[COLOR orchid]' + '24x7 ' + '[COLOR orchid]' + \
                str(title). replace('Live Stream', '') + '[/COLOR]'
        elif not 'MLB NETWORK' in title.upper():
            print ''
            print ('PJ DEBUG inside elif mlb not seen - cName = ' + cName)
            print ('PJ DEBUG inside elif mlb not seen - title = ' + title)
            print ('PJ DEBUG inside elif mlb not seen - time = ' + time)
            #    tempTime = str (time)
            #    tempTime1 = arrow.get(time, 'YYYY-MM-DD HH:mm')
            #    print ('PJ DEBUG - tempTime = ' + str (tempTime))
            #    print ('PJ DEBUG - tempTime1 = ' + tempTime1.format(tFormat))

            evStime1 = arrow.get(time, 'YYYY-MM-DD HH:mm')

            print ('PJ DEBUG trying set evStime1 = ' + str(evStime1))

            evStime = evStime1.replace(tzinfo=siteZone)
            uGtime = evStime.to(siteZone)
            #uGtime1 = uGtime.to(sdZone)
            #uGtime2 = uGtime.to(myZone)

            schedTime = uGtime.to(addonZone)

            print ('PJ DEBUG else reset time zone - localDateTime = ' +
                   str(localDateTime))
            print ('PJ DEBUG else reset time zone - evStime = ' + str(evStime))
            print ('PJ DEBUG else reset time zone - evStime = ' + str(evStime))
            print ('PJ DEBUG else reset time zone - uGtime = ' + str(uGtime))
            print ('PJ DEBUG else reset time zone - schedTime = ' + str(schedTime))

            #    time = 'Live at ' + time.split (' ')[-1] + '(EST)'

            cName = '[COLOR white]' + schedTime.strftime('%d-%b ') + '[COLOR orchid]' + schedTime.strftime(
                '%H:%M (%Z)') + ' [COLOR orchid]'+str(title). replace('Live', ''). strip() + '[/COLOR]'
            print ('PJ DEBUG mlb not seen - cName set in else = ' + cName)

        else:
            print ('PJ DEBUG mlb not seen - cName not set - now in else = ' + cName)

        if not cName:
            #    pass
            cName = '[COLOR red]' + str(time) + ' [COLOR orchid]' + \
                str(title). replace('Live', ''). strip() + '[/COLOR]'
            print ('PJ DEBUG mlb not seen - cName set in if not at end = ' + cName)

        Menu(cName, title, 5, myIcon9, myWall, '', '', '')

######################


def streamplayOffStreamMLB(name):
    from resources.lib import playoffstreamsMLB
    stream = playoffstreamsMLB.getStream(name)
    if stream:
        for i in stream:
            title = i['title']
            cLink = i['stream']
            quality = i['quality']
            cName = cName = '[COLOR white]' + \
                str(quality) + '[/COLOR] [COLOR orchid]' + \
                str(title) + '[/COLOR]'
            Play(cName, cLink, 3, myIcon9, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        mlb()


def mlsliveold():
    from resources.lib import mlsTest
    game_list = mlsTest.get_game()
    if game_list:
        for i in game_list:
            cName = i['title']
            cLink = i['link']
            Menu(cName, cLink, 21, myIcon10, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        mlb()


def mlslive():
    from resources.lib import mlsTest
    game_list = mlsTest.readMLS()

    if game_list:
        for items in game_list:
            game = items.get('game', 'Game Missing')
            stream = items.get('stream', 'Stream Missing')
            schedule = items.get('schedule', 'Schedule Missing')

            #    evStime1 = arrow.get(schedule, 'YYYY-MM-DDTHH:mm')
            #    evStime = evStime1.replace(tzinfo=utcZone)
            schedTime = schedule.to(addonZone)

            art = items.get('art', 'Art Missing')
            cName = '[COLOR white]' + schedTime.strftime('%d %b ') + '[/COLOR][COLOR orchid]' + schedTime.strftime(
                '%H:%M (%Z) ') + '[COLOR orchid]' + game + '[/COLOR]'
            cLink = stream
            if not 'missing' in art.lower():
                icon = art
            else:
                icon = myIcon10

            Menu(cName, cLink, 21, icon, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        mlb()


def playmls(link):
    from resources.lib import mlsTest
    m3u8 = mlsTest.get_stream(link)
    if m3u8:
        Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
             m3u8, 3, myIcon10, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        mlb()
######################


def sixtyfpsnba():
    from resources.lib import sixtyfpsnba as nba
    games = nba.get_games()
    if games:
        for game in games:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 71, myIcon5, myWall, '', '', '')
    else:
        pass


def playsixtyfpsnba(url):
    from resources.lib import sixtyfpsnba as nba
    stream = nba.get_stream(url)
    if stream:
        for i in stream:
            title = i.get("title", "Title Missing")
            stream = i.get("url", "Url Missing")
            Play(title, stream, 3, myIcon5, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nba()
######################
######################


def sixtyfpsnfl():
    from resources.lib import sixtyfpsnfl as nfl
    games = nfl.get_games()
    if games:
        for game in games:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 73, myIcon3, myWall, '', '', '')
    else:
        pass


def playsixtyfpsnfl(url):
    from resources.lib import sixtyfpsnfl as nfl
    stream = nfl.get_stream(url)
    if stream:
        for i in stream:
            title = i.get("title", "Title Missing")
            stream = i.get("url", "Url Missing")
            Play(title, stream, 3, myIcon3, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nfl()
##########ACRONAI############
def arconai_shows():
    from resources.lib import arconai_tv as tv
    shows = tv.get_shows()
    if shows:
        for show in shows:
            title = show.get("title","Title Missing")
            link = show.get("link","Link Missing")
            image = show.get("image","Image Missing")
            Menu(title,link,221,image,'','',"Watch Live " + title + ".","","")
    else:
        pass


def play_arconai_shows(url):
    from resources.lib import arconai_tv as tv
    stream = tv.get_streams(url)
    if stream:
        for s in stream:
            title = s.get("title","Title Missing")
            link = s.get("link","Link Missing")
            Play(title, link, 3, myIcon2, myWall, '', '', '')

def arconai_movies():
    from resources.lib import arconai_tv as tv
    movies = tv.get_movies()
    thumbnail = ''
    fanart = ''
    if movies:
        for movie in movies:
            title = movie.get("title","Title Missing")
            link = movie.get("link","Link Missing")
            image = movie.get("image","Image Missing")
            Menu(title,link,223,image,'','',"Watch Live " + title + ".","","")
    else:
        pass


def play_arconai_movies(url):
    from resources.lib import arconai_tv as tv
    stream = tv.get_streams(url)
    if stream:
        for s in stream:
            title = s.get("title","Title Missing")
            link = s.get("link","Link Missing")
            Play(title, link, 3, myIcon2, myWall, '', '', '')

def arconai_cable():
    from resources.lib import arconai_tv as tv
    cables = tv.get_cables()
    if cables:
        for cable in cables:
            title = cable.get("title","Title Missing")
            link = cable.get("link","Link Missing")
            image = cable.get("image","Image Missing")
            Menu(title,link,225,image,'','',"Watch Live " + title + ".","","")
    else:
        pass


def play_arconai_cable(url):
    from resources.lib import arconai_tv as tv
    stream = tv.get_streams(url)
    if stream:
        for s in stream:
            title = s.get("title","Title Missing")
            link = s.get("link","Link Missing")
            Play(title, link, 3, myIcon2, myWall, '', '', '')
######################


def sixtyfpssoccer():
    from resources.lib import sixtyfpssoccer as soccer
    games = soccer.get_games()
    if games:
        for game in games:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 81, myIcon10, myWall, '', '', '')
    else:
        pass


def playsixtyfpssoccer(url):
    from resources.lib import sixtyfpssoccer as soccer
    stream = soccer.get_stream(url)
    if stream:
        for i in stream:
            title = i.get("title", "Title Missing")
            stream = i.get("url", "Url Missing")
            Play(title, stream, 3, myIcon10, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        fifa()


def sixtyfpsufc():
    from resources.lib import sixtyfpsufc as ufc
    games = ufc.get_games()
    if games:
        for game in games:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 85, myIcon8, myWall, '', '', '')
    else:
        pass


def playsixtyfpsufc(url):
    from resources.lib import sixtyfpsufc as ufc
    stream = ufc.get_stream(url)
    if stream:
        for i in stream:
            title = i.get("title", "Title Missing")
            stream = i.get("url", "Url Missing")
            Play(title, stream, 3, myIcon8, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ufc()

######################


def seventwentynfl():
    from resources.lib import seventwentynfl as nfl
    game_list = nfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 75, myIcon3, myWall, '', '', '')
    else:
        pass


def playseventwentynfl(link):
    from resources.lib import seventwentynfl as nfl
    stream = nfl.get_stream(link)
    if stream:
        for game in stream:
            title = game.get("title", "Title Missing")
            url = game.get("link", "Stream Missing")
            Play(title, url, 3, myIcon3, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nfl()
######################
######################


def volokitxfl():
    from resources.lib import volokitxfl
    game_list = volokitxfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 77, myIcon15, myWall, '', '', '')
    else:
        pass


def playvolokitxfl(link):
    from resources.lib import volokitxfl
    stream = volokitxfl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon15, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        xfl()
######################
######################


def seventwentyncaam():
    from resources.lib import seventwentyncaam as ncaam
    game_list = ncaam.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 79, myIcon14, myWall, '', '', '')
    else:
        pass


def playseventwentyncaam(link):
    from resources.lib import seventwentyncaam as ncaam
    stream = ncaam.get_stream(link)
    if stream:
        for game in stream:
            title = game.get("title", "Title Missing")
            url = game.get("link", "Stream Missing")
            Play(title, url, 3, myIcon14, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ncaab()
######################


def ysstv():
    from resources.lib import yssTV as ytv
    game_list = ytv.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 83, myIcon2, myWall, '', '', '')
    else:
        pass


def playysstv(link):
    from resources.lib import yssTV as ytv
    stream = ytv.get_stream(link)
    if stream:
        for game in stream:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Play(title, link, 3, myIcon2, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        various()


def yssncaab():
    from resources.lib import yssncaab as ncaab
    game_list = ncaab.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 87, myIcon14, myWall, '', '', '')
    else:
        pass


def playyssncaab(link):
    from resources.lib import yssncaab as ncaab
    stream = ncaab.get_stream(link)
    if stream:
        for game in stream:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Play(title, link, 3, myIcon14, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ncaab()

######################
######################


def yssnba():
    from resources.lib import yssnba as nba
    game_list = nba.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 89, myIcon5, myWall, '', '', '')
    else:
        pass


def playyssnba(link):
    from resources.lib import yssnba as nba
    stream = nba.get_stream(link)
    if stream:
        for game in stream:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Play(title, link, 3, myIcon5, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nba()


def yssnfl():
    from resources.lib import yssnfl as nfl
    game_list = nfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 91, myIcon3, myWall, '', '', '')
    else:
        pass


def playyssnfl(link):
    from resources.lib import yssnfl as nfl
    stream = nfl.get_stream(link)
    if stream:
        for game in stream:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Play(title, link, 3, myIcon3, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nfl()


def yssnhl():
    from resources.lib import yssnhl as nhl
    game_list = nhl.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 93, myIcon4, myWall, '', '', '')
    else:
        pass


def playyssnhl(link):
    from resources.lib import yssnhl as nhl
    stream = nhl.get_stream(link)
    if stream:
        for game in stream:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Play(title, link, 3, myIcon4, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nhl()


def ysstrending():
    from resources.lib import ysstrending as trending
    game_list = trending.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 95, myIcon, myWall, '', '', '')
    else:
        pass


def playysstrending(link):
    from resources.lib import ysstrending as trending
    stream = trending.get_stream(link)
    if stream:
        for game in stream:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Play(title, link, 3, myIcon2, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        various()


def yssxfl():
    from resources.lib import yssxfl as xfl
    game_list = xfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Menu(title, link, 97, myIcon15, myWall, '', '', '')
    else:
        pass


def playyssxfl(link):
    from resources.lib import yssxfl as xfl
    stream = xfl.get_stream(link)
    if stream:
        for game in stream:
            title = game.get("title", "Title Missing")
            link = game.get("link", "Link Missing")
            Play(title, link, 3, myIcon15, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        xfl()


def freestreamNHL():
    from resources.lib import freestreamsnhl as fsn
    game_list = fsn.get_games()
    if game_list:
        for game in game_list:
            title = game.get("title", "Title Missing")
            url = game.get("link", "Link Missing")
            Menu(title, url, 69, myIcon4, myWall, '', '', '')
    else:
        pass


def playfreestreamNHL(link):
    from resources.lib import freestreamsnhl as fsn
    stream = fsn.get_stream(link)
    if stream:
        for i in stream:
            title = i.get("title", "Title Missing")
            s = i.get("link", "Stream Missing")
            Play(title, s, 3, myIcon4, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nhl()


def tennislive():
    from resources.lib import tennis
    game_list = tennis.readtennis()

    if game_list:
        for items in game_list:
            game = items.get('game', 'Game Missing')
            stream = items.get('stream', 'Stream Missing')
            schedule = items.get('schedule', 'Schedule Missing')

            #    evStime1 = arrow.get(schedule, 'YYYY-MM-DDTHH:mm')
            #    evStime = evStime1.replace(tzinfo=utcZone)
            schedTime = schedule.to(addonZone)

            art = items.get('art', 'Art Missing')
            cName = '[COLOR white]' + schedTime.strftime('%d %b ') + '[COLOR orchid]' + schedTime.strftime(
                '%H:%M (%Z) ') + '[COLOR deepskyblue]' + game + '[/COLOR]'
            cLink = stream
            if not 'missing' in art.lower():
                icon = art
            else:
                icon = myIcon12

            Menu(cName, cLink, 47, icon, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        tennis()


def playtennis(link):
    from resources.lib import tennis
    m3u8 = tennis.get_stream(link)
    if m3u8:
        Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
             m3u8, 3, myIcon12, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        tennis()

######################


def boxinglive():
    from resources.lib import techjaffaboxing
    game_list = techjaffaboxing.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 59, myIcon13, myWall, '', '', '')
    else:
        pass


def playboxinglive(link):
    from resources.lib import techjaffaboxing
    game = techjaffaboxing.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon13, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        boxing()

################################################


def nbalive():
    from resources.lib import techjaffanba
    game_list = techjaffanba.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 61, myIcon5, myWall, '', '', '')
    else:
        pass


def playnbalive(link):
    from resources.lib import techjaffanba
    stream = techjaffanba.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('link', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon5, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nba()
###############################
############NASCAR#############


def nascar():
    from resources.lib import nascar
    game_list = nascar.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            time = game.get('time', 'Time Missing')
            link = game.get('link', 'Link Missing')
            cname = '[COLOR white]' + \
                str(time) + 'EST' + ' - ' + str(title) + '[/COLOR]'

            Menu(cname, link, 127, myIcon18, myWall, '', '', '')
    else:
        pass


def playnascar(link):
    from resources.lib import nascar
    stream = nascar.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('link', 'Link Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon18, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()

def sportsbay_tv():
    from resources.lib import sportsbay_tv
    game_list = sportsbay_tv.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 227, myIcon2, myWall, '', '', '')
    else:
        pass


def play_sportsbay_tv(link):
    from resources.lib import sportsbay_tv
    stream = sportsbay_tv.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('link', 'Link Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon2, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()
################################
################TENNIS LINE################
def tennis_live():
    from resources.lib import tennis_live
    game_list = tennis_live.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            time = game.get('time', 'Time Missing')
            link = game.get('link', 'Link Missing')
            cname = '[COLOR white]' +  str(time) + 'EST' + ' - ' + str(title) + '[/COLOR]'
        Menu(cname, link, 151, myIcon12, myWall, '', '', '')
    else:
        pass

def play_tennis_live(link):
    from resources.lib import tennis_live
    stream = tennis_live.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('link', 'Link Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon12, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()

def xfllive():
    from resources.lib import techjaffaxfl
    game_list = techjaffaxfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 125, myIcon15, myWall, '', '', '')
    else:
        pass


def playxfllive(link):
    from resources.lib import techjaffaxfl
    stream = techjaffaxfl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('link', 'Stream Missing')
            Play('Play Stream', s, 3, myIcon15, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        xfl()
###############################


def scheduleMLB():
    #    global mlb720List, mlb720Listt, game
    mlb720List = []
    mlb720Listt = []
    from resources.lib import mlb
    mlb720Listt = mlb.getSchedule()
    thisMess = ''
    if mlb720Listt:
        #    for items in mlb720Listt:
        #    game = items.get('game', 'Game Missing')
        #    schedule = items.get('schedule', 'Schedule Missing')
        #    thisMess =thisMess + '[COLOR white]' + ' ' + str(game) + ' ' + '\nSchedule ON: ' + schedule + '\nStatus: Not Live' +'\n'+'\n'+'\n'+''+'[/COLOR]'
        #    koding.Text_Box('[COLOR gold]Schedule List[/COLOR]',thisMess)
        ##    koding.OK_Dialog(title='Schedule List', message=thisMess)
        #    index()
        print ('##########')
        print (' ')
        for items in mlb720Listt:
            cName = ''
            tempTime = ''
            evStime = evStime1 = uGtime = uGtime1 = uGtime2 = schedTime = ''
            game = items.get('game', 'Game Missing')
            #    stream =items.get('stream','Stream Missing')
            #    quality =items.get('quality','Quality Missing')
            schedule = items.get('schedule', 'Schedule Missing')

            print ('PJ DEBUG - game = ' + game)
            print ('PJ DEBUG - schedule = ' + schedule)

            #    if not '24 x 7' in schedule :

            if 'MLB NETWORK' in game.upper():
                #    cName = '[COLOR orchid]'+str (game) + '[COLOR orchid]'+ ' Schedule On: ' + str (schedule) + '[/I][/COLOR]'
                cName = '[COLOR orchid]' + str(schedule) + ' [COLOR orchid]'+str(
                    game). replace('Live', ''). strip() + '[/COLOR]'
                print ('PJ DEBUG inside if mlb seen - cName = ' + cName)

            elif not 'MLB NETWORK' in game.upper():
                print ''
                print ('PJ DEBUG inside elif mlb not seen - cName = ' + cName)
                print ('PJ DEBUG inside elif mlb not seen - game = ' + game)
                print ('PJ DEBUG inside elif mlb not seen - schedule = ' + schedule)
                #    tempTime = str (schedule)
                #    tempTime1 = arrow.get(schedule, 'YYYY-MM-DD HH:mm')
                #    print ('PJ DEBUG - tempTime = ' + str (tempTime))
                #    print ('PJ DEBUG - tempTime1 = ' + tempTime1.format(tFormat))

                evStime1 = arrow.get(schedule, 'YYYY-MM-DD HH:mm')

                print ('PJ DEBUG trying set evStime1 = ' + str(evStime1))

                evStime = evStime1.replace(tzinfo=siteZone)
                uGtime = evStime.to(siteZone)
                #    uGtime1 = uGtime.to(sdZone)
                #    uGtime2 = uGtime.to(myZone)

                schedTime = uGtime.to(addonZone)

                print (
                    'PJ DEBUG else reset time zone - localDateTime = ' + str(localDateTime))
                print ('PJ DEBUG else reset time zone - evStime1 = ' + str(evStime1))
                print ('PJ DEBUG else reset time zone - evStime = ' + str(evStime))
                print ('PJ DEBUG else reset time zone - uGtime = ' + str(uGtime))
                #    print ('PJ DEBUG else reset time zone - uGtime1 = ' + str (uGtime1))
                #    print ('PJ DEBUG else reset time zone - uGtime2 = ' + str (uGtime2))
                print ('PJ DEBUG else reset time zone - schedTime = ' + str(schedTime))
                #    print ('PJ DEBUG evStime - ' + evStime.strftime('%d-%b-%Y %H:%M (%Z%z)' ))

                #    schedule = 'Live at ' + schedule.split (' ')[-1] + '(EST)'

                cName = '[COLOR white]' + schedTime.strftime('%d-%b ') + '[COLORorchid]' + schedTime.strftime(
                    '%H:%M (%Z)') + ' [COLOR orchid]'+str(game). replace('Live', ''). strip() + '[/COLOR]'
                print ('PJ DEBUG mlb not seen - cName set in else = ' + cName)

            else:
                print (
                    'PJ DEBUG mlb not seen - cName not set - now in else = ' + cName)

            if not cName:
                #    pass
                cName = '[COLOR red]' + str(schedule) + ' [COLOR orchid]'+str(
                    game). replace('Live', ''). strip() + '[/COLOR]'
                print ('PJ DEBUG mlb not seen - cName set in if not at end = ' + cName)

            cLink = game  # '' #### stream
            icon = myIcon9

            # USES MODE 12
            Menu(cName, cLink, 12, icon, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        mlb()

######################


def playMLB720(tName):
    from resources.lib import mlb
    # mlb720List = mlb.getStreams1()
    mlb720List = mlb.getStreams(tName)
    gameOn = 'n'
    for items in mlb720List:
        game = items.get('game', 'Game Missing')
        stream = items.get('stream', 'Stream Missing')
        quality = items.get('quality', 'Quality Missing')
        schedule = items.get('schedule', 'Schedule Missing')
        if tName.upper() in game.upper():
            gameOn = 'y'
            cName = '[COLOR orchid]'+str(game) + '[COLOR orchid]' + ' Schedule On: ' + str(
                schedule) + ' [COLOR orchid][I](' + str(quality) + 'k)' + '[/I][/COLOR]'
            cLink = stream
            icon = myIcon9
            Play(cName, cLink, 3, icon, myWall, '', '', '')
        else:
            pass
            #  gameOn ='n'

    if gameOn == 'n':
        thisMess = '[COLOR red][I]Game us not live yet .'+'\n'+'\n'+'[COLOR orchid]' + \
            '                                   ' + \
            'Click OK to quit[/I][/COLOR]'
        koding.OK_Dialog(title=tName, message=thisMess)
        index()
    else:
        pass

######################


def streamMLB720():
    from resources.lib import mlb
    mlb720List, mlb720Listt = mlb.getMLB()
    #mlb720List = ''
    if not mlb720List:
        print 'No MLB Games Available'
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n' + \
            '[COLOR orchid]'+'                                   ' + \
            'Click OK to quit[/I][/COLOR]'
        koding.OK_Dialog(title='MLB Games not available....', message=thisMess)
        mlb()

    #    for items in mlb720Listt:
        #    game = items.get('game', 'Game Missing')
        #    schedule = items.get('schedule', 'Schedule Missing')
        #    cName = 'Status Not Live:' + '[COLOR orchid]'+str (game) + '[COLOR orchid]'+ ' Schedule On: ' + str (schedule)
        #    cLink = ''
        #    icon = myIcon9

        #    Play(cName,cLink,3,icon,myWall,'','','')

    for items in mlb720List:
        game = items.get('game', 'Game Missing')
        stream = items.get('stream', 'Stream Missing')
        quality = items.get('quality', 'Quality Missing')
        schedule = items.get('schedule', 'Schedule Missing')

        cName = '[COLOR orchid]'+str(game) + '[COLOR orchid]' + ' Schedule On: ' + str(
            schedule) + ' [COLOR orchid][I](' + str(quality) + 'k)' + '[/I][/COLOR]'
        cLink = stream
        icon = myIcon9

        Play(cName, cLink, 3, icon, myWall, '', '', '')

    return


def mlbysslive():
    from resources.lib import mlbyss
    game_list = mlbyss.get_game()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 33, myIcon9, myWall, '', '', '')
    else:
        pass

def cs_mma():
    from resources.lib import techjaffamma
    game_list = techjaffamma.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 41, myIcon8, myWall, '', '', '')
    else:
        pass

def play_cs_mma(link):
    from resources.lib import techjaffamma
    stream = techjaffamma.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('link', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon8, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ufc()

def nflsecond():
    from resources.lib import techjaffanfl
    game_list = techjaffanfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 43, myIcon3, myWall, '', '', '')
    else:
        pass


def playnflsecond(link):
    from resources.lib import techjaffanfl
    game = techjaffanfl.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon3, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nfl()
###############STREAMEAST############


def se_boxing():
    from resources.lib import streameast_boxing
    game_list = streameast_boxing.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 103, myIcon13, myWall, '', '', '')
    else:
        pass


def play_se_boxing(link):
    from resources.lib import streameast_boxing
    game = streameast_boxing.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon13, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        boxing()


def se_mlb():
    from resources.lib import streameast_mlb
    game_list = streameast_mlb.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 123, myIcon9, myWall, '', '', '')
    else:
        pass


def play_se_mlb(link):
    from resources.lib import streameast_mlb
    game = streameast_mlb.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon9, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        mlb()


def se_nba():
    from resources.lib import streameast_nba
    game_list = streameast_nba.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 105, myIcon5, myWall, '', '', '')
    else:
        pass


def play_se_nba(link):
    from resources.lib import streameast_nba
    game = streameast_nba.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon5, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nba()


def se_ncaa():
    from resources.lib import streameast_ncaa
    game_list = streameast_ncaa.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 107, myIcon14, myWall, '', '', '')
    else:
        pass


def play_se_ncaa(link):
    from resources.lib import streameast_ncaa
    game = streameast_ncaa.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon14, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ncaa()


def se_tennis():
    from resources.lib import streameast_tennis
    game_list = streameast_tennis.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 109, myIcon12, myWall, '', '', '')
    else:
        pass


def play_se_tennis(link):
    from resources.lib import streameast_tennis
    game = streameast_tennis.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon12, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        tennis()


def se_nhl():
    from resources.lib import streameast_nhl
    game_list = streameast_nhl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 111, myIcon4, myWall, '', '', '')
    else:
        pass


def play_se_nhl(link):
    from resources.lib import streameast_nhl
    game = streameast_nhl.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon4, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nhl()


def se_soccer():
    from resources.lib import streameast_soccer
    game_list = streameast_soccer.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 113, myIcon10, myWall, '', '', '')
    else:
        pass


def play_se_soccer(link):
    from resources.lib import streameast_soccer
    game = streameast_soccer.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon10, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        fifa()


def se_cricket():
    from resources.lib import streameast_cricket
    game_list = streameast_cricket.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 115, myIcon16, myWall, '', '', '')
    else:
        pass


def play_se_cricket(link):
    from resources.lib import streameast_cricket
    game = streameast_cricket.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon16, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()


def se_esports():
    from resources.lib import streameast_esports
    game_list = streameast_esports.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 117, myIcon, myWall, '', '', '')
    else:
        pass


def play_se_esports(link):
    from resources.lib import streameast_esports
    game = streameast_esports.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()


def se_volleyball():
    from resources.lib import streameast_volleyball
    game_list = streameast_volleyball.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 119, myIcon17, myWall, '', '', '')
    else:
        pass


def play_se_volleyball(link):
    from resources.lib import streameast_volleyball
    game = streameast_volleyball.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon17, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()()


def se_nfl():
    from resources.lib import streameast_nfl
    game_list = streameast_nfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 121, myIcon15, myWall, '', '', '')
    else:
        pass


def play_se_nfl(link):
    from resources.lib import streameast_nfl
    game = streameast_nfl.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon15, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nfl()


def se_table():
    from resources.lib import streameast_table
    game_list = streameast_table.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 129, myIcon19, myWall, '', '', '')
    else:
        pass


def play_se_table(link):
    from resources.lib import streameast_table
    game = streameast_table.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon19, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()


def se_hand():
    from resources.lib import streameast_hand
    game_list = streameast_hand.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 131, myIcon20, myWall, '', '', '')
    else:
        pass


def play_se_hand(link):
    from resources.lib import streameast_hand
    game = streameast_hand.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon20, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()

def se_mma():
    from resources.lib import streameast_mma
    game_list = streameast_mma.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 151, myIcon8, myWall, '', '', '')
    else:
        pass


def play_se_mma(link):
    from resources.lib import streameast_mma
    game = streameast_mma.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon8, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ufc()
########
def ac_xfl():
    from resources.lib import acesportz_xfl
    game_list = acesportz_xfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 133, myIcon15, myWall, '', '', '')
    else:
        pass


def play_ac_xfl(link):
    from resources.lib import acesportz_xfl
    stream = acesportz_xfl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon15, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        xfl()
#################6STREAM###############
def sixstream_nba():
    from resources.lib import sixstream_nba
    game_list = sixstream_nba.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 157, myIcon5, myWall, '', '', '')
    else:
        pass


def play_sixstream_nba(link):
    from resources.lib import sixstream_nba
    stream = sixstream_nba.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon5, myWall, '', '', '')

def sixstream_boxing():
    from resources.lib import sixstream_boxing
    game_list = sixstream_boxing.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 155, myIcon8, myWall, '', '', '')
    else:
        pass


def play_sixstream_boxing(link):
    from resources.lib import sixstream_boxing
    stream = sixstream_boxing.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon8, myWall, '', '', '')

def sixstream_nhl():
    from resources.lib import sixstream_nhl
    game_list = sixstream_nhl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 159, myIcon4, myWall, '', '', '')
    else:
        pass


def play_sixstream_nhl(link):
    from resources.lib import sixstream_nhl
    stream = sixstream_nhl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon4, myWall, '', '', '')

def sixstream_nfl():
    from resources.lib import sixstream_nfl
    game_list = sixstream_nfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 161, myIcon3, myWall, '', '', '')
    else:
        pass


def play_sixstream_nfl(link):
    from resources.lib import sixstream_nfl
    stream = sixstream_nfl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon3, myWall, '', '', '')

def sixstream_cfb():
    from resources.lib import sixstream_cfb
    game_list = sixstream_cfb.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 163, myIcon6, myWall, '', '', '')
    else:
        pass


def play_sixstream_cfb(link):
    from resources.lib import sixstream_cfb
    stream = sixstream_cfb.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon6, myWall, '', '', '')

def sixstream_cbk():
    from resources.lib import sixstream_cbk
    game_list = sixstream_cbk.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 165, myIcon14, myWall, '', '', '')
    else:
        pass


def play_sixstream_cbk(link):
    from resources.lib import sixstream_cbk
    stream = sixstream_cbk.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon14, myWall, '', '', '')
#################MARKKY88##############
def markky_bund():
    from resources.lib import markky_bund
    game_list = markky_bund.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 229, myIcon10, myWall, '', '', '')
    else:
        pass


def play_markky_bund(link):
    from resources.lib import markky_bund
    stream = markky_bund.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',s, 3, myIcon10, myWall, '', '', '')

def markky_champ():
    from resources.lib import markky_champ
    game_list = markky_champ.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 231, myIcon10, myWall, '', '', '')
    else:
        pass


def play_markky_champ(link):
    from resources.lib import markky_champ
    stream = markky_champ.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',s, 3, myIcon10, myWall, '', '', '')

def markky_laliga():
    from resources.lib import markky_laliga
    game_list = markky_laliga.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 233, myIcon10, myWall, '', '', '')
    else:
        pass


def play_markky_laliga(link):
    from resources.lib import markky_laliga
    stream = markky_laliga.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',s, 3, myIcon10, myWall, '', '', '')

def markky_ligue():
    from resources.lib import markky_ligue
    game_list = markky_ligue.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 235, myIcon10, myWall, '', '', '')
    else:
        pass


def play_markky_prem(link):
    from resources.lib import markky_prem
    stream = markky_prem.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',s, 3, myIcon10, myWall, '', '', '')

def markky_prem():
    from resources.lib import markky_prem
    game_list = markky_prem.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 237, myIcon10, myWall, '', '', '')
    else:
        pass


def play_markky_prem(link):
    from resources.lib import markky_prem
    stream = markky_prem.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',s, 3, myIcon10, myWall, '', '', '')

def markky_seriesa():
    from resources.lib import markky_seriesa
    game_list = markky_seriesa.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 239, myIcon10, myWall, '', '', '')
    else:
        pass


def play_markky_seriesa(link):
    from resources.lib import markky_seriesa
    stream = markky_seriesa.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',s, 3, myIcon10, myWall, '', '', '')
#################QUAYNET###############
def quaynet_nba():
    from resources.lib import quaynet_nba
    game_list = quaynet_nba.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 137, myIcon5, myWall, '', '', '')
    else:
        pass

def play_quaynet_nba(link):
    from resources.lib import quaynet_nba
    stream = quaynet_nba.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon5, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nba()
#
def quaynet_ncaaf():
    from resources.lib import quaynet_ncaaf
    game_list = quaynet_ncaaf.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 139, myIcon6, myWall, '', '', '')
    else:
        pass

def play_quaynet_ncaaf(link):
    from resources.lib import quaynet_ncaaf
    stream = quaynet_ncaaf.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon6, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ncaa()

#
def quaynet_nhl():
    from resources.lib import quaynet_nhl
    game_list = quaynet_nhl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 141, myIcon4, myWall, '', '', '')
    else:
        pass

def play_quaynet_nhl(link):
    from resources.lib import quaynet_nhl
    stream = quaynet_nhl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon4, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nhl()

def quaynet_boxing():
    from resources.lib import quaynet_boxing
    game_list = quaynet_boxing.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 143, myIcon13, myWall, '', '', '')
    else:
        pass

def play_quaynet_boxing(link):
    from resources.lib import quaynet_boxing
    stream = quaynet_boxing.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon13, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        boxing()

def quaynet_f1():
    from resources.lib import quaynet_f1
    game_list = quaynet_f1.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 145, myIcon, myWall, '', '', '')
    else:
        pass

def play_quaynet_f1(link):
    from resources.lib import quaynet_f1
    stream = quaynet_f1.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()

def quaynet_mma():
    from resources.lib import quaynet_mma
    game_list = quaynet_mma.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 147, myIcon8, myWall, '', '', '')
    else:
        pass

def play_quaynet_mma(link):
    from resources.lib import quaynet_mma
    stream = quaynet_mma.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon8, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()

def quaynet_nfl():
    from resources.lib import quaynet_nfl
    game_list = quaynet_nfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 149, myIcon15, myWall, '', '', '')
    else:
        pass

def play_quaynet_nfl(link):
    from resources.lib import quaynet_nfl
    stream = quaynet_nfl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon15, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nfl()

def quaynet_tv():
    from resources.lib import quaynet_tv
    game_list = quaynet_tv.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 217, myIcon2, myWall, '', '', '')
    else:
        pass

def play_quaynet_tv(link):
    from resources.lib import quaynet_tv
    stream = quaynet_tv.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon2, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        index()
###############SKUANET#####################
def skuanet_nba():
    from resources.lib import skuanet_nba
    game_list = skuanet_nba.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 201, myIcon5, myWall, '', '', '')
    else:
        pass

def play_skuanet_nba(link):
    from resources.lib import skuanet_nba
    stream = skuanet_nba.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon5, myWall, '', '', '')

def skuanet_nfl():
    from resources.lib import skuanet_nfl
    game_list = skuanet_nfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 203, myIcon4, myWall, '', '', '')
    else:
        pass

def play_skuanet_nfl(link):
    from resources.lib import skuanet_nfl
    stream = skuanet_nfl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon4, myWall, '', '', '')

def skuanet_fifa():
    from resources.lib import skuanet_fifa
    game_list = skuanet_fifa.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 205, myIcon10, myWall, '', '', '')
    else:
        pass

def play_skuanet_fifa(link):
    from resources.lib import skuanet_fifa
    stream = skuanet_fifa.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon10, myWall, '', '', '')

def skuanet_fone():
    from resources.lib import skuanet_fone
    game_list = skuanet_fone.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 207, myIcon, myWall, '', '', '')
    else:
        pass

def play_skuanet_fone(link):
    from resources.lib import skuanet_fone
    stream = skuanet_fone.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon, myWall, '', '', '')
##############COSWIT#######################
def coswit_boxing():
    from resources.lib import coswit_boxing
    game_list = coswit_boxing.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 209, myIcon13, myWall, '', '', '')
    else:
        pass

def play_coswit_boxing(link):
    from resources.lib import coswit_boxing
    stream = coswit_boxing.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon13, myWall, '', '', '')

def coswit_nfl():
    from resources.lib import coswit_nfl
    game_list = coswit_nfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 211, myIcon3, myWall, '', '', '')
    else:
        pass

def play_coswit_nfl(link):
    from resources.lib import coswit_nfl
    stream = coswit_nfl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon3, myWall, '', '', '')

def coswit_fifa():
    from resources.lib import coswit_fifa
    game_list = coswit_fifa.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 213, myIcon10, myWall, '', '', '')
    else:
        pass

def play_coswit_fifa(link):
    from resources.lib import coswit_fifa
    stream = coswit_fifa.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon10, myWall, '', '', '')
###########################################
def ws_tv():
    from resources.lib import ws_tv
    game_list = ws_tv.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 215, myIcon2, myWall, '', '', '')
    else:
        pass

def play_ws_tv(link):
    from resources.lib import ws_tv
    stream = ws_tv.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon2, myWall, '', '', '')
################Sports 24##################
def sportstwentyfour_tv():
    from resources.lib import sportstwentyfour_tv
    game_list = sportstwentyfour_tv.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 219, myIcon2, myWall, '', '', '')
    else:
        pass

def play_sportstwentyfour_tv(link):
    from resources.lib import sportstwentyfour_tv
    stream = sportstwentyfour_tv.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon2, myWall, '', '', '')
###########################################
def ac_nba():
    from resources.lib import acesportz_nba
    game_list = acesportz_nba.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing').title()
            link = game.get('link', 'Link Missing')
            Menu(title, link, 135, myIcon5, myWall, '', '', '')
    else:
        pass


def play_ac_nba(link):
    from resources.lib import acesportz_nba
    stream = acesportz_nba.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon5, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nba()


def ncaafsecond():
    from resources.lib import techjaffancaaf
    game_list = techjaffancaaf.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            Menu(title, title, 45, myIcon6, myWall, '', '', '')
    else:
        pass


def playncaafsecond(link):
    from resources.lib import techjaffancaaf
    game = techjaffancaaf.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon6, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ncaa()


def playmmalive(link):
    from resources.lib import techjaffamma
    game = techjaffamma.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon8, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ufc()

#####################


def volokitnfl():
    from resources.lib import volokitnfl
    game_list = volokitnfl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 49, myIcon3, myWall, '', '', '')
    else:
        pass


def playvolokitnfl(link):
    from resources.lib import volokitnfl
    stream = volokitnfl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon3, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nfl()
#####################


def videolivenfl():
    from resources.lib import videoliveNFL
    game_list = videoliveNFL.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 65, myIcon3, myWall, '', '', '')
    else:
        pass


def playvideolivenfl(link):
    from resources.lib import videoliveNFL
    stream = videoliveNFL.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon3, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nfl()
#####################
#####################


def videolivecfb():
    from resources.lib import videoliveCFB
    game_list = videoliveCFB.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 67, myIcon6, myWall, '', '', '')
    else:
        pass


def playvideolivecfb(link):
    from resources.lib import videoliveCFB
    stream = videoliveCFB.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon6, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ncaa()
#####################


def volokitmma():
    from resources.lib import volokitmma
    game_list = volokitmma.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 63, myIcon8, myWall, '', '', '')
    else:
        pass


def playvolokitmma(link):
    from resources.lib import volokitmma
    stream = volokitmma.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon8, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ufc()
#####################


def volokitmlb():
    from resources.lib import volokitmlb
    game_list = volokitmlb.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 53, myIcon9, myWall, '', '', '')
    else:
        pass


def playvolokitmlb(link):
    from resources.lib import volokitmlb
    stream = volokitmlb.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon9, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        mlb()

#####################


def volokitnhl():
    from resources.lib import volokitnhl
    game_list = volokitnhl.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 55, myIcon4, myWall, '', '', '')
    else:
        pass


def volokitnhlfeeds(link):
    from resources.lib import volokitnhl
    feed_list = volokitnhl.get_feeds(link)
    if feed_list:
        for feed in feed_list:
            feed_name = feed.get("name", "Name Missing")
            feed_url = feed.get("feed", "Feed Missing")
            #Menu(ChannelColor(feed_name),feed_url,myIcon4 ,myWall,'','','','')
            Menu(feed_name, feed_url, 5555, myIcon4, myWall, '', '', '')

    else:
        pass


def playvolokitnhl(link):
    from resources.lib import volokitnhl
    stream = volokitnhl.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon4, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nhl()

#####################


def volokitncaa():
    from resources.lib import volokitncaa
    game_list = volokitncaa.get_games()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            link = game.get('link', 'Link Missing')
            Menu(title, link, 57, myIcon6, myWall, '', '', '')
    else:
        pass


def playvolokitncaa(link):
    from resources.lib import volokitncaa
    stream = volokitncaa.get_stream(link)
    if stream:
        for game in stream:
            s = game.get('stream', 'Stream Missing')
            Play('[COLOR orchid]*[/COLOR] [B][COLOR white]Play Stream[/COLOR][/B] [COLOR orchid]*[/COLOR]',
                 s, 3, myIcon6, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ncaa()

#####################


def playmlbyss(link):
    from resources.lib import mlbyss
    game = mlbyss.get_stream(link)
    if game:
        for g in game:
            cName = g.get('title', 'Title Missing')
            cLink = g.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon9, myWall, '', '', '')

    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        mlb()


def ncaaflive():
    from resources.lib import ncaaf
    games = ncaaf.get_game()

    for game in games:
        title = game.get('title', 'Title Missing')

        Menu(title, title, 31, myIcon6, myWall, '', '', '')


def playncaaf(link):
    from resources.lib import ncaaf
    live_game = ncaaf.get_stream(link)
    if live_game:
        for game in live_game:
            cName = game.get('title', 'Title Missing')
            cLink = game.get('stream', 'Stream Missing')
            Play(cName, cLink, 3, myIcon6, myWall, '', '', '')
    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        ncaa()


def nhlhighlight(url):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    if url:
        for month in months:
            Menu(month, url + ' ' + month, 27, myIcon4, myWall, '', '', '')

    else:
        Menu("2018", '2018', 26, myIcon4, myWall, '', '', '')
        Menu("2019", '2019', 26, myIcon4, myWall, '', '', '')


def playnhlhighlight(link):
    from resources.lib import nhlhighlight
    game_list = nhlhighlight.get_highlight(link)

    if game_list:
        for game in game_list:
            date = game.get('date', 'date missing')
            title = game.get('title', 'title missing')
            stream = game.get('link', 'stream missing')

            cName = '[COLOR orchid]'+str(title) + '[COLOR orchid]' + \
                ' Scheduled On: ' + str(date) + '[/COLOR]'
            cLink = stream
            icon = myIcon4

            Play(cName, cLink, 3, icon, myWall, '', '', '')

    else:
        koding.OK_Dialog(
            '[COLOR orchid]*[/COLOR] [B][COLOR white]Stream not available yet[/COLOR][/B] [COLOR orchid]*[/COLOR]', message='Try again Later')
        nhl()
######################


def hdStreams():
    from resources.lib import hdstreams
    hdstreamsList = hdstreams.startUp()
    if not hdstreamsList:
        print 'No Streams  Available at the moment'
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time' + \
            '\n'+'\n'+'[COLOR orchid]'+' '+'Click OK to quit[/I][/COLOR]'
        koding.OK_Dialog(title='hdStreams not available....', message=thisMess)
        various()
    for items in hdstreamsList:
        game = items.get('game', 'Game Missing')
        stream = items.get('stream', 'Stream Missing')
        #quality =items.get('quality','Quality Missing')

        cName = '[COLOR orchid]*[/COLOR] [B][COLOR white]' + \
            str(game) + '[/COLOR][/B] [COLOR orchid]*[/COLOR]'
        cLink = stream
        icon = myIcon2

        Play(cName, cLink, 3, icon, myWall, '', '', '')


######################
def playNFLLIVE():
    from resources.lib import scienceandtechnology
    game_list = scienceandtechnology.get_game()
    if game_list:
        for game in game_list:
            title = game.get('title', 'Title Missing')
            cLink = game.get('stream', 'URL Missing')
            schedule = game.get('schedule', 'Schedule Missing')

            schedTime = schedule.to(addonZone)

            cName = '[COLOR white]' + schedTime.strftime('%d %b ') + '[COLOR orchid]' + schedTime.strftime(
                '%H:%M (%Z) ') + '[COLOR orchid]' + title + '[/COLOR]'
            Play(cName, cLink, 3, myIcon3, myWall, '', '', '')
    else:
        thisMess = '[COLOR red][I]No active NFL Game Right Now'+'\n'+'\n'+'[COLOR orchid]' + \
            '                                   ' + \
            'Click OK to quit[/I][/COLOR]'
        koding.OK_Dialog(title='Try Later', message=thisMess)
        nfl()


def streamMMA720():
    from resources.lib import stream720
    mma720List = stream720.getMMA()
    if not mma720List:
        print 'No MMA Streams  Available'
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n' + \
            '[COLOR orchid]'+'                                   ' + \
            'Click OK to quit[/I][/COLOR]'
        koding.OK_Dialog(
            title='MMA Streams not available....', message=thisMess)
        ufc()
    for items in mma720List:
        game = items.get('game', 'Game Missing')
        stream = items.get('stream', 'Stream Missing')
        quality = items.get('quality', 'Quality Missing')

        cName = '[COLOR orchid]' + \
            str(game) + ' [COLOR orchid][I](' + \
            str(quality) + 'k)' + '[/I][/COLOR]'
        cLink = stream
        if 'wwe' in stream:
            icon = myIcon7
        else:
            icon = myIcon8

        Play(cName, cLink, 3, icon, myWall, '', '', '')

    return


def ncaaList():
    #    openloadMenu()      #openload pair option if reqd
    #    mode = 0
    from resources.lib import ncaa
    ncaaList = ncaa.startScript()
    print 'PJ DEBUG - default ncaa list is ' + str(ncaaList)
    icon = join(artPath, ICON6)
    #   mode = 3   #  play
    if not ncaaList:
        print 'No NBA Games Available'
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n' + \
            '[COLOR orchid]'+'                                   ' + \
            'Click OK to quit[/I][/COLOR]'
        koding.OK_Dialog(title='NCAA Games not available....',
                         message=thisMess)
        ncaa()
    else:
        print 'NCAA Games Available'

        for items in ncaaList:
            game = items.get('game', 'Game Missing')
            stream = items.get('stream', 'Stream Missing')

            print 'Title = ' + str(game)
            print 'Stream = ' + str(stream)

            cName = '[COLOR orchid]'+str(game) + '[/COLOR]'
            cLink = stream
            icon = myIcon11

            Play(cName, cLink, 3, icon, myWall, '', '', '')
    return


def nflLive():
    #    openloadMenu()      #openload pair option if reqd
    #    mode = 0
    #    from resources.lib import free
    from resources.lib import sssfree
    print ('Getting freeList')
    #    freeList = free.startScript()
    freeList = sssfree.startScript()
    print 'PJ DEBUG - free list in default is ' + str(freeList)
    icon = join(artPath, ICON3)
    #    return

    if not freeList:
        koding.OK_Dialog(title='No Game Available',
                         message='Links are normally active 45 minutes before event time. Click OK to quit.')
    else:
        #    print 'Games Available'
        #    passThro = 0
        for items in freeList:
            #    passThro = passThro + 1
            game = items.get('game', 'Game Missing')
            stream = items.get('stream', 'Stream Missing')
            print 'Game = ' + str(game)
            print 'Stream = ' + str(stream)

            cLink = str(stream)
            cName1 = str(game)
            cName = '[COLOR orchid]'+str(game) + '[/COLOR]'
            icon = myIcon3
            if 'NFL NETWORK' in str(game):
                icon = join(artPath, 'NFL-Network.png')
            Play(cName, cLink, 3, icon, myWall, '', '', '')

            #        code = urllib.urlopen(stream).getcode()
            #        print 'PJ DEBUG - NFL code returned ='+str (code)
            #        if str(code).startswith('2') or str(code).startswith('3'):
        #        Play(cName,cLink,3,icon,myWall,'','','')
            #        else:
        #        cName = '[COLOR red][I](offline)  [/I]' + cName
        #        Play(cName,cLink,3,icon,myWall,'','','')

    return


def nba4List():
    #    openloadMenu()      #openload pair option if reqd
    #    mode = 0
    from resources.lib import nba4live
    nba4List = nba4live.startScript()
    print 'PJ DEBUG - default nba4List list is ' + str(nba4List)
    icon = join(artPath, ICON4)
    #   mode = 3   #  play
    if not nba4List:
        print 'No NBA Games Available'
        thisMess = '[COLOR red][I]Links are normally active 45 mins before event time'+'\n'+'\n' + \
            '[COLOR orchid]'+'                                   ' + \
            'Click OK to quit[/I][/COLOR]'
        koding.OK_Dialog(title='NHL Games not available....', message=thisMess)
        nba()
    else:
        print 'NBS Games Available'
        for items in nba4List:
            awayName = items.get('awayName', 'awayName Missing')
            homeName = items.get('homeName', 'homeName Missing')
            stream = items.get('stream', 'Stream Missing')
            awayImage = items.get('awayImage', 'awayImage Missing')
            homeImage = items.get('homeImage', 'homeImage Missing')

            print 'Title = ' + str(awayName) + ' @ ' + str(homeName)
            print 'Stream = ' + str(stream)
            cName = '[COLOR orchid]*[/COLOR] [B][COLOR white]' + \
                str(awayName) + ' @ ' + str(homeName) + \
                '[/COLOR][/B] [COLOR orchid]*[/COLOR]'
            cLink = stream
            icon = myIcon5

            Play(cName, cLink, 3, icon, myWall, '', '', '')

    return
######################
##
######################
# For Reference - SEE VOD3
# def Menu(name,url,mode,iconimage,fanart,description,trailer,choice,showcontext=True,allinfo={})
# Menu(txt,url3,1,ICON,FANART,'','','')
##   Menu('[COLOR red]Favourite Movies[/COLOR]','',4,ICON,FANART,'','',1)
##
# def Play(name,url,mode,iconimage,fanart,description,trailer,choice,showcontext=True,allinfo={})
# Play(txt,url3,100,ICON,FANART,'','','')
######################
#
####################
# KEEP EVERYTHING BELOW
# used everytime
####################
# DO NOT ALTER THIS


def chkStream(url):
    playChk = ''
    xbmc.Player().play(url)
    isplaying = koding.Check_Playback()
    if isplaying:
        playChk = 'yes'
        #        dialog.ok('PLAYBACK SUCCESSFUL','Congratulations, playback was successful')
        xbmc.Player().stop()
    else:
        playChk = 'no'
        #        dialog.ok('PLAYBACK FAILED','Sorry, playback failed :(')
    return playChk
####################
# DO NOT ALTER THIS


def openloadMenu():
    print 'Index mode'
    title = '[COLOR goldenrod]Pair with OpenLoad[/COLOR]'
    link = 'openloadPair()'
    mode = 99
    Menu2(title, link, mode, myIcon3, myWall, '', '', '')
####################
# DO NOT ALTER THIS


def openloadPair():
    myplatform = ''
    if xbmc.getCondVisibility('system.platform.android'):
        myplatform = 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        myplatform = 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        myplatform = 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        myplatform = 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        myplatform = 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        myplatform = 'ios'

    if myplatform == 'android':  # Android
        opensite = xbmc.executebuiltin(
            'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ('https://olpair.com/'))
    else:
        opensite = webbrowser . open('https://olpair.com/')
####################
# DO NOT ALTER THIS


def urlsolver(url):
    host = RESOLVE.HostedMediaFile(url)
    ValidUrl = host.valid_url()
    if ValidUrl == True:
        resolver = RESOLVE.resolve(url)
    elif ValidUrl == False:
        from resources.lib import genesisresolvers
        resolved = genesisresolvers.get(url).result
        if resolved:
            if isinstance(resolved, list):
                for k in resolved:
                    quality = setting('quality')
                    if k['quality'] == 'HD':
                        resolver = k['url']
                        break
                    elif k['quality'] == 'SD':
                        resolver = k['url']
                    elif k['quality'] == '10080p' and setting('10080pquality') == 'true':
                        resolver = k['url']
                        break
            else:
                resolver = resolved
    return resolver
####################
# DO NOT ALTER THIS


def saveXML(xmlPath, fName, data):
    outputFile = fName+'.xml'
    f2 = open(join(xmlPath, outputFile), 'w')
    f2.write(fName+'\n')
    f2.write(str(data)+'\n')
    f2.write('\n')
    f2.close()
####################
# for items that need non playable
# folder menu items
# ie take you to another menu
####################
# DO NOT ALTER THIS


def Menu(name, url, mode, iconimage, fanart, description, trailer, choice, showcontext=True, allinfo={}):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(
        iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&trailer="+urllib.quote_plus(trailer)+"&choice="+str(choice)
    ok = True
    liz = xbmcgui.ListItem(
        name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    liz.setProperty("Fanart_Image", fanart)
    #        liz.setProperty("IsPlayable","true")

    liz.setProperty("IsPlayable", "false")
    #        liz.setProperty("isFolder","true")

    #    if showcontext:
    #    contextMenu = []
    #    if not name in movie_favourites_read:
    #    contextMenu.append(('Add to Movie Favourites','XBMC.RunPlugin(%s?choice=1&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
    #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
    #    if not name in tv_favourites_read:
    #    contextMenu.append(('Add to TV Favorites','XBMC.RunPlugin(%s?choice=2&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
    #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
    #    if not name in music_favourites_read:
    #    contextMenu.append(('Add to Music Favorites','XBMC.RunPlugin(%s?choice=3&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
    #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
    #    if not name in kids_favourites_read:
    #    contextMenu.append(('Add to Kids Favorites','XBMC.RunPlugin(%s?choice=4&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
    #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
    #    liz.addContextMenuItems(contextMenu)
    ok = xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


####################
# for items that need playable
# items and dont need url resolver
###################
# DO NOT ALTER THIS
def Play(name, url, mode, iconimage, fanart, description, trailer, choice, showcontext=True, allinfo={}):
    if iconimage == 'IMDB':
        search_name = name
        url3 = url
        imdbIcon = Imdb_Thumb(name, search_name)
        if imdbIcon == 'NONE':
            iconimage = 'https://m.media-amazon.com/images/G/01/imdb/images/mobile/AppUpsell/IMDbLogo-8429101133._CB470041665_.png'
        else:
            iconimage = imdbIcon

    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(
        iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&trailer="+urllib.quote_plus(trailer)+"&choice="+str(choice)
    ok = True
    liz = xbmcgui.ListItem(
        name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    liz.setProperty("Fanart_Image", fanart)
    liz.setProperty("IsPlayable", "True")
    #
    liz.setProperty("isFolder", "False")
    #    if showcontext:
    #    contextMenu = []
    #    if not name in movie_favourites_read:
    #    contextMenu.append(('Add to Movie Favourites','XBMC.RunPlugin(%s?choice=1&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
    #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
    #    if not name in tv_favourites_read:
    #    contextMenu.append(('Add to TV Favorites','XBMC.RunPlugin(%s?choice=2&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
    #   %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
    #    if not name in music_favourites_read:
    #    contextMenu.append(('Add to Music Favorites','XBMC.RunPlugin(%s?choice=3&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
    #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
    #    if not name in kids_favourites_read:
    #    contextMenu.append(('Add to Kids Favorites','XBMC.RunPlugin(%s?choice=4&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
    #    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))

    #    liz.addContextMenuItems(contextMenu)
    ok = xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz)  # ,isFolder=False)
    return ok
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

####################
# for creating popup window with
# play link choices - needs fixing


def PLAYVIDEO(url):
    Dialog = xbmcgui.Dialog()
    sources = []
    link = openURL(url)
    match = re.compile('<source src="(.+?)".+?res="(.+?)"').findall(link)
    for playlink, quality in match:
        sources.insert(0, {'quality': quality, 'playlink': playlink})
        if len(sources) == len(match):
            choice = Dialog.select('Select Playlink', [
                                   link["quality"] for link in sources])
            if choice != -1:
                playlink = sources[choice]['playlink']
                isFolder = False
                xbmc.Player().play(playlink)
                mode = 9
####################
# DO NOT ALTER THIS


def openURL(url):
    req = urllib2.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    return link
####################
# DO NOT ALTER THIS


def myPlay(name, url):
    stream_url = url
    liz = xbmcgui.ListItem(name, path=stream_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
####################
# DO NOT ALTER THIS


def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params)-1] == '/'):
            params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param


xbmcplugin.setContent(int(sys.argv[1]), 'movies')

params = get_params()
url = None
name = None
mode = None
playlist = None
iconimage = None
fanart = addon_fanart
playlist = None
fav_mode = None
regexs = None
description = None

try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    iconimage = urllib.unquote_plus(params["iconimage"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass
try:
    fanart = urllib.unquote_plus(params["fanart"])
except:
    pass
try:
    description = urllib.unquote_plus(params["description"])
except:
    pass

##################
# MODES
##################
# GLOBAL MODES USED
# DO NOT ALTER THESE
## 0 , 1 , 2 , 3 , 99 , 100 , 101

# GLOBAL MODE USED
# DO NOT ALTER THIS
if mode == None or mode == 0:
    print ('Opening Index mode = {}'.format(mode))
    index()
elif mode == 'nba' or mode == 1000:
    print ('Opening Index mode = {}'.format(mode))
    nba()
elif mode == 'nfl' or mode == 2000:
    print ('Opening Index mode = {}'.format(mode))
    nfl()
elif mode == 'xfl' or mode == 3000:
    print ('Opening Index mode = {}'.format(mode))
    xfl()
elif mode == 'mlb' or mode == 4000:
    print ('Opening Index mode = {}'.format(mode))
    mlb()
elif mode == 'nhl' or mode == 5000:
    print ('Opening Index mode = {}'.format(mode))
    nhl()
elif mode == 'ncaa' or mode == 6000:
    print ('Opening Index mode = {}'.format(mode))
    ncaa()
elif mode == 'ufc' or mode == 7000:
    print ('Opening Index mode = {}'.format(mode))
    ufc()
elif mode == 'ncaab' or mode == 8000:
    print ('Opening Index mode = {}'.format(mode))
    ncaab()
elif mode == 'boxing' or mode == 9000:
    print ('Opening Index mode = {}'.format(mode))
    boxing()
elif mode == 'fifa' or mode == 10000:
    print ('Opening Index mode = {}'.format(mode))
    fifa()
elif mode == 'tennis' or mode == 11000:
    print ('Opening Index mode = {}'.format(mode))
    tennis()
elif mode == 'various' or mode == 12000:
    print ('Opening Index mode = {}'.format(mode))
    various()
elif mode == 1:
    print ('Opening Main mode = {}'.format(mode))
    main()
elif mode == 2:
    print ('this is using std XBMC Player - attempting to play url = {} & mode = {}'.format(url, mode))
    myPLAYER = xbmc.Player()
    myPLAYER.play(url)
elif mode == 3:
    print ('USING STD XBMC PLAYER with resolveurl  if reqd - Attempting to play url = {} & mode = {}'.format(url, mode))
    if 'o' in url and 'load' in url:
        url = urlsolver(url)

    liz = xbmcgui.ListItem(name, path=url)
    infoLabels = {"title": name}
    liz.setInfo(type="video", infoLabels=infoLabels)
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

elif mode == 4:
    print ('Getting NFL Network Live')
    nflLive()
    pass

elif mode == 5:
    print ('Getting MLB Live Games')
    name = url
    streamplayOffStreamMLB(name)
    pass

elif mode == 6:
    print ('Getting NBA Live Games')
    nba4List()
    pass

elif mode == 7:
    print ('Getting NCAA Live Games')
    ncaaList()
    pass

elif mode == 8:
    print ('Getting NHL720 Live Games')
    streamNHL720()
    pass

elif mode == 9:
    print ('TBA')
    pass

elif mode == 10:
    #print ('Getting NHL720 Live Games')
    playOffStreamMLBSchedule()
    pass

elif mode == 11:
    print ('Getting NFL720 Live Games')
    # streamNFL720()
    pass

elif mode == 12:
    print ('Getting MLB720 Live Games')
    # streamMLB720()
    tName = url
    playMLB720(tName)
    pass

elif mode == 13:
    print ('Getting Live MLB schedule')
    scheduleMLB()
    pass

elif mode == 14:
    print ('Getting MMS720 Live Games')
    streamMMA720()
    pass

elif mode == 15:
    print ('Getting HDSTREAMS Live Games')
    hdStreams()
    pass

elif mode == 16:
    playNFLLIVE()
    pass

elif mode == 19:
    print ('TBA')
    pass

elif mode == 20:
    mlslive()
    pass

elif mode == 21:
    link = url
    playmls(url)
    pass

elif mode == 26:
    link = url
    nhlhighlight(link)
    pass

elif mode == 27:
    link = url
    playnhlhighlight(link)
    pass

elif mode == 30:
    ncaaflive()
    pass

elif mode == 31:
    link = url
    playncaaf(link)
    pass

elif mode == 32:
    mlbysslive()
    pass

elif mode == 33:
    link = url
    playmlbyss(link)
    pass

elif mode == 40:
    cs_mma()
    pass

elif mode == 41:
    link = url
    play_cs_mma(link)
    pass

elif mode == 42:
    nflsecond()
    pass

elif mode == 43:
    link = url
    playnflsecond(link)
    pass

elif mode == 44:
    ncaafsecond()
    pass

elif mode == 45:
    link = url
    playncaafsecond(link)
    pass

elif mode == 46:
    tennislive()
    pass

elif mode == 47:
    link = url
    playtennis(url)
    pass

elif mode == 48:
    volokitnfl()
    pass

elif mode == 49:
    link = url
    playvolokitnfl(url)
    pass

elif mode == 52:
    volokitmlb()
    pass

elif mode == 53:
    link = url
    playvolokitmlb(url)
    pass

elif mode == 54:
    volokitnhl()
    pass

elif mode == 55:
    link = url
    volokitnhlfeeds(url)
    pass

elif mode == 5555:
    link = url
    playvolokitnhl(url)
    pass

elif mode == 56:
    volokitncaa()
    pass

elif mode == 57:
    link = url
    playvolokitncaa(url)
    pass

elif mode == 58:
    boxinglive()
    pass

elif mode == 59:
    link = url
    playboxinglive(link)
    pass

elif mode == 60:
    nbalive()
    pass

elif mode == 61:
    link = url
    playnbalive(link)
    pass

elif mode == 62:
    volokitmma()
    pass

elif mode == 63:
    link = url
    playvolokitmma(url)
    pass

elif mode == 64:
    videolivenfl()
    pass

elif mode == 65:
    link = url
    playvideolivenfl(url)
    pass

elif mode == 66:
    videolivecfb()
    pass

elif mode == 67:
    link = url
    playvideolivecfb(url)
    pass

elif mode == 68:
    freestreamNHL()
    pass

elif mode == 69:
    link = url
    playfreestreamNHL(link)
    pass

elif mode == 70:
    sixtyfpsnba()
    pass

elif mode == 71:
    link = url
    playsixtyfpsnba(url)
    pass

elif mode == 72:
    sixtyfpsnfl()
    pass

elif mode == 73:
    link = url
    playsixtyfpsnfl(url)
    pass

elif mode == 74:
    seventwentynfl()
    pass

elif mode == 75:
    link = url
    playseventwentynfl(url)
    pass

elif mode == 76:
    volokitxfl()
    pass

elif mode == 77:
    link = url
    playvolokitxfl(url)
    pass

elif mode == 78:
    seventwentyncaam()
    pass

elif mode == 79:
    link = url
    playseventwentyncaam(url)
    pass

elif mode == 80:
    sixtyfpssoccer()
    pass

elif mode == 81:
    link = url
    playsixtyfpssoccer(url)
    pass

elif mode == 82:
    ysstv()
    pass

elif mode == 83:
    link = url
    playysstv(link)
    pass

elif mode == 84:
    sixtyfpsufc()
    pass

elif mode == 85:
    link = url
    playsixtyfpsufc(url)
    pass

elif mode == 86:
    yssncaab()
    pass

elif mode == 87:
    link = url
    playyssncaab(link)
    pass

elif mode == 88:
    yssnba()
    pass

elif mode == 89:
    link = url
    playyssnba(link)
    pass

elif mode == 90:
    yssnfl()
    pass

elif mode == 91:
    link = url
    playyssnfl(link)
    pass

elif mode == 92:
    yssnhl()
    pass

elif mode == 93:
    link = url
    playyssnhl(link)
    pass

elif mode == 94:
    ysstrending()
    pass

elif mode == 95:
    link = url
    playysstrending(link)
    pass

elif mode == 96:
    yssxfl()
    pass

elif mode == 97:
    link = url
    playyssxfl(link)
    pass

####################
# Leave these modes in
# all the time
####################
elif mode == 99:
    print ('Pairing with Openload')
    openloadPair()
elif mode == 100:
    print ('Getting Selected Links')
elif mode == 101:  # not reqd?
    print ('Play Selected Link - no resolveURL reqd')
    liz = xbmcgui.ListItem(name, path=url)
    infoLabels = {"title": name}
    liz.setInfo(type="video", infoLabels=infoLabels)
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
####################
# Leave these modes in
# all the time
####################

elif mode == 102:
    se_boxing()
    pass

elif mode == 103:
    link = url
    play_se_boxing(link)
    pass

elif mode == 104:
    se_nba()
    pass

elif mode == 105:
    link = url
    play_se_nba(link)
    pass

elif mode == 106:
    se_ncaa()
    pass

elif mode == 107:
    link = url
    play_se_ncaa(link)
    pass

elif mode == 108:
    se_tennis()
    pass

elif mode == 109:
    link = url
    play_se_tennis(link)
    pass

elif mode == 110:
    se_nhl()
    pass

elif mode == 111:
    link = url
    play_se_nhl(link)
    pass

elif mode == 112:
    se_soccer()
    pass

elif mode == 113:
    link = url
    play_se_soccer(link)
    pass

elif mode == 114:
    se_cricket()
    pass

elif mode == 115:
    link = url
    play_se_cricket(link)
    pass

elif mode == 116:
    se_esports()
    pass

elif mode == 117:
    link = url
    play_se_esports(link)
    pass

elif mode == 118:
    se_volleyball()
    pass

elif mode == 119:
    link = url
    play_se_volleyball(link)
    pass

elif mode == 120:
    se_nfl()
    pass

elif mode == 121:
    link = url
    play_se_nfl(link)
    pass

elif mode == 122:
    se_mlb()
    pass

elif mode == 123:
    link = url
    play_se_mlb(link)
    pass

elif mode == 124:
    xfllive()
    pass

elif mode == 125:
    link = url
    playxfllive(link)
    pass

elif mode == 126:
    nascar()
    pass

elif mode == 127:
    link = url
    playnascar(link)
    pass

elif mode == 128:
    se_table()
    pass

elif mode == 129:
    link = url
    play_se_table(link)
    pass

elif mode == 130:
    se_hand()
    pass

elif mode == 131:
    link = url
    play_se_hand(link)
    pass

elif mode == 132:
    ac_xfl()
    pass

elif mode == 133:
    link = url
    play_ac_xfl(link)
    pass

elif mode == 134:
    ac_nba()
    pass

elif mode == 135:
    link = url
    play_ac_nba(link)
    pass

elif mode == 136:
    quaynet_nba()
    pass

elif mode == 137:
    link = url
    play_quaynet_nba(link)
    pass

elif mode == 138:
    quaynet_ncaaf()
    pass

elif mode == 139:
    link = url
    play_quaynet_ncaaf(link)
    pass

elif mode == 140:
    quaynet_nhl()
    pass

elif mode == 141:
    link = url
    play_quaynet_nhl(link)
    pass

elif mode == 142:
    quaynet_boxing()
    pass

elif mode == 143:
    link = url
    play_quaynet_boxing(link)
    pass

elif mode == 144:
    quaynet_f1()
    pass

elif mode == 145:
    link = url
    play_quaynet_f1(link)
    pass

elif mode == 146:
    quaynet_mma()
    pass

elif mode == 147:
    link = url
    play_quaynet_mma(link)
    pass

elif mode == 148:
    quaynet_nfl()
    pass

elif mode == 149:
    link = url
    play_quaynet_nfl(link)
    pass

elif mode == 150:
    se_mma()
    pass

elif mode == 151:
    link = url
    play_se_mma(link)
    pass

elif mode == 152:
    tennis_live()
    pass

elif mode == 153:
    link = url
    play_tennis_live(link)
    pass

elif mode == 154:
    sixstream_boxing()
    pass

elif mode == 155:
    link = url
    play_sixstream_boxing(link)
    pass

elif mode == 156:
    sixstream_nba()
    pass

elif mode == 157:
    link = url
    play_sixstream_nba(link)
    pass

elif mode == 158:
    sixstream_nhl()
    pass

elif mode == 159:
    link = url
    play_sixstream_nhl(link)
    pass

elif mode == 160:
    sixstream_nfl()
    pass

elif mode == 161:
    link = url
    play_sixstream_nfl(link)
    pass

elif mode == 162:
    sixstream_cfb()
    pass

elif mode == 163:
    link = url
    play_sixstream_cfb(link)
    pass

elif mode == 164:
    sixstream_cbk()
    pass

elif mode == 165:
    link = url
    play_sixstream_cbk(link)
    pass

elif mode == 200:
    skuanet_nba()
    pass

elif mode == 201:
    link = url
    play_skuanet_nba(link)
    pass

elif mode == 202:
    skuanet_nfl()
    pass

elif mode == 203:
    link = url
    play_skuanet_nfl(link)
    pass

elif mode == 204:
    skuanet_fifa()
    pass

elif mode == 205:
    link = url
    play_skuanet_fifa(link)
    pass

elif mode == 206:
    skuanet_fone()
    pass

elif mode == 207:
    link = url
    play_skuanet_fone(link)
    pass

elif mode == 208:
    coswit_boxing()
    pass

elif mode == 209:
    link = url
    play_coswit_boxing(link)
    pass

elif mode == 210:
    coswit_nfl()
    pass

elif mode == 211:
    link = url
    play_coswit_nfl(link)
    pass

elif mode == 212:
    coswit_fifa()
    pass

elif mode == 213:
    link = url
    play_coswit_fifa(link)
    pass

elif mode == 214:
    ws_tv()
    pass

elif mode == 215:
    link = url
    play_ws_tv(link)
    pass

elif mode == 216:
    quaynet_tv()
    pass

elif mode == 217:
    link = url
    play_quaynet_tv(link)
    pass

elif mode == 218:
    sportstwentyfour_tv()
    pass

elif mode == 219:
    link = url
    play_sportstwentyfour_tv(link)
    pass

elif mode == 220:
    arconai_shows()
    pass

elif mode == 221:
    link = url
    play_arconai_shows(link)
    pass

elif mode == 222:
    arconai_movies()
    pass

elif mode == 223:
    link = url
    play_arconai_movies(link)
    pass

elif mode == 224:
    arconai_cable()
    pass

elif mode == 225:
    link = url
    play_arconai_cable(link)
    pass

elif mode == 226:
    sportsbay_tv()
    pass

elif mode == 227:
    link = url
    play_sportsbay_tv(link)
    pass

elif mode == 228:
    markky_bund()
    pass

elif mode == 229:
    link = url
    play_markky_bund(link)
    pass

elif mode == 230:
    markky_champ()
    pass

elif mode == 231:
    link = url
    play_markky_champ(link)
    pass

elif mode == 232:
    markky_laliga()
    pass

elif mode == 233:
    link = url
    play_markky_laliga(link)
    pass

elif mode == 234:
    markky_ligue()
    pass

elif mode == 235:
    link = url
    play_markky_ligue(link)
    pass

elif mode == 236:
    markky_prem()
    pass

elif mode == 237:
    link = url
    play_markky_prem(link)
    pass

elif mode == 238:
    markky_seriesa()
    pass

elif mode == 239:
    link = url
    play_markky_seriesa(link)
    pass
xbmcplugin.endOfDirectory(int(sys.argv[1]))
