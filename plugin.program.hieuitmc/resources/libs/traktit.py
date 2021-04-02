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
import time

from xml.etree import ElementTree

from resources.libs.common.config import CONFIG
from resources.libs.common import logging
from resources.libs.common import tools

ORDER = ['tmdbh', 'shadow', 'seren', 'myaccounts', 'openmeta', 'numbers', 'thecrew', 'trakt', 'marauder', 'asgard', 'scrubs', 'goto', 'realizer', 'premiumizer']  
         

TRAKTID = {
    'myaccounts': {
        'name'     : '[B]***My Accounts Trakt For FEN And Venom***[/B]',
        'plugin'   : 'script.module.myaccounts',
        'saved'    : 'myaccounts',
        'path'     : os.path.join(CONFIG.ADDONS, 'script.module.myaccounts'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'script.module.myaccounts', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'script.module.myaccounts', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'myaccounts_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'script.module.myaccounts', 'settings.xml'),
        'default'  : 'trakt.username',
        'data'     : ['trakt.expires', 'trakt.refresh', 'trakt.token', 'trakt.username'],
        'activate' : 'RunScript(script.module.myaccounts, action=traktAuth)'},
		
    'shadow': {
        'name'     : '[B]***Shadow Trakt***[/B]',
        'plugin'   : 'plugin.video.shadow',
        'saved'    : 'shadow',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.shadow'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.shadow', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.shadow', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'shadow_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.shadow', 'settings.xml'),
        'default'  : 'trakt_expires_at',
        'data'     : ['trakt_expires_at', 'trakt_refresh_token', 'trakt_access_token'],
        'activate' : 'RunPlugin(plugin://plugin.video.shadow?mode=157&url=False)'},	
		
    'seren': {
        'name'     : '[B]***Seren Trakt***[/B]',
        'plugin'   : 'plugin.video.seren',
        'saved'    : 'seren',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.seren'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.seren', 'ico-fox-gold-final.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.seren', 'fanart-fox-gold-final.png'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'seren_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.seren', 'settings.xml'),
        'default'  : 'trakt.username',
        'data'     : ['trakt.auth', 'trakt.refresh', 'trakt.expires', 'trakt.username'],
        'activate' : 'RunPlugin(plugin://plugin.video.seren/?action=authTrakt)'},	

    'tmdbh': {
        'name'     : '[B]***TMDBH Trakt (Home Screen Widgets)***[/B]',
        'plugin'   : 'plugin.video.themoviedb.helper',
        'saved'    : 'tmdbh',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.themoviedb.helper'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.themoviedb.helper', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.themoviedb.helper', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'tmdbh_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.themoviedb.helper', 'settings.xml'),
        'default'  : 'trakt_token',
        'data'     : ['trakt_token'],
        'activate' : 'RunScript(plugin.video.themoviedb.helper,authenticate_trakt)'},	
		
    'openmeta': {
        'name'     : '[B]***OpenMeta (Portal) Trakt***[/B]',
        'plugin'   : 'plugin.video.openmeta',
        'saved'    : 'openmeta',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.openmeta'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.openmeta', 'resources/icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.openmeta', 'resources/fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'openmeta_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.openmeta', 'settings.xml'),
        'default'  : 'trakt_access_token',
        'data'     : ['trakt_access_token', 'trakt_api_client_id', 'trakt_api_client_secret', 'trakt_expires_at', 'trakt_refresh_token'],
        'activate' : 'RunPlugin(plugin://plugin.video.openmeta/authenticate_trakt)'},				
		
    'numbers': {
        'name'     : '[B]***Numbers Trakt***[/B]',
        'plugin'   : 'plugin.video.numbersbynumbers',
        'saved'    : 'numbers',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.numbersbynumbers'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.numbersbynumbers', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.numbersbynumbers', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'numbers_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.numbersbynumbers', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.client_id', 'trakt.client_secret', 'trakt.refresh', 'trakt.token', 'trakt.user'],
        'activate' : 'RunPlugin(plugin://plugin.video.numbersbynumbers/?action=authTrakt)'},
		
    'thecrew': {
        'name'     : '[B]***The Crew Trakt***[/B]',
        'plugin'   : 'plugin.video.thecrew',
        'saved'    : 'thecrew',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.thecrew'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.thecrew', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.thecrew', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'thecrew_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.thecrew', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.auth', 'trakt.refresh', 'trakt.token', 'trakt.user'],
        'activate' : 'RunPlugin(plugin://plugin.video.thecrew/?action=authTrakt)'},			
		
    'trakt': {
        'name'     : '[B]***Kodi Trakt***[/B]',
        'plugin'   : 'script.trakt',
        'saved'    : 'trakt',
        'path'     : os.path.join(CONFIG.ADDONS, 'script.trakt'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'script.trakt', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'script.trakt', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'trakt_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'script.trakt', 'settings.xml'),
        'default'  : 'user',
        'data'     : ['Auth_Info', 'authorization', 'user'],
        'activate' : 'RunScript(script.trakt, action=auth_info)'},
		
    'marauder': {
        'name'     : '[B]***Marauder Trakt***[/B]',
        'plugin'   : 'plugin.video.marauder',
        'saved'    : 'marauder',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.marauder'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.marauder', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.marauder', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'marauder_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.marauder', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.authed', 'trakt.client_id', 'trakt.client_secret', 'trakt.refresh', 'trakt.token', 'trakt.user'],
        'activate' : 'RunPlugin(plugin://plugin.video.marauder/?action=authTrakt)'},		
		
    'asgard': {
        'name'     : '[B]***Asgard Trakt***[/B]',
        'plugin'   : 'plugin.video.asgard',
        'saved'    : 'asgard',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.asgard'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.asgard', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.asgard', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'asgard_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.asgard', 'settings.xml'),
        'default'  : 'TRAKT_EXPIRES_AT',
        'data'     : ['TRAKT_EXPIRES_AT', 'TRAKT_ACCESS_TOKEN', 'trakt_api_client_id', 'TRAKT_REFRESH_TOKEN', 'trakt_api_client_secret'],
        'activate' : 'RunPlugin(plugin://plugin.video.asgard/?description=No%20information%20available&amp;fanart=C%3a%5cUsers%5cJay%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.asgard%5cfanart.jpg&amp;iconimage=C%3a%5cUsers%5cJay%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.asgard%5cicon.png&amp;mode=trakt&amp;name=%5bCOLOR%20FFffffffff%5d%5bCOLOR%20goldenrod%5dPair%20TRAKT%5b%2fCOLOR%5d%5b%2fCOLOR%5d&amp;url=https%3a%2f%2fapi.trakt.tv%2fusers%2fme%2flists%2f&quot;,return)'},
		
    'goto': {
        'name'     : '[B]***C GOTO Trakt***[/B]',
        'plugin'   : 'plugin.video.goto',
        'saved'    : 'goto',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.goto'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.goto', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.goto', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'goto_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.goto', 'settings.xml'),
        'default'  : 'TRAKT_EXPIRES_AT',
        'data'     : ['TRAKT_EXPIRES_AT', 'TRAKT_ACCESS_TOKEN', 'trakt_api_client_id', 'TRAKT_REFRESH_TOKEN', 'trakt_api_client_secret'],
        'activate' : 'RunPlugin(plugin://plugin.video.goto/?description=No%20information%20available&amp;fanart=C%3a%5cUsers%5cJay%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.goto%5cfanart.jpg&amp;iconimage=C%3a%5cUsers%5cJay%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.goto%5cicon.png&amp;mode=trakt&amp;name=%5bCOLOR%20FFffffffff%5d%5bCOLORwhite%5dAUTHORIZE%20TRAKT%5b%2fCOLOR%5d%5b%2fCOLOR%5d&amp;url=https%3a%2f%2fapi.trakt.tv%2fusers%2fme%2flists%2f&quot;,return)'},		

    'scrubs': {
        'name'     : '[B]***Scrubs Trakt***[/B]',
        'plugin'   : 'plugin.video.scrubsv2',
        'saved'    : 'scrubs',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.scrubsv2'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.scrubsv2', 'icon.jpg'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.scrubsv2', 'fanart.png'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'scrubs_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.scrubsv2', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.user', 'trakt.user2', 'trakt.token', 'trakt.refresh', 'trakt.auth'],
        'activate' : 'RunPlugin(plugin://plugin.video.scrubsv2/?action=authTrakt)'},

    'premiumizer': {
        'name'     : '[B]***Premiumizer Trakt***[/B]',
        'plugin'   : 'plugin.video.premiumizer',
        'saved'    : 'premiumizer',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.premiumizer'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.premiumizer', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.premiumizer', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'premiumizer_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.premiumizer', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.token', 'trakt.refresh', 'trakt.user'],
        'activate' : 'RunPlugin(plugin://plugin.video.premiumizer/?action=authTrakt)'},
		
    'realizer': {
        'name'     : '[B]***Realizer Trakt***[/B]',
        'plugin'   : 'plugin.video.realizer',
        'saved'    : 'realizer',
        'path'     : os.path.join(CONFIG.ADDONS, 'plugin.video.realizer'),
        'icon'     : os.path.join(CONFIG.ADDONS, 'plugin.video.realizer', 'icon.png'),
        'fanart'   : os.path.join(CONFIG.ADDONS, 'plugin.video.realizer', 'fanart.jpg'),
        'file'     : os.path.join(CONFIG.TRAKTFOLD, 'realizer_trakt'),
        'settings' : os.path.join(CONFIG.ADDON_DATA, 'plugin.video.realizer', 'settings.xml'),
        'default'  : 'trakt.user',
        'data'     : ['trakt.token', 'trakt.refresh', 'trakt.user'],
        'activate' : 'RunPlugin(plugin://plugin.video.realizer/?action=authTrakt)'}

}


