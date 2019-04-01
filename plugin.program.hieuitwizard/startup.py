# -*- coding: utf-8 -*-
################################################################################
#      Copyright (C) 2015 Surfacingx/NaN                                       #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################
# Credits 
# ----------
# Tobias Ussing And Henrik Mosgaard Jensen for parseDOM
# WhiteCream thread for clicking yes on dialog for unknown sources

import xbmc, xbmcvfs, xbmcaddon, xbmcgui,re, os, glob, thread, xbmcplugin, sys
from datetime import date, datetime, timedelta
###############################
import shutil
import urllib2,urllib
import re
from resources.libs import extract, downloader, wizard as wiz

try:    from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database

reload(sys);
sys.setdefaultencoding("utf8")

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR red][B]HieuIT[/B][/COLOR] [COLOR yellow][B]Media Center[/B][/COLOR]'
ADDON          = xbmcaddon.Addon(id='plugin.program.hieuitwizard')
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.hieuitmediacenter'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/zips/repository.hieuitmediacenter/'
HOME           = xbmc.translatePath('special://home/')
ADDONS         = os.path.join(HOME,     'addons')
ADDONPATH      = wiz.addonInfo(ADDON_ID,'path')
ADDONID        = wiz.addonInfo(ADDON_ID,'id')
KODIHOME       = xbmc.translatePath('special://xbmc/')
KODIADDONS     = os.path.join(KODIHOME, 'addons')
DIALOG         = xbmcgui.Dialog()
DP             = xbmcgui.DialogProgress()
PACKAGES       = os.path.join(ADDONS,   'packages')
COLOR1         = wiz.COLOR1
COLOR2         = wiz.COLOR2
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
BACKUPLOCATION = ADDON.getSetting('path') if not ADDON.getSetting('path') == '' else HOME
MYBUILDS       = os.path.join(BACKUPLOCATION, 'My_Builds', '')
SKIN           = xbmc.getSkinDir()
FAILED         = False
INSTALLED      = wiz.getS('installed')

	
while xbmc.Player().isPlayingVideo():
	xbmc.sleep(1000)

if KODIV >= 17:
	NOW = datetime.now()
	temp = wiz.getS('kodi17iscrap')
	if not temp == '':
		if temp > str(NOW - timedelta(minutes=2)):
			wiz.log("Killing Start Up Script")
			sys.exit()
	wiz.log("%s" % (NOW))
	wiz.setS('kodi17iscrap', str(NOW))
	xbmc.sleep(1000)
	if not wiz.getS('kodi17iscrap') == str(NOW):
		wiz.log("Killing Start Up Script")
		sys.exit()
	else:
		wiz.log("Continuing Start Up Script")

wiz.log("[Path Check] Started", xbmc.LOGNOTICE)
path = os.path.split(ADDONPATH)
if not ADDONID == path[1]: DIALOG.ok(ADDONTITLE, '[COLOR %s]Please make sure that the plugin folder is the same as the ADDON_ID.[/COLOR]' % COLOR2, '[COLOR %s]Plugin ID:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, ADDONID), '[COLOR %s]Plugin Folder:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, path)); wiz.log("[Path Check] ADDON_ID and plugin folder doesnt match. %s / %s " % (ADDONID, path))
else: wiz.log("[Path Check] Good!", xbmc.LOGNOTICE)

if KODIADDONS in ADDONPATH:
	wiz.log("Copying path to addons dir", xbmc.LOGNOTICE)
	if not os.path.exists(ADDONS): os.makedirs(ADDONS)
	newpath = xbmc.translatePath(os.path.join('special://home/addons/', ADDONID))
	if os.path.exists(newpath):
		wiz.log("Folder already exists, cleaning House", xbmc.LOGNOTICE)
		wiz.cleanHouse(newpath)
		wiz.removeFolder(newpath)
	try:
		wiz.copytree(ADDONPATH, newpath)
	except Exception, e:
		pass
	wiz.forceUpdate(True)

	
wiz.log("[Auto Install Repo] Started", xbmc.LOGNOTICE)
if AUTOINSTALL == 'Yes' and not os.path.exists(os.path.join(ADDONS, REPOID)):
	workingxml = wiz.workingURL(REPOADDONXML)
	if workingxml == True:
		ver = wiz.parseDOM(wiz.openURL(REPOADDONXML), 'addon', ret='version', attrs = {'id': REPOID})
		if len(ver) > 0:
			installzip = '%s-%s.zip' % (REPOID, ver[0])
			workingrepo = wiz.workingURL(REPOZIPURL+installzip)
			if workingrepo == True:
				DP.create(ADDONTITLE,'Downloading Repo...','', 'Please Wait')
				if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
				lib=os.path.join(PACKAGES, installzip)
				try: os.remove(lib)
				except: pass
				downloader.download(REPOZIPURL+installzip,lib, DP)
				extract.all(lib, ADDONS, DP)
				try:
					f = open(os.path.join(ADDONS, REPOID, 'addon.xml'), mode='r'); g = f.read(); f.close()
					name = wiz.parseDOM(g, 'addon', ret='name', attrs = {'id': REPOID})
					wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name[0]), "[COLOR %s]Add-on updated[/COLOR]" % COLOR2, icon=os.path.join(ADDONS, REPOID, 'icon.png'))
				except:
					pass
				if KODIV >= 17: wiz.addonDatabase(REPOID, 1)
				DP.close()
				xbmc.sleep(500)
				wiz.forceUpdate(True)
				wiz.log("[Auto Install Repo] Successfully Installed", xbmc.LOGNOTICE)
			else: 
				wiz.LogNotify("[COLOR %s]Repo Install Error[/COLOR]" % COLOR1, "[COLOR %s]Invalid url for zip![/COLOR]" % COLOR2)
				wiz.log("[Auto Install Repo] Was unable to create a working url for repository. %s" % workingrepo, xbmc.LOGERROR)
		else:
			wiz.log("Invalid URL for Repo Zip", xbmc.LOGERROR)
	else: 
		wiz.LogNotify("[COLOR %s]Repo Install Error[/COLOR]" % COLOR1, "[COLOR %s]Invalid addon.xml file![/COLOR]" % COLOR2)
		wiz.log("[Auto Install Repo] Unable to read the addon.xml file.", xbmc.LOGERROR)
