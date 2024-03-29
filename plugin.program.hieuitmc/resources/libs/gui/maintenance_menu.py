################################################################################
#      Copyright (C) 2019 drinfernoo                                           #
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

import xbmc
import xbmcgui

import os

from resources.libs.common import directory
from resources.libs.common import logging
from resources.libs.common import tools
from resources.libs.common.config import CONFIG
from resources.libs.gui.main_menu import MainMenu


class MaintenanceMenu:

    def get_listing(self):
        directory.add_file('[COLOR yellow][B]Speedtest[/B][/COLOR] - Kiểm Tra Tốc Độ Mạng', {'mode': 'runspeedtest'}, icon=CONFIG.ICONSPEED, themeit=CONFIG.THEME3)
        directory.add_file('Thiết lập xem Youtube 4K/1080p', {'mode': 'runspeedtest'}, icon=CONFIG.ICONYOUTUBE, themeit=CONFIG.THEME3)
        directory.add_dir('[COLOR red][B]Cleaning Tools[/B][/COLOR] - Dọn dẹp hệ thống', {'mode': 'maint', 'name': 'clean'}, icon=CONFIG.ICONRCLEAR, themeit=CONFIG.THEME1)
        # directory.add_dir('[B]Addon Tools[/B]', {'mode': 'maint', 'name': 'addon'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        directory.add_dir('[COLOR yellow][B]Logging Tools[/B][/COLOR] - Xem báo cáo lỗi KODI', {'mode': 'maint', 'name': 'logging'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        directory.add_file('[COLOR red][B]Refresh KODI[/B][/COLOR] - Khôi phục Kodi về mặc định (giữ nguyên Repository)', {'mode': 'freshstart'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_dir('[B]Misc Maintenance[/B]', {'mode': 'maint', 'name': 'misc'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        # directory.add_dir('[B]Back up/Restore[/B]', {'mode': 'maint', 'name': 'backup'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        # directory.add_dir('[B]System Tweaks/Fixes[/B]', {'mode': 'maint', 'name': 'tweaks'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        directory.add_dir('[COLOR {0}][B]SysInfo[/B][/COLOR] - Xem thông tin hệ thống'.format(CONFIG.COLOR1), {'mode': 'systeminfo'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

    def clean_menu(self):
        from resources.libs import clear
        from resources.libs.common import tools

        on = '[B][COLOR springgreen]ON[/COLOR][/B]'
        off = '[B][COLOR red]OFF[/COLOR][/B]'

        autoclean = 'true' if CONFIG.AUTOCLEANUP == 'true' else 'false'
        cache = 'true' if CONFIG.AUTOCACHE == 'true' else 'false'
        packages = 'true' if CONFIG.AUTOPACKAGES == 'true' else 'false'
        thumbs = 'true' if CONFIG.AUTOTHUMBS == 'true' else 'false'
        # includevid = 'true' if CONFIG.INCLUDEVIDEO == 'true' else 'false'
        # includeall = 'true' if CONFIG.INCLUDEALL == 'true' else 'false'

        sizepack = tools.get_size(CONFIG.PACKAGES)
        sizethumb = tools.get_size(CONFIG.THUMBNAILS)
        archive = tools.get_size(CONFIG.ARCHIVE_CACHE)
        sizecache = (clear.get_cache_size()) - archive
        totalsize = sizepack + sizethumb + sizecache

        directory.add_file(
            'Total Clean Up: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(tools.convert_size(totalsize)), {'mode': 'fullclean'},
            icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Clear Cache: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(tools.convert_size(sizecache)),
                           {'mode': 'clearcache'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        if xbmc.getCondVisibility('System.HasAddon(script.module.urlresolver)') or xbmc.getCondVisibility(
                'System.HasAddon(script.module.resolveurl)'):
            directory.add_file('Clear Resolver Function Caches', {'mode': 'clearfunctioncache'}, icon=CONFIG.ICONMAINT,
                               themeit=CONFIG.THEME3)
        directory.add_file('Clear Packages: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(tools.convert_size(sizepack)),
                           {'mode': 'clearpackages'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file(
            'Clear Thumbnails: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(tools.convert_size(sizethumb)),
            {'mode': 'clearthumb'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        if os.path.exists(CONFIG.ARCHIVE_CACHE):
            directory.add_file('Clear Archive_Cache: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(
                tools.convert_size(archive)), {'mode': 'cleararchive'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Clear Old Thumbnails', {'mode': 'oldThumbs'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Clear Crash Logs', {'mode': 'clearcrash'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Purge Databases', {'mode': 'purgedb'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('Fresh Start', {'mode': 'freshstart'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        # directory.add_file('Auto Clean', fanart=CONFIG.ADDON_FANART, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        # directory.add_file('Auto Clean Up On Startup: {0}'.format(autoclean.replace('true', on).replace('false', off)),
                           # {'mode': 'togglesetting', 'name': 'autoclean'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # if autoclean == 'true':
            # directory.add_file(
                # '--- Auto Clean Frequency: [B][COLOR springgreen]{0}[/COLOR][/B]'.format(
                    # CONFIG.CLEANFREQ[CONFIG.AUTOFREQ]),
                # {'mode': 'changefreq'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # directory.add_file(
                # '--- Clear Cache on Startup: {0}'.format(cache.replace('true', on).replace('false', off)),
                # {'mode': 'togglesetting', 'name': 'clearcache'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # directory.add_file(
                # '--- Clear Packages on Startup: {0}'.format(packages.replace('true', on).replace('false', off)),
                # {'mode': 'togglesetting', 'name': 'clearpackages'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # directory.add_file(
                # '--- Clear Old Thumbs on Startup: {0}'.format(thumbs.replace('true', on).replace('false', off)),
                # {'mode': 'togglesetting', 'name': 'clearthumbs'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('Clear Video Cache', fanart=CONFIG.ADDON_FANART, icon=CONFIG.ICONMAINT,
                           # themeit=CONFIG.THEME1)
        # directory.add_file(
            # '  |---Include Video Cache in Clear Cache: {0}'.format(includevid.replace('true', on).replace('false', off)),
            # {'mode': 'togglecache', 'name': 'includevideo'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

        # if includeall == 'true':
            # includegaia = 'true'
            # includeexodusredux = 'true'
            # includethecrew = 'true'
            # includeyoda = 'true'
            # includevenom = 'true'
            # includenumbers = 'true'
            # includescrubs = 'true'
            # includeseren = 'true'
        # else:
            # includeexodusredux = 'true' if CONFIG.INCLUDEEXODUSREDUX == 'true' else 'false'
            # includegaia = 'true' if CONFIG.INCLUDEGAIA == 'true' else 'false'
            # includethecrew = 'true' if CONFIG.INCLUDETHECREW == 'true' else 'false'
            # includeyoda = 'true' if CONFIG.INCLUDEYODA == 'true' else 'false'
            # includevenom = 'true' if CONFIG.INCLUDEVENOM == 'true' else 'false'
            # includenumbers = 'true' if CONFIG.INCLUDENUMBERS == 'true' else 'false'
            # includescrubs = 'true' if CONFIG.INCLUDESCRUBS == 'true' else 'false'
            # includeseren = 'true' if CONFIG.INCLUDESEREN == 'true' else 'false'

        # if includevid == 'true':
            # directory.add_file(
                # '--- Include All Video Addons: {0}'.format(includeall.replace('true', on).replace('false', off)),
                # {'mode': 'togglecache', 'name': 'includeall'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # if xbmc.getCondVisibility('System.HasAddon(plugin.video.exodusredux)'):
                # directory.add_file(
                    # '--- Include Exodus Redux: {0}'.format(
                        # includeexodusredux.replace('true', on).replace('false', off)),
                    # {'mode': 'togglecache', 'name': 'includeexodusredux'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # if xbmc.getCondVisibility('System.HasAddon(plugin.video.gaia)'):
                # directory.add_file(
                    # '--- Include Gaia: {0}'.format(includegaia.replace('true', on).replace('false', off)),
                    # {'mode': 'togglecache', 'name': 'includegaia'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # if xbmc.getCondVisibility('System.HasAddon(plugin.video.numbersbynumbers)'):
                # directory.add_file(
                    # '--- Include NuMb3r5: {0}'.format(includenumbers.replace('true', on).replace('false', off)),
                    # {'mode': 'togglecache', 'name': 'includenumbers'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # if xbmc.getCondVisibility('System.HasAddon(plugin.video.scrubsv2)'):
                # directory.add_file(
                    # '--- Include Scrubs v2: {0}'.format(includescrubs.replace('true', on).replace('false', off)),
                    # {'mode': 'togglecache', 'name': 'includescrubs'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # if xbmc.getCondVisibility('System.HasAddon(plugin.video.seren)'):
                # directory.add_file(
                    # '--- Include Seren: {0}'.format(includeseren.replace('true', on).replace('false', off)),
                    # {'mode': 'togglecache', 'name': 'includeseren'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # if xbmc.getCondVisibility('System.HasAddon(plugin.video.thecrew)'):
                # directory.add_file(
                    # '--- Include THE CREW: {0}'.format(includethecrew.replace('true', on).replace('false', off)),
                    # {'mode': 'togglecache', 'name': 'includethecrew'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # if xbmc.getCondVisibility('System.HasAddon(plugin.video.venom)'):
                # directory.add_file(
                    # '--- Include Venom: {0}'.format(includevenom.replace('true', on).replace('false', off)),
                    # {'mode': 'togglecache', 'name': 'includevenom'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # if xbmc.getCondVisibility('System.HasAddon(plugin.video.yoda)'):
                # directory.add_file(
                    # '--- Include Yoda: {0}'.format(includeyoda.replace('true', on).replace('false', off)),
                    # {'mode': 'togglecache', 'name': 'includeyoda'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
            # directory.add_file('--- Enable All Video Addons', {'mode': 'togglecache', 'name': 'true'}, icon=CONFIG.ICONMAINT,
                               # themeit=CONFIG.THEME3)
            # directory.add_file('--- Disable All Video Addons', {'mode': 'togglecache', 'name': 'false'}, icon=CONFIG.ICONMAINT,
                               # themeit=CONFIG.THEME3)

    def addon_menu(self):
        directory.add_file('Remove Addons', {'mode': 'removeaddons'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_dir('Remove Addon Data', {'mode': 'removeaddondata'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_dir('Enable/Disable Addons', {'mode': 'enableaddons'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('Enable/Disable Adult Addons', 'toggleadult', icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Force Refresh all Repositories', {'mode': 'forceupdate'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Force Update all Addons', {'mode': 'forceupdate', 'action': 'auto'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

   
    def logging_menu(self):
        errors = int(logging.error_checking(count=True))
        errorsfound = str(errors) + ' Error(s) Found' if errors > 0 else 'None Found'
        wizlogsize = ': [COLOR red]Not Found[/COLOR]' if not os.path.exists(
            CONFIG.WIZLOG) else ": [COLOR springgreen]{0}[/COLOR]".format(
            tools.convert_size(os.path.getsize(CONFIG.WIZLOG)))
            
        directory.add_file('Toggle Debug Logging', {'mode': 'enabledebug'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Upload Log File', {'mode': 'uploadlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('View Errors in Log: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(errorsfound), {'mode': 'viewerrorlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        if errors > 0:
            directory.add_file('View Last Error In Log', {'mode': 'viewerrorlast'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('View Log File', {'mode': 'viewlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('View Wizard Log File', {'mode': 'viewwizlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('Clear Wizard Log File: [COLOR springgreen][B]{0}[/B][/COLOR]'.format(wizlogsize), {'mode': 'clearwizlog'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
   
        
    def misc_menu(self):
        directory.add_file('Kodi 17 Fix.....', {'mode': 'kodi17fix'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_dir('Network Tools', {'mode': 'nettools'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Toggle Unknown Sources', {'mode': 'unknownsources'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Toggle Addon Updates', {'mode': 'toggleupdates'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Reload Skin', {'mode': 'forceskin'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Reload Profile', {'mode': 'forceprofile'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Force Close Kodi', {'mode': 'forceclose'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

    def backuprestore_menu(self):
        backuppath = CONFIG.get_setting('path')
        dialog = xbmcgui.Dialog()
        if backuppath=='':
            if dialog.ok(CONFIG.ADDONTITLE,'Bạn chưa thiết lập đường dẫn lưu file Backup cho Kodi \n Mở Addon Setting và Chọn tab [COLOR green][B]Zip Folder[/B][/COLOR].\n Nhấn [B]OK[/B] để bắt đầu thiết lập'):
                backupdir = dialog.browse(0, '[COLOR yellow]Chọn đường dẫn lưu file Backup[/COLOR]', '', '', False, False)
                CONFIG.set_setting('path', backupdir)
                xbmc.executebuiltin('Container.Refresh()')
                self.backuprestore_menu()
            else: MainMenu().get_listing()
            # xbmc.executebuiltin('Container.Refresh()')
        else:
           directory.add_file('[COLOR {0}][B]Backup Location:[/B][/COLOR] {1}'.format(CONFIG.COLOR1, backuppath), {'mode': 'settings', 'name': 'Maintenance'}, icon=CONFIG.ICONDIR, themeit=CONFIG.THEME3)
           directory.add_file('[COLOR {0}][B]Clean Backup:[/B][/COLOR] Dọn dẹp thư mục Backup'.format(CONFIG.COLOR1), {'mode': 'clearbackup'}, icon=CONFIG.ICONDELPACK, themeit=CONFIG.THEME3)
           directory.add_file('[COLOR red][B]Refresh KODI[/B][/COLOR] - Khôi phục Kodi về mặc định (giữ nguyên Repository)', {'mode': 'freshstart'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
           directory.add_separator()
           directory.add_dir('[COLOR green][B]BACKUP:[/B][/COLOR] Sao lưu Kodi', {'mode': 'maint', 'name': 'backup'}, icon=CONFIG.ICONBACKUP, themeit=CONFIG.THEME1)
           directory.add_dir('[COLOR yellow][B]RESTORE:[/B][/COLOR] Khôi phục Kodi', {'mode': 'maint', 'name': 'restore'}, icon=CONFIG.ICONRESTORE, themeit=CONFIG.THEME1)

    def backup_menu(self):
        directory.add_file('[COLOR {0}][B]Full Backup:[/B][/COLOR] Sao lưu toàn bộ KODI'.format(CONFIG.COLOR1), {'mode': 'backup', 'action': 'build'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[COLOR {0}][B]Backup Addondata:[/B][/COLOR] Sao lưu toàn bộ data của Addon'.format(CONFIG.COLOR1), {'mode': 'backup', 'action': 'addondata'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Back Up]: GuiFix', {'mode': 'backup', 'action': 'gui'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Back Up]: Theme', {'mode': 'backup', 'action': 'theme'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Back Up]: Addon Pack', {'mode': 'backup', 'action': 'addonpack'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

    def restore_menu(self):
        directory.add_file('[COLOR {0}][B]Full Restore:[/B][/COLOR] Khôi Phục Toàn Bộ KODI Từ File Đã Backup'.format(CONFIG.COLOR1), {'mode': 'restore', 'action': 'build'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('[COLOR {0}][B]Restore Addondata:[/B][/COLOR] Khôi Phục Toàn Bộ Data Addon'.format(CONFIG.COLOR1), {'mode': 'restore', 'action': 'addondata'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Restore]: Local Addon Pack', {'mode': 'restore', 'action': 'addonpack'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Restore]: Local GuiFix', {'mode': 'restore', 'action': 'gui'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Restore]: Local Theme', {'mode': 'restore', 'action': 'theme'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Restore]: External Build', {'mode': 'restore', 'action': 'build', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Restore]: External GuiFix', {'mode': 'restore', 'action': 'gui', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Restore]: External Theme', {'mode': 'restore', 'action': 'theme', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Restore]: External Addon Pack', {'mode': 'restore', 'action': 'addonpack', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('[Restore]: External Addon_data', {'mode': 'restore', 'action': 'addondata', 'name': 'external'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

    def tweaks_menu(self):
        directory.add_dir('Advanced Settings', {'mode': 'advanced_settings'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Scan Sources for broken links', {'mode': 'checksources'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_file('Scan For Broken Repositories', {'mode': 'checkrepos'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        #directory.add_file('Remove Non-Ascii filenames', {'mode': 'asciicheck'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        # directory.add_file('Toggle Passwords On Keyboard Entry', {'mode': 'togglepasswords'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        #directory.add_file('Convert Paths to special', {'mode': 'convertpath'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
        directory.add_dir('System Information', {'mode': 'systeminfo'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

    def ce_menu(self):
        directory.add_dir('System Information', {'mode': 'systeminfo'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)