# -*- coding: utf-8 -*-

import os
import xbmc
import xbmcaddon
import xbmcgui
import base64

try:
    from urllib.request import urlopen
    from urllib.request import Request
except ImportError:
    from urllib2 import urlopen
    from urllib2 import Request

ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
HOMEPATH = xbmc.translatePath('special://home/')
ADDONSPATH = os.path.join(HOMEPATH, 'addons')
THISADDONPATH = os.path.join(ADDONSPATH, ADDON_ID)
NEWSFILE      = base64.b64decode(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3dhdGNoZG9nczM2L2RlZHNlYy9tYXN0ZXIvd2F0Y2hkb2dzL3dhdGNoZG9nc25ld3MudHh0')
LOCALNEWS     = os.path.join(THISADDONPATH, 'watchdogsnews.txt')


def news():
    message = open_news_url(NEWSFILE)
    r = open(LOCALNEWS)
    compfile = r.read()

    if len(message) > 1:
        if compfile == message: pass
        else:
            text_file = open(LOCALNEWS, "w")
            text_file.write(message)
            text_file.close()
            compfile = message

    showText('[B][COLOR magenta]News and Info[/COLOR][/B]', compfile)


def open_news_url(url):
    req = Request(url)
    req.add_header('User-Agent', 'klopp')
    response = urlopen(req)
    link = response.read()
    response.close()
    print(link)
    return link


def news_local():
    r = open(LOCALNEWS)
    compfile = r.read()
    showText('[B]Updates and Information[/B]', compfile)


def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50

    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            quit()
            return
        except:
            pass