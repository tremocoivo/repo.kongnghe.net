# -*- coding: utf-8 -*-
####################################################################################
#                          THANK!                                                  #
# Addon nay duoc tong hop tu internet                                              #
# Tham khao code tu Addon raw.maintenance cua tac gia: Foreverska|Gombeek|Raw Media#
# Tham khao code cua Addon Areswizard                                              #
####################################################################################

import time
import ntpath
################### New Update #####################
import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs, glob
import shutil
import urllib2,urllib, uuid
import re
try:    from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database
from datetime import date, datetime, timedelta
from urlparse import urljoin

from resources.libs import GATracker, extract, downloader, skinSwitch, wizard as wiz
#####################################################
reload(sys);
sys.setdefaultencoding("utf8")

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
base       ='https://hieuit.net'
ADDON      =xbmcaddon.Addon(id='plugin.program.hieuitwizard')
dialog     = xbmcgui.Dialog()    
VERSION    = ADDON.getAddonInfo('version')
PATH       = "Hieuit Media Center"            

thumbnailPath = xbmc.translatePath('special://thumbnails');
cachePath     = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath      = xbmc.translatePath('special://temp')
ADDONPATH     = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'plugin.program.hieuitwizard')
mediaPath     = os.path.join(ADDONPATH, 'media')
databasePath  = xbmc.translatePath('special://database')
zip           =  ADDON.getSetting('zipdir')
DP            =  xbmcgui.DialogProgress()
USERDATA      =  xbmc.translatePath(os.path.join('special://home/userdata',''))
ADDON_DATA    =  xbmc.translatePath(os.path.join(USERDATA,'addon_data'))
ADDONS        =  xbmc.translatePath(os.path.join('special://home','addons'))
GUI           =  xbmc.translatePath(os.path.join(USERDATA,'guisettings.xml'))
FAVS          =  xbmc.translatePath(os.path.join(USERDATA,'favourites.xml'))
SOURCE        =  xbmc.translatePath(os.path.join(USERDATA,'sources.xml'))
ADVANCED      =  xbmc.translatePath(os.path.join(USERDATA,'advancedsettings.xml'))
RSS           =  xbmc.translatePath(os.path.join(USERDATA,'RssFeeds.xml'))
KEYMAPS       =  xbmc.translatePath(os.path.join(USERDATA,'keymaps','keyboard.xml'))
USB           =  xbmc.translatePath(os.path.join(zip))
skin          =  xbmc.getSkinDir()
CHANGELOG     =  xbmc.translatePath(os.path.join(ADDONPATH,'changelog.txt'))

################## New Update ####################################
ADDON_ID         = wiz.ADDON_ID
ADDONTITLE       = wiz.ADDONTITLE
HOME             = wiz.HOME
PACKAGES         = os.path.join(ADDONS,    'packages')
ADDOND           = os.path.join(USERDATA,  'addon_data')
ADDONDATA        = os.path.join(USERDATA,  'addon_data', ADDON_ID)
FANART           = os.path.join(ADDONPATH, 'fanart.jpg')
BACKUPLOCATION   = wiz.BACKUPLOCATION
MYBUILDS         = wiz.MYBUILDS
BUILDLINK        = wiz.getS('buildlink')
CUSTOMLINK       = wiz.getS('customlink')
BUILDFILE        = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/wizard.txt'
UPDATEFILE       = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/update.txt'
TWEAKFILE        = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/Tweak/tweak.txt'
DATAFILE         = 'https://raw.githubusercontent.com/tremocoivo/repo.kongnghe.net/master/datafile.txt'
KODIV            = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
if KODIV > 17:
	from resources.libs import zfile as zipfile #FTG mod for Kodi 18
else:
	import zipfile

COLOR1           = wiz.COLOR1
COLOR2           = wiz.COLOR2
EXCLUDES         = wiz.EXCLUDES
KEEPREPOS		 = 'true'
THIRDPARTY       = 'false'
MCNAME           = wiz.mediaCenter()
LOGFILES         = wiz.LOGFILES
DEFAULTPLUGINS   = ['metadata.album.universal', 'metadata.artists.universal', 'metadata.common.fanart.tv', 'metadata.common.imdb.com', 'metadata.common.musicbrainz.org', 'metadata.themoviedb.org', 'metadata.tvdb.com', 'service.xbmc.versioncheck']
#######################################################################

#######################################################################
#                          CLASSES
#######################################################################

class cacheEntry:
    def __init__(self, namei, pathi):
        self.name = namei
        self.path = pathi

#######################################################################
#						Google Analytics
#######################################################################
global analytics

def setupAnalytics():
    global analytics

    if(os.path.isfile(os.path.join(ADDONPATH, "uuid.txt")) != True):
        userID = uuid.uuid1()
        uuidFile = open(os.path.join(ADDONPATH,"uuid.txt"), "w")
        uuidFile.write(str(userID))
        uuidFile.close()

    uuidFile = open(os.path.join(ADDONPATH, "uuid.txt"), "r")
    userID = uuidFile.readline()
    uuidFile.close()

    analytics = GATracker.GAconnection("UA-127046996-1", userID)
	
def MAIN():
    setView('videos', 'MAIN')
    global analytics
    analytics.sendPageView("HieuIT Media Center","MAIN","main")
    #xbmc.executebuiltin("Container.SetViewMode(50)")
    addItem('[COLOR red][B]HIEUIT[/B][/COLOR] [COLOR yellow][B]MOVIES PLAYLIST[/B][/COLOR] [B]- VIP FSHARE[/B]','url', 12,os.path.join(mediaPath, "vip.png"))
    addItem('[COLOR red][B]HIEUIT[/B][/COLOR] [COLOR yellow][B]MOVIES PLAYLIST[/B][/COLOR] [B]- ** FREE **[/B]','url', 121,os.path.join(mediaPath, "free.png"))
    addDir1('[COLOR red][B]INSTALL KODI:[/B][/COLOR] Cài Đặt Kodi Full Addon','url', 14,os.path.join(mediaPath, "hieuit.wizard.png"),FANART, '1-Click Cài Đặt Kodi Với Các Addon Thông Dụng')
    #addDir1('[COLOR red][B]INSTALL KODI:[/B][/COLOR] Cài Đặt Kodi Full Addon','url', 14,os.path.join(mediaPath, "hieuit.wizard.png"))
    addDir1('[B][COLOR green]BACKUP[/COLOR]/[COLOR yellow]RESTORE[/COLOR]:[/B] Sao Lưu/Khôi Phục Bản Kodi Cá Nhân','url', 15,os.path.join(mediaPath, "customkodi.png"),FANART,'Tạo Bản Kodi Để Khôi Phục Khi Cần')		
    addDir1('[COLOR green][B]Restore Data[/B][/COLOR] - Cho Máy Không Dùng Source [COLOR red][B]HieuIT[/B][/COLOR] [COLOR yellow][B]Wizard[/B][/COLOR] ','url', 10,os.path.join(mediaPath, "restoredata.png"),FANART,'Chỉ khôi phục lại data addon mà không phải Restore bản Kodi của HieuITWizard')	
    addDir1('[COLOR yellow][B]TWEAK[/B][/COLOR] - Thiết Lập File [COLOR red][B]AdvancedSetting.xml[/B][/COLOR]','url', 3,os.path.join(mediaPath, "tweak.png"),FANART,'Tăng memcache khi xem phim không bị giật lag')
    addDir1('[COLOR yellow][B]Utilities Tool[/B][/COLOR] - Công Cụ Tiện Ích','url', 4,os.path.join(mediaPath, "utilities.png"),FANART,'Các công cụ cần thiết trong quá trình sử dụng Kodi')
    addDir1('[COLOR yellow][B]UPDATE[/B][/COLOR] - Sửa Lỗi Addon','url', 22,os.path.join(mediaPath, "update.png"),FANART,'Bản cập nhật sửa lỗi các addon khi dùng bản Build của HieuIT Wizard')
    addItem('[COLOR yellow][B]ChangeLog[/B][/COLOR] - Có gì mới?','url', 29,os.path.join(mediaPath, "movieslibrary.png"))	
    addDir1('[B][COLOR yellow]Like[/COLOR] and [COLOR pink]Donate[/COLOR][/B]: Ủng Hộ Tác Giả','url', 9,os.path.join(mediaPath, "donate.png"),FANART,'Lets share to be shared')
	
