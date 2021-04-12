# -*- coding: utf-8 -*-

import xbmcaddon

import os

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE = '[COLOR red][B]HieuITMC[/B][/COLOR] [COLOR yellow][B]Matrix[/B][/COLOR]'
BUILDERNAME = 'HieuITMC '
EXCLUDES = [ADDON_ID, 'repository.hieuitmediacenter']
# Text File with build info in it.
BUILDFILE = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/buildfile.txt'
# Restore data addon
DATAFILE  = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/datafile19.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE = 'http://grumpeh.aion.feralhosting.com/wizard/wizardtexts/KGwizardapk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE = 'Youtube Help'
YOUTUBEFILE = 'http://grumpeh.aion.feralhosting.com/wizard/wizardtexts/KGwizardyoutube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/memcache.txt'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'https://www.yourhost.com/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS = os.path.join(ART, 'hieuit.wizard.png')
ICONMAINT = os.path.join(ART, 'hieuit.wizard.png')
ICONSPEED = os.path.join(ART, 'speedtest.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONCE = os.path.join(ART, 'ce.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'youtube.png')
ICONSAVE = os.path.join(ART, 'backupuserdata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')
ICONMAKECUSTOM = os.path.join(ART, 'customkodi.png')
ICONRESTOREDATA = os.path.join(ART, 'restoredata.png')
ICONADDVANCE = os.path.join(ART, 'tweak.png')
ICONDIR = os.path.join(ART, 'dir.png')
ICONDELPACK = os.path.join(ART, 'packages.png')
ICONBACKUP = os.path.join(ART, 'backup.png')
ICONRESTORE = os.path.join(ART, 'restore.png')
ICONRCLEAR = os.path.join(ART, 'clearcache.png')
ICONULTILITIES = os.path.join(ART, 'utilities.png')
# Hide the section separators 'Yes' or 'No'
HIDESPACERS = 'No'
# Character used in separator
SPACER = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1 = 'yellow'
COLOR2 = 'white'
COLOR3 = 'red'
# Primary menu items   / {0} is the menu item and is required
#THEME1 = u'[COLOR {color1}][I]([COLOR {color1}][B]Chef [/B][/COLOR][COLOR {color2}]Matrix Wizard[COLOR {color1}]) [/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME1 = u'[COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Build Names          / {0} is the menu item and is required
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Alternate items      / {0} is the menu item and is required
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR2)
# Current Build Header / {0} is the menu item and is required
THEME4 = u'[COLOR {color1}]Current Build: [/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Current Theme Header / {0} is the menu item and is required
THEME5 = u'[COLOR {color1}]Current Theme: [/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT = 'Yes'
# You can add \n to do line breaks
CONTACT = 'Thank you!!'
# Images used for the contact window.  http:// for default icon and fanart
CONTACTICON = 'http://'
CONTACTFANART = 'http://_'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE = 'No'
#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL = 'No'
# Addon ID for the repository
REPOID = 'repository.hieuitmediacenter'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/addons.xml'
# Url to folder zip is located in
REPOZIPURL = 'https://'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
# Enable Notification screen Yes or No
ENABLE = 'Yes'
# Url to notification file
NOTIFICATION = 'http://grumpeh.aion.feralhosting.com/wizard/MATRIX/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE = 'Text'
# Font size of header
FONTHEADER = 'Font14'
HEADERMESSAGE = '[COLOR red][B]HieuITMC[/B][/COLOR] [COLOR yellow][B]Matrix[/B][/COLOR]'
# url to image if using Image 424x180
HEADERIMAGE = 'http://'
# Font for Notification Window
FONTSETTINGS = 'Font13'
# Background for Notification Window
BACKGROUND = 'http://'
#########################################################