elif not AUTOINSTALL == 'Yes': wiz.log("[Auto Install Repo] Not Enabled", xbmc.LOGNOTICE)
elif os.path.exists(os.path.join(ADDONS, REPOID)): wiz.log("[Auto Install Repo] Repository already installed")

wiz.log("[Installed Check] Started", xbmc.LOGNOTICE)
if INSTALLED == 'true':
	if KODIV >= 17:
		wiz.kodi17Fix()
		# if SKIN in ['skin.confluence', 'skin.estuary']:
			# checkSkin()
		FAILED = True
	# elif not EXTRACT == '100' and not BUILDNAME == "":
		# wiz.log("[Installed Check] Build was extracted %s/100 with [ERRORS: %s]" % (EXTRACT, EXTERROR), xbmc.LOGNOTICE)
		# yes=DIALOG.yesno(ADDONTITLE, '[COLOR %s]%s[/COLOR] [COLOR %s]was not installed correctly!' % (COLOR1, COLOR2, BUILDNAME), 'Installed: [COLOR %s]%s[/COLOR] / Error Count: [COLOR %s]%s[/COLOR]' % (COLOR1, EXTRACT, COLOR1, EXTERROR), 'Would you like to try again?[/COLOR]', nolabel='[B]No Thanks![/B]', yeslabel='[B]Retry Install[/B]')
		# wiz.clearS('build')
		# FAILED = True
		# if yes: 
			# wiz.ebi("PlayMedia(plugin://%s/?mode=install&name=%s&url=fresh)" % (ADDON_ID, urllib.quote_plus(BUILDNAME)))
			# wiz.log("[Installed Check] Fresh Install Re-activated", xbmc.LOGNOTICE)
		# else: wiz.log("[Installed Check] Reinstall Ignored")
	# elif SKIN in ['skin.confluence', 'skin.estuary']:
		# wiz.log("[Installed Check] Incorrect skin: %s" % SKIN, xbmc.LOGNOTICE)
		# defaults = wiz.getS('defaultskin')
		# if not defaults == '':
			# if os.path.exists(os.path.join(ADDONS, defaults)):
				# skinSwitch.swapSkins(defaults)
				# x = 0
				# xbmc.sleep(1000)
				# while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)") and x < 150:
					# x += 1
					# xbmc.sleep(200)

				# if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
					# wiz.ebi('SendClick(11)')
					# wiz.lookandFeelData('restore')
		# if not wiz.currSkin() == defaults and not BUILDNAME == "":
			# gui = wiz.checkBuild(BUILDNAME, 'gui')
			# FAILED = True
			# if gui == 'http://':
				# wiz.log("[Installed Check] Guifix was set to http://", xbmc.LOGNOTICE)
				# DIALOG.ok(ADDONTITLE, "[COLOR %s]It looks like the skin settings was not applied to the build." % COLOR2, "Sadly no gui fix was attatched to the build", "You will need to reinstall the build and make sure to do a force close[/COLOR]")
			# elif wiz.workingURL(gui):
				# yes=DIALOG.yesno(ADDONTITLE, '%s was not installed correctly!' % BUILDNAME, 'It looks like the skin settings was not applied to the build.', 'Would you like to apply the GuiFix?', nolabel='[B]No, Cancel[/B]', yeslabel='[B]Apply Fix[/B]')
				# if yes: wiz.ebi("PlayMedia(plugin://%s/?mode=install&name=%s&url=gui)" % (ADDON_ID, urllib.quote_plus(BUILDNAME))); wiz.log("[Installed Check] Guifix attempting to install")
				# else: wiz.log('[Installed Check] Guifix url working but cancelled: %s' % gui, xbmc.LOGNOTICE)
			# else:
				# DIALOG.ok(ADDONTITLE, "[COLOR %s]It looks like the skin settings was not applied to the build." % COLOR2, "Sadly no gui fix was attatched to the build", "You will need to reinstall the build and make sure to do a force close[/COLOR]")
				# wiz.log('[Installed Check] Guifix url not working: %s' % gui, xbmc.LOGNOTICE)
	else:
		wiz.log('[Installed Check] Install seems to be completed correctly', xbmc.LOGNOTICE)
	# if not wiz.getS('pvrclient') == "":
		# wiz.toggleAddon(wiz.getS('pvrclient'), 1)
		# wiz.ebi('StartPVRManager')
	wiz.addonUpdates('reset')
	# if KEEPTRAKT == 'true': traktit.traktIt('restore', 'all'); wiz.log('[Installed Check] Restoring Trakt Data', xbmc.LOGNOTICE)
	# if KEEPREAL  == 'true': debridit.debridIt('restore', 'all'); wiz.log('[Installed Check] Restoring Real Debrid Data', xbmc.LOGNOTICE)
	# if KEEPLOGIN == 'true': loginit.loginIt('restore', 'all'); wiz.log('[Installed Check] Restoring Login Data', xbmc.LOGNOTICE)
	wiz.clearS('install')
else: wiz.log("[Installed Check] Not Enabled", xbmc.LOGNOTICE)