def INSTALLKODI():
    setView('videos', 'MAIN')
    #global analytics 	
    analytics.sendPageView("HieuIT Media Center","Installkodi","HieuIT Wizard")
    if not BUILDLINK == '':
         link = OPEN_URL(BUILDLINK).replace('\n','').replace('\r','')
         match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
         addItem('Custom Build URL: [COLOR yellow]%s[/COLOR]' %(BUILDLINK),'url',998,'')
         addItem('[COLOR yellow][B]Reset:[/B][/COLOR] Xóa link trả về mặc định','url',28,'')		 
         addItem('Bạn đang dùng [COLOR yellow][B]%s[/B][/COLOR] Version: [COLOR green]%s[/COLOR]' % (MCNAME, KODIV), 'url', 9999, '') 
         addItem('===== [COLOR red][B]BẢN BUILD CỦA BẠN[/B][/COLOR] =====', 'url', 9999, '')
         for name,url,iconimage,fanart,description in match:
             addDir(name,url,1,iconimage,fanart,description)
    else:
         link = OPEN_URL(BUILDFILE).replace('\n','').replace('\r','')
         match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
         addItem('[COLOR yellow][B]Custom Build URL:[/B][/COLOR] Nhập list của bạn','url',27,'')		 
         addItem('Bạn đang dùng [COLOR yellow][B]%s (%s)[/B][/COLOR] Version: [COLOR green]%s[/COLOR]' % (MCNAME,platform(), KODIV), 'url', 999, '') 
         addItem('===== [COLOR red][B]CHỌN BẢN BUILD MUỐN SỬ DỤNG[/B][/COLOR] =====', 'url', 999, '')
         for name,url,iconimage,fanart,description in match:
              addDir(name,url,1,iconimage,fanart,description)
		  
