# -*- coding: utf-8 -*-

import sys

# from resources.lib.modules import log_utils
from resources.lib.modules import control
#####from resources.lib.modules import youtube
from resources.lib.modules import youtube_menu

#####import os,sys,re,datetime,urlparse

thishandle = int(sys.argv[1])

class yt_index:  # initializes as musicvids, functions can override based on action and subid.
    def __init__(self):
        self.action = 'musicvids'
        self.base_url = 'https://raw.githubusercontent.com/watchdogs36/dedsec/master/watchdogs/extra/'
        self.mainmenu = self.base_url + 'musicvids.txt'
        self.submenu = '%s/%s.txt'
        self.default_icon = '%s/icons/music_video_folder_icon.png'
        self.default_fanart = '%s/icons/music_video_folder_fanart.jpg'

    def init_vars(self, action):
        try:
            if action == 'youtube':
                self.action = 'youtube'
                self.base_url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3dhdGNoZG9nczM2L2RlZHNlYy9tYXN0ZXIvd2F0Y2hkb2dzL2V4dHJhLw=='.decode('base64')
                self.mainmenu = 'JXN5dG1haW4udHh0'.decode('base64') % (self.base_url)

            elif action == 'tvReviews':
                self.action   = 'tvReviews'
                self.base_url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3dhdGNoZG9nczM2L2RlZHNlYy9tYXN0ZXIvd2F0Y2hkb2dzL2V4dHJhLw=='.decode('base64')
                self.mainmenu = 'JXN0dnRyYWlsZXIudHh0'.decode('base64') % (self.base_url)

            elif action == 'movieReviews':
                self.action   = 'movieReviews'
                self.base_url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3dhdGNoZG9nczM2L2RlZHNlYy9tYXN0ZXIvd2F0Y2hkb2dzL2V4dHJhLw=='.decode('base64')
                self.mainmenu = 'JXNtb3ZpZXRyYWlsZXIudHh0'.decode('base64') % (self.base_url)

            self.submenu = self.submenu % (self.base_url, '%s')
            self.default_icon = self.default_icon % (self.base_url)
            self.default_fanart = self.default_fanart % (self.base_url)
        except:
            pass


    def root(self, action):
        try:
            self.init_vars(action)

            menuItems = youtube_menu.youtube_menu().processMenuFile(self.mainmenu)

            for name, section, searchid, subid, playlistid, channelid, videoid, iconimage, fanart, description in menuItems:
                if subid != 'false': # Means this item points to a submenu
                    youtube_menu.youtube_menu().addMenuItem(name, self.action, subid, iconimage, fanart, description, True)
                elif searchid != 'false': # Means this is a search term
                    youtube_menu.youtube_menu().addSearchItem(name, searchid, iconimage, fanart)
                elif videoid != 'false': # Means this is a video id entry
                    youtube_menu.youtube_menu().addVideoItem(name, videoid, iconimage, fanart)
                elif channelid != 'false': # Means this is a channel id entry
                    if channelid.startswith('UC'):
                        youtube_menu.youtube_menu().addChannelItem(name, channelid, iconimage, fanart)
                    else:
                        # This really needs it's own userid created in the .txt files
                        youtube_menu.youtube_menu().addUserItem(name, channelid, iconimage, fanart)
                elif playlistid != 'false': # Means this is a playlist id entry
                    youtube_menu.youtube_menu().addPlaylistItem(name, playlistid, iconimage, fanart)
                elif section != 'false': # Means this is a section placeholder/info line
                    youtube_menu.youtube_menu().addSectionItem(name, self.default_icon, self.default_fanart)
            self.endDirectory()
        except:
            pass


    def get(self, action, subid):
        try:
            self.init_vars(action)

            thisMenuFile = self.submenu % (subid)
            menuItems = youtube_menu.youtube_menu().processMenuFile(thisMenuFile)

            for name, section, searchid, subid, playlistid, channelid, videoid, iconimage, fanart, description in menuItems:
                if subid != 'false': # Means this item points to a submenu
                    youtube_menu.youtube_menu().addMenuItem(name, self.action, subid, iconimage, fanart, description, True)
                elif searchid != 'false': # Means this is a search term
                    youtube_menu.youtube_menu().addSearchItem(name, searchid, iconimage, fanart)
                elif videoid != 'false': # Means this is a video id entry
                    youtube_menu.youtube_menu().addVideoItem(name, videoid, iconimage, fanart)
                elif channelid != 'false': # Means this is a channel id entry
                    if channelid.startswith('UC'):
                        youtube_menu.youtube_menu().addChannelItem(name, channelid, iconimage, fanart)
                    else:
                        # This really needs it's own userid created in the .txt files
                        youtube_menu.youtube_menu().addUserItem(name, channelid, iconimage, fanart)
                elif playlistid != 'false': # Means this is a playlist id entry
                    youtube_menu.youtube_menu().addPlaylistItem(name, playlistid, iconimage, fanart)
                elif section != 'false': # Means this is a section placeholder/info line
                    youtube_menu.youtube_menu().addSectionItem(name, self.default_icon, self.default_fanart)
            self.endDirectory()
        except:
            pass


    def endDirectory(self):
        control.directory(thishandle, cacheToDisc=True)