def trakt_user(who):
    user = None
    if TRAKTID[who]:
        if os.path.exists(TRAKTID[who]['path']):
            try:
                add = tools.get_addon_by_id(TRAKTID[who]['plugin'])
                user = add.getSetting(TRAKTID[who]['default'])
            except:
                return None
    return user


def trakt_it(do, who):
    if not os.path.exists(CONFIG.ADDON_DATA):
        os.makedirs(CONFIG.ADDON_DATA)
    if not os.path.exists(CONFIG.TRAKTFOLD):
        os.makedirs(CONFIG.TRAKTFOLD)
    if who == 'all':
        for log in ORDER:
            if os.path.exists(TRAKTID[log]['path']):
                try:
                    addonid = tools.get_addon_by_id(TRAKTID[log]['plugin'])
                    default = TRAKTID[log]['default']
                    user = addonid.getSetting(default)
                    
                    update_trakt(do, log)
                except:
                    pass
            else:
                logging.log('[Trakt Data] {0}({1}) is not installed'.format(TRAKTID[log]['name'], TRAKTID[log]['plugin']), level=xbmc.LOGERROR)
        CONFIG.set_setting('traktnextsave', tools.get_date(days=3, formatted=True))
    else:
        if TRAKTID[who]:
            if os.path.exists(TRAKTID[who]['path']):
                update_trakt(do, who)
        else:
            logging.log('[Trakt Data] Invalid Entry: {0}'.format(who), level=xbmc.LOGERROR)