def RESTOREDATAFILE():
    setView('videos', 'MAIN')
    analytics.sendPageView("HieuIT Media Center","Installkodi","HieuIT Wizard")
    link = OPEN_URL(DATAFILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
          addDir(name,url,25,iconimage,fanart,description)
    addItem('[COLOR yellow][B]Restore From File[/B][/COLOR] - Chọn file data cần khôi phục','url', 101, os.path.join(mediaPath,"dir.png"))
    if not CUSTOMLINK == '':
         link = OPEN_URL(CUSTOMLINK).replace('\n','').replace('\r','')
         match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
         addItem('===== [COLOR red][B]LIST DATA CÁ NHÂN[/B][/COLOR] =====', 'url', 9999, '')
         addItem('Custom Data URL: [COLOR yellow]%s[/COLOR]' %(CUSTOMLINK),'url',997,'')
         addItem('[COLOR yellow][B]Reset:[/B][/COLOR] Xóa link trả về mặc định','url',281,'')		 
         
         for name,url,iconimage,fanart,description in match:
             addDir(name,url,25,iconimage,fanart,description)
    else:
         addItem('[COLOR yellow][B]Restore From URL[/B][/COLOR] - Nhập URL list data cần khôi phục','url', 271, os.path.join(mediaPath,"dir.png"))
	
def BACKUP_RESTORE():
  setView('videos', 'MAIN')
  analytics.sendPageView("HieuIT Media Center","backup_restore","backup_restore")
  if zip=='':
   if dialog.ok(ADDONTITLE,'Bạn chưa thiết lập đường dẫn lưu file Backup cho Kodi','Mở Addon Setting và Chọn tab [COLOR green][B]Zip Folder[/B][/COLOR].','Nhấn [B]OK[/B] để bắt đầu thiết lập'):
         backupdir = dialog.browse(0, '[COLOR %s]Chọn đường dẫn lưu file Backup[/COLOR]' % COLOR2, '', '', False, False)
         wiz.setS('zipdir',backupdir)
   wiz.refresh()
    #ADDON.openSettings()
  else:
     #setView('files', 'MAIN')
     addDir2('[COLOR green][B]BACKUP:[/B][/COLOR] Sao lưu Kodi','url',16,os.path.join(mediaPath,"backup.png"),'Tạo bản Build Kodi cá nhân hóa')
     addDir2('[COLOR yellow][B]RESTORE:[/B][/COLOR] Khôi phục Kodi','url',17,os.path.join(mediaPath,"restore.png"),'Khôi phục lại bản build đã tạo trước đó hoặc tải trên interter')

def BACKUP_OPTION():
    analytics.sendPageView("HieuIT Media Center","backup_option","backupmenu")
    setView('videos', 'MAIN')
    if not zip == '':
        addItem('Thư Mục Backup Mặc Định: [COLOR yellow]%s[/COLOR] <-- Nhấn để đổi thư mục' % (MYBUILDS),'url', 999, os.path.join(mediaPath,"dir.png"))	
        addDir2('[COLOR green][B]FULL BACKUP:[/B][/COLOR] Sao Lưu Toàn Bộ Hệ Thống','url',18,os.path.join(mediaPath,"fullbackup.png"),'Back Up Your Full System')
        #addDir2('[COLOR yellow]Backup Addons:[/COLOR] Sao luu tat ca Addon','addons',19,'','Back Up Your Addons')
        addDir2('[COLOR yellow]Backup UserData:[/COLOR] Sao Lưu Setting Tất Cả Addon','addon_data',19,os.path.join(mediaPath,"backupuserdata.png"),'Back Up Your Addon Userdata')  
        addDir2('[COLOR yellow]Backup Guisettings.xml:[/COLOR] Sao Lưu Setting Của Kodi',GUI,191,os.path.join(mediaPath,"backupsetting.png"),'Back Up Your guisettings.xml')
        if os.path.exists(FAVS):
            addDir2('[COLOR yellow]Backup Favourites:[/COLOR] Sao Lưu Mục Yêu Thích',FAVS,20,os.path.join(mediaPath,"backupFavourites.png"),'Back Up Your favourites.xml')
        if os.path.exists(SOURCE):
            addDir2('[COLOR yellow]Backup Source:[/COLOR] Sao Lưu Các Link Trong File Manager',SOURCE,20,os.path.join(mediaPath,"backupsource.png"),'Back Up Your sources.xml')
        if os.path.exists(ADVANCED):
            addDir2('[COLOR yellow]Backup AdvancedSettings:[/COLOR] Sao Lưu File Advancedsettings.xml',ADVANCED,20,os.path.join(mediaPath,"backupcachesetting.png"),'Back Up Your advancedsettings.xml')
        if os.path.exists(KEYMAPS):
            addDir2('[COLOR yellow]Backup keyboard:[/COLOR] Sao Lưu Phím Tắt Kodi',KEYMAPS,20,os.path.join(mediaPath,"backupkeymap.png"),'Back Up Your keyboard.xml')

def RESTORE_OPTION():
    setView('videos', 'MAIN')
    analytics.sendPageView("HieuIT Media Center","restore_option","restoremenu")
    #if os.path.exists(os.path.join(USB,'backup.zip')):	
    addDir2('[COLOR green][B]FULL RESTORE:[/B][/COLOR] Khôi Phục Toàn Bộ Từ File Đã Backup','url',21,os.path.join(mediaPath,"fullrestore.png"),'Restore all from backup file')   
    #if os.path.exists(os.path.join(USB,'addon_data.zip')):   
    addDir2('[COLOR yellow]Restore UserData:[/COLOR] Khôi Phục Setting Các Addon','addon_data',211,os.path.join(mediaPath,"restoreuserdata.png"),'Restore Your AddonData')

    if os.path.exists(os.path.join(USB,'guisettings.xml')):
        addDir2('[COLOR yellow]Restore Guisettings:[/COLOR] Khôi Phục Setting Của Kodi',GUI,20,os.path.join(mediaPath,"restoresetting.png"),'Restore Your guisettings.xml')
    
    if os.path.exists(os.path.join(USB,'favourites.xml')):
        addDir2('[COLOR yellow]Restore Favourites:[/COLOR] Khôi Phục Mục Yêu Thích',FAVS,20,os.path.join(mediaPath,"restorefavourite.png"),'Restore Your favourites.xml')
        
    if os.path.exists(os.path.join(USB,'sources.xml')):
        addDir2('[COLOR yellow]Restore Source:[/COLOR] Khôi Phục Link Trong File Manager',SOURCE,20,os.path.join(mediaPath,"restoresource.png"),'Restore Your sources.xml')
        
    if os.path.exists(os.path.join(USB,'advancedsettings.xml')):
        addDir2('[COLOR yellow]Restore AdvancedSettings:[/COLOR] Khôi Phục File Advancedsettings.xml',ADVANCED,20,os.path.join(mediaPath,"restorecachesetting.png"),'Restore Your advancedsettings.xml')        

    if os.path.exists(os.path.join(USB,'keyboard.xml')):
        addDir2('[COLOR yellow]Restore Keyboard:[/COLOR] Khôi Phục Phím Tắt Kodi',KEYMAPS,20,os.path.join(mediaPath,"restorekeymap.png"),'Restore Your keyboard.xml')
		
def RESTORE_ZIP_FILE(name,url):
        
    if 'addon_data' in url:
        
		wiz.backUpOptions('addondata')
    #else:
        # ZIPFILE = xbmc.translatePath(os.path.join(USB,'addon_data.zip'))
        #DIR = ADDON_DATA
		return

def RESTORE_BACKUP_XML(name,url,description):
    if 'Backup' in name:
        TO_READ   = open(url).read()
        TO_WRITE  = os.path.join(USB,description.split('Your ')[1])
        
        f = open(TO_WRITE, mode='w')
        f.write(TO_READ)
        f.close() 
         
    else:
    
        if 'guisettings.xml' in description:
            a = open(os.path.join(USB,description.split('Your ')[1])).read()
            
            r='<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>'% skin
            
            match=re.compile(r).findall(a)
            
            for type,string,setting in match:
                setting=setting.replace('&quot;','') .replace('&amp;','&') 
                xbmc.executebuiltin("Skin.Set%s(%s,%s)"%(type.title(),string,setting))  
        else:    
            TO_WRITE   = os.path.join(url)
            TO_READ  = open(os.path.join(USB,description.split('Your ')[1])).read()
            
            f = open(TO_WRITE, mode='w')
            f.write(TO_READ)
            f.close()  
    dialog.ok(ADDONTITLE, "", 'Đã xong!','')

def systemInfo():
	infoLabel = ['System.FriendlyName', 
				 'System.BuildVersion', 
				 'System.CpuUsage',
				 'System.ScreenMode',
				 'Network.IPAddress',
				 'Network.MacAddress',
				 'System.Uptime',
				 'System.TotalUptime',
				 'System.FreeSpace',
				 'System.UsedSpace',
				 'System.TotalSpace',
				 'System.Memory(free)',
				 'System.Memory(used)',
				 'System.Memory(total)']
	data      = []; x = 0
	for info in infoLabel:
		temp = wiz.getInfo(info)
		y = 0
		while temp == "Busy" and y < 10:
			temp = wiz.getInfo(info); y += 1; wiz.log("%s sleep %s" % (info, str(y))); xbmc.sleep(200)
		data.append(temp)
		x += 1
	
	ram_free      = wiz.convertSize(int(float(data[11][:-2]))*1024*1024)
	addItem('[COLOR white]Ram còn trống:[/COLOR] [COLOR yellow]%s[/COLOR]' % (ram_free),'url', 9999, '')		

# def restoredata():
    # #analytics.sendPageView("HieuIT Media Center","restoredata","Data Addon")
    # setView('videos', 'MAIN')
    # addItem('Data Addon Gdrive 0.8.66 - Dành cho Kodi 16/SPMC', 'url', 122,os.path.join(mediaPath, "gdrive.png"))
    # addItem('Data  Addon Google Drive', 'url', 13,os.path.join(mediaPath, "ggdrive.png"))

def enableAddon(id):
	ADDONID2 = id
	query = xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.GetAddonDetails","id":1,"params":{"addonid":"%s", "properties": ["enabled"]}' % ADDONID2)
	if '"enabled":false' in query:
		#xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s","enabled":false}}' % ADDONID2)
		dialog.ok(ADDONTITLE, "Addon này hiện đã được [COLOR yellow]Enable[/COLOR] rồi")
	else:
		xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s", "enabled":true}}' % ADDONID2)
		dialog.ok(ADDONTITLE, "Đã Enable[COLOR yellow] %s[/COLOR] thành công" %(ADDONID2))

def fixyoutube():
	y = dialog.yesno("[COLOR red][B]CẢNH BÁO !!![/COLOR][/B]", "Tất cả [COLOR yellow]thiết lập của Youtube & InputStream[/COLOR] đã lưu trước đó sẽ bị ghi đè.", "Bạn có muốn tiếp tục?") 
	if y == 0:   
		pass
	else:
		resolution=dialog.yesno(ADDONTITLE, 'Chọn thiết lập mặc định cho Youtube:' , '[COLOR yellow][B]Xem 4K:[/B][/COLOR] Dành cho máy cấu hình mạnh', '[COLOR green][B]1080p:[/B][/COLOR] Tối ưu nhất', nolabel='[B][COLOR green]Chọn 1080p[/COLOR][/B]',yeslabel='[B][COLOR yellow]Chọn 4K[/COLOR][/B]')
		if resolution == 1:
			wizard("fixyoutube4k",'https://dl.dropboxusercontent.com/s/10urp5vj7acbzwp/fix_youtube4k.zip',description)
			wiz.clearS('build')
			wiz.refresh()
		else:
			wizard("fixyoutube1080p",'https://dl.dropboxusercontent.com/s/vkr6rmchwuuppca/fix_youtube1080.zip',description)
			wiz.clearS('build')
			wiz.refresh()
	dialog.ok(ADDONTITLE, 'Cài đặt xong, khởi động lại KODI để có hiệu lực','Nhấn OK để thoát')
	wiz.killxbmc(True)	
			
def inputvideo():
	myplatform = platform()
	if myplatform == 'android':
		enableAddon('inputstream.adaptive')
		fixyoutube()
	elif myplatform == 'linux':
		INPUTSTREAM = os.path.join(ADDONS,'inputstream.adaptive')
		if not os.path.exists(INPUTSTREAM):
			wizard("inputstream",'https://dl.dropboxusercontent.com/s/06kufgcxs2sgrjz/fix_inputstreamL.zip',description)
			wiz.clearS('build')
		else:pass
		wiz.forceUpdate()
		xbmc.sleep(500)
		enableAddon('inputstream.adaptive')
		fixyoutube()
	elif myplatform == 'windows':
		INPUTSTREAM = os.path.join(ADDONS,'inputstream.adaptive')
		if not os.path.exists(INPUTSTREAM):
			wizard("inputstream",'https://dl.dropboxusercontent.com/s/emlfk5d13iyhtvl/fix_inputstreamW.zip',description)
			wiz.clearS('build')
		else:pass
		wiz.forceUpdate()
		xbmc.sleep(500)
		enableAddon('inputstream.adaptive')
		fixyoutube()


def inputurl():
	#urltemp = wiz.getS('buildlink')
	keyboardHandle = xbmc.Keyboard(wiz.getS('buildlink'),'[COLOR yellow]Nhập link chứa list Build của bạn: (hỗ trợ bit.ly, gg.gg)[/COLOR]\n[I](Xem cách tạo list tại https://hieuit.net/hieuitwizard)[/I]')
	keyboardHandle.doModal()
	if (keyboardHandle.isConfirmed()):
		queryText = keyboardHandle.getText()
		if len(queryText) == 0:
			sys.exit()	
		else:
			working = wiz.workingURL(queryText)
			if not working == True:
				dialog.ok(ADDONTITLE,'Sai URL','Vui lòng nhập lại')
				inputurl()
			else:	
				wiz.setS('buildlink',queryText)

def dataurl():
	#urltemp = wiz.getS('buildlink')
	keyboardHandle = xbmc.Keyboard(wiz.getS('customlink'),'[COLOR yellow]Nhập link chứa list Data của bạn: (hỗ trợ bit.ly, gg.gg)[/COLOR]\n[I](Xem cách tạo list tại https://hieuit.net/hieuitwizard)[/I]')
	keyboardHandle.doModal()
	if (keyboardHandle.isConfirmed()):
		queryText = keyboardHandle.getText()
		if len(queryText) == 0:
			sys.exit()
			
		else:
			working = wiz.workingURL(queryText)
			if not working == True:
				dialog.ok(ADDONTITLE,'Sai URL','Vui lòng nhập lại')
				inputurl()
			else:	
				wiz.setS('customlink',queryText)
	
def Tweak():
    setView('videos', 'MAIN')
    analytics.sendPageView("HieuIT Media Center","Tweak","Tang Toc Cache")
    systemInfo()
    if os.path.exists(ADVANCED):
        addItem('===== [COLOR red][B]ADVANCEDSETTING CONFIG[/B][/COLOR] =====', 'url', 9999, '')	
        addDir("Xem file [COLOR yellow]advancedsettings.xml[/COLOR]", 'url',301, '', '','Xem nội dung file Advancedsettings.xml')
        addDir("Xóa file [COLOR yellow]advancedsettings.xml[/COLOR]", 'url',302, '', '','Xóa file Advancedsettings.xml')
    else: 
        addItem('[COLOR red][B]NOTE:[/B][/COLOR] Bạn chưa thiết lập file [COLOR yellow]advancedsettings.xml[/COLOR]', 'url', 9999, '')
    addItem('===== [COLOR red][B]AUTO SET RAMCACHE[/B][/COLOR] =====', 'url', 9999, '')		
    link = OPEN_URL(TWEAKFILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,2,iconimage,fanart,description)
    #xbmc.executebuiltin("Container.SetViewMode(50)")
	
def viewxml(name):
    f = open(ADVANCED,mode='r'); msg = f.read(); f.close()	
    wiz.TextBox("[B][COLOR lime]Your advancedsettings.xml file[/B][/COLOR]",msg)
	
def removexmlfile(name):
    if os.path.exists(ADVANCED):
        os.remove(ADVANCED)
        #notification(ADDONTITLE, 'advancedsettings.xml removed', '4000', iconart)
        wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]advancedsettings.xml removed[/COLOR]' % COLOR2)
        wiz.refresh()

