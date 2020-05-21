import xbmc


if __name__ == '__main__':
	plugin = 'plugin://plugin.video.watchdogs/'
	path = 'RunPlugin(%s?action=contextWatchdogsSettings&opensettings=false)' % plugin
	xbmc.executebuiltin(path)
	xbmc.executebuiltin('RunPlugin(%s?action=widgetRefresh)' % plugin)