def clear_saved(who, over=False):
    if who == 'all':
        for trakt in TRAKTID:
            clear_saved(trakt,  True)
    elif TRAKTID[who]:
        file = TRAKTID[who]['file']
        if os.path.exists(file):
            os.remove(file)
            logging.log_notify("[COLOR {0}]{1}[/COLOR]".format(CONFIG.COLOR1, TRAKTID[who]['name']),
                               '[COLOR {0}]Trakt Data: Removed![/COLOR]'.format(CONFIG.COLOR2),
                               2000,
                               TRAKTID[who]['icon'])
        CONFIG.set_setting(TRAKTID[who]['saved'], '')
    if not over:
        xbmc.executebuiltin('Container.Refresh()')


def update_trakt(do, who):
    file = TRAKTID[who]['file']
    settings = TRAKTID[who]['settings']
    data = TRAKTID[who]['data']
    addonid = tools.get_addon_by_id(TRAKTID[who]['plugin'])
    saved = TRAKTID[who]['saved']
    default = TRAKTID[who]['default']
    user = addonid.getSetting(default)
    suser = CONFIG.get_setting(saved)
    name = TRAKTID[who]['name']
    icon = TRAKTID[who]['icon']

    if do == 'update':
        if not user == '':
            try:
                root = ElementTree.Element(saved)
                
                for setting in data:
                    trakt = ElementTree.SubElement(root, 'trakt')
                    id = ElementTree.SubElement(trakt, 'id')
                    id.text = setting
                    value = ElementTree.SubElement(trakt, 'value')
                    value.text = addonid.getSetting(setting)
                  
                tree = ElementTree.ElementTree(root)
                tree.write(file)
                
                user = addonid.getSetting(default)
                CONFIG.set_setting(saved, user)
                logging.log('Trakt Data Saved for {0}'.format(name), level=xbmc.LOGNOTICE)
            except Exception as e:
                logging.log("[Trakt Data] Unable to Update {0} ({1})".format(who, str(e)), level=xbmc.LOGERROR)
        else:
            logging.log('Trakt Data Click To Authorize {0}'.format(name))
    elif do == 'restore':
        if os.path.exists(file):
            tree = ElementTree.parse(file)
            root = tree.getroot()
            
            try:
                for setting in root.findall('trakt'):
                    id = setting.find('id').text
                    value = setting.find('value').text
                    addonid.setSetting(id, value)
                
                user = addonid.getSetting(default)
                CONFIG.set_setting(saved, user)
                logging.log('Trakt Data Restored for {0}'.format(name), level=xbmc.LOGNOTICE)
            except Exception as e:
                logging.log("[Trakt Data] Unable to Restore {0} ({1})".format(who, str(e)), level=xbmc.LOGERROR)
        else:
            logging.log('Trakt Data Not Found for {0}'.format(name))
    elif do == 'clearaddon':
        logging.log('{0} SETTINGS: {1}'.format(name, settings))
        if os.path.exists(settings):
            try:
                tree = ElementTree.parse(settings)
                root = tree.getroot()
                
                for setting in root.findall('setting'):
                    if setting.attrib['id'] in data:
                        logging.log('Removing Setting: {0}'.format(setting.attrib))
                        root.remove(setting)
                            
                tree.write(settings)
                
                logging.log_notify("[COLOR {0}]{1}[/COLOR]".format(CONFIG.COLOR1, name),
                                   '[COLOR {0}]Addon Data: Cleared![/COLOR]'.format(CONFIG.COLOR2),
                                   2000,
                                   icon)
            except Exception as e:
                logging.log("[Trakt Data] Unable to Clear Addon {0} ({1})".format(who, str(e)), level=xbmc.LOGERROR)
    xbmc.executebuiltin('Container.Refresh()')