def UPDATE():
    setView('videos', 'MAIN')
    analytics.sendPageView("HieuIT Media Center","Update","Update Addon")
    link = OPEN_URL(UPDATEFILE).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,201,iconimage,fanart,description)
    #xbmc.executebuiltin("Container.SetViewMode(50)")		

    
def utilities():
    analytics.sendPageView("HieuIT Media Center","menucache","Xoa cache")
    #analytics.sendPageView("RawMaintenenance","maintenance","maint")
    setView('videos', 'MAIN')
    addItem('Thiết lập xem Youtube 4K/1080p', 'url', 26,os.path.join(mediaPath, "youtube4k.png"))
    addItem('[COLOR yellow][B]Speedtest[/B][/COLOR] - Kiểm Tra Tốc Độ Mạng','url', 23,os.path.join(mediaPath, "speedtest.png"))
    addItem('Clear Cache - Xóa Cache','url', 5,os.path.join(mediaPath, "deletecache.png"))
    addItem('Delete Thumbnails - Xóa Ảnh Xem Trước Của Video/Addon', 'url', 6,os.path.join(mediaPath, "thumbnail.png"))
    addItem('Purge Packages - Xóa Các Gói Cài Đặt Cũ', 'url', 7,os.path.join(mediaPath, "packages.png"))
    addItem('[COLOR red][B]Delete All - Xóa Tất Cả[/B][/COLOR]', 'url', 8,os.path.join(mediaPath, "clearcache.png"))	
    addItem('[COLOR red][B]Refresh KODI[/B][/COLOR] - Khôi phục Kodi về mặc định (giữ nguyên Repository)','url', 24,os.path.join(mediaPath, "reset.png"))

    
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    
###########################
###### Fresh Install ######
###########################
def freshStart(install=None, over=False):
	# if KEEPTRAKT == 'true':
		# traktit.autoUpdate('all')
		# wiz.setS('traktlastsave', str(THREEDAYS))
	# if KEEPREAL == 'true':
		# debridit.autoUpdate('all')
		# wiz.setS('debridlastsave', str(THREEDAYS))
	# if KEEPLOGIN == 'true':
		# loginit.autoUpdate('all')
		# wiz.setS('loginlastsave', str(THREEDAYS))
	if over == True: yes_pressed = 1
	elif install == 'restore': yes_pressed=dialog.yesno(ADDONTITLE, 'Lựa chọn cách bạn sẽ cài đặt bản build này:' , '[COLOR yellow][B]Fresh Install:[/B][/COLOR] Xóa toàn bộ và thay bằng bản build mới', '[COLOR green][B]Override Install:[/B][/COLOR] Cập nhật bản build vào bản Kodi hiện tại', nolabel='[B][COLOR green]Override Install[/COLOR][/B]',yeslabel='[B][COLOR yellow]Fresh Install[/COLOR][/B]')
	elif install: yes_pressed=dialog.yesno(ADDONTITLE, "Bạn có chắc muốn xóa toàn bộ Kodi về mặc định", "Trước khi cài đặt bản build [COLOR %s]%s[/COLOR]?" % (COLOR1, install), nolabel='[B][COLOR red]Hủy[/COLOR][/B]', yeslabel='[B][COLOR green]Tiếp tục[/COLOR][/B]')
	else: yes_pressed=dialog.yesno(ADDONTITLE, "[COLOR %s]Bạn có muốn khôi phục" % COLOR2, "Các thiết lập của Kodi về mặc định?[/COLOR]", nolabel='[B][COLOR red]Hủy[/COLOR][/B]', yeslabel='[B][COLOR green]Tiếp tục[/COLOR][/B]')
	if yes_pressed:
		if not wiz.currSkin() in 'skin.estuary':
			skin = 'skin.estuary'
			skinSwitch.swapSkins(skin)
			x = 0
			xbmc.sleep(1000)
			while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)") and x < 150:
				x += 1
				xbmc.sleep(200)
				wiz.ebi('SendAction(Select)')
			if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
				wiz.ebi('SendClick(11)')
			else: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]Fresh Install: Skin Swap Timed Out![/COLOR]' % COLOR2); return False
			xbmc.sleep(1000)
		if not wiz.currSkin() in ['skin.confluence', 'skin.estuary']:
			wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]Fresh Install: Skin Swap Failed![/COLOR]' % COLOR2)
			return
		wiz.addonUpdates('set')
		xbmcPath=os.path.abspath(HOME)
		DP.create(ADDONTITLE,"[COLOR %s]Calculating files and folders" % COLOR2,'', 'Please Wait![/COLOR]')
		total_files = sum([len(files) for r, d, files in os.walk(xbmcPath)]); del_file = 0
		DP.update(0, "[COLOR %s]Gathering Excludes list." % COLOR2)
		#EXCLUDES.append('My_Builds')
		EXCLUDES.append('archive_cache')
		#if KEEPREPOS == 'true':
		repos = glob.glob(os.path.join(ADDONS, 'repo*/'))
		for item in repos:
				repofolder = os.path.split(item[:-1])[1]
				if not repofolder == EXCLUDES:
					EXCLUDES.append(repofolder)
		# if KEEPSUPER == 'true':
			# EXCLUDES.append('plugin.program.super.favourites')
		# if KEEPWHITELIST == 'true':
			# pvr = ''
			# whitelist = wiz.whiteList('read')
			# if len(whitelist) > 0:
				# for item in whitelist:
					# try: name, id, fold = item
					# except: pass
					# if fold.startswith('pvr'): pvr = id 
					# depends = dependsList(fold)
					# for plug in depends:
						# if not plug in EXCLUDES:
							# EXCLUDES.append(plug)
						# depends2 = dependsList(plug)
						# for plug2 in depends2:
							# if not plug2 in EXCLUDES:
								# EXCLUDES.append(plug2)
					# if not fold in EXCLUDES:
						# EXCLUDES.append(fold)
				# if not pvr == '': wiz.setS('pvrclient', fold)
		# if wiz.getS('pvrclient') == '':
			# for item in EXCLUDES:
				# if item.startswith('pvr'):
					# wiz.setS('pvrclient', item)
		DP.update(0, "[COLOR %s]Clearing out files and folders:" % COLOR2)
		latestAddonDB = wiz.latestDB('Addons')
		for root, dirs, files in os.walk(xbmcPath,topdown=True):
			dirs[:] = [d for d in dirs if d not in EXCLUDES]
			for name in files:
				del_file += 1
				fold = root.replace('/','\\').split('\\')
				x = len(fold)-1
				# if name == 'sources.xml' and fold[-1] == 'userdata' and KEEPSOURCES == 'true': wiz.log("Keep Sources: %s" % os.path.join(root, name), xbmc.LOGNOTICE)
				# elif name == 'favourites.xml' and fold[-1] == 'userdata' and KEEPFAVS == 'true': wiz.log("Keep Favourites: %s" % os.path.join(root, name), xbmc.LOGNOTICE)
				# elif name == 'profiles.xml' and fold[-1] == 'userdata' and KEEPPROFILES == 'true': wiz.log("Keep Profiles: %s" % os.path.join(root, name), xbmc.LOGNOTICE)
				# elif name == 'advancedsettings.xml' and fold[-1] == 'userdata' and KEEPADVANCED == 'true':  wiz.log("Keep Advanced Settings: %s" % os.path.join(root, name), xbmc.LOGNOTICE)
				if name in LOGFILES: wiz.log("Keep Log File: %s" % name, xbmc.LOGNOTICE)
				elif name.endswith('.db'):
					try:
						if name == latestAddonDB and KODIV >= 17: wiz.log("Ignoring %s on v%s" % (name, KODIV), xbmc.LOGNOTICE)
						else: os.remove(os.path.join(root,name))
					except Exception, e: 
						if not name.startswith('Textures13'):
							wiz.log('Failed to delete, Purging DB', xbmc.LOGNOTICE)
							wiz.log("-> %s" % (str(e)), xbmc.LOGNOTICE)
							wiz.purgeDb(os.path.join(root,name))
				else:
					DP.update(int(wiz.percentage(del_file, total_files)), '', '[COLOR %s]File: [/COLOR][COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name), '')
					try: os.remove(os.path.join(root,name))
					except Exception, e: 
						wiz.log("Error removing %s" % os.path.join(root, name), xbmc.LOGNOTICE)
						wiz.log("-> / %s" % (str(e)), xbmc.LOGNOTICE)
			if DP.iscanceled(): 
				DP.close()
				wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Fresh Start Cancelled[/COLOR]" % COLOR2)
				return False
		for root, dirs, files in os.walk(xbmcPath,topdown=True):
			dirs[:] = [d for d in dirs if d not in EXCLUDES]
			for name in dirs:
				DP.update(100, '', 'Cleaning Up Empty Folder: [COLOR %s]%s[/COLOR]' % (COLOR1, name), '')
				if name not in ["Database","userdata","temp","addons","addon_data"]:
					shutil.rmtree(os.path.join(root,name),ignore_errors=True, onerror=None)
			if DP.iscanceled(): 
				DP.close()
				wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Fresh Start Cancelled[/COLOR]" % COLOR2)
				return False
		DP.close()
		#wiz.clearS('build')
		if over == True:
			return True
		elif install == 'restore': 
			return True
		elif install: 
			#buildWizard(install, 'normal', over=True)
			name = wiz.getS('buildname')
			wizard(name,url,description)
			wiz.addonUpdates('reset')
			dialog.ok(ADDONTITLE, '[COLOR yellow]Đã cài đặt thành công![/COLOR]', 'Nhấn [B]OK[/B] để thoát Kodi')
			wiz.killxbmc(True)
		else:
			# if INSTALLMETHOD == 1: todo = 1
			# elif INSTALLMETHOD == 2: todo = 0
			# else: todo = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to [COLOR %s]Force close[/COLOR] kodi or [COLOR %s]Reload Profile[/COLOR]?[/COLOR]" % (COLOR2, COLOR1, COLOR1), yeslabel="[B][COLOR red]Reload Profile[/COLOR][/B]", nolabel="[B][COLOR green]Force Close[/COLOR][/B]")
			# if todo == 1: wiz.reloadFix('fresh')
			# else: wiz.addonUpdates('reset'); wiz.killxbmc(True)
			wiz.addonUpdates('reset')
			wiz.killxbmc(True)
	else: 
		if not install == 'restore':
			wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]Fresh Install: Cancelled![/COLOR]' % COLOR2)
			wiz.refresh()

###########################
###### Build Install ######
###########################
def buildWizard():
	wiz.setS('buildname', name)
	yes = dialog.yesno(ADDONTITLE, 'Hỗ trợ cài đặt nhanh Kodi kèm theo các Addon xem phim chỉ trong vòng 1 nốt nhạc', 'Bạn có muốn làm ngay không?', nolabel='[B][COLOR red]Không[/COLOR][/B]',yeslabel='[B][COLOR green]OK, làm ngay[/COLOR][/B]')
	if yes == 0:
		pass
	else:
		choice = dialog.yesno(ADDONTITLE, 'Lựa chọn cách bạn sẽ cài đặt bản build này:' , '[COLOR yellow][B]Fresh Install:[/B][/COLOR] Xóa toàn bộ và thay bằng bản build mới', '[COLOR green][B]Override Install:[/B][/COLOR] Cập nhật bản build vào bản Kodi hiện tại', nolabel='[B][COLOR yellow]Fresh Install[/COLOR][/B]',yeslabel='[B][COLOR green]Override Install[/COLOR][/B]')
		if choice == 0:
			freshStart(name)
		else: 
			wizard(name,url,description)
			if KODIV >= 17: wiz.addonDatabase(ADDON_ID, 1)
			dialog.ok(ADDONTITLE, '[COLOR yellow]Đã cài đặt thành công![/COLOR]', 'Nhấn [B]OK[/B] để thoát Kodi')
			wiz.killxbmc(True)