def auto_update(who):
    if who == 'all':
        for log in TRAKTID:
            if os.path.exists(TRAKTID[log]['path']):
                auto_update(log)
    elif TRAKTID[who]:
        if os.path.exists(TRAKTID[who]['path']):
            u = trakt_user(who)
            su = CONFIG.get_setting(TRAKTID[who]['saved'])
            n = TRAKTID[who]['name']
            if not u or u == '':
                return
            elif su == '':
                trakt_it('update', who)
            elif not u == su:
                dialog = xbmcgui.Dialog()

                if dialog.yesno(CONFIG.ADDONTITLE,
                                    "Would you like to save the [COLOR {0}]Trakt Data[/COLOR] for [COLOR {1}]{2}[/COLOR]?".format(CONFIG.COLOR2, CONFIG.COLOR1, n),
                                    "Addon: [COLOR springgreen][B]{0}[/B][/COLOR]".format(u),
                                    "Saved:[/COLOR] [COLOR red][B]{0}[/B][/COLOR]".format(su) if not su == '' else 'Saved:[/COLOR] [COLOR red][B]None[/B][/COLOR]',
                                    yeslabel="[B][COLOR springgreen]Save Data[/COLOR][/B]",
                                    nolabel="[B][COLOR red]No Cancel[/COLOR][/B]"):
                    trakt_it('update', who)
            else:
                trakt_it('update', who)


def import_list(who):
    if who == 'all':
        for log in TRAKTID:
            if os.path.exists(TRAKTID[log]['file']):
                import_list(log)
    elif TRAKTID[who]:
        if os.path.exists(TRAKTID[who]['file']):
            file = TRAKTID[who]['file']
            addonid = tools.get_addon_by_id(TRAKTID[who]['plugin'])
            saved = TRAKTID[who]['saved']
            default = TRAKTID[who]['default']
            suser = CONFIG.get_setting(saved)
            name = TRAKTID[who]['name']
            
            tree = ElementTree.parse(file)
            root = tree.getroot()
            
            for setting in root.findall('trakt'):
                id = setting.find('id').text
                value = setting.find('value').text
            
                addonid.setSetting(id, value)

            logging.log_notify("[COLOR {0}]{1}[/COLOR]".format(CONFIG.COLOR1, name),
                       '[COLOR {0}]Trakt Data: Imported![/COLOR]'.format(CONFIG.COLOR2))


def activate_trakt(who):
    if TRAKTID[who]:
        if os.path.exists(TRAKTID[who]['path']):
            act = TRAKTID[who]['activate']
            addonid = tools.get_addon_by_id(TRAKTID[who]['plugin'])
            if act == '':
                addonid.openSettings()
            else:
                xbmc.executebuiltin(TRAKTID[who]['activate'])
        else:
            dialog = xbmcgui.Dialog()

            dialog.ok(CONFIG.ADDONTITLE, '{0} is not currently installed.'.format(TRAKTID[who]['name']))
    else:
        xbmc.executebuiltin('Container.Refresh()')
        return

    check = 0
    while not trakt_user(who):
        if check == 30:
            break
        check += 1
        time.sleep(10)
    xbmc.executebuiltin('Container.Refresh()')