def restoreit(type):
	if type == 'build':
		x = freshStart('restore')
		if x == False: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Local Restore Cancelled[/COLOR]" % COLOR2); return
	if not wiz.currSkin() in ['skin.confluence', 'skin.estuary']:
		wiz.skinToDefault()
	wiz.restoreLocal(type)

def datagame():
    path = os.path.join(xbmc.translatePath('special://home'),'userdata', 'sources.xml')
    if not os.path.exists(path):
        f = open(path, mode='w')
        f.write('<sources><games><source><name>[Local] GAMES</name><path pathversion="1">special://home/Game</path></source></games></sources>')
        f.close()
        return
        
    f   = open(path, mode='r')
    str = f.read()
    f.close()
    if not'special://home/Game' in str:
        if '</games>' in str:
            str = str.replace('</games>','<source><name>[Local] GAMES</name><path pathversion="1">special://home/Game</path></source></games>')
            f = open(path, mode='w')
            f.write(str)
            f.close()
        else:
            str = str.replace('</sources>','<games><source><name>[Local] GAMES</name><path pathversion="1">special://home/Game</path></source></games></sources>')
            f = open(path, mode='w')
            f.write(str)
            f.close()
			
def datafile():
	yes = dialog.yesno(ADDONTITLE, 'Tất cả data addon đã lưu trước đó sẽ bị ghi đè', 'Bạn có muốn tiếp tục không?', nolabel='[B][COLOR red]Không[/COLOR][/B]',yeslabel='[B][COLOR green]OK, làm ngay[/COLOR][/B]')
	if yes == 0:
		return
	else:
		wizard(name,url,description)
		if 'googledrive' in url:
			global analytics
			analytics.sendEvent("HieuIT Wizard", "Restore ggdrive")
			dialog.ok(ADDONTITLE, "Đã khôi phục xong [COLOR green]%s[/COLOR]" % (name), "Nhấn OK và thưởng thức ^^")
			wiz.clearS('build')
			wiz.refresh()
			xbmc.executebuiltin('RunAddon(plugin.googledrive)')	
		if 'gdrive' in url:
			dialog.ok(ADDONTITLE, "Đã khôi phục xong [COLOR green]%s[/COLOR]" % (name), "Nhấn OK và thưởng thức ^^")
			wiz.clearS('build')
			wiz.refresh()
			xbmc.executebuiltin('RunAddon(plugin.video.gdrive)')
		if 'Game' in url:
			global analytics
			analytics.sendEvent("HieuIT Wizard", "Restore Game")
			datagame()
			dialog.ok(ADDONTITLE, "Đã khôi phục xong [COLOR green]%s[/COLOR]" % (name), "Nhấn OK để thoát KODI")
			wiz.clearS('build')
			wiz.killxbmc(True)
		
		

def restorefile():
	file = dialog.browse(1, '[COLOR %s]Chọn file muốn Khôi phục[/COLOR]' % COLOR2, 'files', '.zip', False, False)
	#log("[RESTORE BACKUP %s] File: %s " % (type.upper(), file), xbmc.LOGNOTICE)
	if file == "" or not file.endswith('.zip'):
		wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR yellow]Khôi phục Data:[/COLOR] Đã bị hủy")
		return
	DP.create(ADDONTITLE,'[COLOR %s]Đang giải nén file' % COLOR2,'', 'Chờ chút nhé[/COLOR]')
	if not os.path.exists(USERDATA): os.makedirs(USERDATA)
	if not os.path.exists(ADDOND): os.makedirs(ADDOND)
	if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
	loc = HOME
	wiz.log("Restoring to %s" % loc, xbmc.LOGNOTICE)
	display = os.path.split(file)
	fn = display[1]
	try:
		zipfile.ZipFile(file,  'r')
	except:
		DP.update(0, '[COLOR %s]Không đọc được file Zip.' % COLOR2, 'Đang copy vào thư mục Packages')
		pack = os.path.join('special://home', 'addons', 'packages', fn)
		xbmcvfs.copy(file, pack)
		file = xbmc.translatePath(pack)
		DP.update(0, '', 'Copy file vào Packages: Hoàn thành')
		zipfile.ZipFile(file, 'r')
	percent, errors, error = extract.all(file,loc,DP)
	#fixmetas()
	#clearS('build')
	DP.close()
	#defaultSkin()
	#lookandFeelData('save')
	if not file.find('packages') == -1:
		try: os.remove(file)
		except: pass
	dialog.ok(ADDONTITLE, "Khôi phục xong, nhấn OK và thưởng thức ^^")
			
def wizard(name,url,description):
    ################## New code ###################################
	wiz.clearS('build')
	zipname = name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
	if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
	DP.create(ADDONTITLE,'[B]Đang Tải:[/B] %s' % (name),'', 'Chờ Chút Nhé...')
	lib=os.path.join(PACKAGES, '%s.zip' % zipname)
	try: os.remove(lib)
	except: pass
	downloader.download(url, lib, DP)
	xbmc.sleep(500)
	title = '[B]Đang cài đặt:[/B] %s' % (name)
	DP.update(0, title,'', 'Chờ Chút Nhé...')
	percent, errors, error = extract.all(lib,HOME,DP, title=title)
	if int(float(percent)) > 0:
		wiz.setS('buildname', name)
		#wiz.setS('buildversion', wiz.checkBuild( name,'version'))
		#wiz.setS('buildtheme', '')
		# wiz.setS('latestversion', wiz.checkBuild( name,'version'))
		# wiz.setS('lastbuildcheck', str(NEXTCHECK))
		wiz.setS('installed', 'true')
		# wiz.setS('extract', str(percent))
		# wiz.setS('errors', str(errors))
		wiz.log('INSTALLED %s: [ERRORS:%s]' % (percent, errors))
		try: os.remove(lib)
		except: pass
		if int(float(errors)) > 0:
			yes=dialog.yesno(ADDONTITLE, '[COLOR %s][COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name), 'Đã hoàn thành: [COLOR %s]%s%s[/COLOR] [Lỗi:[COLOR %s]%s[/COLOR]]' % (COLOR1, percent, '%', COLOR1, errors), 'Bạn có muốn xem thống kê lỗi?[/COLOR]', nolabel='[B][COLOR red]Không cần[/COLOR][/B]',yeslabel='[B][COLOR green]Xem ngay[/COLOR][/B]')
			if yes:
				if isinstance(errors, unicode):
					error = error.encode('utf-8')
				wiz.TextBox(ADDONTITLE, error)
	DP.close()
	
def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'


def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name).decode("utf-8")+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir1(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name).decode("utf-8")+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

def addDir2(name,url,mode,iconimage,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name).decode("utf-8")+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
        if mode==17 or mode==16:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
		
def addItem(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name).decode("utf-8")+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

#######################################################################
#						Delete All Cache
#######################################################################
def setupCacheEntries():
    entries = 5 #make sure this refelcts the amount of entries you have
    dialogName = ["WTF", "4oD", "BBC iPlayer", "Simple Downloader", "ITV"]
    pathName = ["special://profile/addon_data/plugin.video.whatthefurk/cache", "special://profile/addon_data/plugin.video.4od/cache",
					"special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache","special://profile/addon_data/script.module.simple.downloader",
                    "special://profile/addon_data/plugin.video.itv/Images"]
                    
    cacheEntries = []
    
    for x in range(entries):
        cacheEntries.append(cacheEntry(dialogName[x],pathName[x]))
    
    return cacheEntries


def clearCache():
    global analytics
    analytics.sendEvent("HieuIT Wizard", "Clear Cache")
    
    if os.path.exists(cachePath)==True:    
        for root, dirs, files in os.walk(cachePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:

                #dialog = xbmcgui.Dialog()
                #if dialog.yesno("Delete XBMC Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        try:
                            if (f == "xbmc.log" or f == "xbmc.old.log"): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if os.path.exists(tempPath)==True:    
        for root, dirs, files in os.walk(tempPath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                #dialog = xbmcgui.Dialog()
                #if dialog.yesno("Delete XBMC Temp Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        try:
                            if (f == "xbmc.log" or f == "xbmc.old.log"): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
        
        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                #dialog = xbmcgui.Dialog()
                #if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'Other'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
        
        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                #dialog = xbmcgui.Dialog()
                #if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'LocalAndRental'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass    
                
    cacheEntries = setupCacheEntries()
                                         
    for entry in cacheEntries:
        clear_cache_path = xbmc.translatePath(entry.path)
        if os.path.exists(clear_cache_path)==True:    
            for root, dirs, files in os.walk(clear_cache_path):
                file_count = 0
                file_count += len(files)
                if file_count > 0:

                    #dialog = xbmcgui.Dialog()
                    #if dialog.yesno("Raw Manager",str(file_count) + "%s cache files found"%(entry.name), "Do you want to delete them?"):
                        for f in files:
                            os.unlink(os.path.join(root, f))
                        for d in dirs:
                            shutil.rmtree(os.path.join(root, d))
                            
                else:
                    pass
                

    dialog = xbmcgui.Dialog()
    #dialog.ok("HieuIT Wizard", "Done Clearing Cache files")
    
    
def deleteThumbnails():
    global analytics
    analytics.sendEvent("HieuIT Wizard", "Delete thumb")
    
    if os.path.exists(thumbnailPath)==True:  
            dialog = xbmcgui.Dialog()
            if dialog.yesno("Delete Thumbnails", "This option deletes all thumbnails", "Are you sure you want to do this?"):
                for root, dirs, files in os.walk(thumbnailPath):
                    file_count = 0
                    file_count += len(files)
                    if file_count > 0:                
                        for f in files:
                            try:
                                os.unlink(os.path.join(root, f))
                            except:
                                pass                
    else:
        pass
    
    text13 = os.path.join(databasePath,"Textures13.db")
    os.unlink(text13)
        
    dialog.ok("Restart XBMC", "Please restart XBMC to rebuild thumbnail library")
        
def purgePackages():
    global analytics
    analytics.sendEvent("HieuIT Wizard", "Del package")
    
    purgePath = xbmc.translatePath('special://home/addons/packages')
    dialog = xbmcgui.Dialog()
    for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
    #if dialog.yesno("Delete Package Cache Files", "%d packages found."%file_count, "Delete Them?"):  
        #for root, dirs, files in os.walk(purgePath):
            #file_count = 0
            #file_count += len(files)
            if file_count > 0:            
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
                dialog = xbmcgui.Dialog()
                dialog.ok("HieuIT Wizard", "Deleting Packages all done")
            else:
                dialog = xbmcgui.Dialog()
                dialog.ok("HieuIT Wizard", "No Packages to Purge")       
				

def restoreggdrive():
    global analytics
    analytics.sendEvent("HieuIT Wizard", "restore ggdrive")
    y = dialog.yesno("[COLOR red][B]CẢNH BÁO !!![/COLOR][/B]", "Tất cả [COLOR yellow]Account đã thêm vào Google Drive[/COLOR] sẽ bị ghi đè.", "Bạn có muốn tiếp tục?") 
    if y == 0:   
        pass
    else:
        wizard("dataggdrive",'https://dl.dropboxusercontent.com/s/nofqcb6rd9l7v6i/data_ggdrive.zip',description)
        wiz.clearS('build')
        wiz.refresh()
        dialog.ok("Done!", "Khôi phục xong, nhấn OK và thưởng thức ^^")
        xbmc.executebuiltin('RunAddon(plugin.googledrive)')		

def restoregdrive():
    global analytics
    analytics.sendEvent("HieuIT Wizard", "restore gdrive")
    y = dialog.yesno("[COLOR red][B]CẢNH BÁO !!![/COLOR][/B]", "Tất cả [COLOR yellow]Account đã thêm vào GDrive[/COLOR] sẽ bị ghi đè.", "Bạn có muốn tiếp tục?") 
    if y == 0:   
        pass
    else:
        wizard("dataggdrive",'https://dl.dropboxusercontent.com/s/82w2elvg2t2kood/data_gdrive.zip',description)
        wiz.clearS('build')
        wiz.refresh()
        dialog.ok("Done!", "Khôi phục xong, nhấn OK và thưởng thức ^^")
        xbmc.executebuiltin('RunAddon(plugin.video.gdrive)')

def speedMenu():
    global analytics
    analytics.sendEvent("HieuIT Wizard", "Speedtest")
    xbmc.executebuiltin('Runscript("special://home/addons/plugin.program.hieuitwizard/speedtest.py")')
	
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
setupAnalytics()        
                      
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


# def setView(content, viewType):
    # set content type so library shows more views and info
    # if content:
        # xbmcplugin.setContent(int(sys.argv[1]), content)
    # if ADDON.getSetting('auto-view')=='true':
        # xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
		
def setView(content, viewType):
	if wiz.getS('auto-view')=='false':
		views = wiz.getS(viewType)
		if views == '50' and KODIV >= 17 and SKIN == 'skin.estuary': views = '55'
		if views == '51' and KODIV >= 17 and SKIN == 'skin.estuary': views = '50'
		wiz.ebi("Container.SetViewMode(%s)" %  views)
 
        
if mode==None or url==None or len(url)<1:
        MAIN()
       
elif mode==1:
        global analytics
        analytics.sendEvent("HieuIT Wizard", "BuildWizard")
        buildWizard()
        
elif mode==2:
        global analytics
        analytics.sendEvent("HieuIT Wizard", "Set memcache")
        wizard(name,url,description)
        dialog.ok("DONE!", 'Đã cài đặt xong. Khởi động lại Kodi để kiểm tra.')	
        wiz.clearS('build')
        wiz.killxbmc(True)		

elif mode==201:
        wizard(name,url,description)
        dialog.ok("DONE!", 'Đã cài đặt xong. Khởi động lại Kodi để kiểm tra.')	
        wiz.clearS('build')
        wiz.killxbmc(True)        
		
elif mode==3:
        Tweak()
		
elif mode==301:
        viewxml(name)
		
elif mode==302:
        removexmlfile(name)
		
elif mode==4:
        utilities()
		
elif mode==5:
        clearCache()
        dialog.ok("HieuIT Wizard", "Done Clearing Cache files")		
        
elif mode==6:
        deleteThumbnails()
        
elif mode==7:
        purgePackages()
        
elif mode==8:
        clearCache()
        dialog.ok("HieuIT Wizard", "Done Clearing Cache files")	
        purgePackages()
        deleteThumbnails()
        	

elif mode==9:
	xbmcaddon.Addon(id='plugin.program.hieuitwizard').openSettings()
	MAIN()
    	
elif mode==10:
        #restoredata()
		RESTOREDATAFILE()
        	
elif mode ==101:
		restorefile()
		
elif mode==11:
        restorelibrary()       		

elif mode==12:
        #restoregdrive()
        global analytics
        analytics.sendEvent("HieuIT Wizard", "HieuIT Playlist")		
        xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.thongld.vnplaylist/section/0@1l6TcaMsEINocqUPyLF0mhSBUW5y36tDwVDXpXImx4eY/%5BCOLOR+yellow%5DMovies+%28by+HieuIT%29%5B%2FCOLOR%5D,return)')

elif mode==121:
        #restoregdrive()
        global analytics
        analytics.sendEvent("HieuIT Wizard", "HieuIT FREE")		
        xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.thongld.vnplaylist/section/0@1dqRmuJgGP_6SE5v8nStJujeEW63xGUDRt3C_sQ5Pdg4/%5BCOLOR+yellow%5DMovies+%28by+HieuIT%29%5B%2FCOLOR%5D,return)')
		
elif mode==122:
        restoregdrive()		

elif mode==13:
        restoreggdrive()
		
elif mode==14:
        INSTALLKODI()

elif mode==15:
    BACKUP_RESTORE()

elif mode==16:
        BACKUP_OPTION()

elif mode==17:
        RESTORE_OPTION()	

elif mode==18:
		global analytics
		analytics.sendEvent("HieuIT Wizard", "Full Backup")
		wiz.backUpOptions('build')

elif mode==19:
        RESTORE_ZIP_FILE(name,url)		
		
elif mode==20:
        RESTORE_BACKUP_XML(name,url,description)
		
elif mode==21:
        #RESTORE()
		restoreit('build')
        #wiz.restoreLocal(type)

elif mode==211:
        #RESTORE()
		wiz.restoreLocal('addondata')
		
elif mode==191      : wiz.backUpOptions('guifix')
		
elif mode==22:
        UPDATE()

elif mode==23:
       speedMenu()
	  
elif mode==24:
       freshStart()
	   
elif mode ==25:
		datafile()

elif mode ==26:
        #global analytics
        analytics.sendEvent("HieuIT Wizard", "InputStream")
        inputvideo()
		
elif mode ==27:
		inputurl()
		wiz.refresh()

elif mode ==271:
		dataurl()
		wiz.refresh()
		
elif mode ==28:
		wiz.clearS('build')
		wiz.refresh()

elif mode ==281:
		wiz.clearS('data')
		wiz.refresh()

elif mode ==29:
		f = open(CHANGELOG,mode='r'); msg = f.read(); f.close()
		wiz.TextBox(ADDONTITLE, msg)

elif mode==997:
        #dialog.ok(ADDONTITLE, 'Thay đổi Data URL trong tab [COLOR yellow]Custom Link[/COLOR]', 'Nhấn [B]OK[/B] để bắt đầu')
        #wiz.openS('Build Link')
        dataurl()
        wiz.refresh()
	   
elif mode==998:
        dialog.ok(ADDONTITLE, 'Thay đổi Build URL trong tab [COLOR yellow]Build Link[/COLOR]', 'Nhấn [B]OK[/B] để bắt đầu')
        #wiz.openS('Build Link')
        inputurl()
        wiz.refresh()
		
elif mode==999:
        dialog.ok(ADDONTITLE, 'Thay đổi thư mục Backup mặc định trong tab [COLOR yellow]Zip Folder[/COLOR]', 'Nhấn [B]OK[/B] để bắt đầu')
        backupdir = dialog.browse(0, '[COLOR %s]Chọn đường dẫn lưu file Backup[/COLOR]' % COLOR2, '', '', False, False)
        wiz.setS('zipdir',backupdir)
        wiz.refresh()
		#viewBuild(name)
		
xbmcplugin.endOfDirectory(int(sys.argv[1]))

