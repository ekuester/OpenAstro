#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This file is part of openastro.org.

    OpenAstro.org is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenAstro.org is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with OpenAstro.org. If not, see <http://www.gnu.org/licenses/>.
"""
"""
# https://docs.gtk.org/gtk4/
# https://pygobject.gnome.org/tutorials/gtk4.html
# https://discourse.gnome.org/t/scaling-images-with-cairo-is-much-slower-in-gtk4/7701
# https://blog.gtk.org/2018/03/16/textures-and-paintables/
"""

MENU_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="MenuBar">
    <submenu>
    <attribute name="label" translatable="yes">Application</attribute>
      <section>
        <item>
          <attribute name="action">win.maximize</attribute>
          <attribute name="label" translatable="yes">Maximize</attribute>
        </item>
      </section>
      <section>
        <item>
          <attribute name="action">win.about</attribute>
          <attribute name="label" translatable="yes">_About</attribute>
        </item>
        <item>
          <attribute name="action">app.quit</attribute>
          <attribute name="label" translatable="yes">_Quit</attribute>
        </item>
      </section>
    </submenu>
    <submenu>
      <attribute name="label" translatable="yes">Settings</attribute>
      <section>
        <item>
          <attribute name="label" translatable="yes">Set Location</attribute>
          <attribute name="action">win.settingsLocation</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Configuration</attribute>
          <attribute name="action">win.settingsConfiguration</attribute>
        </item>
      </section>
    </submenu>
    <submenu>
      <attribute name="label" translatable="yes">Chart Types</attribute>
      <section>
        <item>
          <attribute name="label" translatable="yes">Radix Chart</attribute>
          <attribute name="action">win.specialRadix</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Transit Chart</attribute>
          <attribute name="action">win.specialTransit</attribute>
        </item>
      </section>
      <section>
        <item>
          <attribute name="label" translatable="yes">Synastry Chart</attribute>
          <attribute name="action">win.chartType</attribute>
          <attribute name="target">Synastry</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Composite Chart</attribute>
          <attribute name="action">win.chartType</attribute>
          <attribute name="target">Composite</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Combine Chart</attribute>
          <attribute name="action">win.chartType</attribute>
          <attribute name="target">Combine</attribute>
        </item>
      </section>
      <section>
        <item>
          <attribute name="label" translatable="yes">Solar Return</attribute>
          <attribute name="action">win.specialSolar</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Solar Progression</attribute>
          <attribute name="action">win.specialProgression</attribute>
        </item>
      </section>
    </submenu>
    <submenu>
      <attribute name="label" translatable="yes">Tables</attribute>
        <item>
          <attribute name="label" translatable="yes">Monthly Timeline</attribute>
          <attribute name="action">win.tableMonthlyTimeline</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Cusp Aspects</attribute>
          <attribute name="action">win.tableCuspAspects</attribute>
        </item>
    </submenu>
    <submenu>
      <attribute name="label" translatable="yes">Zoom</attribute>
        <section>
          <item>
            <attribute name="label" translatable="yes">In</attribute>
            <attribute name="action">win.zoom</attribute>
            <attribute name="target">zIn</attribute>
          </item>
          <item>
            <attribute name="label" translatable="yes">80%</attribute>
            <attribute name="action">win.zoom</attribute>
            <attribute name="target">z80</attribute>
          </item>
          <item>
            <attribute name="label" translatable="yes">100%</attribute>
            <attribute name="action">win.zoom</attribute>
            <attribute name="target">z100</attribute>
            <attribute name="accel">1</attribute>
          </item>
          <item>
            <attribute name="label" translatable="yes">150%</attribute>
            <attribute name="action">win.zoom</attribute>
            <attribute name="target">z150</attribute>
          </item>
          <item>
            <attribute name="label" translatable="yes">200%</attribute>
            <attribute name="action">win.zoom</attribute>
            <attribute name="target">z200</attribute>
          </item>
          <item>
            <attribute name="label" translatable="yes">Out</attribute>
            <attribute name="action">win.zoom</attribute>
            <attribute name="target">zOut</attribute>
          </item>
        </section>
    </submenu>
    <submenu>
      <attribute name="label" translatable="yes">Extra</attribute>
        <item>
          <attribute name="label" translatable="yes">Export Database</attribute>
          <attribute name="action">win.exportdb</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Import Database</attribute>
          <attribute name="action">win.importdb</attribute>
        </item>
    </submenu>
    <submenu>
      <attribute name="label" translatable="yes">Help</attribute>
      <section>
        <item>
          <attribute name="label" translatable="yes">About</attribute>
          <attribute name="action">win.about</attribute>
        </item>
      </section>
    </submenu>
  </menu>
  <menu id="AppMenu">
    <section>
      <item>
        <attribute name="label" translatable="yes">New</attribute>
        <attribute name="action">app.new</attribute>
      </item>
      <item>
        <attribute name="action">win.maximize</attribute>
        <attribute name="label" translatable="yes">Maximize</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">Quit</attribute>
        <attribute name="action">app.quit</attribute>
      </item>
    </section>
  </menu>
</interface>
"""

CHART_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="ChartUI">
    <section>
      <item>
        <attribute name="label" translatable="yes">New</attribute>
        <attribute name="action">win.newChart</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">Open</attribute>
        <attribute name="action">win.openChart</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">Save</attribute>
        <attribute name="action">win.saveChart</attribute>
      </item>
    </section>
    <submenu>
      <attribute name="label" translatable="yes">Import</attribute>
      <section>
        <item>
          <attribute name="label" translatable="yes">Oroboros (*.xml)</attribute>
          <attribute name="action">win.import</attribute>
          <attribute name="target">importOroboros</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Astrolog (*.dat)</attribute>
          <attribute name="action">win.import</attribute>
          <attribute name="target">importAstrolog</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Skylendar (*.skif)</attribute>
          <attribute name="action">win.import</attribute>
          <attribute name="target">importSkylendar</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">Zet8 Dbase (*.zbs)</attribute>
          <attribute name="action">win.import</attribute>
          <attribute name="target">importZet8</attribute>
        </item>
      </section>
    </submenu>
    <submenu>
      <attribute name="label" translatable="yes">Export</attribute>
      <section>
        <item>
          <attribute name="label" translatable="yes">PNG file</attribute>
          <attribute name="action">win.export</attribute>
          <attribute name="target">pngfile</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">JPG file</attribute>
          <attribute name="action">win.export</attribute>
          <attribute name="target">jpgfile</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">SVG file</attribute>
          <attribute name="action">win.export</attribute>
          <attribute name="target">svgfile</attribute>
        </item>
        <item>
          <attribute name="label" translatable="yes">PDF file</attribute>
          <attribute name="action">win.export</attribute>
          <attribute name="target">pdffile</attribute>
        </item>
      </section>
    </submenu>
    <section>
      <item>
        <attribute name="label" translatable="yes">Close</attribute>
        <attribute name="action">win.close</attribute>
      </item>
    </section>
  </menu>
</interface>
"""

EVENT_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="EventUI">
    <section>
      <item>
        <attribute name="label" translatable="yes">Edit Event</attribute>
        <attribute name="action">win.eventData</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">Open Database</attribute>
        <attribute name="action">win.openDatabase</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="label" translatable="yes">Open Famous People Database</attribute>
        <attribute name="action">win.openDataFamous</attribute>
      </item>
    </section>
  </menu>
</interface>
"""

BEGIN_XML = """<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="UpdateUI">
    <section>
"""
E_ITEM = """      <item>
        <attribute name="label" translatable="yes">empty</attribute>
        <attribute name="action">win.empty</attribute>
      </item>"""
M_ITEM = """      <item>
        <attribute name="label" translatable="yes">$label</attribute>
        <attribute name="action">win.$db</attribute>
        <attribute name="target" type="i">$idx</attribute>
      </item>"""
END_XML = """
    </section>
  </menu>
</interface>
"""

#basics
import math, sys, os.path, datetime, socket, gettext, codecs, webbrowser, pytz

#copyfile
from shutil import copyfile

#pysqlite
import sqlite3

#template processing
from string import Template

#minidom parser
from xml.dom.minidom import parseString

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
gi.require_version('Rsvg', '2.0')
from gi.repository import GLib, Gio, Gtk, Gdk, GObject, Rsvg

#local modukes
from openastromod import zonetab, geoname, importfile, dignities, swiss as ephemeris

#for debugging set to True
DEBUG = False
#for debugging set to True
LOCAL = False
if "--local" in sys.argv:
	LOCAL = True
#radius of zodiac
RADIUS = 240
OFFSET = 64
RATIO = math.sqrt(2)
VERSION = "1.1.100"

APPLICATION_ID = "org.openastro.AstroApp"
#maximal number of items of history
LIMIT=10
#dimensions of chart
CHARTX = 772.2 
CHARTY = 546.0
#radius of zodiac
RADIUS = 240

""" Construct FileFilters """
FILTER_ALL_FILES = Gtk.FileFilter()
FILTER_ALL_FILES.set_name(name='ALL')
FILTER_ALL_FILES.add_pattern(pattern='*')

FILTER_DAT_FILES = Gtk.FileFilter()
FILTER_DAT_FILES.set_name(name='DAT')
FILTER_DAT_FILES.add_pattern(pattern='*.dat')
FILTER_DAT_FILES.add_mime_type(mime_type='chart/dat')

FILTER_JPG_FILES = Gtk.FileFilter()
FILTER_JPG_FILES.set_name(name='JPG')
FILTER_JPG_FILES.add_pattern(pattern='*.jpg')
FILTER_JPG_FILES.add_mime_type(mime_type='image/jpg')

FILTER_OAC_FILES = Gtk.FileFilter()
FILTER_OAC_FILES.set_name(name='OAC')
FILTER_OAC_FILES.add_pattern(pattern='*.oac')
FILTER_OAC_FILES.add_mime_type(mime_type='chart/oac')

FILTER_PDF_FILES = Gtk.FileFilter()
FILTER_PDF_FILES.set_name(name='PDF')
FILTER_PDF_FILES.add_pattern(pattern='*.pdf')
FILTER_PDF_FILES.add_mime_type(mime_type='application/pdf')

FILTER_PNG_FILES = Gtk.FileFilter()
FILTER_PNG_FILES.set_name(name='PNG')
FILTER_PNG_FILES.add_pattern(pattern='*.png')
FILTER_PNG_FILES.add_mime_type(mime_type='image/png')

FILTER_PY_FILES = Gtk.FileFilter()
FILTER_PY_FILES.set_name(name='Python')
FILTER_PY_FILES.add_pattern(pattern='*.py')
FILTER_PY_FILES.add_mime_type(mime_type='text/x-python')

FILTER_SKIF_FILES = Gtk.FileFilter()
FILTER_SKIF_FILES.set_name(name='SKIF')
FILTER_SKIF_FILES.add_pattern(pattern='*.skif')
FILTER_SKIF_FILES.add_mime_type(mime_type='chart/skif')

FILTER_SQL_FILES = Gtk.FileFilter()
FILTER_SQL_FILES.set_name(name='SQL')
FILTER_SQL_FILES.add_pattern(pattern='*.sql')
FILTER_SQL_FILES.add_mime_type(mime_type='database/sql')

FILTER_SVG_FILES = Gtk.FileFilter()
FILTER_SVG_FILES.set_name(name='SVG')
FILTER_SVG_FILES.add_pattern(pattern='*.svg')
FILTER_SVG_FILES.add_mime_type(mime_type='image/svg')

FILTER_TXT_FILES = Gtk.FileFilter()
FILTER_TXT_FILES.set_name(name='TXT')
FILTER_TXT_FILES.add_pattern(pattern='*.txt')
FILTER_TXT_FILES.add_mime_type(mime_type='text/plain')

FILTER_XML_FILES = Gtk.FileFilter()
FILTER_XML_FILES.set_name(name='XML')
FILTER_XML_FILES.add_pattern(pattern='*.xml')
FILTER_XML_FILES.add_mime_type(mime_type='application/xml')

FILTER_ZBS_FILES = Gtk.FileFilter()
FILTER_ZBS_FILES.set_name(name='ZBS')
FILTER_ZBS_FILES.add_pattern(pattern='*.zbs')
FILTER_ZBS_FILES.add_mime_type(mime_type='chart/zbs')

#directories
if LOCAL:
	DATADIR=os.path.dirname(__file__)
elif os.path.exists(os.path.join(sys.prefix,'share','openastro.org')):
	DATADIR=os.path.join(sys.prefix,'share','openastro.org')
elif os.path.exists(os.path.join('usr','local','share','openastro.org')):
	DATADIR=os.path.join('usr','local','share','openastro.org')
elif os.path.exists(os.path.join('usr','share','openastro.org')):
	DATADIR=os.path.join('usr','share','openastro.org')
else:
	print("Exiting... can't find data directory")
	sys.exit()

#Translations
LANGUAGES_LABEL={
			"ar":"الْعَرَبيّة",
			"pt_BR":"Português brasileiro",
			"bg":"български език",
			"ca":"català",
			"cs":"čeština",
			"da":"dansk",
			"nl":"Nederlands",
			"eo":"Esperanto",
			"en":"English",
			"fi":"suomi",
			"fr":"Français",
			"de":"Deutsch",
			"el":"ελληνικά",
			"hu":"magyar nyelv",
			"it":"Italiano",
			"ja":"日本",
			"nds":"Plattdüütsch",
			"nb":"Bokmål",
			"pl":"język polski",
			"rom":"rromani ćhib",
			"ru":"Русский",
			"es":"Español",
			"sv":"svenska",
			"uk":"українська мова",
			"zh_TW":"正體字"
		}

TDomain = os.path.join(DATADIR, 'locale')
if not LOCAL:
	TDomain = os.path.dirname(DATADIR)
	TDomain = os.path.join(TDomain, 'locale')
LANGUAGES=list(LANGUAGES_LABEL.keys())
TRANSLATION={}
for i in range(len(LANGUAGES)):
	try:
		TRANSLATION[LANGUAGES[i]] = gettext.translation("openastro",TDomain,languages=[LANGUAGES[i]])
	except IOError as err:
		print("IOError! Invalid languages specified (%s) in %s" %(LANGUAGES[i],TDomain))
		TRANSLATION[LANGUAGES[i]] = gettext.translation("openastro",TDomain,languages=['en'])
try:
	TRANSLATION["default"] = gettext.translation("openastro",TDomain)
except IOError as err:
	print("OpenAstro.org has not yet been translated in your language! Could not load translation...")
	TRANSLATION["default"] = gettext.translation("openastro",TDomain,languages=['en'])

def dprint(str):
	""" debug print function """
	if "--debug" in sys.argv or DEBUG:
		print('%s' % str)


""" OpenAstro configuration class """
class OpenAstroCfg:
	def __init__(self):
		self.version = VERSION
		dprint("-------------------------------")
		dprint('  OpenAstro.org '+str(self.version))
		dprint("-------------------------------")
		self.homedir = os.path.expanduser("~")
		# printing variables
		self.pages = 1
		self.pagesY = 0
		#check for astrodir
		self.astrodir = os.path.join(self.homedir, '.openastro.org')
		if os.path.isdir(self.astrodir) == False:
			os.mkdir(self.astrodir)
		#check for tmpdir
		self.tmpdir = os.path.join(self.astrodir, 'tmp')
		if os.path.isdir(self.tmpdir) == False:
			os.mkdir(self.tmpdir)
		#check for swiss local dir
		self.swissLocalDir = os.path.join(self.astrodir, 'swiss_ephemeris')
		if os.path.isdir(self.swissLocalDir) == False:
			os.mkdir(self.swissLocalDir)
		#geonames database
		if LOCAL:
			self.geonamesdb = os.path.join(DATADIR, 'data', 'geonames.sql' )
		else:
			self.geonamesdb = os.path.join(DATADIR, 'geonames.sql' )
		#icons
		icons = os.path.join(DATADIR,'icons')
		self.iconWindow = os.path.join(icons, 'openastro.svg')
		self.iconAspects = os.path.join(icons, 'aspects')
		#basic files
		self.about = os.path.join(DATADIR, 'about.xpm')
		self.comments = os.path.join(DATADIR, 'COMMENTS')
		self.license = os.path.join(DATADIR, 'LICENSE')
		self.tempfilename = os.path.join(self.tmpdir,"openAstroChart.svg")
		self.tempfilenameprint = os.path.join(self.tmpdir,"openAstroChartPrint.svg")
		self.tempfilenametable = os.path.join(self.tmpdir,"openAstroChartTable.svg")
		self.tempfilenametableprint = os.path.join(self.tmpdir,"openAstroChartTablePrint.svg")
		self.xml_ui = os.path.join(DATADIR, 'openastro-ui.xml')
		self.xml_svg = os.path.join(DATADIR, 'openastro-svg.xml')
		self.xml_svg_table = os.path.join(DATADIR, 'openastro-svg-table.xml')
		#sqlite databases		
		self.astrodb = os.path.join(self.astrodir, 'astrodb.sql')
		self.peopledb = os.path.join(self.astrodir, 'peopledb.sql')
		if LOCAL:
			self.famousdb = os.path.join(DATADIR, 'data', 'famous.sql' )
		else:
			self.famousdb = os.path.join(DATADIR, 'famous.sql' )
		return

#Sqlite database
class OpenAstroSqlite:
	def __init__(self):
		self.dbcheck=False
		self.dbpurge="IGNORE"

		#--dbcheck puts dbcheck to true
		if "--dbcheck" in sys.argv:
			self.dbcheck=True
			dprint("  Database Check Enabled!")
			dprint("-------------------------------")

		#--purge purges database
		if "--purge" in sys.argv:
			self.dbcheck=True
			self.dbpurge="REPLACE"
			dprint("  Database Check Enabled!")
			dprint("  Database Purge Enabled!")
			dprint("-------------------------------")

		self.open()
		#get table names from sqlite_master for astrodb
		sql='SELECT name FROM sqlite_master'
		self.cursor.execute(sql)
		list=self.cursor.fetchall()
		self.tables={}
		for i in range(len(list)):
			self.tables[list[i][0]]=1

		#get table names from sqlite_master for peopledb
		sql='SELECT name FROM sqlite_master'
		self.pcursor.execute(sql)
		list=self.pcursor.fetchall()
		self.ptables={}
		for i in range(len(list)):
			self.ptables[list[i][0]]=1

		#check for event_natal table in peopledb
		self.ptable_event_natal = {
			"id":"INTEGER PRIMARY KEY",
			"name":"VARCHAR(50)",
			"year":"VARCHAR(4)",
			"month":"VARCHAR(2)",
			"day":"VARCHAR(2)",
			"hour":"VARCHAR(50)",
			"geolon":"VARCHAR(50)",
			"geolat":"VARCHAR(50)",
			"altitude":"VARCHAR(50)",
			"location":"VARCHAR(150)",
			"timezone":"VARCHAR(50)",
			"notes":"VARCHAR(500)",
			"image":"VARCHAR(250)",
			"countrycode":"VARCHAR(2)",
			"geonameid":"INTEGER",
			"timezonestr":"VARCHAR(100)",
			"extra":"VARCHAR(500)"
			}
		if 'event_natal' not in self.ptables:
			sql='CREATE TABLE IF NOT EXISTS event_natal (id INTEGER PRIMARY KEY,name VARCHAR(50)\
				 ,year VARCHAR(4),month VARCHAR(2), day VARCHAR(2), hour VARCHAR(50), geolon VARCHAR(50)\
			 	,geolat VARCHAR(50), altitude VARCHAR(50), location VARCHAR(150), timezone VARCHAR(50)\
			 	,notes VARCHAR(500), image VARCHAR(250), countrycode VARCHAR(2), geonameid INTEGER\
			 	,timezonestr VARCHAR(100), extra VARCHAR(250))'
			self.pcursor.execute(sql)
			dprint('creating sqlite table event_natal in peopledb')

		#check for astrocfg table in astrodb
		if 'astrocfg' not in self.tables:
			#0=cfg_name, 1=cfg_value
			sql='CREATE TABLE IF NOT EXISTS astrocfg (name VARCHAR(150) UNIQUE,value VARCHAR(150))'
			self.cursor.execute(sql)
			self.dbcheck=True
			dprint('creating sqlite table astrocfg in astrodb')

		#check for astrocfg version
		sql='INSERT OR IGNORE INTO astrocfg (name,value) VALUES(?,?)'
		self.cursor.execute(sql,("version", app.cfg.version))
		#get astrocfg dict
		sql='SELECT value FROM astrocfg WHERE name="version"'
		self.cursor.execute(sql)
		self.astrocfg = {}
		self.astrocfg["version"]=self.cursor.fetchone()[0]

		#check for updated version 
		if self.astrocfg['version'] != str(app.cfg.version):
			dprint('version mismatch(%s != %s), checking table structure' % (self.astrocfg['version'], app.cfg.version))
			#insert current version and set dbcheck to true
			self.dbcheck = True
			sql='INSERT OR REPLACE INTO astrocfg VALUES("version","'+str(app.cfg.version)+'")'
			self.cursor.execute(sql)

		#default astrocfg keys (if dbcheck)
		if self.dbcheck:
			dprint('dbcheck astrodb.astrocfg')
			default = {
				"version":str(app.cfg.version),
				"use_geonames.org":"0",
				"houses_system":"P",
				"language":"default",
				"postype":"geo",
				"chartview":"traditional",
				"zodiactype":"tropical",
				"siderealmode":"FAGAN_BRADLEY"
			 }
			for k, v in default.items():
				sql='INSERT OR %s INTO astrocfg (name,value) VALUES(?,?)' % (self.dbpurge)
				self.cursor.execute(sql,(k,v))

		#get astrocfg dict
		sql='SELECT * FROM astrocfg'
		self.cursor.execute(sql)
		self.astrocfg = {}
		for row in self.cursor:
			self.astrocfg[row['name']]=row['value']
		#install language
		self.setLanguage(self.astrocfg['language'])
		self.lang_label=LANGUAGES_LABEL
		#fix inconsitencies between in people's database
		if self.dbcheck:
			sql='PRAGMA table_info(event_natal)'
			self.pcursor.execute(sql)
			list=self.pcursor.fetchall()
			vacuum = False
			cnames=[]
			for i in range(len(list)):
				cnames.append(list[i][1])
			for key,val in self.ptable_event_natal.items():
				if key not in cnames:
					sql = 'ALTER TABLE event_natal ADD %s %s'%(key,val)
					dprint("dbcheck peopledb.event_natal adding %s %s"%(key,val))
					self.pcursor.execute(sql)
					vacuum = True
			if vacuum:
				sql = "VACUUM"
				self.pcursor.execute(sql)

				dprint('dbcheck peopledb.event_natal: updating table definitions!')

		#check for history table in astrodb
		if 'history' not in self.tables:
			#0=id,1=name,2=year,3=month,4=day,5=hour,6=geolon,7=geolat,8=alt,9=location,10=tz
			sql='CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY,name VARCHAR(50)\
				 ,year VARCHAR(50),month VARCHAR(50), day VARCHAR(50), hour VARCHAR(50), geolon VARCHAR(50)\
			 	,geolat VARCHAR(50), altitude VARCHAR(50), location VARCHAR(150), timezone VARCHAR(50)\
			 	,notes VARCHAR(500), image VARCHAR(250), countrycode VARCHAR(2), geonameid INTEGER, extra VARCHAR(250))'
			self.cursor.execute(sql)

			dprint('creating sqlite table history in astrodb')

		#fix inconsitencies between 0.6x and 0.7x in history table
		if self.dbcheck:
			sql='PRAGMA table_info(history)'
			self.cursor.execute(sql)
			list=self.cursor.fetchall()
			cnames=[]
			for i in range(len(list)):
				cnames.append(list[i][1])
			vacuum = False
			if "notes" not in cnames:
				sql = 'ALTER TABLE history ADD notes VARCHAR(500)'
				self.cursor.execute(sql)
				vacuum = True
			if "image" not in cnames:
				sql = 'ALTER TABLE history ADD image VARCHAR(250)'
				self.cursor.execute(sql)
				vacuum = True
			if "countrycode" not in cnames:
				sql = 'ALTER TABLE history ADD countrycode VARCHAR(2)'
				self.cursor.execute(sql)
				vacuum = True
			if "geonameid" not in cnames:
				sql = 'ALTER TABLE history ADD geonameid INTEGER'
				self.cursor.execute(sql)
				vacuum = True
			if "extra" not in cnames:
				sql = 'ALTER TABLE history ADD extra VARCHAR(250)'
				self.cursor.execute(sql)
				vacuum = True
			if vacuum:
				sql = "VACUUM"
				self.cursor.execute(sql)

				dprint('dbcheck: updating history table definitions!')

		#check for settings_aspect table in astrodb
		if 'settings_aspect' not in self.tables:
			sql='CREATE TABLE IF NOT EXISTS settings_aspect (degree INTEGER UNIQUE, name VARCHAR(50)\
				 ,color VARCHAR(50),visible INTEGER, visible_grid INTEGER\
				 ,is_major INTEGER, is_minor INTEGER, orb VARCHAR(5))'
			self.cursor.execute(sql)
			self.dbcheck=True

			dprint('creating sqlite table settings_aspect in astrodb')

		#if update, check if everything is in order
		if self.dbcheck:
			sql='PRAGMA table_info(settings_aspect)'
			self.cursor.execute(sql)
			list=self.cursor.fetchall()
			cnames=[]
			for i in range(len(list)):
				cnames.append(list[i][1])
			vacuum = False
			if "visible" not in cnames:
				sql = 'ALTER TABLE settings_aspect ADD visible INTEGER'
				self.cursor.execute(sql)
				vacuum = True
			if "visible_grid" not in cnames:
				sql = 'ALTER TABLE settings_aspect ADD visible_grid INTEGER'
				self.cursor.execute(sql)
				vacuum = True
			if "is_major" not in cnames:
				sql = 'ALTER TABLE settings_aspect ADD is_major INTEGER'
				self.cursor.execute(sql)
				vacuum = True
			if "is_minor" not in cnames:
				sql = 'ALTER TABLE settings_aspect ADD is_minor INTEGER'
				self.cursor.execute(sql)
				vacuum = True
			if "orb" not in cnames:
				sql = 'ALTER TABLE settings_aspect ADD orb VARCHAR(5)'
				self.cursor.execute(sql)
				vacuum = True
			if vacuum:
				sql = "VACUUM"
				self.cursor.execute(sql)
		#default values for settings_aspect (if dbcheck)
		if self.dbcheck:
			dprint('dbcheck astrodb.settings_aspect')
			degree = [ 0 , 30 , 45 , 60 , 72 , 90 , 120 , 135 , 144 , 150 , 180 ]
			name = [ _('conjunction') , _('semi-sextile') , _('semi-square') , _('sextile') , _('quintile') , _('square') , _('trine') , _('sesquiquadrate') , _('biquintile') , _('quincunx') , _('opposition') ]
			color = [ '#5757e2' ,	'#810757' , 			'#b14e58' ,	 '#d59e28' , '#1f99b3' ,'#dc0000' , '#36d100' , '#985a10' , 		  '#7a9810' , 	'#fff600' ,		 '#510060' ]
			visible =      [ 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 ]
			visible_grid = [ 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 ]
			is_major =     [ 1 , 0 , 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 1 ]
			is_minor =     [ 0 , 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 ]
			orb =         [ 10 , 3 , 3 , 6 , 2 , 8 , 8 , 3 , 2 , 3 , 10 ]
			#insert values
			for i in range(len(degree)):
				sql='INSERT OR %s INTO settings_aspect \
				(degree, name, color, visible, visible_grid, is_major, is_minor, orb)\
				VALUES(%s,"%s","%s",%s,%s,%s,%s,"%s")' % ( self.dbpurge,degree[i],name[i],color[i],visible[i],
				visible_grid[i],is_major[i],is_minor[i],orb[i] )
				self.cursor.execute(sql)
		#check for colors table in astrodb
		if 'color_codes' not in self.tables:
			sql='CREATE TABLE IF NOT EXISTS color_codes (name VARCHAR(50) UNIQUE\
				 ,code VARCHAR(50))'
			self.cursor.execute(sql)
			self.dbcheck=True

			dprint('creating sqlite table color_codes in astrodb')

		#default values for colors (if dbcheck)
		self.defaultColors = {
			"paper_0":"#000000",
			"paper_1":"#ffffff",
			"zodiac_bg_0":"#482900",
			"zodiac_bg_1":"#6b3d00",
			"zodiac_bg_2":"#5995e7",
			"zodiac_bg_3":"#2b4972",
			"zodiac_bg_4":"#c54100",
			"zodiac_bg_5":"#2b286f",
			"zodiac_bg_6":"#69acf1",
			"zodiac_bg_7":"#ffd237",
			"zodiac_bg_8":"#ff7200",
			"zodiac_bg_9":"#863c00",
			"zodiac_bg_10":"#4f0377",
			"zodiac_bg_11":"#6cbfff",
			"zodiac_icon_0":"#482900",
			"zodiac_icon_1":"#6b3d00",
			"zodiac_icon_2":"#5995e7",
			"zodiac_icon_3":"#2b4972",
			"zodiac_icon_4":"#c54100",
			"zodiac_icon_5":"#2b286f",
			"zodiac_icon_6":"#69acf1",
			"zodiac_icon_7":"#ffd237",
			"zodiac_icon_8":"#ff7200",
			"zodiac_icon_9":"#863c00",
			"zodiac_icon_10":"#4f0377",
			"zodiac_icon_11":"#6cbfff",
			"zodiac_radix_ring_0":"#ff0000",
			"zodiac_radix_ring_1":"#ff0000",
			"zodiac_radix_ring_2":"#ff0000",
			"zodiac_transit_ring_0":"#ff0000",
			"zodiac_transit_ring_1":"#ff0000",
			"zodiac_transit_ring_2":"#0000ff",
			"zodiac_transit_ring_3":"#0000ff",
			"houses_radix_line":"#ff0000",
			"houses_transit_line":"#0000ff",
			"aspect_0":"#5757e2",
			"aspect_30":"#810757",
			"aspect_45":"#b14e58",
			"aspect_60":"#d59e28",
			"aspect_72":"#1f99b3",
			"aspect_90":"#dc0000",
			"aspect_120":"#36d100",
			"aspect_135":"#985a10",
			"aspect_144":"#7a9810",
			"aspect_150":"#fff600",
			"aspect_180":"#510060",
			"planet_0":"#984b00",
			"planet_1":"#150052",
			"planet_2":"#520800",
			"planet_3":"#400052",
			"planet_4":"#540000",
			"planet_5":"#47133d",
			"planet_6":"#124500",
			"planet_7":"#6f0766",
			"planet_8":"#06537f",
			"planet_9":"#713f04",
			"planet_10":"#4c1541",
			"planet_11":"#4c1541",
			"planet_12":"#331820",
			"planet_13":"#585858",
			"planet_14":"#000000",
			"planet_15":"#666f06",
			"planet_16":"#000000",
			"planet_17":"#000000",
			"planet_18":"#000000",
			"planet_19":"#000000",
			"planet_20":"#000000",
			"planet_21":"#000000",
			"planet_22":"#000000",
			"planet_23":"#ff7e00",
			"planet_24":"#FF0000",
			"planet_25":"#0000FF",
			"planet_26":"#000000",
			"planet_27":"#000000",
			"planet_28":"#000000",
			"planet_29":"#000000",
			"planet_30":"#000000",
			"planet_31":"#000000",
			"planet_32":"#000000",
			"planet_33":"#000000",
			"planet_34":"#000000",
			"lunar_phase_0":"#000000",
			"lunar_phase_1":"#FFFFFF",
			"lunar_phase_2":"#CCCCCC"
		}
		if self.dbcheck:
			dprint('dbcheck astrodb.color_codes')
			#insert values
			for k,v in self.defaultColors.items():
				sql='INSERT OR %s INTO color_codes \
				(name, code)\
				VALUES("%s","%s")' % ( self.dbpurge , k, v )
				self.cursor.execute(sql)
		#check for label table in astrodb
		if 'label' not in self.tables:
			sql='CREATE TABLE IF NOT EXISTS label (name VARCHAR(150) UNIQUE\
				 ,value VARCHAR(200))'
			self.cursor.execute(sql)
			self.dbcheck=True

			dprint('creating sqlite table label in astrodb')

		#default values for label (if dbcheck)
		self.defaultLabel = {
			"cusp":_("Cusp"),
			"longitude":_("Longitude"),
			"latitude":_("Latitude"),
			"north":_("North"),
			"east":_("East"),
			"south":_("South"),
			"west":_("West"),
			"apparent_geocentric":_("Apparent Geocentric"),
			"true_geocentric":_("True Geocentric"),
			"topocentric":_("Topocentric"),
			"heliocentric":_("Heliocentric"),
			"fire":_("Fire"),
			"earth":_("Earth (element)"),
			"air":_("Air"),
			"water":_("Water"),
			"radix":_("Radix"),
			"transit":_("Transit"),
			"synastry":_("Synastry"),
			"composite":_("Composite"),
			"combine":_("Combine"),
			"solar":_("Solar"),
			"secondary_progressions":_("Secondary Progressions")
		}
		if self.dbcheck:
			dprint('dbcheck astrodb.label')
			#insert values
			for k,v in self.defaultLabel.items():
				sql='INSERT OR %s INTO label \
				(name, value)\
				VALUES("%s","%s")' % ( self.dbpurge , k, v )
				self.cursor.execute(sql)
		#check for settings_planet table in astrodb
		self.table_settings_planet={
				"id":"INTEGER UNIQUE",
				"name":"VARCHAR(50)",
				"color":"VARCHAR(50)",
				"visible":"INTEGER",
				"element_points":"INTEGER",
				"zodiac_relation":"VARCHAR(50)",
				"label":"VARCHAR(50)",
				"label_short":"VARCHAR(20)",
				"visible_aspect_line":"INTEGER",
				"visible_aspect_grid":"INTEGER"
				}
		if 'settings_planet' not in self.tables:
			sql='CREATE TABLE IF NOT EXISTS settings_planet (id INTEGER UNIQUE, name VARCHAR(50)\
				,color VARCHAR(50),visible INTEGER, element_points INTEGER, zodiac_relation VARCHAR(50)\
			 	,label VARCHAR(50), label_short VARCHAR(20), visible_aspect_line INTEGER\
			 	,visible_aspect_grid INTEGER)'
			self.cursor.execute(sql)
			self.dbcheck=True

			dprint('creating sqlite table settings_planet in astrodb')

		#default values for settings_planet (if dbcheck)
		if self.dbcheck:
			dprint('dbcheck astrodb.settings_planet')
			self.value_settings_planet={}
			self.value_settings_planet['name'] = [
			'sun','moon','mercury','venus','mars','jupiter','saturn',
			'uranus','neptune','pluto','mean node','true node','mean apogee','osc. apogee',
			'earth','chiron','pholus','ceres','pallas','juno','vesta',
			'intp. apogee','intp. perigee','Asc','Mc','Dsc','Ic','day pars',
			'night pars','south node', 'marriage pars', 'black sun', 'vulcanus', 'persephone',
			'true lilith']
			orb = [
			#sun
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}',
			#moon
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}',
			#mercury
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}',
			#venus
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}',
			#mars
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}',
			#jupiter
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}',
			#saturn
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}',
			#uranus
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}',
			#neptunus
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}',
			#pluto
			'{0:10,180:10,90:10,120:10,60:6,30:3,150:3,45:3,135:3,72:1,144:1}'
			]
			self.value_settings_planet['label'] = [
			_('Sun'),_('Moon'),_('Mercury'),_('Venus'),_('Mars'),_('Jupiter'),_('Saturn'),
			_('Uranus'),_('Neptune'),_('Pluto'),_('North Node'),'?',_('Lilith'),_('Osc. Lilith'),
			_('Earth'),_('Chiron'),_('Pholus'),_('Ceres'),_('Pallas'),_('Juno'),_('Vesta'),
			'intp. apogee','intp. perigee',_('Asc'),_('Mc'),_('Dsc'),_('Ic'),_('Day Pars'),
			_('Night Pars'),_('South Node'),_('Marriage Pars'),_('Black Sun'),_('Vulcanus'),
			_('Persephone'),_('True Lilith')]
			self.value_settings_planet['label_short'] = [
			'sun','moon','mercury','venus','mars','jupiter','saturn',
			'uranus','neptune','pluto','Node','?','Lilith','?',
			'earth','chiron','pholus','ceres','pallas','juno','vesta',
			'intp. apogee','intp. perigee','Asc','Mc','Dsc','Ic','DP',
			'NP','SNode','marriage','blacksun','vulcanus','persephone','truelilith']
			self.value_settings_planet['color'] = [
			'#984b00','#150052','#520800','#400052','#540000','#47133d','#124500',
			'#6f0766','#06537f','#713f04','#4c1541','#4c1541','#33182','#000000',
			'#000000','#666f06','#000000','#000000','#000000','#000000','#000000',
			'#000000','#000000','orange','#FF0000','#0000FF','#000000','#000000',
			'#000000','#000000','#000000','#000000','#000000','#000000','#000000']
			self.value_settings_planet['visible'] = [
			1,1,1,1,1,1,1,
			1,1,1,1,0,1,0,
			0,1,0,0,0,0,0,
			0,0,1,1,0,0,1,
			1,0,0,0,0,0,0]
			self.value_settings_planet['visible_aspect_line'] = [
			1,1,1,1,1,1,1,
			1,1,1,1,0,1,0,
			0,1,0,0,0,0,0,
			0,0,1,1,0,0,1,
			1,0,0,0,0,0,0]
			self.value_settings_planet['visible_aspect_grid'] = [
			1,1,1,1,1,1,1,
			1,1,1,1,0,1,0,
			0,1,0,0,0,0,0,
			0,0,1,1,0,0,1,
			1,0,0,0,0,0,0]
			self.value_settings_planet['element_points'] = [
			40,40,15,15,15,10,10,
			10,10,10,20,0,0,0,
			0,5,0,0,0,0,0,
			0,0,40,20,0,0,0,
			0,0,0,0,0,0,0]
			#zodiac relation gives 10 extra points in element calculation
			self.value_settings_planet['zodiac_relation'] = [
			'4','3','2,5','1,6','0','8','9',
			'10','11','7','-1','-1','-1','-1',
			'-1','-1','-1','-1','-1','-1','-1',
			'-1','-1','-1','-1','-1','-1','-1',
			'-1','-1','-1','-1','-1','-1','-1']
			#if update, check if everything is in order with settings_planet
			sql='PRAGMA table_info(settings_planet)'
			self.cursor.execute(sql)
			list=self.cursor.fetchall()
			vacuum = False
			cnames=[]
			for i in range(len(list)):
				cnames.append(list[i][1])
			for key,val in self.table_settings_planet.items():
				if key not in cnames:
					sql = 'ALTER TABLE settings_planet ADD %s %s'%(key,val)
					dprint("dbcheck astrodb.settings_planet adding %s %s"%(key,val))
					self.cursor.execute(sql)
					#update values for col
					self.cursor.execute("SELECT id FROM settings_planet ORDER BY id DESC LIMIT 1")
					c = self.cursor.fetchone()[0]+1
					for rowid in range(c):
						sql = 'UPDATE settings_planet SET %s=? WHERE id=?' %(key)
						self.cursor.execute(sql,(self.value_settings_planet[key][rowid],rowid))
					vacuum = True
			if vacuum:
				sql = "VACUUM"
				self.cursor.execute(sql)
			#insert values for planets that don't exists
			for i in range(len(self.value_settings_planet['name'])):
				sql='INSERT OR %s INTO settings_planet VALUES(?,?,?,?,?,?,?,?,?,?)'%(self.dbpurge)
				values=(i,
						self.value_settings_planet['name'][i],
						self.value_settings_planet['color'][i],
						self.value_settings_planet['visible'][i],
						self.value_settings_planet['element_points'][i],
						self.value_settings_planet['zodiac_relation'][i],
						self.value_settings_planet['label'][i],
						self.value_settings_planet['label_short'][i],
						self.value_settings_planet['visible_aspect_line'][i],
						self.value_settings_planet['visible_aspect_grid'][i]
						)
				self.cursor.execute(sql,values)
		#commit initial changes
		self.updateHistory()
		self.link.commit()
		self.plink.commit()
		self.close()

	def setLanguage(self, lang=None):
		if lang==None or lang=="default":
			TRANSLATION["default"].install()
			dprint("installing default language")
		else:
			TRANSLATION[lang].install()
			dprint("installing language (%s)"%(lang))
		return

	def addHistory(self):
		self.open()
		sql = 'INSERT INTO history  (id,name,year,month,day,hour,geolon,geolat,altitude,location,timezone,countrycode) VALUES (null,?,?,?,?,?,?,?,?,?,?,?)'
		tuple = (app.name, app.year, app.month, app.day, app.hour, app.geolon, app.geolat, app.altitude, app.location, app.timezone, app.countrycode)
		self.cursor.execute(sql,tuple)
		self.link.commit()
		self.updateHistory()
		self.close()

	def getAstrocfg(self,key):
		self.open()
		sql='SELECT value FROM astrocfg WHERE name="%s"' % key
		self.cursor.execute(sql)
		one=self.cursor.fetchone()
		self.close()
		if one == None:
			return None
		else:
			return one[0]

	def setAstrocfg(self,key,val):
		sql='INSERT OR REPLACE INTO astrocfg (name,value) VALUES (?,?)'
		self.query([sql],[(key,val)])
		self.astrocfg[key]=val
		return

	def getColors(self):
		self.open()
		sql='SELECT * FROM color_codes'
		self.cursor.execute(sql)
		list=self.cursor.fetchall()
		out={}
		for i in range(len(list)):
			out[list[i][0]] = list[i][1]
		self.close()
		return out

	def getLabel(self):
		self.open()
		sql='SELECT * FROM label'
		self.cursor.execute(sql)
		list=self.cursor.fetchall()
		out={}
		for i in range(len(list)):
			out[list[i][0]] = list[i][1]
		self.close()
		return out

	def getDatabase(self):
		self.open()

		sql = 'SELECT * FROM event_natal ORDER BY id ASC'
		self.pcursor.execute(sql)
		dict = []
		for row in self.pcursor:
			s={}
			for key,val in self.ptable_event_natal.items():
				if row[key] == None:
					s[key]=""
				else:
					s[key]=row[key]
			dict.append(s)
		self.close()
		return dict

	def getSettingsPlanet(self):
		self.open()
		sql = 'SELECT * FROM settings_planet ORDER BY id ASC'
		self.cursor.execute(sql)
		dict = []
		for row in self.cursor:
			s={}
			for key,val in self.table_settings_planet.items():
				s[key]=row[key]
			dict.append(s)
		self.close()
		return dict

	def getSettingsAspect(self):
		self.open()
		sql = 'SELECT * FROM settings_aspect ORDER BY degree ASC'
		self.cursor.execute(sql)
		dict = []
		for row in self.cursor:
			#degree, name, color, visible, visible_grid, is_major, is_minor, orb
			dict.append({'degree':row['degree'],'name':row['name'],'color':row['color']
			,'visible':row['visible'],'visible_grid':row['visible_grid']
			,'is_major':row['is_major'],'is_minor':row['is_minor'],'orb':row['orb']})
		self.close()
		return dict

	def getSettingsLocation(self):
		#look if location is known
		if 'home_location' not in self.astrocfg or 'home_timezonestr' not in self.astrocfg:
			self.open()
			sql='INSERT OR REPLACE INTO astrocfg (name,value) VALUES("home_location","")'
			self.cursor.execute(sql)
			sql='INSERT OR REPLACE INTO astrocfg (name,value) VALUES("home_geolat","")'
			self.cursor.execute(sql)
			sql='INSERT OR REPLACE INTO astrocfg (name,value) VALUES("home_geolon","")'
			self.cursor.execute(sql)
			sql='INSERT OR REPLACE INTO astrocfg (name,value) VALUES("home_countrycode","")'
			self.cursor.execute(sql)
			sql='INSERT OR REPLACE INTO astrocfg (name,value) VALUES("home_timezonestr","")'
			self.cursor.execute(sql)
			self.link.commit()
			self.close
			return '','','','',''
		else:
			return self.astrocfg['home_location'],self.astrocfg['home_geolat'],self.astrocfg['home_geolon'],self.astrocfg['home_countrycode'],self.astrocfg['home_timezonestr']

	def setSettingsLocation(self, lat, lon, loc, cc, tzstr):
		self.open()
		sql = 'UPDATE astrocfg SET value="%s" WHERE name="home_location"' % loc
		self.cursor.execute(sql)
		sql = 'UPDATE astrocfg SET value="%s" WHERE name="home_geolat"' % lat
		self.cursor.execute(sql)
		sql = 'UPDATE astrocfg SET value="%s" WHERE name="home_geolon"' % lon
		self.cursor.execute(sql)
		sql = 'UPDATE astrocfg SET value="%s" WHERE name="home_countrycode"' % cc
		self.cursor.execute(sql)
		sql = 'UPDATE astrocfg SET value="%s" WHERE name="home_timezonestr"' % tzstr
		self.cursor.execute(sql)
		self.link.commit()
		self.close()

	def updateHistory(self):
		sql='SELECT * FROM history'
		self.cursor.execute(sql)
		self.history = self.cursor.fetchall()
		#check if limit is exceeded
		limit=LIMIT
		if len(self.history) > limit:
			sql = "DELETE FROM history WHERE id < '"+str(self.history[len(self.history)-limit][0])+"'"
			self.cursor.execute(sql)
			self.link.commit()
			#update self.history
			sql = 'SELECT * FROM history'
			self.cursor.execute(sql)
			self.history = self.cursor.fetchall()
		return

	"""
	Function to import zet8 databases
	"""
	def importZet8(self, target_db, data):

		target_con = sqlite3.connect(target_db)
		target_con.row_factory = sqlite3.Row
		target_cur = target_con.cursor()

		#get target names
		target_names={}
		sql='SELECT name FROM event_natal'
		target_cur.execute(sql)
		for row in target_cur:
			target_names[row['name']]=1
		for k,v in target_names.items():
			for i in range(1,10):
				if '%s (#%s)' % (k,i) in target_names:
					target_names[k] += 1

		#read input write target
		for row in data:

			if row['name'] in target_names:
				name_suffix = ' (#%s)' % target_names[row['name']]
				target_names[row['name']] += 1
			else:
				name_suffix = ''

			gname = self.gnearest( float(row['latitude']),float(row['longitude']) )

			sql = 'INSERT INTO event_natal (id,name,year,month,day,hour,geolon,geolat,altitude,\
				location,timezone,notes,image,countrycode,geonameid,timezonestr,extra) VALUES \
				(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
			tuple = (row['name']+name_suffix,row['year'],row['month'],row['day'],row['hour'],row['longitude'],
				row['latitude'],25,row['location'],row['timezone'],"",
				"",gname['geonameid'],gname['timezonestr'],"")
			target_cur.execute(sql,tuple)

		#Finished, close connection
		target_con.commit()
		target_cur.close()
		target_con.close()
		return

	"""
	Function to merge two databases containing entries for persons
	databaseMerge(target_db,input_db)

	database format:
	'CREATE TABLE IF NOT EXISTS event_natal (id INTEGER PRIMARY KEY,name VARCHAR(50),\
	 year VARCHAR(4),month VARCHAR(2), day VARCHAR(2), hour VARCHAR(50), geolon VARCHAR(50),\
	 geolat VARCHAR(50), altitude VARCHAR(50), location VARCHAR(150), timezone VARCHAR(50),\
	 notes VARCHAR(500), image VARCHAR(250), countrycode VARCHAR(2), geonameid INTEGER,\
	 timezonestr VARCHAR(100), extra VARCHAR(250))'
	"""
	def databaseMerge(self,target_db,input_db):
		dprint('db.databaseMerge: %s << %s'%(target_db,input_db))
		target_con = sqlite3.connect(target_db)
		target_con.row_factory = sqlite3.Row
		target_cur = target_con.cursor()
		input_con = sqlite3.connect(input_db)
		input_con.row_factory = sqlite3.Row
		input_cur = input_con.cursor()
		#get target names
		target_names={}
		sql='SELECT name FROM event_natal'
		target_cur.execute(sql)
		for row in target_cur:
			target_names[row['name']]=1
		for k,v in target_names.items():
			for i in range(1,10):
				if '%s (#%s)'% (k,i) in target_names:
					target_names[k] += 1

		#read input write target
		sql='SELECT * FROM event_natal'
		input_cur.execute(sql)
		for row in input_cur:
			if row['name'] in target_names:
				name_suffix = ' (#%s)' % target_names[row['name']]
				target_names[row['name']] += 1
			else:
				name_suffix = ''
			sql = 'INSERT INTO event_natal (id,name,year,month,day,hour,geolon,geolat,altitude,\
				location,timezone,notes,image,countrycode,geonameid,timezonestr,extra) VALUES \
				(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
			tuple = (row['name']+name_suffix,row['year'],row['month'],row['day'],row['hour'],row['geolon'],
				row['geolat'],row['altitude'],row['location'],row['timezone'],row['notes'],
				row['image'],row['countrycode'],row['geonameid'],row['timezonestr'],row['extra'])
			target_cur.execute(sql,tuple)

		#Finished, close connection
		target_con.commit()
		target_cur.close()
		target_con.close()
		input_cur.close()
		input_con.close()
		return

	"""
	Basic Query Functions for common databases
	"""
	def query(self, sql, tuple=None):
		l=sqlite3.connect(app.cfg.astrodb)
		c=l.cursor()
		for i in range(len(sql)):
			if tuple == None:
				c.execute(sql[i])
			else:
				c.execute(sql[i],tuple[i])
		l.commit()
		c.close()
		l.close()

	def pquery(self, sql, tuple=None):
		l=sqlite3.connect(app.cfg.peopledb)
		c=l.cursor()
		for i in range(len(sql)):
			if tuple == None:
				c.execute(sql[i])
			else:
				c.execute(sql[i],tuple[i])
		l.commit()
		c.close()
		l.close()

	def gnearest(self, lat=None, lon=None):
		#check for none
		if lat==None or lon==None:
			return {'country':None,'admin1':None,'geonameid':None,'continent':None,'timezonestr':None}
		#get closest value to lat lon
		dprint('gnearest: using %s,%s' %(lat,lon))
		diff = {}
		sql = 'SELECT id,latitude,longitude FROM geonames WHERE latitude >= %s AND latitude <= %s AND longitude >= %s AND longitude <= %s' % (lat-0.5,lat+0.5,lon-0.5,lon+0.5)
		self.gquery(sql)
		for row in self.gcursor:
			diff[zonetab.distance( lat , lon , row['latitude'] , row['longitude'])]=row['id']
		self.gclose()
		keys=list(diff.keys())
		keys.sort()
 
		dict={}
		if keys == []:
			dict = {'country':None,'admin1':None,'geonameid':None,'continent':None,'timezonestr':None}
			dprint('gnearest: no town found within 66km range!')
		else:
			sql = 'SELECT * FROM geonames WHERE id=%s LIMIT 1' % (diff[keys[0]])
			self.gquery(sql)
			geoname = self.gcursor.fetchone()
			self.gclose()
			dict['country']=geoname['country']
			dict['admin1']=geoname['admin1']
			dict['geonameid']=geoname['geonameid']
			dict['timezonestr']=geoname['timezone']
			sql = 'SELECT * FROM countryinfo WHERE isoalpha2="%s" LIMIT 1' % (geoname['country'])
			self.gquery(sql) 
			countryinfo = self.gcursor.fetchone()
			dict['continent']=countryinfo['continent']
			self.gclose()
			dprint('gnearest: found town %s at %s,%s,%s' % (geoname['name'],geoname['latitude'],
				geoname['longitude'],geoname['timezone']))
		return dict

	def gquery(self, sql, tuple=None):
		self.glink = sqlite3.connect(app.cfg.geonamesdb)
		self.glink.row_factory = sqlite3.Row
		self.gcursor = self.glink.cursor()
		if tuple:
			self.gcursor.execute(sql,tuple)
		else:
			self.gcursor.execute(sql)

	def gclose(self):
		self.glink.commit()
		self.gcursor.close()
		self.glink.close()

	def open(self):
		self.link = sqlite3.connect(app.cfg.astrodb)
		self.link.row_factory = sqlite3.Row
		self.cursor = self.link.cursor()

		self.plink = sqlite3.connect(app.cfg.peopledb)
		self.plink.row_factory = sqlite3.Row
		self.pcursor = self.plink.cursor()

	def close(self):
		self.cursor.close()
		self.pcursor.close()
		self.link.close()
		self.plink.close()

class ViewSVG(Gtk.Widget):
	def __init__(self, path, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# loads now SVG files, Pixbuf not needed anymore
		self.setupSVG(path)

	def setupSVG(self, path):
		self.texture = Gdk.Texture.new_from_filename(path)
		self.scale = 1

	def do_snapshot(self, snapshot):
		width = self.texture.get_intrinsic_width() * self.scale
		height = self.texture.get_intrinsic_height() * self.scale
		self.texture.snapshot(snapshot, width, height)

	def do_get_request_mode(self):
		return Gtk.SizeRequestMode.CONSTANT_SIZE

	def do_measure(self, orientation, for_size):
		if orientation == Gtk.Orientation.HORIZONTAL:
			width = self.texture.get_intrinsic_width() * self.scale
			return (width, width, -1, -1)
		else:
			height = self.texture.get_intrinsic_height() * self.scale
			return (height, height, -1, -1)

def dprint(str):
	""" debug print function """
	if "--debug" in sys.argv or DEBUG:
		print('%s' % str)

class AstroWindow(Gtk.ApplicationWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.props.show_menubar = True
		""" >>> set icon changed in GTK4 """

		#belonges in the windows group and hence have the 'win' prefix
		max_action = Gio.SimpleAction.new_stateful(
			"maximize", None, GLib.Variant.new_boolean(False)
		)
		max_action.connect("change-state", self.on_maximize_toggle)
		self.add_action(max_action)

		# Keep it in sync with the actual state
		self.connect(
			"notify::maximized",
			lambda obj, _pspec: max_action.set_state(
				GLib.Variant.new_boolean(obj.props.maximized)
			),
		)
		#Menuitem 'About'
		about_action = Gio.SimpleAction.new("about", None)
		about_action.connect("activate", self.about_callback)
		self.add_action(about_action)

		# Menu 'Chart'
		newChart_action = Gio.SimpleAction.new("newChart", None)
		newChart_action.connect("activate", self.eventDataNew_callback)
		self.add_action(newChart_action)
		openChart_action = Gio.SimpleAction.new("openChart", None)
		openChart_action.connect("activate", self.openChart_callback)
		self.add_action(openChart_action)
		saveChart_action = Gio.SimpleAction.new("saveChart", None)
		saveChart_action.connect("activate", self.saveChart_callback)
		self.add_action(saveChart_action)
		 # Menu item 'Import'
		import_action = Gio.SimpleAction.new_stateful(
			"import", GLib.VariantType.new('s'), #submit a string type
			GLib.Variant.new_string('importAstrolog')
		)
		import_action.connect("activate", self.import_callback)
		self.add_action(import_action)
		 # Menu item 'Export'
		export_action = Gio.SimpleAction.new_stateful(
			"export", GLib.VariantType.new('s'), #submit a string type
			GLib.Variant.new_string('jpgfile')
		)
		export_action.connect("activate", self.export_callback)
		self.add_action(export_action)
		# Menu item 'Close'
		close_action = Gio.SimpleAction.new("close", None)
		close_action.connect("activate", self.on_close)
		self.add_action(close_action)

		# Menu 'Event'
		event_action = Gio.SimpleAction.new("eventData", None)
		event_action.connect("activate", self.eventData_callback)
		self.add_action(event_action)
		openBase_action = Gio.SimpleAction.new("openDatabase", None)
		openBase_action.connect("activate", self.openDatabase_callback)
		self.add_action(openBase_action)
		openFamous_action = Gio.SimpleAction.new("openDataFamous", None)
		openFamous_action.connect("activate", self.openDataFamous_callback)
		self.add_action(openFamous_action)

		# Menu 'Settings'
		setLocation_action = Gio.SimpleAction.new("settingsLocation", None)
		setLocation_action.connect("activate", self.setLocation_callback)
		self.add_action(setLocation_action)
		setConfig_action = Gio.SimpleAction.new("settingsConfiguration", None)
		setConfig_action.connect("activate", self.setConfiguration_callback)
		self.add_action(setConfig_action)

		# Menu 'Chart Types'
		radix_action = Gio.SimpleAction.new("specialRadix", None)
		radix_action.connect("activate", self.specialRadix_callback)
		self.add_action(radix_action)
		transit_action = Gio.SimpleAction.new("specialTransit", None)
		transit_action.connect("activate", self.specialTransit_callback)
		self.add_action(transit_action)

		chart_type_action = Gio.SimpleAction.new_stateful("chartType",GLib.VariantType.new('s'),GLib.Variant.new_string('Synastry'))
		chart_type_action.connect("activate", self.chartType_callback)
		self.add_action(chart_type_action)

		solar_action = Gio.SimpleAction.new("specialSolar", None)
		solar_action.connect("activate", self.specialSolar_callback)
		self.add_action(solar_action)
		progression_action = Gio.SimpleAction.new("specialProgression", None)
		progression_action.connect("activate", self.specialProgression_callback)
		self.add_action(progression_action)

		# Menu 'Tables'
		timeline_action = Gio.SimpleAction.new("tableMonthlyTimeline", None)
		timeline_action.connect("activate", self.tableMonthlyTimeline_callback)
		self.add_action(timeline_action)
		cuspaspects_action = Gio.SimpleAction.new("tableCuspAspects", None)
		cuspaspects_action.connect("activate", self.tableCuspAspects_callback)
		self.add_action(cuspaspects_action)

		# Menu 'Zoom'
		zoom_action = Gio.SimpleAction.new_stateful("zoom", GLib.VariantType.new('s'), GLib.Variant.new_string('zIn'))
		zoom_action.connect("activate", self.zoom_callback)
		self.add_action(zoom_action)
		app.set_accels_for_action(detailed_action_name="win.zoom::zIn", accels=["<Ctrl>plus"])
		app.set_accels_for_action(detailed_action_name="win.zoom::z100", accels=["<Ctrl>1"])
		app.set_accels_for_action(detailed_action_name="win.zoom::zOut", accels=["<Ctrl>minus"])

		# Menu 'Extra'
		exportdb_action = Gio.SimpleAction.new("exportdb", None)
		exportdb_action.connect("activate", self.exportdb_callback)
		self.add_action(exportdb_action)
		importdb_action = Gio.SimpleAction.new("importdb", None)
		importdb_action.connect("activate", self.importdb_callback)
		self.add_action(importdb_action)

		self.first_time = True
		self.updateUI()

		# display astrological chart
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.set_child(box)
		scrolled_window = Gtk.ScrolledWindow()
		# Draw svg pixbuf
		chart_name = app.makeSVG()
		#drawing_area to render SVG
		self.image = ViewSVG(chart_name)
		self.image.set_vexpand(True)
		self.image.set_hexpand(True)
		self.image.set_valign(Gtk.Align.CENTER)
		self.image.set_halign(Gtk.Align.CENTER)
		scrolled_window.set_child(self.image)
		box.append(scrolled_window)

	def on_change_label_state(self, action, value):
		action.set_state(value)
		self.label.set_text(value.get_string())

	def on_maximize_toggle(self, action, value):
		action.set_state(value)
		if value.get_boolean():
			self.maximize()
		else:
			self.unmaximize()

	"""
	Function to check if we have an internet connection
	for geonames.org geocoder
	"""
	def checkInternetConnection(self):
		if app.db.getAstrocfg('use_geonames.org') == "0":
			self.iconn = False
			dprint('iconn: not using geocoding!')
			return
		# from openastromod import timeoutsocket
		# timeoutsocket.setDefaultSocketTimeout(2)
		HOST='api.geonames.org'
		PORT=80
		s = None
		try:
			socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM)
		except socket.error as msg:
			self.iconn = False
			dprint('iconn: no connection (getaddrinfo)')
			return
		for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
			af, socktype, proto, canonname, sa = res
			try:
				s = socket.socket(af, socktype, proto)
			except socket.error as msg:
				s = None
				continue
			try:
				s.connect(sa)
			except (socket.error, timeoutsocket.Timeout):
				s.close()
				s = None
				continue
			break
		if s is None:
			self.iconn = False
			dprint('iconn: no connection')
		else:
			self.iconn = True
			dprint('iconn: got connection')
			#timeoutsocket.setDefaultSocketTimeout(20)
			s.close()
		return

	def updateUI(self):
		#get menubar of application
		parent_app = self.get_application()
		menu = parent_app.get_menubar()
		#create history actions, last will be first
		entries = app.db.history
		l = len(entries)
		t_item = Template(M_ITEM)
		items = []
		if len(entries) > 0:
			#maximal 10 entries
			i = LIMIT
			for entry in reversed(entries):
				i -= 1
				l -= 1
				if (i < 0) or (l < 0):
					break
				# substitute id and name
				item = t_item.substitute(db='historydb', idx=entry[0], label=entry[1])
				items.append(item)
			history_items = '\n'.join(items)
		if self.first_time:
			#generate 'Chart' menu
			chart_builder = Gtk.Builder()
			chart_builder.add_from_string(CHART_XML)
			self.chart_menu = chart_builder.get_object("ChartUI")
			#make action for 'quickopendb'
			history_action = Gio.SimpleAction.new_stateful(
				"historydb",
				GLib.VariantType.new('i'),
				GLib.Variant.new_int32(value=0)
			)
			history_action.connect("activate", self.historydb_callback)
			self.add_action(history_action)
		else:
			menu.remove(0)
		if len(items) > 0:
			history_xml = BEGIN_XML + history_items + END_XML
		else:
			#insert 'empty' menu item
			history_xml = BEGIN_XML + E_ITEM + END_XML
		update_builder = Gtk.Builder()
		update_builder.add_from_string(history_xml)
		history_menu = update_builder.get_object("UpdateUI")
		self.chart_menu.insert_submenu(3, 'History', history_menu)
		#becomes first item in menubar
		menu.insert_submenu(1, 'Chart', self.chart_menu)
		# create 'Quick Open' actions
		self.DB = app.db.getDatabase()
		t_item = Template(M_ITEM)
		items = []
		for entry in self.DB:
			# substitute id and name
			item = t_item.substitute(db='quickopendb', idx=entry['id'], label=entry['name'])
			items.append(item)
		quick_open_items = '\n'.join(items)
		if self.first_time:
			#generate 'Event' menu
			event_builder = Gtk.Builder()
			event_builder.add_from_string(EVENT_XML)
			self.event_menu = event_builder.get_object("EventUI")
			#make action for 'quickopendb'
			quick_open_action = Gio.SimpleAction.new_stateful(
				"quickopendb",
				GLib.VariantType.new('i'),
				GLib.Variant.new_int32(value=0)
			)
			quick_open_action.connect("activate", self.quickopendb_callback)
			self.add_action(quick_open_action)
		else:
			menu.remove(2)
		if len(items) > 0:
			quick_open_xml = BEGIN_XML + quick_open_items + END_XML
		else:
			#insert 'empty' menu item
			quick_open_xml = BEGIN_XML + E_ITEM + END_XML
		update_builder = Gtk.Builder()
		update_builder.add_from_string(quick_open_xml)
		quick_open_menu = update_builder.get_object("UpdateUI")
		self.event_menu.insert_submenu(1, 'Quick Open Database', quick_open_menu)
		menu.insert_submenu(2, 'Event', self.event_menu)
		self.first_time = False

	def historydb_callback(self, action, parameter):
		idx = parameter.get_int32()
		action.set_state(parameter)
		for entry in app.db.history:
			if entry['id'] == idx:
				self.updateChartList(None, entry)
				break

	def quickopendb_callback(self, action, parameter):
		idx = parameter.get_int32()
		action.set_state(parameter)
		for entry in self.DB:
			if entry['id'] == idx:
				self.updateChartList(None, entry)
				break

	def updateChartList(self, b, list):
		""" Update the chart with input list data """
		app.type = "Radix"
		app.charttype = app.label["radix"]
		app.name = str(list["name"])
		app.year = int(list["year"])
		app.month = int(list["month"])
		app.day = int(list["day"])
		app.hour = float(list["hour"])
		app.geolon = float(list["geolon"])
		app.geolat = float(list["geolat"])
		app.altitude = int(list["altitude"])
		app.location = str(list["location"])
		app.timezone = float(list["timezone"])
		app.countrycode = ''
		if "countrycode" in list:
			app.countrycode = list["countrycode"]
		if "timezonestr" in list:
			app.timezonestr = list["timezonestr"]
		else:
			app.timezonestr = app.db.gnearest(app.geolat,app.geolon)['timezonestr']
		app.geonameid = None
		if "geonameid" in list:
			app.geonameid = list['geonameid']
		app.utcToLocal()
		self.updateChart()

	def updateChart(self):
		chart_name = app.makeSVG()
		self.image.setupSVG(chart_name)
		self.image.queue_resize()

	def updateChartData(self):
		# check for internet connection
		self.checkInternetConnection()
		if self.iconn:
			result = geoname.search(self.geoLoc.get_text(),self.geoCC.get_text())
			if result:
				self.geoLocFound = True
				lat = float(result[0]['lat'])
				lon = float(result[0]['lng'])
				gid = int(result[0]['geonameId'])
				cc = result[0]['countryCode']
				tzstr = result[0]['timezonestr']
				loc = '%s, %s' % (result[0]['name'],result[0]['countryName'])
				dprint('updateChartData: %s,%s found; %s %s %s' % (
					self.geoLoc.get_text(),self.geoCC.get_text(),lat,lon,loc))
			else:
				self.geoLocFound = False
				#revert to defaults
				lat = app.geolat
				lon = app.geolon
				loc = app.location
				cc = app.countrycode
				tzstr = app.timezonestr
				gid = app.geonameid

				dprint('updateChartData: %s,%s not found, reverting to defaults' % (
					self.geoLoc.get_text(),self.geoCC.get_text()) )

				self.geoLoc.set_text(_('City not found! Try Again.'))
				return
		else:
			# using geonames database
			self.geoLocFound = True
			lat = float(self.GEON_lat)
			lon = float(self.GEON_lon)
			loc = self.GEON_loc
			cc = self.GEON_cc
			tzstr = self.GEON_tzstr
			gid = self.GEON_id
		# calculate timezone
		app.timezonestr = tzstr
		app.geonameid = gid
		# aware datetime object
		dt_input = datetime.datetime(self.dateY.get_value_as_int(), self.dateM.get_value_as_int(), self.dateD.get_value_as_int(), self.timeH.get_value_as_int(), self.timeM.get_value_as_int(), self.timeS.get_value_as_int())
		dt = pytz.timezone(app.timezonestr).localize(dt_input)

		dprint( dt.strftime('%Y-%m-%d %H:%M:%S %Z%z') )
		dprint( 'Daylight Saving Time: %s' %((dt.dst().seconds / 3600.0)) )

		# naive datetime object UTC
		dt_utc = dt.replace(tzinfo=None) - dt.utcoffset()
		# set globals
		app.year = dt_utc.year
		app.month = dt_utc.month
		app.day = dt_utc.day
		app.hour = app.decHourJoin(dt_utc.hour, dt_utc.minute, dt_utc.second)
		app.timezone = app.offsetToTz(dt.utcoffset())
		app.name = self.name.get_text()
		# location
		app.geolat=lat
		app.geolon=lon
		app.location=loc
		app.countrycode=cc
		# update local time
		app.utcToLocal()
		# update labels
		labelDar = str(app.year_loc)+'-%(#1)02d-%(#2)02d' % {'#1':app.month_loc,'#2':app.day_loc}
		self.labelDate.set_text(labelDar)
		labelTzStr = '%(#1)02d:%(#2)02d:%(#3)02d' % {'#1':app.hour_loc,'#2':app.minute_loc,'#3':app.second_loc} + app.decTzStr(app.timezone)
		self.labelTz.set_text(labelTzStr)
		self.ename.set_text(app.name)
		self.entry2.set_text(' %s: %s\n %s: %s\n %s: %s' % ( _('Latitude'),lat,_('Longitude'),lon,_('Location'),loc) )

	""" Open chart in OAC format """
	def openChart_callback(self, action, parameter):
		gio_list_store = Gio.ListStore.new(Gtk.FileFilter)
		gio_list_store.append(item=FILTER_ALL_FILES)
		gio_list_store.append(item=FILTER_OAC_FILES)
		gio_list_store.append(item=FILTER_TXT_FILES)

		file_dialog = Gtk.FileDialog.new()
		file_dialog.set_title(title=_('Open'))
		file_dialog.set_initial_name(name=_('file-name'))
		file_dialog.set_modal(modal=True)
		file_dialog.set_filters(filters=gio_list_store)
		file_dialog.open(parent=self, callback=self.on_file_dialog_dismissed)

	def on_file_dialog_dismissed(self, file_dialog, gio_task):
		if gio_task.get_name() == 'gtk_file_dialog_open':
			try:
				local_file = file_dialog.open_finish(gio_task)
			except GLib.Error:
				return
			app.importOAC(local_file)
			self.eventData(False)
		elif gio_task.get_name() == 'gtk_file_dialog_save':
			try:
				local_file = file_dialog.save_finish(gio_task)
			except GLib.Error:
				return
			app.exportOAC(local_file)

		"""
		print(f'File name: {local_file.get_basename()}')
		print(f'File path: {local_file.get_path()}')
		print(f'File URI: {local_file.get_uri()}\n')
		"""

	""" Select file to import by FileDialog """
	def file_to_open(self, filters, name, import_app):
		file_dialog = Gtk.FileDialog.new()
		file_dialog.set_title(title=_('Select file to import'))
		file_dialog.set_initial_name(name)
		file_dialog.set_modal(modal=True)
		file_dialog.set_filters(filters=filters)
		file_dialog.open(parent=self, callback=self.on_open_file_dialog_completed, user_data=import_app)

	def on_open_file_dialog_completed(self, file_dialog, gio_task, import_app):
		try:
			local_file = file_dialog.open_finish(gio_task)
		except GLib.Error:
			return
		import_app(local_file)
		self.updateChart()

	""" Import chart in different formats """
	def import_callback(self, action, parameter):
		# mark choosed menu item
		selected = parameter.get_string()
		action.set_state(parameter)
		gio_filters = Gio.ListStore.new(Gtk.FileFilter)
		gio_filters.append(item=FILTER_ALL_FILES)
		#select file formats
		if selected == 'importOroboros':
			gio_filters.append(item=FILTER_XML_FILES)
			self.file_to_open(filters=gio_filters, name='', import_app=app.importOroboros)
		elif selected == 'importAstrolog':
			gio_filters.append(item=FILTER_DAT_FILES)
			self.file_to_open(filters=gio_filters, name='', import_app=app.importAstrolog)
		elif selected == 'importSkylendar':
			gio_filters.append(item=FILTER_SKIF_FILES)
			self.file_to_open(filters=gio_filters, name='', import_app=app.importSkylendar)
		elif selected == 'importZet8':
			gio_filters.append(item=FILTER_ZBS_FILES)
			self.file_to_open(filters=gio_filters, name='', import_app=app.importZet8)

		dprint('Dialog closed, no files selected')


	""" Save chart in OAC format """
	def saveChart_callback(self, action, parameter):
		gio_list_store = Gio.ListStore.new(Gtk.FileFilter)
		gio_list_store.append(item=FILTER_ALL_FILES)
		gio_list_store.append(item=FILTER_OAC_FILES)
		gio_list_store.append(item=FILTER_TXT_FILES)
		file_dialog = Gtk.FileDialog.new()
		file_dialog.set_title(title=_('Save Chart'))
		file_dialog.set_initial_name(name=_('AstroChart.oac'))
		file_dialog.set_modal(modal=True)
		file_dialog.set_filters(filters=gio_list_store)
		file_dialog.save(parent=self, callback=self.on_file_dialog_dismissed)

	""" Select file for saving by FileDialog"""
	def file_to_save(self, filters, name, export_app):
		file_dialog = Gtk.FileDialog.new()
		file_dialog.set_title(title=_('Select file for saving'))
		file_dialog.set_initial_name(name=name)
		file_dialog.set_modal(modal=True)
		file_dialog.set_filters(filters=filters)
		file_dialog.save(parent=self, callback=self.save_file_dialog_completed, user_data=export_app)

	def save_file_dialog_completed(self, file_dialog, gio_task, export_app):
		try:
			local_file = file_dialog.save_finish(gio_task)
		except GLib.Error:
			return
		export_app(local_file)

	def exportPNG(self, local_file):
		os.system("%s %s %s" % ('magick', app.cfg.tempfilename,"'"+local_file.get_path()+"'"))

	def exportJPG(self, local_file):
		os.system("%s %s %s" % ('magick', app.cfg.tempfilename,"'"+local_file.get_path()+"'"))

	def exportSVG(self, local_file):
		copyfile(app.cfg.tempfilename, local_file.get_path())

	def exportPDF(self, local_file):
		#prepare printing into PDF
		settings = Gtk.PrintSettings()
		settings.set_resolution(300)
		print_op = Gtk.PrintOperation()
		print_op.set_unit(Gtk.Unit.MM)
		print_op.set_print_settings(settings)
		print_op.connect("begin_print", self.doPrintBegin)
		print_op.connect("draw_page", self.doPrintDraw)
		print_op.set_export_filename(local_file.get_path())
		result = print_op.run(Gtk.PrintOperationAction.EXPORT, self)
		if result == Gtk.PrintOperationResult.ERROR:
			print_op.cancel()
		return

	""" Export chart in different formats """
	def export_callback(self, action, parameter):
		# mark choosed menu item
		selected = parameter.get_string()
		action.set_state(parameter)
		gio_filters = Gio.ListStore.new(Gtk.FileFilter)
		gio_filters.append(item=FILTER_ALL_FILES)
		#select file formats
		if selected == 'pngfile':
			initial_name = 'AstroData.png'
			gio_filters.append(item=FILTER_PNG_FILES)
			self.file_to_save(filters=gio_filters, name=initial_name, export_app=self.exportPNG)
		elif selected == 'jpgfile':
			initial_name = 'AstroData.jpg'
			gio_filters.append(item=FILTER_JPG_FILES)
			self.file_to_save(filters=gio_filters, name=initial_name, export_app=self.exportJPG)
		elif selected == 'svgfile':
			initial_name = 'AstroData.svg'
			gio_filters.append(item=FILTER_SVG_FILES)
			self.file_to_save(filters=gio_filters, name=initial_name, export_app=self.exportSVG)
		elif selected == 'pdffile':
			initial_name = 'AstroData.pdf'
			gio_filters.append(item=FILTER_PDF_FILES)
			self.file_to_save(filters=gio_filters, name=initial_name, export_app=self.exportPDF)

	"""
	 Print Operations
	"""
	def doPrintBegin(self, operation, context):
		operation.set_n_pages(1)
		operation.set_use_full_page(False)
		ps = Gtk.PageSetup()
		ps.set_orientation(Gtk.PageOrientation.LANDSCAPE)
		ps.set_paper_size(Gtk.PaperSize(Gtk.PAPER_NAME_A4))
		operation.set_default_page_setup(ps)

	def doPrintDraw(self, operation, context, page_nr):
		""" Render SVG into cairo context """
		cr = context.get_cairo_context()
		#draw svg
		printing={}
		printing['pagenum']=page_nr
		printing['width']=context.get_width()
		printing['height']=context.get_height()
		printing['dpi_x']=context.get_dpi_x()
		printing['dpi_y']=context.get_dpi_y()
		#make printing svg
		app.makeSVG(printing=printing)
		svg = Rsvg.Handle.new_from_file(app.cfg.tempfilenameprint)
		#render SVG into cairo context
		if svg is not None:
			cr = Gtk.PrintContext.get_cairo_context(context)
			svg.set_dpi(300)
			viewport = Rsvg.Rectangle()
			viewport.x=0
			viewport.y=0
			viewport.width = Gtk.PrintContext.get_width(context)
			viewport.height = Gtk.PrintContext.get_height(context)
			svg.render_document(cr, viewport)

	def quickopendb_callback(self, action, parameter):
		idx = parameter.get_int32()
		action.set_state(parameter)
		for entry in self.DB:
			if entry['id'] == idx:
				self.updateChartList(None, entry)
				break

	def eventDataNew_callback(self, action, parameter):
		# default location
		app.location = app.home_location
		app.geolat = float(app.home_geolat)
		app.geolon = float(app.home_geolon)
		app.countrycode = app.home_countrycode
		# timezone string, example Europe/Amsterdam
		now = datetime.datetime.now()
		app.timezone_str = zonetab.nearest_tz(app.geolat,app.geolon,zonetab.timezones())[2]
		#aware datetime object
		dt_input = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
		dt = pytz.timezone(app.timezonestr).localize(dt_input)
		#naive utc datetime object
		dt_utc = dt.replace(tzinfo=None) - dt.utcoffset()
		# default
		app.name = _("New Chart")
		app.charttype = app.label["radix"]
		app.year = dt_utc.year
		app.month = dt_utc.month
		app.day = dt_utc.day
		app.hour = app.decHourJoin(dt_utc.hour,dt_utc.minute,dt_utc.second)
		app.timezone = app.offsetToTz(dt.utcoffset())
		# make locals
		app.utcToLocal()
		# open editor
		self.eventData(edit=False)

	def eventData_callback(self, action, parameter):
		self.eventData(edit=False)

	def eventData(self, edit):
		self.settingsLocationMode = False
		# create a new window
		self.window2 = Gtk.Window()
		#??????????????
		#self.window2.set_icon_from_file(app.cfg.iconWindow)
		self.window2.set_title(_("Edit Event Details"))
		#self.window2.connect("delete_event", lambda w,e: self.window2.destroy())
		#self.window2.move(150,150)
		#self.window2.set_border_width(10)
		# check internet connection
		self.checkInternetConnection()
		# create a grid
		grid = Gtk.Grid()
		grid.set_column_spacing(8)
		grid.set_row_spacing(8)
		self.window2.set_child(grid)
		#Name entry
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		grid.attach(hbox, 0, 1, 4, 1)
		label = Gtk.Label(label = _("Name")+":")
		hbox.append(child=label)
		self.name = Gtk.Entry()
		self.name.set_max_length(50)
		self.name.set_width_chars(25)
		self.name.set_text(app.name)
		hbox.prepend(child=self.name)
		# name entry (non editable)
		self.ename = Gtk.Label(label=app.name)
		grid.attach(self.ename, 4, 1, 1, 1)
		# data of location (non editable)
		self.entry2 = Gtk.Label(label=' '+_('Latitude')+': %s\n '%app.geolat+_('Longitude')+': %s\n '%app.geolon+_('Location')+': %s'%app.location)
		grid.attach(self.entry2, 4, 2, 1, 2)
		#do we have a  connection
		if self.iconn:
			#use geocoders,
			hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
			grid.attach(hbox, 0, 3, 1, 1)
			# entry for location (editable)
			label = Gtk.Label(label=_("City")+": ")
			hbox.prepend(child=label)
			self.geoLoc = Gtk.Entry()
			self.geoLoc.set_max_length(50)
			self.geoLoc.set_width_chars(20)
			self.geoLoc.set_text(app.location.partition(',')[0])
			hbox.prepend(child=self.geoLoc)
			label = Gtk.Label(label=" "+_("Country-code")+": ")
			hbox.prepend(child=label)
			self.geoCC = Gtk.Entry()
			self.geoCC.set_max_length(2)
			self.geoCC.set_width_chars(2)
			self.geoCC.set_text(app.countrycode)
			hbox.prepend(child=self.geoCC)
		else:
			#otherwise use geonames sql database and get nearest geoname
			self.GEON_nearest = app.db.gnearest(app.geolat, app.geolon)
			# continents
			self.contbox = Gtk.ComboBox()
			self.contstore = Gtk.ListStore(str, str)
			cell = Gtk.CellRendererText()
			self.contbox.pack_start(cell, False)
			self.contbox.add_attribute(cell, 'text', 0)
			grid.attach(self.contbox, 0, 3, 1, 1)
			#self.contbox.set_wrap_width(1)
			sql = 'SELECT * FROM continent ORDER BY name ASC'
			app.db.gquery(sql)
			continentinfo = []
			self.searchcontinent = {}
			i = 0
			activecont = 3
			for row in app.db.gcursor:
				self.searchcontinent[row['code']] = i
				if row['code'] == self.GEON_nearest['continent']:
					activecont = i
					self.GEON_nearest['continent'] = None
				self.contstore.append([row['name'], row['code']])
				i += 1
			app.db.gclose()
			self.contbox.set_model(self.contstore)
			# countries
			self.countrybox = Gtk.ComboBox()
			cell = Gtk.CellRendererText()
			self.countrybox.pack_start(cell, False)
			self.countrybox.add_attribute(cell, 'text', 0)
			grid.attach(self.countrybox, 1, 3, 1, 1)
			#self.countrybox.set_wrap_width(1) 
			self.countrybox.connect('changed', self.eventDataChangedCountrybox)
			# provinces
			self.provbox = Gtk.ComboBox()
			cell = Gtk.CellRendererText()
			self.provbox.pack_start(cell, False)
			self.provbox.add_attribute(cell, 'text', 0)
			grid.attach(self.provbox, 2, 3, 1, 1)
			#self.provbox.set_wrap_width(1) 
			self.provbox.connect('changed', self.eventDataChangedProvbox)
			# cities
			self.citybox = Gtk.ComboBox()
			cell = Gtk.CellRendererText()
			self.provbox.pack_start(cell, False)
			self.citybox.add_attribute(cell, 'text', 0)
			grid.attach(self.citybox, 3, 3, 1, 1)
			#self.citybox.set_wrap_width(2) 
			self.citybox.connect('changed', self.eventDataChangedCitybox)
			# add search in database
			label = Gtk.Label(label=_("Search City")+":")
			grid.attach(label, 1, 4, 1, 1)
			self.citysearch = Gtk.Entry()
			self.citysearch.set_placeholder_text(_("Name of city?"))
			self.citysearch.set_max_length(34)
			self.citysearch.set_width_chars(24)
			grid .attach(self.citysearch, 2, 4, 1, 1)
			# CAVEAT: ChangedContbox callback relies on other box changes
			self.contbox.connect('changed', self.eventDataChangedContbox)
			self.contbox.set_active(activecont)
			self.citysearchbutton = Gtk.Button.new_with_mnemonic(label = _("Search"))
			self.citysearchbutton.connect("clicked", self.citySearch)
			self.citysearch.connect("activate", self.citySearch)
			grid .attach(self.citysearchbutton, 3, 4, 1, 1)
			label = Gtk.Label(label="("+_("For example: London, GB")+")")
			grid.attach(label, 4, 4, 1, 1)
		# Year month day entry
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		grid.attach(hbox, 0, 5, 3, 1)
		label = Gtk.Label(label=_("Year")+":")
		hbox.prepend(child=label)
		# years from 1800 to 2400
		adjustment = Gtk.Adjustment(lower=1800, upper=2400, step_increment=1, page_increment=10)
		self.dateY = Gtk.SpinButton()
		self.dateY.props.adjustment = adjustment
		self.dateY.set_numeric(True)
		self.dateY.set_value(app.year_loc)
		hbox.prepend(child=self.dateY)
		label = Gtk.Label(label=_("Month")+":")
		hbox.prepend(child=label)
		adjustment = Gtk.Adjustment(lower=1, upper=12, step_increment=1)
		self.dateM = Gtk.SpinButton()
		self.dateM.props.adjustment = adjustment
		self.dateM.set_numeric(True)
		self.dateM.set_value(app.month_loc)
		hbox.prepend(child=self.dateM)
		label = Gtk.Label(label=_("Day")+":")
		hbox.prepend(child=label)
		adjustment = Gtk.Adjustment(lower=1, upper=31, step_increment=1)
		self.dateD = Gtk.SpinButton()
		self.dateD.props.adjustment = adjustment
		self.dateD.set_numeric(True)
		self.dateD.set_value(app.day_loc)
		hbox.prepend(child=self.dateD)
		# date entry (non editable)
		labelDateStr = str(app.year_loc)+'-%(#1)02d-%(#2)02d' % {'#1':app.month_loc, '#2':app.day_loc}
		self.labelDate = Gtk.Label(label=labelDateStr)
		grid.attach(self.labelDate, 3, 5, 1, 1)
		# time entry (editable) (Hour, Minutes, Seconds, Timezone)
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		grid.attach(hbox, 0, 6, 3, 1)
		label = Gtk.Label(label=_("Hour")+":")
		hbox.prepend(child=label)
		adjustment = Gtk.Adjustment(lower=0, upper=23, step_increment=1)
		self.timeH = Gtk.SpinButton()
		self.timeH.props.adjustment = adjustment
		self.timeH.set_numeric(True)
		self.timeH.set_value(app.hour_loc)
		hbox.prepend(child=self.timeH)
		label = Gtk.Label(label=_("Min")+":")
		hbox.prepend(child=label)
		adjustment = Gtk.Adjustment(lower=1, upper=59, step_increment=1)
		self.timeM = Gtk.SpinButton()
		self.timeM.props.adjustment = adjustment
		self.timeM.set_numeric(True)
		self.timeM.set_value(app.minute_loc)
		hbox.prepend(child=self.timeM)
		label = Gtk.Label(label="Sec:")
		hbox.prepend(child=label)
		adjustment = Gtk.Adjustment(lower=0, upper=59, step_increment=1)
		self.timeS = Gtk.SpinButton()
		self.timeS.props.adjustment = adjustment
		self.timeS.set_numeric(True)
		self.timeS.set_value(app.second_loc)
		hbox.prepend(child=self.timeS)
		#time entry (non editable)
		labelTzStr = '%(#1)02d:%(#2)02d:%(#3)02d' % {'#1':app.hour_loc, '#2':app.minute_loc, '#3':app.second_loc} + app.decTzStr(app.timezone)
		self.labelTz = Gtk.Label(label=labelTzStr)
		grid.attach(self.labelTz, 3, 6, 1, 1)
		# buttonbox
		buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		grid.attach(buttonbox, 1, 7, 4, 1)
		# save to database button
		if edit:
			self.savebutton = Gtk.Button.new_with_mnemonic(label = _("Save"))
			self.savebutton.connect("clicked", self.openDatabaseEditAsk)
			buttonbox.prepend(child=self.savebutton)
		else:
			self.savebutton = Gtk.Button.new_with_mnemonic(label = _("Add to Database"))
			self.savebutton.connect("clicked", self.eventDataSaveAsk)
			buttonbox.prepend(child=self.savebutton)
		# Apply button
		button = Gtk.Button.new_with_mnemonic(label = _("Apply"))
		button.connect("clicked", self.eventDataApply)
		buttonbox.prepend(child=button)
  		#ok button
		if edit == False:
			button = Gtk.Button.new_with_mnemonic(label = _("OK"))
			button.connect("clicked", self.eventDataSubmit)
			buttonbox.prepend(child=button)
		# cancel button
		button = Gtk.Button.new_with_mnemonic(label = _("Cancel"))
		button.connect("clicked", lambda w: self.window2.destroy())
		buttonbox.prepend(child=button)
		self.window2.present()

	def citySearch(self, widget):
		#text entry
		city = self.citysearch.get_text()
		#look for country in search string
		isoalpha2 = None
		if city.find(","):
			split = city.split(",")
			for x in range(len(split)):
				sql = "SELECT * FROM countryinfo WHERE (isoalpha2 LIKE ? OR name LIKE ?) LIMIT 1"
				y = split[x].strip()
				app.db.gquery(sql,(y,y))
				result = app.db.gcursor.fetchone()
				if result != None:
					isoalpha2 = result["isoalpha2"]
					city = city.replace(split[x]+",","").replace(","+split[x],"").strip()
					break
		#normal search
		normal = city
		fuzzy = "%"+city+"%"
		if isoalpha2:
			extra = " AND country='%s'"%(isoalpha2)
		else:
			extra = ""
		sql = "SELECT * FROM geonames WHERE (name LIKE ? OR asciiname LIKE ?)%s LIMIT 1" %(extra)
		app.db.gquery(sql,(normal,normal))
		result = app.db.gcursor.fetchone()
		if result == None:
			sql = "SELECT * FROM geonames WHERE (name LIKE ? OR asciiname LIKE ?)%s LIMIT 1" %(extra)
			app.db.gquery(sql,(fuzzy,fuzzy))
			result = app.db.gcursor.fetchone()
		if result == None:
			sql = "SELECT * FROM geonames WHERE (alternatenames LIKE ?)%s LIMIT 1"%(extra)
			app.db.gquery(sql,(fuzzy,))
			result = app.db.gcursor.fetchone()
		if result != None:
			#set continent
			sql = "SELECT continent FROM countryinfo WHERE isoalpha2=? LIMIT 1"
			app.db.gquery(sql,(result["country"],))
			self.contbox.set_active(self.searchcontinent[app.db.gcursor.fetchone()[0]])
			#set country
			self.countrybox.set_active(self.searchcountry[result["country"]])
			#set admin1
			self.provbox.set_active(self.searchprov[result["admin1"]])
			#set city
			self.citybox.set_active(self.searchcity[result["geonameid"]])
		return

	def eventDataChangedContbox(self, combobox):
		model = combobox.get_model()
		index = combobox.get_active()

		store = Gtk.ListStore(str,str)
		store.clear()
		sql = "SELECT * FROM countryinfo WHERE continent=? ORDER BY name ASC"
		app.db.gquery(sql,(model[index][1],))
		list = []
		i=0
		activecountry=0
		self.searchcountry={}
		for row in app.db.gcursor:
			self.searchcountry[row['isoalpha2']]=i
			if self.GEON_nearest['country'] == row['isoalpha2']:
				activecountry=i
				self.GEON_nearest['country']=None
			list.append((row['name'],row['isoalpha2']))
			i+=1
		app.db.gclose()
		for i in range(len(list)):
			store.append(list[i])
		self.countrybox.set_model(store)
		self.countrybox.set_active(activecountry) 
		return
      
	def eventDataChangedCountrybox(self, combobox):
		model = combobox.get_model()
		index = combobox.get_active()
		self.provlist = Gtk.ListStore(str,str,str,str)
		self.provlist.clear()
		sql = "SELECT * FROM admin1codes WHERE country=? ORDER BY admin1 ASC"
		app.db.gquery(sql,(model[index][1],))
		list = []
		i=0
		activeprov=0
		self.searchprov={}
		for row in app.db.gcursor:
			self.searchprov[row["admin1"]] = i
			if self.GEON_nearest['admin1'] == row['admin1']:
				activeprov=i
				self.GEON_nearest['admin1'] = None
			list.append((row['province'],row['country'],row['admin1'],model[index][0]))
			i+=1
		app.db.gclose()
		for i in range(len(list)):
			self.provlist.append(list[i])
		self.provbox.set_model(self.provlist)
		self.provbox.set_active(activeprov) 
		return

	def eventDataChangedProvbox(self, combobox):
		model = combobox.get_model()
		index = combobox.get_active()

		self.citylist = Gtk.ListStore(str,str,str,str,str,str,str,str)
		self.citylist.clear()
		sql = 'SELECT * FROM geonames WHERE country=? AND admin1=? ORDER BY name ASC'
		app.db.gquery(sql,(model[index][1],model[index][2]))
		list = []
		i=0
		activecity=0
		self.searchcity={}
		for row in app.db.gcursor:
			self.searchcity[row["geonameid"]]=i
			if self.GEON_nearest['geonameid'] == row['geonameid']:
				activecity=i
				self.GEON_nearest['geonameid'] = None
			list.append((row['name'], str(row['latitude']), str(row['longitude']), model[index][3], model[index][0], row['country'], str(row['geonameid']), row['timezone']))
			i+=1
		app.db.gclose()
		for i in range(len(list)):
			self.citylist.append(list[i])
		self.citybox.set_model(self.citylist)
		self.citybox.set_active(activecity) 
		return

	def eventDataChangedCitybox(self, combobox):
		model = combobox.get_model()
		index = combobox.get_active()
		#change label for eventdata
		self.GEON_lat = model[index][1]
		self.GEON_lon = model[index][2]
		self.GEON_loc = '%s, %s, %s' % (model[index][0],model[index][4],model[index][3])
		self.GEON_cc = model[index][5]
		self.GEON_id = model[index][6]
		self.GEON_tzstr = model[index][7]
		dprint( 'evenDataChangedCitybox: %s:%s:%s:%s:%s:%s' % (self.GEON_loc, self.GEON_lat, self.GEON_lon, self.GEON_cc, self.GEON_tzstr, self.GEON_id) )
		#settingslocationmode
		if self.settingsLocationMode:
			self.LLoc.set_text(_('Location')+': %s'%(self.GEON_loc))
			self.LLat.set_text(_('Latitude')+': %s'%(self.GEON_lat))
			self.LLon.set_text(_('Longitude')+': %s'%(self.GEON_lon))
		else:
			self.entry2.set_text(' %s: %s\n %s: %s\n %s: %s' % (_('Latitude'), self.GEON_lat, _('Longitude'), self.GEON_lon, _('Location'), self.GEON_loc) )

	def eventDataSaveAsk(self, widget):
		#check for duplicate name
		en = app.db.getDatabase()
		for i in range(len(en)):
			if en[i]["name"] == self.name.get_text():
				dialog = Gtk.Window(title=_('Found Duplicate'))
				""" set_icon """
				#dialog.set_icon_from_file(app.cfg.iconWindow)
				dialog.set_default_size(256,-1)
				vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
				double = Gtk.Label(label=_('There is allready an entry for this name, please choose another'))
				double.set_wrap(True)
				vbox.append(double)
				button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
				#OK button
				button = Gtk.Button.new_with_mnemonic(label=_("OK"))
				button.connect("clicked", lambda w: dialog.destroy())
				button_box.append(button)
				button_box.append(button)
				vbox.append(button_box)
				dialog.set_child(vbox)
				dialog.present()
				return
		#ask for confirmation
		dialog = Gtk.Window(title=_('Question'))
		""" set_icon """
		#dialog.set_icon_from_file(app.cfg.iconWindow)
		dialog.set_default_size(256,-1)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		confirm = Gtk.Label(label=_('Are you sure you want to save this entry to the database?'))
		confirm.set_wrap(True)
		vbox.append(confirm)
		button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		#OK button
		button = Gtk.Button.new_with_mnemonic(label=_("OK"))
		button.connect("clicked", self.eventDataSave, dialog)
		button_box.append(button)
		#Cancel button
		button = Gtk.Button.new_with_mnemonic(label=_("Cancel"))
		button.connect("clicked", lambda w: dialog.destroy())
		button_box.append(button)
		vbox.append(button_box)
		dialog.set_child(vbox)
		dialog.present()
		return

	def eventDataSave(self, dialog):
		#update chart data
		self.updateChartData()
		#set query to save
		#add data from event_natal table
		sql='INSERT INTO event_natal (id, name, year, month, day, hour, geolon, geolat, altitude, location, timezone, notes, image, countrycode, geonameid, timezonestr, extra) VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
		tuple=(app.name,app.year,app.month,app.day,app.hour, app.geolon, app.geolat, app.altitude, app.location, app.timezone, '', '', app.countrycode, app.geonameid, app.timezonestr, '')
		app.db.pquery([sql],[tuple])
		dprint('saved to database: '+app.name)
		dialog.destroy()
		self.updateUI()

	def eventDataSubmit(self, widget):
		#check if no changes were made
		if self.name.get_text() == app.name and \
		self.dateY.get_text() == str(app.year_loc) and \
		self.dateM.get_text() == '%(#)02d' % {'#':app.month_loc} and \
		self.dateD.get_text() == '%(#)02d' % {'#':app.day_loc} and \
		self.eH.get_text() == '%(#)02d' % {'#':app.hour_loc} and \
		self.eM.get_text() == '%(#)02d' % {'#':app.minute_loc} and \
		self.eS.get_text() == '%(#)02d' % {'#':app.second_loc}:
			if self.iconn and self.geoCC.get_text() == app.countrycode and self.geoLoc.get_text() == app.location.partition(',')[0]:
				# go ahead ;)
				self.window2.destroy()
				return
		#apply data
		self.eventDataApply(widget)
		if self.geoLocFound:
			self.window2.destroy()
			#update history
			app.db.addHistory()
			self.updateUI()
			return
		else:
			return

	def eventDataApply(self, widget):
		#update chart data
		app.charttype = app.label["radix"]
		app.type = "Radix"
		app.transit = False
		self.updateChartData()
		#update chart
		self.updateChart()

	def openDatabase_callback(self, action, parameter):
		self.openDatabase(extraDB=None)

	def openDatabase(self, extraDB):
		self.win_OD = Gtk.Window()
		""" set_icon """
		#self.win_OD.set_icon_from_file(app.cfg.iconWindow)
		self.win_OD.set_title(_('Open Database Entry'))
		self.win_OD.set_default_size(600, 450)
		#self.win_OD.move(150,150)
		#self.win_OD.connect("delete_event", lambda w,e: self.win_OD.destroy())
		#listmodel
		self.listmodel = Gtk.ListStore(int, str,str,str)
		self.win_OD_treeview = Gtk.TreeView(model=self.listmodel)
		#selection
		self.win_OD_selection = self.win_OD_treeview.get_selection()
		self.win_OD_selection.set_mode(Gtk.SelectionMode.SINGLE)
		#treeview columns
		self.win_OD_tvcolumn0 = Gtk.TreeViewColumn(_('Id'))
		self.win_OD_tvcolumn1 = Gtk.TreeViewColumn(_('Name'))
		self.win_OD_tvcolumn2 = Gtk.TreeViewColumn(_('Birth Date (Local)'))
		self.win_OD_tvcolumn3 = Gtk.TreeViewColumn(_('Location'))
		#add data from event_natal table
		if extraDB is not None:
			self.win_OD_treeview.set_enable_search(False)
			self.DB = extraDB
		else:
			self.win_OD_treeview.set_enable_search(True)
			self.DB = app.db.getDatabase()
		for i in range(len(self.DB)):
			h,m,s = app.decHour(float(self.DB[i]["hour"]))
			dt_utc=datetime.datetime(int(self.DB[i]["year"]), int(self.DB[i]["month"]), int(self.DB[i]["day"]), h, m, s)
			dt = dt_utc + datetime.timedelta(seconds=float(self.DB[i]["timezone"])*float(3600))
			birth_date = str(dt.year)+'-%(#1)02d-%(#2)02d %(#3)02d:%(#4)02d:%(#5)02d' % {'#1':dt.month,'#2':dt.day,'#3':dt.hour,'#4':dt.minute,'#5':dt.second}
			self.listmodel.append([self.DB[i]["id"],self.DB[i]["name"],birth_date,self.DB[i]["location"]])
		#add columns to treeview
		self.win_OD_treeview.append_column(self.win_OD_tvcolumn0)
		self.win_OD_treeview.append_column(self.win_OD_tvcolumn1)
		self.win_OD_treeview.append_column(self.win_OD_tvcolumn2)
		self.win_OD_treeview.append_column(self.win_OD_tvcolumn3)
		#cell renderers
		cell0 = Gtk.CellRendererText()
		cell1 = Gtk.CellRendererText()
		cell2 = Gtk.CellRendererText()
		cell3 = Gtk.CellRendererText()
		# add cells to columns
		self.win_OD_tvcolumn0.pack_start(cell0, True)
		self.win_OD_tvcolumn1.pack_start(cell1, True)
		self.win_OD_tvcolumn2.pack_start(cell2, True)
		self.win_OD_tvcolumn3.pack_start(cell3, True)
		#set the cell attributes to the listmodel column
		self.win_OD_tvcolumn0.set_attributes(cell0, text = 0)
		self.win_OD_tvcolumn1.set_attributes(cell1, text = 1)
		self.win_OD_tvcolumn2.set_attributes(cell2, text = 2)
		self.win_OD_tvcolumn3.set_attributes(cell3, text = 3)
		#set treeview options
		self.win_OD_treeview.set_search_column(1)
		self.win_OD_tvcolumn0.set_sort_column_id(0)
		self.win_OD_tvcolumn1.set_sort_column_id(1)
		self.win_OD_tvcolumn2.set_sort_column_id(2)
		self.win_OD_tvcolumn3.set_sort_column_id(3)
		#add treeview to scrolledwindow
		scrolled_window = Gtk.ScrolledWindow()
		scrolled_window.set_vexpand(True)
		scrolled_window.set_child(self.win_OD_treeview)
		scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.ALWAYS)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		vbox.set_vexpand(True)
		vbox.append(scrolled_window)
		button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		button_box.set_spacing(4)
		button_box.set_homogeneous(False)
		#buttons
		if extraDB is None:
			button = Gtk.Button.new_with_mnemonic(label=_("Edit"))
			button.connect("clicked", self.openDatabaseEdit)
			button_box.append(button)
			button = Gtk.Button.new_with_mnemonic(label=_("Delete"))
			button.connect("clicked", self.openDatabaseDel)
			button_box.append(button)
			button = Gtk.Button.new_with_mnemonic(label=_("Open"))
			button.connect("clicked", self.openDatabaseOpen)
			button_box.append(button)
			button = Gtk.Button.new_with_mnemonic(label=_("Cancel"))
			button.connect("clicked", lambda w: self.win_OD.destroy())
			button_box.append(button)
		else:
			label=Gtk.Label(label=_("Search Name")+":")
			self.namesearch = Gtk.Entry()
			self.namesearch.set_max_length(34)
			self.namesearch.set_width_chars(24)
			self.namesearchbutton = Gtk.Button.new_with_mnemonic(label=_('Search'))
			self.namesearchbutton.connect("clicked", self.nameSearch)
			self.namesearch.connect("activate", self.nameSearch)
			self.nameresetbutton = Gtk.Button.new_with_mnemonic(label=_('Reset'))
			self.nameresetbutton.connect("clicked", self.nameSearchReset)
			button_box.append(self.nameresetbutton)
			button_box.append(label)
			button_box.append(self.namesearch)
			button_box.append(self.namesearchbutton)
			button = Gtk.Button.new_with_mnemonic(label=_("Open"))
			button.connect("clicked", self.openDatabaseOpen)
			button_box.prepend(button)
			button = Gtk.Button.new_with_mnemonic(label=_("Close"))
			button.connect("clicked", lambda w: self.win_OD.destroy())
			button_box.append(button)
		#display window
		self.win_OD_treeview.connect("row-activated", lambda w,e,f: self.openDatabaseOpen(w))
		vbox.append(button_box)
		self.win_OD.set_child(vbox)
		self.win_OD_treeview.set_model(model=self.listmodel)
		self.win_OD.present()
		return

	def openDatabaseEdit(self, widget):
		model = self.win_OD_selection.get_selected()[0]
		iter = self.win_OD_selection.get_selected()[1]
		for i in range(len(self.DB)):
			if self.DB[i]["id"] == model.get_value(iter,0):
				self.oDE_list = self.DB[i]
		app.type="Radix"
		app.charttype = app.label["radix"]
		app.transit = False
		self.updateChartList(widget, self.oDE_list)
		self.eventData(edit=True)
		return

	def openDatabaseEditAsk(self, widget):
		#check for duplicate name without duplicate id
		en = app.db.getDatabase()
		for i in range(len(en)):
			if en[i]["name"] == self.name.get_text() and self.oDE_list["id"] != en[i]["id"]:
				dialog = Gtk.Window(title=_('Duplicate'))

				dialog.add_button(Gtk.STOCK_OK, Gtk.ResponseType.DELETE_EVENT)
				""" set_icon """
				#dialog.set_icon_from_file(app.cfg.iconWindow)
				dialog.connect("response", lambda w,e: dialog.destroy())
				dialog.connect("close", lambda w,e: dialog.destroy())
				dialog.vbox.append(Gtk.Label(label=_('There is allready an entry for this name, please choose another')))
				dialog.present()
				return
		#ask for confirmation
		dialog=Gtk.Dialog(
			title=_('Question'),
			parent=self.window2,
			flags=0
		)
		dialog.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.REJECT)
		dialog.add_button(Gtk.STOCK_OK, Gtk.ResponseType.ACCEPT)
		dialog.set_destroy_with_parent(True)
		""" set_icon """
		#dialog.set_icon_from_file(app.cfg.iconWindow)
		dialog.connect("close", lambda w,e: dialog.destroy())
		dialog.connect("response",self.openDatabaseEditSave)
		dialog.vbox.append(Gtk.Label(label=_('Are you sure you want to Save?')))
		dialog.present()

	def openDatabaseOpen(self, widget):
		model = self.win_OD_selection.get_selected()[0]
		iter = self.win_OD_selection.get_selected()[1]
		for i in range(len(self.DB)):
			if self.DB[i]["id"] == model.get_value(iter,0):
				list = self.DB[i]
		app.type="Radix"
		app.charttype = app.label["radix"]
		app.transit = False
		self.updateChartList(widget, list)
		self.win_OD.destroy()

	def openDatabaseEditSave(self, widget, response_id):
		if response_id == Gtk.ResponseType.ACCEPT:
			#update chart data
			self.updateChartData()
			#set query to save
			sql = 'UPDATE event_natal SET name=?,year=?,month=?,day=?,hour=?, geolon=?, geolat=?, altitude=?, location=?, timezone=?, notes=?, image=?, countrycode=?, timezonestr=?, geonameid=? WHERE id=?'
			values = (app.name, app.year, app.month, app.day, app.hour, app.geolon, app.geolat, app.altitude, app.location, app.timezone, '', '', app.countrycode,app.timezonestr,app.geonameid,self.oDE_list["id"])
			app.db.pquery([sql],[values])
			dprint('saved edit to database: '+app.name)
			widget.destroy()
			self.window2.destroy()
			self.win_OD.destroy()
			self.openDatabase_callback( None, None)
			self.updateUI()
		else:
			widget.destroy()
			dprint('rejected save to database')

	def openDatabaseDel(self, widget):
		#get name from selection
		model = self.win_OD_selection.get_selected()[0]
		iter = self.win_OD_selection.get_selected()[1]
		for i in range(len(self.DB)):
			if self.DB[i]["id"] == model.get_value(iter,0):
				self.ODDlist = self.DB[i]
		name = self.ODDlist["name"]
		dialog = Gtk.Window(title=_('Question'))
		vbox = Gtk.Box(orientation=Gtk.Orientation.Vertical)
		button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


		vbox.append(Gtk.Label(label=_('Are you sure you want to delete')+' '+name+'?'))

		dialog.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.REJECT)
		dialog.add_button(Gtk.STOCK_OK, Gtk.ResponseType.ACCEPT)
		dialog.set_destroy_with_parent(True)
		dialog.connect("close", lambda w,e: dialog.destroy())
		dialog.connect("response",self.openDatabaseDelDo)

		vbox.append(button_box)
		dialog.set_child(vbox)
		dialog.present()

	def openDatabaseDelDo(self, widget, response_id):
		if response_id == Gtk.ResponseType.ACCEPT:
			#get id from selection
			del_id = self.ODDlist["id"]
			#delete database entry
			sql='DELETE FROM event_natal WHERE id='+str(del_id)
			app.db.pquery([sql])

			dprint('deleted database entry: '+self.ODDlist["name"])

			widget.destroy()
			self.win_OD.destroy()
			self.openDatabase(extraDB=None)
			self.updateUI()
		else:
			widget.destroy()
			dprint('rejected database deletion')

	def nameSearch(self, widget):
		self.listmodel.clear()
		self.DB = self.getDatabaseFamous(limit="15",search=self.namesearch.get_text())
		for i in range(len(self.DB)):
			h, m, s = app.decHour(float(self.DB[i]["hour"]))
			dt_utc=datetime.datetime(int(self.DB[i]["year"]),int(self.DB[i]["month"]),int(self.DB[i]["day"]),h,m,s)
			dt = dt_utc + datetime.timedelta(seconds=float(self.DB[i]["timezone"])*float(3600))
			birth_date = str(dt.year)+'-%(#1)02d-%(#2)02d %(#3)02d:%(#4)02d:%(#5)02d' % {'#1':dt.month,'#2':dt.day,'#3':dt.hour,'#4':dt.minute,'#5':dt.second}
			self.listmodel.append([self.DB[i]["id"],self.DB[i]["name"],birth_date,self.DB[i]["location"]])
		return

	def nameSearchReset(self, widget):
		self.listmodel.clear()
		self.DB = self.getDatabaseFamous(limit="2000", search=None)
		for i in range(len(self.DB)):
			h,m,s = app.decHour(float(self.DB[i]["hour"]))
			dt_utc=datetime.datetime(int(self.DB[i]["year"]),int(self.DB[i]["month"]),int(self.DB[i]["day"]),h,m,s)
			dt = dt_utc + datetime.timedelta(seconds=float(self.DB[i]["timezone"])*float(3600))
			birth_date = str(dt.year)+'-%(#1)02d-%(#2)02d %(#3)02d:%(#4)02d:%(#5)02d' % {'#1':dt.month,'#2':dt.day,'#3':dt.hour,'#4':dt.minute,'#5':dt.second}
			self.listmodel.append([self.DB[i]["id"],self.DB[i]["name"],birth_date,self.DB[i]["location"]])
		return

	def openDataFamous_callback(self, action, parameter):
		self.openDatabase(extraDB=self.getDatabaseFamous(limit="2000", search=None))

	def getDatabaseFamous(self, limit, search):
		""" Start searching from year 1800 onwards """
		self.flink = sqlite3.connect(app.cfg.famousdb)
		self.flink.row_factory = sqlite3.Row
		self.fcursor = self.flink.cursor()
		if search is not None:
			sql='SELECT * FROM famous WHERE year>? AND \
			(lastname LIKE ? OR firstname LIKE ? OR name LIKE ?)\
			 LIMIT %s'%(limit)
			self.fcursor.execute(sql,(1800,search,search,search))
		else:
			sql='SELECT * FROM famous WHERE year>? LIMIT %s'%(limit)
			self.fcursor.execute(sql,(1800,))
		oldDB=self.fcursor.fetchall()
		self.fcursor.close()
		self.flink.close()
		#p rocess database
		newDB = []
		for a in range(len(oldDB)):
			# minus years
			if oldDB[a][12] == '571/': #Muhammad
				year = 571
			elif oldDB[a][12] <= 0:
				year = 1
			else:
				year = oldDB[a][12]
			month = oldDB[a][13]
			day = oldDB[a][14]
			hour = oldDB[a][15]
			h,m,s = app.decHour(hour)
			# aware datetime object
			dt_input = datetime.datetime(year,month,day,h,m,s)
			dt = pytz.timezone(oldDB[a][20]).localize(dt_input)
			# naive utc datetime object
			dt_utc = dt.replace(tzinfo=None) - dt.utcoffset()
			# timezone
			timezone=app.offsetToTz(dt.utcoffset())
			year = dt_utc.year
			month = dt_utc.month
			day = dt_utc.day
			hour = app.decHourJoin(dt_utc.hour,dt_utc.minute,dt_utc.second)
			newDB.append({
						"id":oldDB[a][0], #index
						"name":oldDB[a][3]+" "+oldDB[a][4], #christian name, name
						"year":year, #year
						"month":month, #month
						"day":day, #day
						"hour":hour, #hour
						"geolon":oldDB[a][18], #geolon
						"geolat":oldDB[a][17], #geolat
						"altitude":"25", #altitude
						"location":oldDB[a][16], #location
						"timezone":timezone, #timezone
						"notes":"",#notes
						"image":"",#image
						"countrycode":oldDB[a][8], #countrycode
						"geonameid":oldDB[a][19], #geonameid
						"timezonestr":oldDB[a][20], #timezonestr
						"extra":"" #extra
						})
		return newDB

	def chartType_callback(self, action, parameter):
		selected = parameter.get_string()
		action.set_state(parameter)
		if selected == "Synastry":
			selectstr = "Select for Synastry"
		elif selected == "Composite":
			selectstr = "Select for Composite"
		elif selected == "Combine":
			selectstr = "Select for Combine"
		self.openDatabaseSelect(selectstr, selected)

	def openDatabaseSelect(self, selectstr, type):
		self.win_OD = Gtk.Window()
		self.win_OD.set_title(_('Select Database Entry'))
		""" >>> set_icon """
		#self.win_OD.set_icon_from_file(app.cfg.iconWindow)
		self.win_OD.set_size_request(512, 464)
		#self.win_OD.move(150,150)
		#self.win_OD.connect("delete_event", lambda w,e: self.openDatabaseSelectReject())
		#define listmodel		
		self.listmodel = Gtk.ListStore(int,str,str,str)	
		self.win_OD_treeview = Gtk.TreeView(model=self.listmodel)
		#selection
		self.win_OD_selection = self.win_OD_treeview.get_selection()
		self.win_OD_selection.set_mode(Gtk.SelectionMode.SINGLE)
		#treeview columns		
		self.win_OD_tvcolumn0 = Gtk.TreeViewColumn(_('Id'))
		self.win_OD_tvcolumn1 = Gtk.TreeViewColumn(_('Name'))
		self.win_OD_tvcolumn2 = Gtk.TreeViewColumn(_('Birth Date (Local)'))
		self.win_OD_tvcolumn3 = Gtk.TreeViewColumn(_('Location'))
		#add data from event_natal table
		self.DB = app.db.getDatabase()
		for i in range(len(self.DB)):
			h,m,s = app.decHour(float(self.DB[i]["hour"]))
			dt_utc=datetime.datetime(int(self.DB[i]["year"]),int(self.DB[i]["month"]),int(self.DB[i]["day"]),h,m,s)
			dt = dt_utc + datetime.timedelta(seconds=float(self.DB[i]["timezone"])*float(3600))
			birth_date = str(dt.year)+'-%(#1)02d-%(#2)02d %(#3)02d:%(#4)02d:%(#5)02d' % {'#1':dt.month,'#2':dt.day,'#3':dt.hour,'#4':dt.minute,'#5':dt.second}			
			self.listmodel.append([self.DB[i]["id"],self.DB[i]["name"],birth_date,self.DB[i]["location"]])
		#add columns to treeview
		self.win_OD_treeview.append_column(self.win_OD_tvcolumn0)
		self.win_OD_treeview.append_column(self.win_OD_tvcolumn1)
		self.win_OD_treeview.append_column(self.win_OD_tvcolumn2)
		self.win_OD_treeview.append_column(self.win_OD_tvcolumn3)
		#cell renderers
		cell0 = Gtk.CellRendererText()
		cell1 = Gtk.CellRendererText()
		cell2 = Gtk.CellRendererText()
		cell3 = Gtk.CellRendererText()
		#add cells to columns
		self.win_OD_tvcolumn0.pack_start(cell0, True)
		self.win_OD_tvcolumn1.pack_start(cell1, True)
		self.win_OD_tvcolumn2.pack_start(cell2, True)
		self.win_OD_tvcolumn3.pack_start(cell3, True)
		# set the cell attributes to the listmodel column
		self.win_OD_tvcolumn0.set_attributes(cell0, text = 0)
		self.win_OD_tvcolumn1.set_attributes(cell1, text = 1)
		self.win_OD_tvcolumn2.set_attributes(cell2, text = 2)
		self.win_OD_tvcolumn3.set_attributes(cell3, text = 3)
		#set treeview options
		self.win_OD_treeview.set_search_column(1)
		self.win_OD_tvcolumn0.set_sort_column_id(0)
		self.win_OD_tvcolumn1.set_sort_column_id(1)
		self.win_OD_tvcolumn2.set_sort_column_id(2)
		self.win_OD_tvcolumn3.set_sort_column_id(3)
		#add treeview to scrolledwindow
		scrolledwindow = Gtk.ScrolledWindow()
		scrolledwindow.set_child(self.win_OD_treeview)
		scrolledwindow.set_vexpand(True)
		#scrolledwindow.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.ALWAYS)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		vbox.set_vexpand(True)
		vbox.append(scrolledwindow)

		button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		button_box.set_homogeneous(True)
		#buttons
		button = Gtk.Button.new_with_mnemonic(label=_('Cancel'))
		button.connect("clicked", lambda w: self.openDatabaseSelectReject())
		button_box.append(button)	
		button = Gtk.Button.new_with_mnemonic(label=selectstr)
		button.connect("clicked", lambda w: self.openDatabaseSelectReturn(type))
		button_box.prepend(button)		
		#display window
		vbox.append(button_box)
		self.win_OD.set_child(vbox)
		self.win_OD_treeview.set_model(model=self.listmodel)
		self.win_OD.present()

	def openDatabaseSelectReject(self):
		self.win_OD.destroy()
		return

	def openDatabaseSelectReturn(self, type):
		model = self.win_OD_selection.get_selected()[0]
		iter = self.win_OD_selection.get_selected()[1]
		for i in range(len(self.DB)):
			if self.DB[i]["id"] == model.get_value(iter,0):
				list = self.DB[i]
		#synastry
		if type == "Synastry":
			app.type="Transit"
			app.t_name=str(list["name"])
			app.t_year=int(list["year"])
			app.t_month=int(list["month"])
			app.t_day=int(list["day"])
			app.t_hour=float(list["hour"])
			app.t_geolon=float(list["geolon"])
			app.t_geolat=float(list["geolat"])
			app.t_altitude=int(list["altitude"])
			app.t_location=str(list["location"])
			app.t_timezone=float(list["timezone"])
			app.charttype="%s (%s)" % (app.label["synastry"],app.t_name)
			app.transit=True
			chart_name = app.makeSVG()
		elif type == "Composite":
			app.type="Composite"
			app.t_name=str(list["name"])
			app.t_year=int(list["year"])
			app.t_month=int(list["month"])
			app.t_day=int(list["day"])
			app.t_hour=float(list["hour"])
			app.t_geolon=float(list["geolon"])
			app.t_geolat=float(list["geolat"])
			app.t_altitude=int(list["altitude"])
			app.t_location=str(list["location"])
			app.t_timezone=float(list["timezone"])
			app.charttype="%s (%s)" % (app.label["composite"],app.t_name)
			app.transit=False
			chart_name = app.makeSVG()
		elif type == "Combine":
			app.type="Combine"
			app.t_name=str(list["name"])
			app.t_year=int(list["year"])
			app.t_month=int(list["month"])
			app.t_day=int(list["day"])
			app.t_hour=float(list["hour"])
			app.t_geolon=float(list["geolon"])
			app.t_geolat=float(list["geolat"])
			app.t_altitude=int(list["altitude"])
			app.t_location=str(list["location"])
			app.t_timezone=float(list["timezone"])
			#calculate combine between both utc times
			h,m,s = app.decHour(app.hour)
			dt1 = datetime.datetime(app.year,app.month,app.day,h,m,s)
			h,m,s = app.decHour(app.t_hour)
			dt2 = datetime.datetime(app.t_year,app.t_month,app.t_day,h,m,s)
			if dt1 > dt2:
				delta = dt1 - dt2
				hdelta = delta // 2
				combine = dt2 + hdelta
			else:
				delta = dt2 - dt1
				hdelta = delta // 2
				combine = dt1 + hdelta
			#take lon,lat middle
			app.c_geolon = (app.geolon + app.t_geolon)/2.0
			app.c_geolat = (app.geolat + app.t_geolat)/2.0
			app.c_altitude = (app.t_altitude + app.altitude)/2.0
			app.c_year = combine.year
			app.c_month = combine.month
			app.c_day = combine.day
			app.c_hour = app.decHourJoin(combine.hour,combine.minute,combine.second)
			app.charttype="%s (%s)" % (app.label["combine"],app.t_name)
			app.transit=False
			#set new date for printing in svg
			app.year = app.c_year
			app.month = app.c_month
			app.day = app.c_day
			app.hour = app.c_hour
			app.geolat = app.c_geolat
			app.geolon = app.c_geolon
			app.timezone_str = zonetab.nearest_tz(app.geolat,app.geolon,zonetab.timezones())[2]
			#aware datetime object
			dt_input = datetime.datetime(combine.year, combine.month, combine.day, combine.hour, combine.minute, combine.second)
			dt = pytz.timezone(app.timezone_str).localize(dt_input)
			app.timezone=app.offsetToTz(dt.utcoffset())
			app.utcToLocal()
			chart_name = app.makeSVG()
		self.image.setupSVG(chart_name)
		self.image.queue_resize()
		self.win_OD.close()		

	"""
	 Menu items for general configuration
	  settingsConfiguration
	  settingsConfigurationSubmit
	"""
	def setConfiguration_callback(self, action, parameter):
		# create a new window
		self.win_SC = Gtk.Window(parent=self)
		""" >>> set_icon changed in GTK4 """

		self.win_SC.set_title(_("General Configuration"))
		#self.win_SC.connect("delete_event", lambda w,e: self.win_SC.destroy())
		#self.win_SC.move(200,150)
		#self.win_SC.set_border_width(5)
		self.win_SC.set_default_size(364,512)
		#data dictionary
		data = {}
		#create a VBox
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		#create a grid with 8 rows and 1 column
		grid = Gtk.Grid()
		grid.set_column_spacing(8)
		grid.set_row_spacing(8)
		#grid.set_border_width(10)
		grid.set_column_homogeneous(True)
		# options
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		hbox.set_spacing(8)
		geobase = Gtk.Label(label=_("Use Online Geocoding (ws.geonames.org)"))
		hbox.prepend(geobase)
		data['use_geonames.org'] = Gtk.CheckButton()
		hbox.append(data['use_geonames.org'])
		grid.attach(hbox, 0, 0, 1, 1)
		if app.db.getAstrocfg('use_geonames.org') == "1":
			data['use_geonames.org'].set_active(True)
		# house system
		data['houses_system'] = Gtk.ComboBoxText.new()
		grid.attach(Gtk.Label(label=_('Houses System')), 0, 1, 1, 1)
		grid.attach(data['houses_system'], 0, 2, 1, 1)
		hsys={
			"P":"Placidus",
			"K":"Koch",
			"O":"Porphyrius",
			"R":"Regiomontanus",
			"C":"Campanus",
			"A":"Equal (Cusp 1 = Asc)",
			"V":"Vehlow Equal (Asc = 1/2 House 1)",
			"W":"Whole",
			"X":"Axial Rotation",
			"H":"Azimuthal or Horizontal System",
			"T":"Polich/Page ('topocentric system')",
			"B":"Alcabitus",
			"G":"Gauquelin sectors",
			"M":"Morinus"
		}
		self.houses_list=["P","K","O","R","C","A","V","W","X","H","T","B","G","M"]
		active=0
		for n in range(len(self.houses_list)):
			data['houses_system'].append_text(hsys[self.houses_list[n]])
			if app.db.astrocfg['houses_system'] == self.houses_list[n]:
				active = n
		data['houses_system'].set_active(active)
		#position calculation (geo,truegeo,topo,helio)
		data['postype'] = Gtk.ComboBoxText.new()
		grid.attach(Gtk.Label(label=_('Position Calculation')), 0, 3, 1, 1)
		grid.attach(data['postype'], 0, 4, 1, 1)
		postype={
			"geo":app.label["apparent_geocentric"]+" "+_("(default)"),
			"truegeo":app.label["true_geocentric"],
			"topo":app.label["topocentric"],
			"helio":app.label["heliocentric"]
		}
		self.postype_list=["geo","truegeo","topo","helio"]
		active = 0
		for n in range(len(self.postype_list)):
			data['postype'].append_text(postype[self.postype_list[n]])
			if app.db.astrocfg['postype'] == self.postype_list[n]:
				active = n
		data['postype'].set_active(active)
		#chart view (traditional,european)
		data['chartview'] = Gtk.ComboBoxText.new()
		grid.attach(Gtk.Label(label=_('Chart View')), 0, 5, 1, 1)
		grid.attach(data['chartview'], 0, 6, 1, 1)
		chartview={
			"traditional":_("Planets in Zodiac"),
			"european":_("Planets around Zodiac")
		}
		self.chartview_list=["traditional","european"]
		active=0
		for n in range(len(self.chartview_list)):
			data['chartview'].append_text(chartview[self.chartview_list[n]])
			if app.db.astrocfg['chartview'] == self.chartview_list[n]:
				active = n
		data['chartview'].set_active(active)
		#zodiac type (tropical, sidereal)
		data['zodiactype'] = Gtk.ComboBoxText.new()
		grid.attach(Gtk.Label(label=_('Zodiac Type')), 0, 7, 1, 1)
		grid.attach(data['zodiactype'], 0, 8, 1, 1)
		chartview={"tropical":_("Tropical"), "sidereal":_("Sidereal")}
		self.zodiactype_list=["tropical","sidereal"]
		active = 0
		for n in range(len(self.zodiactype_list)):
			data['zodiactype'].append_text(chartview[self.zodiactype_list[n]])
			if app.db.astrocfg['zodiactype'] == self.zodiactype_list[n]:
				active = n
		data['zodiactype'].set_active(active)
		#sidereal mode
		data['siderealmode'] = Gtk.ComboBoxText.new()
		if app.db.astrocfg['zodiactype'] != 'sidereal':
			data['siderealmode'].set_sensitive(False)

		def zodiactype_changed(button):
			if self.zodiactype_list[data['zodiactype'].get_active()] != 'sidereal':
				data['siderealmode'].set_sensitive(False)
			else:
				data['siderealmode'].set_sensitive(True)

		data['zodiactype'].connect("changed",zodiactype_changed)
		grid.attach(Gtk.Label(label=_('Sidereal Mode')), 0, 9, 1, 1)
		grid.attach(data['siderealmode'], 0, 10, 1, 1)
		self.siderealmode_chartview={
				"FAGAN_BRADLEY":_("Fagan Bradley"),
				"LAHIRI":_("Lahiri"),
				"DELUCE":_("Deluce"),
				"RAMAN":_("Ramanb"),
				"USHASHASHI":_("Ushashashi"),
				"KRISHNAMURTI":_("Krishnamurti"),
				"DJWHAL_KHUL":_("Djwhal Khul"),
				"YUKTESHWAR":_("Yukteshwar"),
				"JN_BHASIN":_("Jn Bhasin"),
				"BABYL_KUGLER1":_("Babyl Kugler 1"),
				"BABYL_KUGLER2":_("Babyl Kugler 2"),
				"BABYL_KUGLER3":_("Babyl Kugler 3"),
				"BABYL_HUBER":_("Babyl Huber"),
				"BABYL_ETPSC":_("Babyl Etpsc"),
				"ALDEBARAN_15TAU":_("Aldebaran 15Tau"),
				"HIPPARCHOS":_("Hipparchos"),
				"SASSANIAN":_("Sassanian"),
				"J2000":_("J2000"),
				"J1900":_("J1900"),
				"B1950":_("B1950")
				}
		self.siderealmode_list=["FAGAN_BRADLEY",
				"LAHIRI",
				"DELUCE",
				"RAMAN",
				"USHASHASHI",
				"KRISHNAMURTI",
				"DJWHAL_KHUL",
				"YUKTESHWAR",
				"JN_BHASIN",
				"BABYL_KUGLER1",
				"BABYL_KUGLER2",
				"BABYL_KUGLER3",
				"BABYL_HUBER",
				"BABYL_ETPSC",
				"ALDEBARAN_15TAU",
				"HIPPARCHOS",
				"SASSANIAN",
				"J2000",
				"J1900",
				"B1950"]
		active=0
		for n in range(len(self.siderealmode_list)):
			data['siderealmode'].append_text(self.siderealmode_chartview[self.siderealmode_list[n]])
			if app.db.astrocfg['siderealmode'] == self.siderealmode_list[n]:
				active = n
		data['siderealmode'].set_active(active)
		#language
		data['language'] = Gtk.ComboBoxText.new()
		grid.attach(Gtk.Label(label=_('Language')), 0, 11, 1, 1)
		grid.attach(data['language'], 0, 12, 1, 1)
		data['language'].append_text(_("Default"))
		active=0
		for i in range(len(LANGUAGES)):
			data['language'].append_text(app.db.lang_label[LANGUAGES[i]])
			if app.db.astrocfg['language'] == LANGUAGES[i]:
				active = i+1
		data['language'].set_active(active)
		#make the ui layout with ok button
		scrolled_window = Gtk.ScrolledWindow()
		scrolled_window.set_vexpand(True)
		scrolled_window.set_child(grid)
		vbox.append(scrolled_window)
		#self.win_SC.vbox.pack_start(scrolledwindow, True, True, 0)
		button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		button_box.set_homogeneous(True)
		# ok button
		button = Gtk.Button.new_with_mnemonic(label=_("OK"))
		button.connect("clicked", self.settingsConfigurationSubmit, data)
		#button.set_can_default(True)
		#self.win_SC.action_area.pack_start(button, True, True, 0)
		#button.grab_default()
		button_box.prepend(button)
		# cancel button
		button = Gtk.Button.new_with_mnemonic(label=_("Cancel"))
		button.connect("clicked", lambda w: self.win_SC.destroy())
		#self.win_SC.action_area.pack_start(button, True, True, 0)
		button_box.prepend(button)
		vbox.append(button_box)
		self.win_SC.set_child(vbox)
		self.win_SC.present()

	def settingsConfigurationSubmit(self, widget, data):
		update = False
		if data['use_geonames.org'].get_active():
			app.db.setAstrocfg("use_geonames.org","1")
		else:
			app.db.setAstrocfg("use_geonames.org","0")
		# houses system
		if self.houses_list[data['houses_system'].get_active()] != app.db.astrocfg['houses_system']:
			update = True
		app.db.setAstrocfg("houses_system",self.houses_list[data['houses_system'].get_active()])
		# position calculation
		if self.postype_list[data['postype'].get_active()] != app.db.astrocfg['postype']:
			update = True
		app.db.setAstrocfg("postype",self.postype_list[data['postype'].get_active()])
		#chart view
		if self.chartview_list[data['chartview'].get_active()] != app.db.astrocfg['chartview']:
			update = True
		app.db.setAstrocfg("chartview",self.chartview_list[data['chartview'].get_active()])
		#zodiac type
		if self.zodiactype_list[data['zodiactype'].get_active()] != app.db.astrocfg['zodiactype']:
			update = True
		app.db.setAstrocfg("zodiactype",self.zodiactype_list[data['zodiactype'].get_active()])
		#sidereal mode
		if self.siderealmode_list[data['siderealmode'].get_active()] != app.db.astrocfg['siderealmode']:
			update = True
		app.db.setAstrocfg("siderealmode",self.siderealmode_list[data['siderealmode'].get_active()])
		#language
		model = data['language'].get_model()
		active = data['language'].get_active()
		if active == 0:
			active_lang = "default"
		else:
			active_lang = LANGUAGES[active-1]
		if active_lang != app.db.astrocfg['language']:
			update = True
		app.db.setAstrocfg("language",active_lang)

		# set language to be used
		app.db.setLanguage(active_lang)
		self.updateUI()
		# updatechart
		if update:
			self.updateChart()
		self.win_SC.destroy()
		return

	"""
	Menu item to set home location:
		settingsLocation
		settingsLocationSubmit
		settingsLocationApply
		settingsLocationDestroy
	"""
	def setLocation_callback(self, action, parameter):
		self.settingsLocationMode = True
		# check connection to the internet
		self.checkInternetConnection()
		# create a new window
		self.win_SL = Gtk.Window()
		""" >>> set_icon changed in GTK4 """

		self.win_SL.set_title(_("Please Set Your Home Location"))
		""" >>> settingsLocationDestroy changed in GTK4 """
		#self.win_SL.connect("delete_event", lambda w,e: self.settingsLocationDestroy())
		#self.win_SL.move(150,150)
		#self.win_SL.set_border_width(10)
		# create a grid, method 'attach', left, top, width, height
		grid = Gtk.Grid()
		grid.set_column_spacing(15)
		grid.set_row_spacing(15)
		self.win_SL.set_child(grid)
		# display of location (non editable)
		location = Gtk.Label(label=_('Location')+':')
		grid.attach(location, 0, 1, 1, 1)
		self.LLoc = Gtk.Label(label=app.home_location)
		grid.attach_next_to(Gtk.Label(label=app.home_location), location, Gtk.PositionType.RIGHT, 1, 1)
		latitude = Gtk.Label(label=_('Latitude')+':')
		grid.attach(latitude, 0, 2, 1, 1)
		self.LLat = Gtk.Label(label=app.home_geolat)
		grid.attach_next_to(Gtk.Label(label=app.home_geolat), latitude, Gtk.PositionType.RIGHT, 1, 1)
		longitude = Gtk.Label(label=_('Longitude')+':')
		grid.attach(longitude, 0, 3, 1, 1)
		self.LLon = Gtk.Label(label=app.home_geolon)
		grid.attach_next_to(Gtk.Label(label=app.home_geolon), longitude, Gtk.PositionType.RIGHT, 1, 1)
		# use geocoders if we have an internet connection else geonames database
		if self.iconn:
			# entry for location (edigrid)
			hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
			label = Gtk.Label(label=_("City")+": ")
			hbox.append(label)
			self.geoLoc = Gtk.Entry()
			self.geoLoc.set_max_length(100)
			self.geoLoc.set_width_chars(30)
			self.geoLoc.set_text(app.home_location.partition(',')[0])
			hbox.append(self.geoLoc)
			label = Gtk.Label(label=" "+_("Country-code")+": ")
			hbox.append(label)
			self.geoCC = Gtk.Entry()
			self.geoCC.set_max_length(2)
			self.geoCC.set_width_chars(2)
			self.geoCC.set_text(app.home_countrycode)
			hbox.append(self.geoCC)
			grid.attach(hbox, 0, 0, 2, 1)
		else:
			hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
			grid.attach(hbox, 0, 0, 2, 1)
			# get nearest home
			self.GEON_nearest = app.db.gnearest(app.geolat,app.geolon)
			# continents
			self.contbox = Gtk.ComboBox()
			self.contstore = Gtk.ListStore(str,str)
			cell = Gtk.CellRendererText()
			self.contbox.pack_start(cell, False)
			self.contbox.add_attribute(cell, 'text', 0)
			hbox.append(self.contbox)
			#self.contbox.set_wrap_width(1)
			sql = 'SELECT * FROM continent ORDER BY name ASC'
			app.db.gquery(sql)
			continentinfo=[]
			i = 0
			activecont = 3
			for row in app.db.gcursor:
				if row['code'] == self.GEON_nearest['continent']:
					activecont = i
					self.GEON_nearest['continent'] = None
				self.contstore.append([row['name'],row['code']])
				i += 1
			app.db.gclose()
			self.contbox.set_model(self.contstore)
			# countries
			self.countrybox = Gtk.ComboBox()
			cell = Gtk.CellRendererText()
			self.countrybox.pack_start(cell, False)
			self.countrybox.add_attribute(cell, 'text', 0)
			hbox.append(self.countrybox)
			#self.countrybox.set_wrap_width(1) 
			self.countrybox.connect('changed', self.eventDataChangedCountrybox)
			# provinces
			self.provbox = Gtk.ComboBox()
			cell = Gtk.CellRendererText()
			self.provbox.pack_start(cell, False)
			self.provbox.add_attribute(cell, 'text', 0)
			hbox.append(self.provbox)
			#self.provbox.set_wrap_width(1) 
			self.provbox.connect('changed', self.eventDataChangedProvbox)
			# cities
			self.citybox = Gtk.ComboBox()
			cell = Gtk.CellRendererText()
			self.citybox.pack_start(cell, False)
			self.citybox.add_attribute(cell, 'text', 0)
			hbox.append(self.citybox)
			#self.citybox.set_wrap_width(2) 
			self.citybox.connect('changed', self.eventDataChangedCitybox)
			self.contbox.connect('changed', self.eventDataChangedContbox)
			self.contbox.set_active(activecont)
		# buttonbox
		buttonbox = Gtk.Box(homogeneous=False, spacing=5)
		grid.attach(buttonbox, 0, 4, 2, 1)
   		# ok button
		button = Gtk.Button.new_with_mnemonic(label="OK")
		button.connect("clicked", self.settingsLocationSubmit)
		#button.set_can_default(True)
		buttonbox.append(button)
		#button.grab_default()
		# Apply button
		button = Gtk.Button.new_with_mnemonic(label=_('Apply'))
		button.connect("clicked", self.settingsLocationApply)
		buttonbox.append(button)
		# Cancel button
		button = Gtk.Button.new_with_mnemonic(label=_("Cancel"))
		button.connect("clicked", lambda w: self.settingsLocationDestroy())
		buttonbox.append(button)
		# show all
		self.win_SL.present()

	def settingsLocationSubmit(self, widget):
		self.settingsLocationApply(widget)
		if self.geoLocFound:
			self.settingsLocationDestroy()
			return
		else:
			return

	def settingsLocationApply(self, widget):
		# check for internet connection to decide geocode/database
		self.geoLocFound = True
		if self.iconn:
			result = geoname.search(self.geoLoc.get_text(),self.geoCC.get_text())
			if result:
				self.geoLocFound = True
				lat=float(result[0]['lat'])
				lon=float(result[0]['lng'])
				tzstr=result[0]['timezonestr']
				cc=result[0]['countryCode']
				loc='%s, %s' % (result[0]['name'],result[0]['countryName'])
				dprint('settingsLocationApply: %s found; %s %s %s' % (self.geoLoc.get_text(), lat,lon,loc))
			else:
				self.geoLocFound = False
				#revert to defaults
				lat=app.geolat
				lon=app.geolon
				loc=app.location
				cc=app.countrycode
				tzstr=app.timezonestr
				dprint('settingsLocationApply: %s not found, reverting to defaults' % self.geoLoc.get_text() )
				self.geoLoc.set_text('City Not Found, Try Again!')
				return
		else:
			lat = float(self.GEON_lat)
			lon = float(self.GEON_lon)
			loc = self.GEON_loc
			cc = self.GEON_cc
			tzstr = self.GEON_tzstr
		# apply settings to database
		app.db.setSettingsLocation(lat, lon, loc, cc, tzstr)
		app.home_location=loc
		app.home_geolat=lat
		app.home_geolon=lon
		app.home_countrycode=cc
		app.home_timezonestr=tzstr
		app.location=loc
		app.timezonestr=tzstr
		app.geolat=lat
		app.geolon=lon
		app.countrycode=cc
		app.transit=False
		app.name=_("Here and Now")
		app.type="Radix"
		self.LLat.set_text(str(lat))
		self.LLon.set_text(str(lon))
		self.LLoc.set_text(str(loc))
		# set defaults for chart creation
		now = datetime.datetime.now()
		dt_input = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
		dt = pytz.timezone(app.timezonestr).localize(dt_input)
		dt_utc = dt.replace(tzinfo=None) - dt.utcoffset()
		app.name=_("Here and Now")
		app.charttype = app.label["radix"]
		app.year = dt_utc.year
		app.month=dt_utc.month
		app.day=dt_utc.day
		app.hour = app.decHourJoin(dt_utc. hour, dt_utc. minute, dt_utc. second)
		app.timezone=app.offsetToTz(dt.utcoffset())
		app.altitude=25
		app.utcToLocal()
		self.updateChart()

		dprint('Setting New Home Location: %s %s %s' % (lat,lon,loc) )

		return

	def settingsLocationDestroy(self):
		self.settingsLocationMode = False
		self.win_SL.close()
		return

	"""
	 'Chart Types' Menu Items Callbacks
	  specialRadix
	  specialTransit
	  specialSolar
	  specialProgression
	"""
	def specialRadix_callback(self, action, parameter):
		app.type = "Radix"
		app.charttype = app.label["radix"]
		app.transit = False
		self.updateChart()

	def specialTransit_callback(self, action, parameter):
		app.type = "Transit"
		app.charttype = app.label["transit"]
		app.transit = True
		app.t_geolon = float(app.home_geolon)
		app.t_geolat = float(app.home_geolat)

		now = datetime.datetime.now()
		app.timezone_str = zonetab.nearest_tz(app.t_geolat, app.t_geolon, zonetab. timezones())[2]
		#aware datetime object
		dt_input = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
		dt = pytz.timezone(app.timezone_str).localize(dt_input)
		#naive utc datetime object
		dt_utc = dt.replace(tzinfo=None) - dt.utcoffset()
		#transit data
		app.t_year = dt_utc.year
		app.t_month = dt_utc.month
		app.t_day = dt_utc.day
		app.t_hour = app.decHourJoin(dt_utc.hour, dt_utc.minute, dt_utc.second)
		app.t_timezone = app.offsetToTz(dt.utcoffset())
		app.t_altitude = 25
		#make svg with transit
		app.charttype = "%s (%s-%02d-%02d %02d:%02d)" % (app.charttype, dt.year, dt.month, dt.day, dt.hour, dt.minute)
		self.updateChart()

	def specialSolar_callback(self, action, parameter):
		# create a new window
		self.win_SS = Gtk.Window()
		""" >>> set_icon """
		#self.win_SS.set_icon_from_file(app.cfg.iconWindow)
		self.win_SS.set_title(_("Select year for Solar Return"))
		#self.win_SS.connect("delete_event", lambda w,e: self.win_SS.destroy())
		#self.win_SS.move(150,150)
		#self.win_SS.set_border_width(5)
		self.win_SS.set_size_request(300,100)
		#create a grid
		grid = Gtk.Grid()
		grid.set_column_spacing(8)
		grid.set_row_spacing(8)
		#grid.set_border_width(10)
		# options
		header = Gtk.Label(label=_("Select year for Solar Return")+":")
		grid.attach(header, 0, 0, 2, 1)
		label_year = Gtk.Label(label=_('Year')+": ")
		#hbox.pack_start(label_year, True, False, 8)
		grid.attach(label_year, 0, 1, 1, 1)
		spinner = {}
		adjustment = Gtk.Adjustment(lower=1, upper=2600, step_increment=1, page_increment=10)
		spinner['Y'] = Gtk.SpinButton()
		spinner['Y'].props.adjustment = adjustment
		spinner['Y'].set_numeric(True)
		spinner['Y'].set_value(datetime.datetime.now().year)
		grid.attach(spinner['Y'], 1, 1, 1, 1)
		#ok button
		button = Gtk.Button.new_with_mnemonic(label = _("OK"))
		button.connect("clicked", self.specialSolarSubmit, spinner)
		#button.set_can_default(True)
		grid.attach(button, 0, 2, 1, 1)
		#self.win_SS.action_area.pack_start(button, True, True, 0)
		#button.grab_default()
		#cancel button
		button = Gtk.Button.new_with_mnemonic(label = _("Cancel"))
		button.connect("clicked", lambda w: self.win_SS.destroy())
		grid.attach(button, 1, 2, 1, 1)
		#self.win_SS.action_area.pack_start(button, True, True, 0)
		self.win_SS.set_child(grid)
		self.win_SS.present()

	def specialSolarSubmit(self, widget, spinner):
		y = spinner['Y'].get_value_as_int()
		app.localToSolar(y)
		self.win_SS.close()
		self.updateChart()

	def specialProgression_callback(self, action, parameter):
		# create a new window
		self.win_SSP = Gtk.Window()
		""" set_icon """
		#self.win_SSP.set_icon_from_file(app.cfg.iconWindow)
		self.win_SSP.set_title(_("Enter Date"))
		#self.win_SSP.connect("delete_event", lambda w,e: self.win_SSP.destroy())
		#self.win_SSP.move(150,150)
		#self.win_SSP.set_border_width(5)
		self.win_SSP.set_size_request(320,180)
		#create a grid
		grid = Gtk.Grid()
		grid.set_column_spacing(8)
		grid.set_row_spacing(8)
		#grid.set_border_width(10)
		grid.set_vexpand(True)
		# options
		header = Gtk.Label(label=_("Select date for Secondary Progression")+":")
		grid.attach(header, 0, 0, 6, 1)
		label_year = Gtk.Label(label=_('Year')+": ")
		grid.attach(label_year, 0, 1, 1, 1)
		spinner = {}
		adjustment = Gtk.Adjustment(lower=1, upper=2400, step_increment=1, page_increment=10)
		spinner['Y'] = Gtk.SpinButton()
		spinner['Y'].props.adjustment = adjustment
		spinner['Y'].set_numeric(True)
		spinner['Y'].set_value(datetime.datetime.now().year)
		grid.attach(spinner['Y'], 1, 1, 1, 1)
		label_month = Gtk.Label(label=_('Month')+": ")
		grid.attach(label_month, 2, 1, 1, 1)
		adjustment = Gtk.Adjustment(lower=1, upper=12, step_increment=1)
		spinner['M'] = Gtk.SpinButton()
		spinner['M'].props.adjustment = adjustment
		spinner['M'].set_numeric(True)
		spinner['M'].set_value(datetime.datetime.now().month)
		grid.attach(spinner['M'], 3, 1, 1, 1)
		label_day = Gtk.Label(label=_('Day')+": ")
		grid.attach(label_day, 4, 1, 1, 1)
		adjustment = Gtk.Adjustment(lower=1, upper=31, step_increment=1)
		spinner['D'] = Gtk.SpinButton()
		spinner['D'].props.adjustment = adjustment
		spinner['D'].set_numeric(True)
		spinner['D'].set_value(datetime.datetime.now().day)
		grid.attach(spinner['D'], 5, 1, 1, 1)
		# pack_start(child, expand = True, fill = True, padding = 0)
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		hbox.append(Gtk.Label(label=_('Hour')+": "))
		adjustment = Gtk.Adjustment(lower=0, upper=23, step_increment=1)
		spinner['h'] = Gtk.SpinButton()
		spinner['h'].props.adjustment = adjustment
		spinner['h'].set_numeric(True)
		spinner['h'].set_value(datetime.datetime.now().hour)
		hbox.append(spinner['h'])
		hbox.append(Gtk.Label(label=_('Minute')+": "))
		adjustment = Gtk.Adjustment(lower=0, upper=59, step_increment=1)
		spinner['m'] = Gtk.SpinButton()
		spinner['m'].props.adjustment = adjustment
		spinner['m'].set_numeric(True)
		spinner['m'].set_value(datetime.datetime.now().minute)
		hbox.append(spinner['m'])
		grid.attach(hbox, 1, 2, 5, 1)
		#make the ui layout with ok button
		#self.win_SSP.vbox.append(grid)
		#ok button
		button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		button_box.set_homogeneous(True)
		button_box.set_vexpand(False)
		button = Gtk.Button.new_with_mnemonic(label = _("OK"))
		button.connect("clicked", self.specialSecondaryProgressionSubmit, spinner)
		#button.set_can_default(True)
		button_box.prepend(button)
		#self.win_SSP.action_area.pack_start(button, False, True, 0)
		#button.grab_default()
		#cancel button
		button = Gtk.Button.new_with_mnemonic(label = _("Cancel"))
		button.connect("clicked", lambda w: self.win_SSP.destroy())
		button_box.append(button)
		#self.win_SSP.action_area.pack_start(button, True, True, 0)
		grid.attach(button_box, 0, 3, 5, 1)
		self.win_SSP.set_child(grid)
		self.win_SSP.present()

	def specialSecondaryProgressionSubmit(self, widget, spinner):
		y = spinner['Y'].get_value_as_int()
		mon = spinner['M'].get_value_as_int()
		d = spinner['D'].get_value_as_int()
		h = spinner['h'].get_value_as_int()
		m = spinner['m'].get_value_as_int()
		dt = datetime.datetime(y, mon, d, h, m)
		app.localToSecondaryProgression(dt)
		self.win_SSP.destroy()
		self.updateChart()

	"""
	 Menu 'Tables' callbacks
	  MonthlyTimeline
	  MonthlyTimelineShow
	  MonthlyTimelinePrint
	  MonthlyTimelinePrintBegin
	  MonthlyTimelinePrintDraw
	  tableExposeEvent
	  CuspAspects
	"""
	def tableMonthlyTimeline_callback(self, action, parameter):
		self.dialog = Gtk.Window(title=_("Select Month in Year"))
		self.dialog.set_destroy_with_parent(True)
		self.dialog.connect("destroy", lambda w: dialog.destroy())
		self.dialog.set_default_size(272, 128)
		#dialog.move(64,128)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		vbox.set_vexpand(True)
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		hbox.set_homogeneous(True)
		label_year = Gtk.Label(label=_('Year')+": ")
		hbox.append(label_year)
		self.tMTspinner = {}
		adjustment = Gtk.Adjustment(lower=1, upper=2400, step_increment=1, page_increment=10)
		self.tMTspinner['Y'] = Gtk.SpinButton()
		self.tMTspinner['Y'].props.adjustment = adjustment
		self.tMTspinner['Y'].set_numeric(True)
		self.tMTspinner['Y'].set_value(datetime.datetime.now().year)
		hbox.append(self.tMTspinner['Y'])
		vbox.append(hbox)
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		hbox.set_homogeneous(True)
		label_month = Gtk.Label(label=_('Month')+": ")
		hbox.append(label_month)
		adjustment = Gtk.Adjustment(lower=1, upper=12, step_increment=1)
		self.tMTspinner['M'] = Gtk.SpinButton()
		self.tMTspinner['M'].props.adjustment = adjustment
		self.tMTspinner['M'].set_numeric(True)
		self.tMTspinner['M'].set_value(datetime.datetime.now().month)
		hbox.append(self.tMTspinner['M'])
		vbox.append(hbox)
		button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		button_box.set_homogeneous(True)
		#buttons
		button = Gtk.Button.new_with_mnemonic(label=_('Cancel'))
		button.connect("clicked", lambda w: dialog.destroy())
		button_box.append(button)	
		button = Gtk.Button.new_with_mnemonic(label=_('OK'))
		button.connect("clicked", lambda w: self.tableMonthlyTimelineShow(spinner=self.tMTspinner))
		button_box.prepend(button)		
		#display window
		vbox.append(button_box)
		self.dialog.set_child(vbox)
		self.dialog.present()

	def tableMonthlyTimelineShow(self, spinner):
		self.dialog.close()
		self.tabletype="timeline"
		self.tMT_year = spinner['Y'].get_value_as_int()
		self.tMT_month = spinner['M'].get_value_as_int()
		app.makeTimelineSVG(printing=None,y=self.tMT_year,m=self.tMT_month)
			#generate window
		self.win_TMT = Gtk.Window()
		#self.win_TMT.connect("destroy", lambda w: self.win_TMT.destroy())
		self.win_TMT.set_title("OpenAstro.org Monthly Timeline")
		""" >>> set_icon """
		#self.win_TMT.set_icon_from_file(app.cfg.iconWindow)
		self.win_TMT.set_default_size(1024, 732)
		#self.win_TMT.move(50,50)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		button = Gtk.Button.new_with_mnemonic(label=_('Print'))
		button.connect("clicked", lambda w: self.tablesChartPrint(app.pages,pdf=False,window=self.win_TMT,name="Timeline-%s.pdf"%(app.name)))
		button_box.append(button)
		button = Gtk.Button.new_with_mnemonic(label=_('Save as PDF'))
		button.connect("clicked", lambda w: self.tablesChartPrint(app.pages,pdf=True,window=self.win_TMT,name="Timeline-%s.pdf"%(app.name)))
		button_box.append(button)
		vbox.append(button_box)
		self.win_TMT.image = ViewSVG(app.cfg.tempfilenametable)
		self.win_TMT.image.set_vexpand(True)
		self.win_TMT.image.set_hexpand(True)
		self.win_TMT.image.set_valign(Gtk.Align.CENTER)
		self.win_TMT.image.set_halign(Gtk.Align.CENTER)
		scrolled_window = Gtk.ScrolledWindow()
		scrolled_window.set_child(self.win_TMT.image)
		vbox.append(scrolled_window)
		self.win_TMT.set_child(vbox)
		self.win_TMT.present()

	def tablesChartPrint(self, pages, pdf, window, name):
		settings = None
		window.print_op = Gtk.PrintOperation()
		window.print_op.set_unit(Gtk.Unit.MM)
		if settings != None: 
			window.print_op.set_print_settings(settings)
		window.print_op.connect("begin_print", self.tablesChartPrintBegin, app.pages)
		window.print_op.connect("draw_page", self.tablesChartPrintDraw)
		res = None
		if pdf:
			initial_name = name
			gio_filters = Gio.ListStore.new(Gtk.FileFilter)
			gio_filters.append(item=FILTER_ALL_FILES)
			gio_filters.append(item=FILTER_PDF_FILES)
			self.file_to_save(filters=gio_filters, name=initial_name, export_app=self.tablesChartPDF)
		else:
			res = window.print_op.run(Gtk.PrintOperationAction.PRINT_DIALOG, window)		
		if res == Gtk.PrintOperationResult.ERROR:
			error_dialog = Gtk.MessageDialog(window,0,Gtk.MESSAGE_ERROR,Gtk.ButtonS_CLOSE,"Error printing:\n")
			error_dialog.set_destroy_with_parent(True)
			error_dialog.connect("response", lambda w,id: w.destroy())
			error_dialog.show()
		elif res == Gtk.PrintOperationResult.APPLY:
			settings = window.print_op.get_print_settings()

	def tablesChartPDF(self, local_file):
		if (self.tabletype == "timeline"):
			window = self.win_TMT
		elif (self.tabletype == "cuspaspects"):
			window = self.win_TCA
		window.print_op.set_export_filename(local_file.get_path())
		res = window.print_op.run(Gtk.PrintOperationAction.EXPORT, window)
		window.close()

	def tablesChartPrintBegin(self, operation, context, pages):
		operation.set_n_pages(app.pages)
		operation.set_use_full_page(False)
		ps = Gtk.PageSetup()
		ps.set_orientation(Gtk.PageOrientation.PORTRAIT)
		ps.set_paper_size(Gtk.PaperSize(Gtk.PAPER_NAME_A4))
		operation.set_default_page_setup(ps)

	def tablesChartPrintDraw(self, operation, context, page_nr):
		cr = Gtk.PrintContext.get_cairo_context(context)
		#print options
		printing={}
		printing['pagenum']=page_nr
		printing['width']=Gtk.PrintContext.get_width(context)
		printing['height']=Gtk.PrintContext.get_height(context)
		printing['dpi_x']=Gtk.PrintContext.get_dpi_x(context)
		printing['dpi_y']=Gtk.PrintContext.get_dpi_y(context)
		#draw svg
		if(self.tabletype == "timeline"):
			app.makeTimelineSVG(printing=printing,y=self.tMT_year,m=self.tMT_month)
			#draw svg for printing
			svg = Rsvg.Handle.new_from_file(app.cfg.tempfilenametableprint)
		elif(self.tabletype == "cuspaspects"):
			app.makeCuspAspectsSVG(printing=printing)
			#draw svg for printing
			svg = Rsvg.Handle.new_from_file(app.cfg.tempfilenametableprint)
		viewport = Rsvg.Rectangle()
		viewport.x = 0
		viewport.y = 0
		viewport.width = Gtk.PrintContext.get_width(context)
		viewport.height = Gtk.PrintContext.get_height(context)
		svg.render_document(cr, viewport)

	def tableExposeEvent(self, drawing, context):
		if (self.tabletype == "timeline"):
			svg = self.svg_TMT
		elif (self.tabletype == "cuspaspects"):
			svg = self.svg_TCA
		if svg is not None:
			w = svg.get_property("width")
			h = svg.get_property("height")
			drawing.set_size_request(w, h)
			# prepare viewport for display
			viewport = Rsvg.Rectangle()
			viewport.x=0
			viewport.y=0
			viewport.width = w
			viewport.height = h
			svg.render_document(context, viewport)

	def tableCuspAspects_callback(self, action, parameter):
		self.tabletype="cuspaspects"
		app.makeCuspAspectsSVG(printing=None)
		#generate window
		self.win_TCA = Gtk.Window()
		self.win_TCA.connect("destroy", lambda w: self.win_TCA.destroy())
		self.win_TCA.set_title("OpenAstro.org Cusp Aspects")
		""" >>> set_icon """
		#self.win_TCA.set_icon_from_file(app.cfg.iconWindow)
		self.win_TCA.set_default_size(924,732)
		#self.win_TCA.move(50,50)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		vbox.set_vexpand(True)
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		button = Gtk.Button.new_with_mnemonic(label=_('Print'))
		button.connect("clicked", lambda w: self.tablesChartPrint(pages=1,pdf=False,window=self.win_TCA,name="CuspAspects-%s.pdf"%(app.name)))
		hbox.append(button)
		button = Gtk.Button.new_with_mnemonic(label=_('Save as PDF'))
		button.connect("clicked", lambda w: self.tablesChartPrint(pages=1,pdf=True,window=self.win_TCA,name="CuspAspects-%s.pdf"%(app.name)))
		hbox.append(button)
		vbox.append(hbox)
		self.win_TCA.image = ViewSVG(app.cfg.tempfilenametable)
		self.win_TCA.image.set_vexpand(True)
		self.win_TCA.image.set_hexpand(True)
		self.win_TCA.image.set_valign(Gtk.Align.CENTER)
		self.win_TCA.image.set_halign(Gtk.Align.CENTER)
		scrolled_window = Gtk.ScrolledWindow()
		scrolled_window.set_child(self.win_TCA.image)
		vbox.append(scrolled_window)
		self.win_TCA.set_child(vbox)
		self.win_TCA.present()

	""" Menu 'Zoom' """
	def zoom_callback(self, action, parameter):
		""" check for zoom level and draw """
		z_level = parameter.get_string()
		action.set_state(parameter)
		#action.set_state(parameter)
		ratio = self.image.scale
		if z_level == 'zIn':
			self.image.scale += 0.1
		elif z_level == 'z80':
			self.image.scale = 0.8
		elif z_level == 'z100':
			self.image.scale = 1.0
		elif z_level == 'z150':
			self.image.scale = 1.5
		elif z_level == 'z200':
			self.image.scale = 2.0
		elif z_level == 'zOut':
			if ratio >= 0.2:
				self.image.scale -= 0.1
			else:
				return
		self.image.queue_resize()

	"""
	'Extra' Menu Items Functions
	  exportdb
	  importdb'
	"""
	def exportdb_callback(self, action, parameter):
		gio_filters = Gio.ListStore.new(Gtk.FileFilter)
		gio_filters.append(item=FILTER_ALL_FILES)
		gio_filters.append(item=FILTER_SQL_FILES)
		self.file_to_save(filters=gio_filters, name='openastro-database.sql', export_app=self.exportSQL)

	def exportSQL(self, local_file):
		copyfile(app.cfg.peopledb, local_file.get_path())

	def importdb_callback(self, action, parameter):
		gio_filters = Gio.ListStore.new(Gtk.FileFilter)
		gio_filters.append(item=FILTER_ALL_FILES)
		gio_filters.append(item=FILTER_SQL_FILES)
		self.file_to_open(filters=gio_filters, name='openastro-database.sql', import_app=self.importSQL)

	def importSQL(self, local_file):
		app.db.databaseMerge(app.cfg.peopledb, local_file.get_path())

	# callback function for about (see the AboutDialog example)
	def about_callback(self, action, parameter):
		about = Gtk.AboutDialog(transient_for=self, modal=True)
		about.set_logo(Gdk.Texture.new_from_filename('about.xpm'));
		about.set_program_name("Gtk4 OpenAstro.org - Open Source Astrology")
		about.set_size_request(480, -1)
		about.set_version('Gtk4 Version ' + VERSION)
		about.set_authors(["Pelle van der Scheer, Amsterdam / The Netherlands"])
		documenters = ["Erich Küster, Krefeld / Nortrhine-Westfalia / Germany"]
		about.set_copyright("Copyright © 2012-2026 Pelle van der Scheer. All rights reserved.")
		with open('COMMENTS', "r") as f:
			comments = f.read()
		about.set_comments(comments)
		with open('LICENSE', "r") as f:
			license = f.read()
		about.set_license(license)
		about.set_website("https://pygobject.gnome.org/tutorials/gtk4.html");
		about.set_website_label("GTK4 — PyGObject")
		# show the aboutdialog
		about.present()

	# a callback function to destroy the aboutdialog
	def on_close(self, action, parameter):
		self.close()

class AstroApplication(Gtk.Application):
	def __init__(self, *args, **kwargs):
		super().__init__(
			*args,
			application_id=APPLICATION_ID,
			flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
			**kwargs,
		)
		display = Gdk.Display.get_default()
		monitor = display.get_primary_monitor()
		geometry = monitor.get_geometry()
		self.screen_width = geometry.width
		self.screen_height = geometry.height
		#calculate available screen size, correct dimensions
		self.height = self.screen_height-OFFSET
		self.width = self.height * RATIO
		self.window = None

		self.add_main_option(
			"local",
			ord("l"),
			GLib.OptionFlags.NONE,
			GLib.OptionArg.NONE,
			"AstroChart Standakone",
			None,
		)

	def do_startup(self):
		Gtk.Application.do_startup(self)

		quit_action = Gio.SimpleAction.new("quit", None)
		quit_action.connect("activate", self.on_quit)
		self.add_action(quit_action)
		self.set_accels_for_action("app.quit", ["<Primary>Q"])
		""" Configuration / Data Base / Calculations / Window """
		#configuration
		self.cfg = OpenAstroCfg()
		# handle data bases
		self.db = OpenAstroSqlite()
		#get label configuration
		self.label = self.db.getLabel()
		#check for home
		self.home_location,self.home_geolat,self.home_geolon,self.home_countrycode,self.home_timezonestr = app.db.getSettingsLocation()
		if self.home_location == '' or self.home_geolat == '' or self.home_geolon == '':
			dprint('Unknown home location, asking for new')
			self.ask_for_home = True
			self.home_location='Ooyerhoek'
			self.home_geolon=6.219530
			self.home_geolat=52.120710
			self.home_countrycode='NL'
			self.home_timezonestr='Europe/Amsterdam'
		else:
			self.ask_for_home = False
			dprint('known home location: %s %s %s' % (self.home_location, self.home_geolat, self.home_geolon))
		#default location
		self.location=self.home_location
		self.geolat=float(self.home_geolat)
		self.geolon=float(self.home_geolon)
		self.countrycode=self.home_countrycode
		self.timezonestr=self.home_timezonestr
		#current datetime
		now = datetime.datetime.now()
		#aware datetime object
		dt_input = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
		dt = pytz.timezone(self.timezonestr).localize(dt_input)
		#naive utc datetime object
		dt_utc = dt.replace(tzinfo=None) - dt.utcoffset()
		#Default
		self.name = _("Here and Now")
		self.charttype = self.label["radix"]
		self.year = dt_utc.year
		self.month = dt_utc.month
		self.day = dt_utc.day
		self.hour = self.decHourJoin(dt_utc.hour,dt_utc.minute,dt_utc.second)
		self.timezone = self.offsetToTz(dt.utcoffset())
		self.altitude = 25
		self.geonameid = None
		# Make locals
		self.utcToLocal()
		# configuration
		# ZOOM 1 = 100%
		self.zoom = 1
		self.type = "Radix"
		# Default dpi for svg
		self.default_dpi=400
		# 12 zodiacs
		self.zodiac = ['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces']
		self.zodiac_short = ['Ari','Tau','Gem','Cnc','Leo','Vir','Lib','Sco','Sgr','Cap','Aqr','Psc']
		self.zodiac_color = ['#482900','#6b3d00','#5995e7','#2b4972','#c54100','#2b286f','#69acf1','#ffd237','#ff7200','#863c00','#4f0377','#6cbfff']
		self.zodiac_element = ['fire','earth','air','water','fire','earth','air','water','fire','earth','air','water']
		#get color configuration
		self.colors = self.db.getColors()
		builder = Gtk.Builder.new_from_string(MENU_XML, -1)
		self.menubar = builder.get_object("MenuBar")
		self.set_menubar(self.menubar)

	def do_activate(self):
		# allow only a single window and raise any existing ones
		if self.window is None:
			# Windows are associated with the application
			# when the last one is closed the application shuts down
			self.window = AstroWindow(application=self, title="AstroChart Window")
			#self.window.menu = menubar
		self.window.set_default_size(self.width, self.height)
		self.window.present()

	def utcToLocal(self):
		# make local time variables from global UTC
		h, m, s = self.decHour(self.hour)
		utc = datetime.datetime(self.year, self.month, self.day, h, m, s)
		tz = datetime.timedelta(seconds=float(self.timezone)*float(3600))
		loc = utc + tz
		self.year_loc = loc.year
		self.month_loc = loc.month
		self.day_loc = loc.day
		self.hour_loc = loc.hour
		self.minute_loc = loc.minute
		self.second_loc = loc.second

		# print some info
		dprint('utcToLocal: '+str(utc)+' => '+str(loc)+self.decTzStr(self.timezone))

	def localToSolar(self, newyear):
		solaryearsecs = 31556925.51 # 365 days, 5 hours, 48 minutes, 45.51 seconds
		dprint("localToSolar: from %s to %s" %(self.year,newyear))
		h,m,s = self.decHour(self.hour)
		dt_original = datetime.datetime(self.year,self.month,self.day,h,m,s)
		dt_new = datetime.datetime(newyear,self.month,self.day,h,m,s)

		dprint("localToSolar: first sun %s" % (self.planets_degree_ut[0]) )

		mdata = ephemeris.ephData(newyear, self.month, self.day, self.hour, self.geolon, self.geolat, self.altitude, self.planets, self.zodiac, self.db.astrocfg)
		dprint("localToSolar: second sun %s" % (mdata.planets_degree_ut[0]) )
		sundiff = self.planets_degree_ut[0] - mdata.planets_degree_ut[0]
		dprint("localToSolar: sundiff %s" %(sundiff))
		sundelta = ( sundiff / 360.0 ) * solaryearsecs
		dprint("localToSolar: sundelta %s" % (sundelta))
		dt_delta = datetime.timedelta(seconds=int(sundelta))
		dt_new = dt_new + dt_delta
		mdata = ephemeris.ephData(dt_new.year, dt_new.month, dt_new.day, self.decHourJoin(dt_new.hour, dt_new.minute, dt_new.second), self.geolon, self.geolat, self.altitude, self.planets, self.zodiac, self.db.astrocfg)

		dprint("localToSolar: new sun %s" % (mdata.planets_degree_ut[0]))

		#get precise
		step = 0.000011408 # 1 seconds in degrees
		sundiff = self.planets_degree_ut[0] - mdata.planets_degree_ut[0]
		sundelta = sundiff / step
		dt_delta = datetime.timedelta(seconds=int(sundelta))
		dt_new = dt_new + dt_delta
		mdata = ephemeris.ephData(dt_new.year, dt_new.month, dt_new.day, self.decHourJoin(dt_new.hour, dt_new.minute, dt_new.second), self.geolon, self.geolat, self.altitude, self.planets, self.zodiac, self.db.astrocfg)

		dprint("localToSolar: new sun #2 %s" % (mdata.planets_degree_ut[0]))

		step = 0.000000011408 # 1 milli seconds in degrees
		sundiff = self.planets_degree_ut[0] - mdata.planets_degree_ut[0]
		sundelta = sundiff / step
		dt_delta = datetime.timedelta(milliseconds=int(sundelta))
		dt_new = dt_new + dt_delta
		mdata = ephemeris.ephData(dt_new.year, dt_new.month, dt_new.day, self.decHourJoin(dt_new.hour, dt_new.minute, dt_new.second), self.geolon, self.geolat, self.altitude, self.planets, self.zodiac, self.db.astrocfg)

		dprint("localToSolar: new sun #3 %s" % (mdata.planets_degree_ut[0]))

		self.s_year = dt_new.year
		self.s_month = dt_new.month
		self.s_day = dt_new.day
		self.s_hour = self.decHourJoin(dt_new.hour,dt_new.minute,dt_new.second)
		self.s_geolon = self.geolon
		self.s_geolat = self.geolat
		self.s_altitude = self.altitude
		self.type = "Solar"
		self.charttype = "%s (%s-%02d-%02d %02d:%02d:%02d UTC)" % (self.label["solar"], self.s_year, self.s_month, self.s_day, dt_new.hour, dt_new.minute, dt_new.second)
		self.transit = False
		return

	"""
	 Secondary Progression
	  Calculate years between birth and date,
	  add as days to birth date
	"""	
	def localToSecondaryProgression(self, dt):
		# remove timezone
		dt_utc = dt - datetime.timedelta(seconds=float(self.timezone)*float(3600))
		y,mth,d,hrs = ephemeris.years_diff(self.year, self.month, self.day, self.hour,
dt_utc.year, dt_utc.month, dt_utc.day,self.decHourJoin(dt_utc.hour,dt_utc.minute, dt_utc.second))
		h,m,s = self.decHour(hrs)
		dt_new = datetime.datetime(y,mth,d,h,m,s)
		self.sp_year = dt_new.year
		self.sp_month = dt_new.month
		self.sp_day = dt_new.day
		self.sp_hour = self.decHourJoin(dt_new.hour,dt_new.minute,dt_new.second)
		self.sp_geolon = self.geolon
		self.sp_geolat = self.geolat
		self.sp_altitude = self.altitude
		self.houses_override = [dt_new.year, dt_new.month, dt_new.day, self.hour]

		dprint("localToSecondaryProgression: got UTC %s-%s-%s %s:%s:%s"%(dt_new.year, dt_new.month, dt_new.day, dt_new.hour, dt_new.minute, dt_new.second))

		self.type = "SecondaryProgression"
		self.charttype="%s (%s-%02d-%02d %02d:%02d)" % (self.label["secondary_progressions"], dt.year, dt.month, dt.day, dt.hour, dt.minute)
		self.transit = False
		return

	""" make horoscope with zodiac ring """
	def makeSVG( self , printing=None ):
		#empty element points
		self.fire=0.0
		self.earth=0.0
		self.air=0.0
		self.water=0.0
		#get database planet settings	
		self.planets = self.db.getSettingsPlanet()
		#get database aspect settings
		self.aspects = self.db.getSettingsAspect()
		#Combine module data
		if self.type == "Combine":
			#make calculations
			module_data = ephemeris.ephData(self.c_year,self.c_month,self.c_day,self.c_hour,self.c_geolon,self.c_geolat,self.c_altitude,self.planets,self.zodiac,self.db.astrocfg)
		#Solar module data
		if self.type == "Solar":
			module_data = ephemeris.ephData(self.s_year,self.s_month,self.s_day,self.s_hour,self.s_geolon,self.s_geolat,self.s_altitude,self.planets,self.zodiac,self.db.astrocfg)
		elif self.type == "SecondaryProgression":
			module_data = ephemeris.ephData(self.sp_year,self.sp_month,self.sp_day,self.sp_hour,self.sp_geolon,self.sp_geolat,self.sp_altitude,self.planets,self.zodiac,self.db.astrocfg,houses_override=self.houses_override)				
		elif self.type == "Transit" or self.type == "Composite":
			module_data = ephemeris.ephData(self.year,self.month,self.day,self.hour,self.geolon,self.geolat,self.altitude,self.planets,self.zodiac,self.db.astrocfg)
			t_module_data = ephemeris.ephData(self.t_year,self.t_month,self.t_day,self.t_hour,self.t_geolon,self.t_geolat,self.t_altitude,self.planets,self.zodiac,self.db.astrocfg)
		else:
			#make calculations
			module_data = ephemeris.ephData(self.year,self.month,self.day,self.hour,self.geolon,self.geolat,self.altitude,self.planets,self.zodiac,self.db.astrocfg)
		#Transit module data
		if self.type == "Transit" or self.type == "Composite":
			#grab transiting module data
			self.t_planets_sign = t_module_data.planets_sign
			self.t_planets_degree = t_module_data.planets_degree
			self.t_planets_degree_ut = t_module_data.planets_degree_ut
			self.t_planets_retrograde = t_module_data.planets_retrograde
			self.t_houses_degree = t_module_data.houses_degree
			self.t_houses_sign = t_module_data.houses_sign
			self.t_houses_degree_ut = t_module_data.houses_degree_ut
		#grab normal module data
		self.planets_sign = module_data.planets_sign
		self.planets_degree = module_data.planets_degree
		self.planets_degree_ut = module_data.planets_degree_ut
		self.planets_retrograde = module_data.planets_retrograde
		self.houses_degree = module_data.houses_degree
		self.houses_sign = module_data.houses_sign
		self.houses_degree_ut = module_data.houses_degree_ut		
		self.lunar_phase = module_data.lunar_phase
		#make composite averages
		if self.type == "Composite":
			#new houses
			asc = self.houses_degree_ut[0]
			t_asc = self.t_houses_degree_ut[0]
			for i in range(12):
				#difference in distances measured from ASC
				diff = self.houses_degree_ut[i] - asc
				if diff < 0:
					diff = diff + 360.0
				t_diff = self.t_houses_degree_ut[i] - t_asc
				if t_diff < 0:
					t_diff = t_diff + 360.0	
				newdiff = (diff + t_diff) / 2.0
				#new ascendant
				if asc > t_asc:
					diff = asc - t_asc
					if diff > 180:
						diff = 360.0 - diff
						nasc = asc + (diff / 2.0)
					else:
						nasc = t_asc + (diff / 2.0)
				else:
					diff = t_asc - asc
					if diff > 180:
						diff = 360.0 - diff
						nasc = t_asc + (diff / 2.0)
					else:
						nasc = asc + (diff / 2.0)
				#new house degrees
				self.houses_degree_ut[i] = nasc + newdiff
				if self.houses_degree_ut[i] > 360:
					self.houses_degree_ut[i] = self.houses_degree_ut[i] - 360.0	
				#new house sign				
				for x in range(len(self.zodiac)):
					deg_low=float(x*30)
					deg_high=float((x+1)*30)
					if self.houses_degree_ut[i] >= deg_low:
						if self.houses_degree_ut[i] <= deg_high:
							self.houses_sign[i]=x
							self.houses_degree[i] = self.houses_degree_ut[i] - deg_low
			#new planets
			for i in range(23):
				#difference in degrees
				p1 = self.planets_degree_ut[i]
				p2 = self.t_planets_degree_ut[i]
				if p1 > p2:
					diff = p1 - p2
					if diff > 180:
						diff = 360.0 - diff
						self.planets_degree_ut[i] = (diff / 2.0) + p1
					else:
						self.planets_degree_ut[i] = (diff / 2.0) + p2
				else:
					diff = p2 - p1
					if diff > 180:
						diff = 360.0 - diff
						self.planets_degree_ut[i] = (diff / 2.0) + p2
					else:
						self.planets_degree_ut[i] = (diff / 2.0) + p1
				if self.planets_degree_ut[i] > 360:
					self.planets_degree_ut[i] = self.planets_degree_ut[i] - 360.0
			#list index 23 is asc, 24 is Mc, 25 is Dsc, 26 is Ic
			self.planets_degree_ut[23] = self.houses_degree_ut[0]
			self.planets_degree_ut[24] = self.houses_degree_ut[9]
			self.planets_degree_ut[25] = self.houses_degree_ut[6]
			self.planets_degree_ut[26] = self.houses_degree_ut[3]
			#new planet signs
			for i in range(27):
				for x in range(len(self.zodiac)):
					deg_low=float(x*30)
					deg_high=float((x+1)*30)
					if self.planets_degree_ut[i] >= deg_low:
						if self.planets_degree_ut[i] <= deg_high:
							self.planets_sign[i]=x
							self.planets_degree[i] = self.planets_degree_ut[i] - deg_low
							self.planets_retrograde[i] = False
		#width and height from screen
		ratio = float(self.screen_width) / float(self.screen_height)
		if ratio < 1.3: #1280x1024
			wm_off = 96
		else: # 1024x768, 800x600, 1280x800, 1680x1050
			wm_off = 64
		#correct dimensions
		self.height = self.screen_height-wm_off
		self.width = self.height * RATIO
		chartX = CHARTX
		chartY = CHARTY
		chartY += OFFSET
		#check for printer
		if printing == None:
			svgWidth = self.width
			svgHeight = self.height
			rotate = "0"
			translate = "0"
			viewbox = '0 0 {} {}'.format(chartX,chartY)
		else:
			svgWidth = printing['width']
			svgHeight = printing['height']
			rotate = "0"
			translate = "0"
			#set viewbox with 297mm * 2.6 + 210mm * 2.6
			viewbox = '0 0 {} {}'.format(chartX,chartY)
		#template dictionary		
		td=dict()
		r=RADIUS
		if(self.db.astrocfg['chartview']=="european"):
			self.c1=56
			self.c2=92
			self.c3=112
		else:				
			self.c1=0
			self.c2=36
			self.c3=120
		#transit
		if self.type == "Transit":
			td['transitRing']=self.transitRing( r )
			td['degreeRing']=self.degreeTransitRing( r )
			#circles
			td['c1'] = 'cx="' + str(r) + '" cy="' + str(r) + '" r="' + str(r-36) + '"'
			td['c1style'] = 'fill: none; stroke: %s; stroke-width: 1px; stroke-opacity:.4;'%(self.colors['zodiac_transit_ring_2'])
			td['c2'] = 'cx="' + str(r) + '" cy="' + str(r) + '" r="' + str(r-72) + '"'
			td['c2style'] = 'fill: %s; fill-opacity:.4; stroke: %s; stroke-opacity:.4; stroke-width: 1px'%(self.colors['paper_1'],self.colors['zodiac_transit_ring_1'])
			td['c3'] = 'cx="' + str(r) + '" cy="' + str(r) + '" r="' + str(r-160) + '"'
			td['c3style'] = 'fill: %s; fill-opacity:.8; stroke: %s; stroke-width: 1px'%(self.colors['paper_1'],self.colors['zodiac_transit_ring_0'])
			td['makeAspects'] = self.makeAspectsTransit( r , (r-160))
			td['makeAspectGrid'] = self.makeAspectTransitGrid( r )
			td['makePatterns'] = ''
		else:
			td['transitRing']=""
			td['degreeRing']=self.degreeRing( r )
			#circles
			td['c1'] = 'cx="' + str(r) + '" cy="' + str(r) + '" r="' + str(r-self.c1) + '"'
			td['c1style'] = 'fill: none; stroke: %s; stroke-width: 1px; '%(self.colors['zodiac_radix_ring_2'])
			td['c2'] = 'cx="' + str(r) + '" cy="' + str(r) + '" r="' + str(r-self.c2) + '"'
			td['c2style'] = 'fill: %s; fill-opacity:.2; stroke: %s; stroke-opacity:.4; stroke-width: 1px'%(self.colors['paper_1'],self.colors['zodiac_radix_ring_1'])
			td['c3'] = 'cx="' + str(r) + '" cy="' + str(r) + '" r="' + str(r-self.c3) + '"'
			td['c3style'] = 'fill: %s; fill-opacity:.8; stroke: %s; stroke-width: 1px'%(self.colors['paper_1'],self.colors['zodiac_radix_ring_0'])
			td['makeAspects'] = self.makeAspects( r , (r-self.c3))
			td['makeAspectGrid'] = self.makeAspectGrid( r )
			td['makePatterns'] = self.makePatterns()
		td['circleX']=str(0)
		td['circleY']=str(0)
		td['svgWidth']=str(svgWidth)
		td['svgHeight']=str(svgHeight)
		td['viewbox']=viewbox
		td['stringTitle']=self.name
		td['stringName']=self.charttype
		#bottom left
		siderealmode_chartview={
				"FAGAN_BRADLEY":_("Fagan Bradley"),
				"LAHIRI":_("Lahiri"),
				"DELUCE":_("Deluce"),
				"RAMAN":_("Ramanb"),
				"USHASHASHI":_("Ushashashi"),
				"KRISHNAMURTI":_("Krishnamurti"),
				"DJWHAL_KHUL":_("Djwhal Khul"),
				"YUKTESHWAR":_("Yukteshwar"),
				"JN_BHASIN":_("Jn Bhasin"),
				"BABYL_KUGLER1":_("Babyl Kugler 1"),
				"BABYL_KUGLER2":_("Babyl Kugler 2"),
				"BABYL_KUGLER3":_("Babyl Kugler 3"),
				"BABYL_HUBER":_("Babyl Huber"),
				"BABYL_ETPSC":_("Babyl Etpsc"),
				"ALDEBARAN_15TAU":_("Aldebaran 15Tau"),
				"HIPPARCHOS":_("Hipparchos"),
				"SASSANIAN":_("Sassanian"),
				"J2000":_("J2000"),
				"J1900":_("J1900"),
				"B1950":_("B1950")
				}
		if self.db.astrocfg['zodiactype'] == 'sidereal':
			td['bottomLeft1']=_("Sidereal")
			td['bottomLeft2']=siderealmode_chartview[self.db.astrocfg['siderealmode']]
		else:
			td['bottomLeft1']=_("Tropical")
			td['bottomLeft2'] = '%s: %s (%s) %s (%s)' % (_("Lunar Phase"),self.lunar_phase['sun_phase'],_("Sun"),self.lunar_phase['moon_phase'],_("Moon"))
		td['bottomLeft3'] = '%s: %s' % (_("Lunar Phase"),self.dec2deg(self.lunar_phase['degrees']))
		td['bottomLeft4'] = ''
		#lunar phase
		deg=self.lunar_phase['degrees']
		if(deg<90.0):
			maxr=deg
			if(deg>80.0): maxr=maxr*maxr
			lfcx=20.0+(deg/90.0)*(maxr+10.0)
			lfr=10.0+(deg/90.0)*maxr
			lffg,lfbg=self.colors["lunar_phase_0"],self.colors["lunar_phase_1"]
		elif(deg<180.0):
			maxr=180.0-deg
			if(deg<100.0): maxr=maxr*maxr
			lfcx=20.0+((deg-90.0)/90.0*(maxr+10.0))-(maxr+10.0)
			lfr=10.0+maxr-((deg-90.0)/90.0*maxr)
			lffg,lfbg=self.colors["lunar_phase_1"],self.colors["lunar_phase_0"]
		elif(deg<270.0):
			maxr=deg-180.0
			if(deg>260.0): maxr=maxr*maxr
			lfcx=20.0+((deg-180.0)/90.0*(maxr+10.0))
			lfr=10.0+((deg-180.0)/90.0*maxr)
			lffg,lfbg=self.colors["lunar_phase_1"],self.colors["lunar_phase_0"]
		elif(deg<361):
			maxr=360.0-deg
			if(deg<280.0): maxr=maxr*maxr
			lfcx=20.0+((deg-270.0)/90.0*(maxr+10.0))-(maxr+10.0)
			lfr=10.0+maxr-((deg-270.0)/90.0*maxr)
			lffg,lfbg=self.colors["lunar_phase_0"],self.colors["lunar_phase_1"]
		td['lunar_phase_fg'] = lffg		
		td['lunar_phase_bg'] = lfbg
		td['lunar_phase_cx'] = '%s' %(lfcx)
		td['lunar_phase_r'] = '%s' %(lfr)
		td['lunar_phase_outline'] = self.colors["lunar_phase_2"]
		#rotation based on latitude
		td['lunar_phase_rotate'] = "%s" % (-90.0-self.geolat)
		#stringlocation
		if len(self.location) > 35:
			split=self.location.split(",")
			if len(split) > 1:
				td['stringLocation']=split[0]+", "+split[-1]
				if len(td['stringLocation']) > 35:
					td['stringLocation'] = td['stringLocation'][:35]+"..."
			else:
				td['stringLocation']=self.location[:35]+"..."
		else:
			td['stringLocation']=self.location
		td['stringDateTime']=str(self.year_loc)+'-%(#1)02d-%(#2)02d %(#3)02d:%(#4)02d:%(#5)02d' % {'#1':self.month_loc,'#2':self.day_loc,'#3':self.hour_loc,'#4':self.minute_loc,'#5':self.second_loc} + self.decTzStr(self.timezone)
		td['stringLat']="%s: %s" %(self.label['latitude'],self.lat2str(self.geolat))
		td['stringLon']="%s: %s" %(self.label['longitude'],self.lon2str(self.geolon))
		postype={"geo":self.label["apparent_geocentric"],"truegeo":self.label["true_geocentric"],
				"topo":self.label["topocentric"],"helio":self.label["heliocentric"]}
		td['stringPosition']=postype[self.db.astrocfg['postype']]
		#paper_color_X
		td['paper_color_0']=self.colors["paper_0"]
		td['paper_color_1']=self.colors["paper_1"]
		#planets_color_X
		for i in range(len(self.planets)):
			td['planets_color_%s'%(i)]=self.colors["planet_%s"%(i)]
		#zodiac_color_X
		for i in range(12):
			td['zodiac_color_%s'%(i)]=self.colors["zodiac_icon_%s" %(i)]
		#orb_color_X
		for i in range(len(self.aspects)):
			td['orb_color_%s'%(self.aspects[i]['degree'])]=self.colors["aspect_%s" %(self.aspects[i]['degree'])]
		#config zoom from versions v1.1.68 on
		td['cfgZoom']="1.0"
		#zoom in earlier versions below 1.1.68
		#td['cfgZoom']=str(self.zoom)
		#other configs
		td['cfgRotate']=rotate
		td['cfgTranslate']=translate
		#functions
		td['makeZodiac'] = self.makeZodiac( r )
		td['makeHouses'] = self.makeHouses( r )
		td['makePlanets'] = self.makePlanets( r )
		td['makeElements'] = self.makeElements( r )
		td['makeLegend'] = self.makeLegend()
		td['makePlanetGrid'] = self.makePlanetGrid()
		td['makeHousesGrid'] = self.makeHousesGrid()
		#read template
		f=open(self.cfg.xml_svg)
		template=Template(f.read()).substitute(td)
		f.close()
		if printing is None:
			f=open(self.cfg.tempfilename,"w")
			dprint("Creating SVG: lat="+str(self.geolat)+' lon='+str(self.geolon)+' loc='+self.location)
		else:
			f=open(self.cfg.tempfilenameprint,"w")
			dprint("Printing SVG: lat="+str(self.geolat)+' lon='+str(self.geolon)+'loc='+self.location)
		#write template
		f.write(template)
		f.close()
		#return filename
		return self.cfg.tempfilename

	""" make graphic for monthly timeline """
	def makeTimelineSVG(self,printing,y,m):
		tz = datetime.timedelta(seconds=float(self.timezone)*float(3600))
		startdate = datetime.datetime(y,m,1,12) - tz
		q,r = divmod(startdate.month, 12)
		enddate = datetime.datetime(startdate.year+q, r+1, 1,12)
		delta = enddate - startdate
		atgrid={}
		astypes={}
		retrogrid={}
		for d in range(delta.days):
			cdate = startdate + datetime.timedelta(days=d)
			tmoddata = ephemeris.ephData(cdate.year,cdate.month,cdate.day,cdate.hour, self.geolon,self.geolat,self.altitude,self.planets,self.zodiac,self.db.astrocfg)
			#planets_sign,planets_degree,planets_degree_ut,planets_retrograde,houses_degree
			#houses_sign,houses_degree_ut
			for i in range(len(self.planets)):
				start=self.planets_degree_ut[i]
				for x in range(i+1):
					end=tmoddata.planets_degree_ut[x]
					diff=float(self.degreeDiff(start,end))
					#skip asc/dsc/mc/ic on tmoddata
					if 23 <= x <= 26:
						continue
					#skip moon on tmoddate
					if x == 1:
						continue
					#loop orbs
					if (self.planets[i]['visible'] == 1) & (self.planets[x]['visible'] == 1):	
						for z in range(len(self.aspects)):
							#only major aspects
							if self.aspects[z]['is_major'] != 1:
								continue
							#check for personal planets and determine orb
							orb_before = 4
							orb_after = 4
							#check if we want to display this aspect	
							if	( float(self.aspects[z]['degree']) - orb_before ) <= diff <= ( float(self.aspects[z]['degree']) + orb_after ):
								orb = diff - self.aspects[z]['degree']
								if orb < 0:
									orb = orb/-1						
								#aspect grid dictionary
								s="%02d%02d%02d"%(i,z,x)
								astypes[s]=(i,x,z)
								
								if s not in retrogrid:
									retrogrid[s]={}
								retrogrid[s][d]=tmoddata.planets_retrograde[x]
									
								if s not in atgrid:
									atgrid[s]={}
								atgrid[s][d]=orb
		#sort
		keys = list(astypes.keys())
		keys.sort()
		self.pages = int(math.ceil(len(keys)/65.0))
		out = ""
		#make numbers of days in month
		dx=[80]
		skipdays = [9,19]
		for d in range(delta.days):
			if d in skipdays:
				dx.append(dx[-1]+40)
			else:
				dx.append(dx[-1]+20)	
		for p in range(self.pages):
			if p == 0:
				ystart = 10
			else:
				ystart = (1188 * p) + 62
			pagelen = (len(keys)+1)-p*65
			if pagelen > 65:
				pagelen = 66
			ylen = ((len(keys)+1)-p*65)*16	
			for a in range(delta.days):
				out += '<text x="%s" y="%s" style="fill: %s; font-size: 10">%02d</text>\n'%(
					dx[a],ystart,self.colors['paper_0'],a+1)
				out += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke: %s; stroke-width: .5; stroke-opacity:1;"/>\n'%(
					dx[a]-5,ystart,dx[a]-5,ystart+pagelen*16,self.colors['paper_0'])	
				#skipdays line
				if a in skipdays:
					out += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke: %s; stroke-width: .5; stroke-opacity:1;"/>\n'%(
						dx[a]-5+20,ystart,dx[a]-5+20,ystart+pagelen*16,self.colors['paper_0'])						
			#last line
			out += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke: %s; stroke-width: .5; stroke-opacity:1;"/>\n'%(
					dx[-1]-5,ystart,dx[-1]-5,ystart+pagelen*16,self.colors['paper_0'])
		#get the number of total aspects
		c = 0
		for m in range(len(keys)):
			i,x,z = astypes[keys[m]]
			c += 1
			pagenum = int(math.ceil(c/65.0))
			pagey = (pagenum - 1) * 200
			y = (c*16) + pagey
			#horizontal lines
			out += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke: %s; stroke-width: .5; stroke-opacity:1;"/>\n'%(
				0,y-1,dx[skipdays[0]]+15,y-1,self.colors['paper_0'])
			for s in range(len(skipdays)):
				if s is len(skipdays)-1:
					out += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke: %s; stroke-width: .5; stroke-opacity:1;"/>\n'%(
						dx[skipdays[s]+1]-5,y-1,dx[-1],y-1,self.colors['paper_0'])
				else:
					out += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke: %s; stroke-width: .5; stroke-opacity:1;"/>\n'%(
						dx[skipdays[s]+1]-5,y-1,dx[skipdays[s+1]]+15,y-1,self.colors['paper_0'])
			#outer planet
			out += '<g transform="translate(0,%s)"><g transform="scale(.5)"><use x="0" y="0" xlink:href="#%s" /></g></g>\n'%(
				y,self.svgSafeHref(self.planets[x]['name']))
			#aspect
			out += '<g><use x="20" y="%s" xlink:href="#orb%s" /></g>\n'%(
				y,self.aspects[z]['degree'])			
			#inner planet
			out += '<g transform="translate(40,%s)"><g transform="scale(.5)"><use x="0" y="0" xlink:href="#%s" /></g></g>\n'%(y,
				self.svgSafeHref(self.planets[i]['name']))		
			for d in range(delta.days):					
				if d in atgrid[keys[m]]:
					orb = atgrid[keys[m]][d]
					op = .1+(.7-(orb/(4/.7))) #4 is maxorb
					if op > 1:
						op = 1
					strop = str(float(orb))
					out += '<rect x="%s" y="%s" width="20" height="16" style="fill: %s; fill-opacity:%s;" />'%(dx[d]-5,y-1,self.colors["aspect_%s" %(self.aspects[z]['degree'])],op)
					#check for retrograde outer planet
					if retrogrid[keys[m]][d]:
						out += '<g transform="translate(%s,%s)"><g transform="scale(.3)">\
							<use x="0" y="0" xlink:href="#retrograde" style="fill:%s; fill-opacity:.8;" /></g></g>\n'%(dx[d]+10,y+10,self.colors['paper_0'],)							
					out += '<text x="%s" y="%s" style="fill: %s; font-size: 10">%s</text>\n'%(
						dx[d],y+9,self.colors['paper_0'],strop[:3])
				else:
					out += ""
		#template
		td = {}
		td['paper_color_0']=self.colors["paper_0"]
		td['paper_color_1']=self.colors["paper_1"]
		for i in range(len(self.planets)):
			td['planets_color_%s'%(i)]=self.colors["planet_%s"%(i)]
		for i in range(12):
			td['zodiac_color_%s'%(i)]=self.colors["zodiac_icon_%s" %(i)]
		for i in range(len(self.aspects)):
			td['orb_color_%s'%(self.aspects[i]['degree'])]=self.colors["aspect_%s" %(self.aspects[i]['degree'])]
		td['stringTitle'] = "%s Timeline for %s"%(
			startdate.strftime("%B %Y"),self.name)
		self.pagesY = (1188 * self.pages)+10 #ten is buffer between self.pages
		if printing is None:
			td['svgWidth'] = 1050
			td['svgHeight'] = (td['svgWidth']/840.0)* self.pagesY
			td['viewbox'] = "0 0 840 %s" %(self.pagesY) 
		else:
			# add buffer of ten between self.pages
			self.pagesY += 10
			td['svgWidth'] = printing['width']
			td['svgHeight'] = printing['height']
			td['viewbox'] = "0 %s 840 1188" %( printing['pagenum']*(1188+10) )
		td['data'] = out
		#self.pages rectangles
		pagesRect,x,y,w,h="",0,0,840,1188
		for p in range(self.pages):
			if p == 0:
				offset=0
			else:
				offset=10
			pagesRect += '<rect x="%s" y="%s" width="%s" height="%s" style="fill: %s;" />'%(x,y+(p*1188)+offset,w,h,self.colors['paper_1'],)
		td['pagesRect'] = pagesRect
		#read and write template
		f=open(self.cfg.xml_svg_table)
		template=Template(f.read()).substitute(td)
		f.close()
		if printing is None:
			f=open(self.cfg.tempfilenametable,"w")
		else:
			f=open(self.cfg.tempfilenametableprint,"w")
		f.write(template)
		f.close()

	""" make graphic for cusp aspects """
	def makeCuspAspectsSVG(self, printing):
		#data
		out='<g transform="scale(1.5)">'
		xindent=50
		yindent=200
		box=14
		style='stroke:%s; stroke-width: 1px; stroke-opacity:.6; fill:none' % (app.colors['paper_0'],)
		textstyle="font-size: 11px; color: %s" % (app.colors['paper_0'],)
		#draw cusps
		for cusp in range(len(app.houses_degree_ut)):
				x = xindent - box
				y = yindent - (box*(cusp+1))
				out += '<text x="%s" y="%s" style="%s">%s</text>\n'%(x-30, y+box-5, textstyle, app.label['cusp']+" "+str(cusp+1))
		# add some space
		xindent += 32
		revr=range(len(app.planets))
		for a in revr:
			if 23 <= a <= 26:
				continue; #skip asc/dsc/mc/ic
			if a == 11 or a == 13 or a == 21 or a == 22:
				continue; #skip ?,?,intp. apogee, intp. perigee
			start=app.planets_degree_ut[a]
			#first planet 
			out += '<rect x="%s" y="%s" width="%s" height="%s" style="%s"/>\n' %(xindent,yindent,box,box,style)
			out += '<use transform="scale(0.4)" x="%s" \
					y="%s" xlink:href="#%s" />\n'%((xindent+2)*2.5,(yindent+1)*2.5, app.planets[a]['name'])
			yorb=yindent - box
			for b in range(12):
				end=app.houses_degree_ut[b]
				diff=app.degreeDiff(start,end)
				out += '<rect x="%s" y="%s" width="%s" height="%s" style="%s"/>\n'%(xindent,yorb,box,box,style)
				for z in range(len(app.aspects)):
					if	( float(app.aspects[z]['degree']) - float(app.aspects[z]['orb']) ) <= diff <= ( float(app.aspects[z]['degree']) + float(app.aspects[z]['orb']) ) and app.aspects[z]['visible_grid'] == 1:
							out += '<use x="%s" y="%s" xlink:href="#orb%s" />\n'%(xindent,yorb+1,app.aspects[z]['degree'])
				yorb=yorb-box
			xindent += box
		#add cusp to cusp
		xindent = 50
		yindent = 400
		#draw cusps
		for cusp in range(len(app.houses_degree_ut)):
				x = xindent - box
				y = yindent - (box*(cusp+1))
				out += '<text x="%s" y="%s" style="%s">%s</text>\n'%(x-30, y+box-5, textstyle, app.label['cusp']+" "+str(cusp+1))
		#add some space
		xindent += 32
		for a in range(12):
			start=app.houses_degree_ut[a]
			#first planet 
			out += '<rect x="%s" y="%s" width="%s" height="%s" style="%s"/>\n' %(xindent,yindent,box,box,style)
			out += '<text x="%s" y="%s" style="%s">%s</text>\n'%((xindent+2), (yindent+box-4), textstyle, ""+str(a+1))
			yorb=yindent - box
			for b in range(12):
				end=app.houses_degree_ut[b]
				diff=app.degreeDiff(start,end)
				out += '<rect x="%s" y="%s" width="%s" height="%s" style="%s"/>\n'%(xindent,yorb,box,box,style)
				for z in range(len(app.aspects)):
					if	( float(app.aspects[z]['degree']) - float(app.aspects[z]['orb']) ) <= diff <= ( float(app.aspects[z]['degree']) + float(app.aspects[z]['orb']) ) and app.aspects[z]['visible_grid'] == 1:
							out += '<use x="%s" y="%s" xlink:href="#orb%s" />\n'%(xindent,yorb+1,app.aspects[z]['degree'])
				yorb=yorb-box
			xindent += box	
		out += "</g>"
		#template
		td = {}
		td['paper_color_0']=app.colors["paper_0"]
		td['paper_color_1']=app.colors["paper_1"]
		for i in range(len(app.planets)):
			td['planets_color_%s'%(i)]=app.colors["planet_%s"%(i)]
		for i in range(12):
			td['zodiac_color_%s'%(i)]=app.colors["zodiac_icon_%s" %(i)]
		for i in range(len(app.aspects)):
			td['orb_color_%s'%(app.aspects[i]['degree'])]=app.colors["aspect_%s" %(app.aspects[i]['degree'])]
		td['stringTitle'] = "Cusp Aspects for %s"%(app.name)
		self.pages=1
		#ten is buffer between self.pages
		self.pagesY = (1188 * self.pages)+10
		if printing is None:
			td['svgWidth'] = 1050
			td['svgHeight'] = (td['svgWidth']/840.0)* self.pagesY
			td['viewbox'] = "0 0 840 %s" %( self.pagesY ) 
		else:
			td['svgWidth'] = printing['width']
			td['svgHeight'] = printing['height']
			td['viewbox'] = "0 %s 840 1188" %( printing['pagenum']*(1188+10) )
		td['data'] = out
		td['pagesRect'] = '<rect x="0" y="0" width="840" height="1188" style="fill: %s;" />' % (app.colors['paper_1'],)
		#read and write template
		f=open(self.cfg.xml_svg_table)
		template=Template(f.read()).substitute(td)
		f.close()
		if printing is None:
			f=open(self.cfg.tempfilenametable,"w")
		else:
			f=open(self.cfg.tempfilenametableprint,"w")
		f.write(template)
		f.close()
		return self.cfg.tempfilenametable

	""" Draw transit ring """
	def transitRing( self , r ):
		out = '<circle cx="%s" cy="%s" r="%s" style="fill: none; stroke: %s; stroke-width: 36px; stroke-opacity: .4;"/>' % (r,r,r-18,self.colors['paper_1'])
		out += '<circle cx="%s" cy="%s" r="%s" style="fill: none; stroke: %s; stroke-width: 1px; stroke-opacity: .6;"/>' % (r,r,r,self.colors['zodiac_transit_ring_3'])
		return out

	def degreeRing( self , r ):
		""" Draw degree ring """
		out=''
		for i in range(72):
			offset = float(i*5) - self.houses_degree_ut[6]
			if offset < 0:
				offset = offset + 360.0
			elif offset > 360:
				offset = offset - 360.0
			x1 = self.sliceToX( 0 , r-self.c1 , offset ) + self.c1
			y1 = self.sliceToY( 0 , r-self.c1 , offset ) + self.c1
			x2 = self.sliceToX( 0 , r+2-self.c1 , offset ) - 2 + self.c1
			y2 = self.sliceToY( 0 , r+2-self.c1 , offset ) - 2 + self.c1
			out += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke: %s; stroke-width: 1px; stroke-opacity:.9;"/>\n' % (
				x1,y1,x2,y2,self.colors['paper_0'] )
		return out

	def degreeTransitRing( self , r ):
		out=''
		for i in range(72):
			offset = float(i*5) - self.houses_degree_ut[6]
			if offset < 0:
				offset = offset + 360.0
			elif offset > 360:
				offset = offset - 360.0
			x1 = self.sliceToX( 0 , r , offset )
			y1 = self.sliceToY( 0 , r , offset )
			x2 = self.sliceToX( 0 , r+2 , offset ) - 2
			y2 = self.sliceToY( 0 , r+2 , offset ) - 2
			out += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke: #F00; stroke-width: 1px; stroke-opacity:.9;"/>\n' %(x1, y1, x2, y2)
		return out

	def lat2str( self, coord ):
		""" Floating latitude an longitude to string """
		sign=self.label["north"]
		if coord < 0.0:
			sign=self.label["south"]
			coord = abs(coord)
		deg = int(coord)
		min = int( (float(coord) - deg) * 60 )
		sec = int( round( float( ( (float(coord) - deg) * 60 ) - min) * 60.0 ) )
		return "%s°%s'%s\" %s" % (deg,min,sec,sign)

	def lon2str( self, coord ):
		sign=self.label["east"]
		if coord < 0.0:
			sign=self.label["west"]
			coord = abs(coord)
		deg = int(coord)
		min = int( (float(coord) - deg) * 60 )
		sec = int( round( float( ( (float(coord) - deg) * 60 ) - min) * 60.0 ) )
		return "%s°%s'%s\" %s" % (deg,min,sec,sign)

	def decHour( self , input ):
		""" decimal hour to minutes and seconds
			corrected for rounding error in case of repeating decimal
		"""
		total= int(input * 3600 + 0.5)
		m, s = divmod(total, 60)
		h, m = divmod(m, 60)
		return [h,m,s]

	def decHourJoin( self, inH, inM, inS ):
		""" join hour, minutes, seconds, timezone integere to hour float """
		dh = float(inH)
		dm = float(inM)/60
		ds = float(inS)/3600
		output = dh + dm + ds
		return output

	def offsetToTz( self, dtoffset ):
		""" Datetime offset to float in hours """
		dh = float(dtoffset.days * 24)
		sh = float(dtoffset.seconds / 3600.0)
		output = dh + sh
		return output

	def decTzStr( self, tz ):
		""" Decimal timezone string """
		if tz > 0:
			h = int(tz)
			m = int((float(tz)-float(h))*float(60))
			return " [+%(#1)02d:%(#2)02d]" % {'#1':h,'#2':m}
		else:
			h = int(tz)
			m = int((float(tz)-float(h))*float(60))/-1
			return " [-%(#1)02d:%(#2)02d]" % {'#1':h/-1,'#2':m}

	def degreeDiff( self, a ,b ):
		""" Degree difference """
		out=float()
		if a > b:
			out=a-b
		if a < b:
			out=b-a
		if out > 180.0:
			out=360.0-out
		return out

	def dec2deg( self, dec, type="3" ):
		""" Decimal to degrees (a°b'c") """
		dec=float(dec)
		a=int(dec)
		a_new=(dec-float(a)) * 60.0
		b_rounded = int(round(a_new))
		b=int(a_new)
		c=int(round((a_new-float(b))*60.0))
		if type=="3":
			out = '%(#1)02d&#176;%(#2)02d&#39;%(#3)02d&#34;' % {'#1':a,'#2':b, '#3':c}
		elif type=="2":
			out = '%(#1)02d&#176;%(#2)02d&#39;' % {'#1':a,'#2':b_rounded}
		elif type=="1":
			out = '%(#1)02d&#176;' % {'#1':a}
		return str(out)

	def drawAspect( self, r, ar, degA, degB, color ):
		""" draw svg aspects: ring, aspect ring, degreeA degreeB """
		offset = (int(self.houses_degree_ut[6]) / -1) + int(degA)
		x1 = self.sliceToX( 0 , ar , offset ) + (r-ar)
		y1 = self.sliceToY( 0 , ar , offset ) + (r-ar)
		offset = (int(self.houses_degree_ut[6]) / -1) + int(degB)
		x2 = self.sliceToX( 0 , ar , offset ) + (r-ar)
		y2 = self.sliceToY( 0 , ar , offset ) + (r-ar)
		out = '			<line x1="'+str(x1)+'" y1="'+str(y1)+'" x2="'+str(x2)+'" y2="'+str(y2)+'" style="stroke: '+color+'; stroke-width: 1; stroke-opacity: .9;"/>\n'
		return out

	def sliceToX(self, slice, r, offset ):
		plus = (math.pi * offset) / 180
		radial = ((math.pi/6) * slice) + plus
		return r * (math.cos(radial)+1)

	def sliceToY(self , slice , r, offset):
		plus = (math.pi * offset) / 180
		radial = ((math.pi/6) * slice) + plus
		return r * ((math.sin(radial)/-1)+1)

	def zodiacSlice(self, num, r, style, type ):
		# pie slices
		if self.db.astrocfg["houses_system"] == "G":
			offset = 360 - self.houses_degree_ut[18]
		else:
			offset = 360 - self.houses_degree_ut[6]
		#check transit
		if self.type == "Transit":
			dropin=0
		else:
			dropin = self.c1
		slice = '<path d="M' + str(r) + ',' + str(r) + ' L' + str(dropin + self.sliceToX(num,r-dropin,offset)) + ',' + str( dropin + self.sliceToY(num,r-dropin,offset)) + ' A' + str(r-dropin) + ',' + str(r-dropin) + ' 0 0,0 ' + str(dropin + self.sliceToX(num+1,r-dropin,offset)) + ',' + str(dropin + self.sliceToY(num+1,r-dropin,offset)) + ' z" style="' + style + '"/>'
		# symbols
		offset = offset + 15
		# check transit
		if self.type == "Transit":
			dropin=54
		else:
			dropin=18+self.c1
		sign = '<g transform="translate(-16,-16)"><use x="' + str(dropin + self.sliceToX(num,r-dropin,offset)) + '" y="' + str(dropin + self.sliceToY(num,r-dropin,offset)) + '" xlink:href="#' + type + '" /></g>\n'
		return slice + '\n' + sign

	def makeZodiac( self, r ):
		output = ""
		for i in range(len(self.zodiac)):
			output = output + self.zodiacSlice( i , r , "fill:" + self.colors["zodiac_bg_%s"%(i)] + "; fill-opacity: 0.5;" , self.zodiac[i]) + '\n'
		return output

	def makeHouses( self, r ):
		path = ""
		if self.db.astrocfg["houses_system"] == "G":
			xr = 36
		else:
			xr = 12
		for i in range(xr):
			# check transit
			if self.type == "Transit":
				dropin=160
				roff=72
				t_roff=36
			else:
				dropin=self.c3
				roff=self.c1
			# offset is negative desc houses_degree_ut[6]
			offset = (int(self.houses_degree_ut[int(xr/2)]) / -1) + int(self.houses_degree_ut[i])
			x1 = self.sliceToX( 0 , (r-dropin) , offset ) + dropin
			y1 = self.sliceToY( 0 , (r-dropin) , offset ) + dropin
			x2 = self.sliceToX( 0 , r-roff , offset ) + roff
			y2 = self.sliceToY( 0 , r-roff , offset ) + roff
			if i < (xr-1):
				text_offset = offset + int(self.degreeDiff( self.houses_degree_ut[(i+1)], self.houses_degree_ut[i] ) / 2 )
			else:
				text_offset = offset + int(self.degreeDiff( self.houses_degree_ut[0], self.houses_degree_ut[(xr-1)] ) / 2 )
			# mc, asc, dsc, ic
			if i == 0:
				linecolor=self.planets[23]['color']
			elif i == 9:
				linecolor=self.planets[24]['color']
			elif i == 6:
				linecolor=self.planets[25]['color']
			elif i == 3:
				linecolor=self.planets[26]['color']
			else:
				linecolor=self.colors['houses_radix_line']
			# transit houses lines
			if self.type == "Transit":
				#degrees for point zero
				zeropoint = 360 - self.houses_degree_ut[6]
				t_offset = zeropoint + self.t_houses_degree_ut[i]
				if t_offset > 360:
					t_offset = t_offset - 360
				t_x1 = self.sliceToX( 0 , (r-t_roff) , t_offset ) + t_roff
				t_y1 = self.sliceToY( 0 , (r-t_roff) , t_offset ) + t_roff
				t_x2 = self.sliceToX( 0 , r , t_offset )
				t_y2 = self.sliceToY( 0 , r , t_offset )
				if i < 11:
					t_text_offset = t_offset + int(self.degreeDiff( self.t_houses_degree_ut[(i+1)], self.t_houses_degree_ut[i] ) / 2 )
				else:
					t_text_offset = t_offset + int(self.degreeDiff( self.t_houses_degree_ut[0], self.t_houses_degree_ut[11] ) / 2 )
				#linecolor
				if i == 0 or i == 9 or i == 6 or i == 3:
					t_linecolor=linecolor
				else:
					t_linecolor = self.colors['houses_transit_line']
				xtext = self.sliceToX( 0 , (r-8) , t_text_offset ) + 8
				ytext = self.sliceToY( 0 , (r-8) , t_text_offset ) + 8
				path = path + '<text style="fill: #00f; fill-opacity: .4; font-size: 14px"><tspan x="'+str(xtext-3)+'" y="'+str(ytext+3)+'">'+str(i+1)+'</tspan></text>\n'
				path = path + '<line x1="'+str(t_x1)+'" y1="'+str(t_y1)+'" x2="'+str(t_x2)+'" y2="'+str(t_y2)+'" style="stroke: '+t_linecolor+'; stroke-width: 2px; stroke-opacity:.3;"/>\n'
			# if transit
			if self.type == "Transit":
				dropin=84
			elif self.db.astrocfg["chartview"] == "european":
				dropin=100
			else:
				dropin=48
			xtext = self.sliceToX( 0 , (r-dropin) , text_offset ) + dropin #was 132
			ytext = self.sliceToY( 0 , (r-dropin) , text_offset ) + dropin #was 132
			path = path + '<line x1="'+str(x1)+'" y1="'+str(y1)+'" x2="'+str(x2)+'" y2="'+str(y2)+'" style="stroke: '+linecolor+'; stroke-width: 2px; stroke-dasharray:3,2; stroke-opacity:.4;"/>\n'
			path = path + '<text style="fill: #f00; fill-opacity: .6; font-size: 14px"><tspan x="'+str(xtext-3)+'" y="'+str(ytext+3)+'">'+str(i+1)+'</tspan></text>\n'
		return path

	def makePlanets( self , r ):
		planets_degut={}
		diff=range(len(self.planets))
		for i in range(len(self.planets)):
			if self.planets[i]['visible'] == 1:
				# list of planets sorted by degree
				planets_degut[self.planets_degree_ut[i]]=i
			#element: get extra points if planet is in own zodiac
			pz = self.planets[i]['zodiac_relation']
			cz = self.planets_sign[i]
			extrapoints = 0
			if pz != -1:
				for e in range(len(pz.split(','))):
					if int(pz.split(',')[e]) == int(cz):
						extrapoints = 10
			# calculate element points for all planets
			ele = self.zodiac_element[self.planets_sign[i]]
			if ele == "fire":
				self.fire = self.fire + self.planets[i]['element_points'] + extrapoints
			elif ele == "earth":
				self.earth = self.earth + self.planets[i]['element_points'] + extrapoints
			elif ele == "air":
				self.air = self.air + self.planets[i]['element_points'] + extrapoints
			elif ele == "water":
				self.water = self.water + self.planets[i]['element_points'] + extrapoints
		output = ""
		keys = list(planets_degut.keys())
		keys.sort()
		switch=0
		planets_degrouped = {}
		groups = []
		planets_by_pos = list(range(len(planets_degut)))
		planet_drange = 3.4
		# get groups closely together
		group_open = False
		for e in range(len(keys)):
			i=planets_degut[keys[e]]
			# get distances between planets
			if e == 0:
				prev = self.planets_degree_ut[planets_degut[keys[-1]]]
				next = self.planets_degree_ut[planets_degut[keys[1]]]
			elif e == (len(keys)-1):
				prev = self.planets_degree_ut[planets_degut[keys[e-1]]]
				next = self.planets_degree_ut[planets_degut[keys[0]]]
			else:
				prev = self.planets_degree_ut[planets_degut[keys[e-1]]]
				next = self.planets_degree_ut[planets_degut[keys[e+1]]]
			diffa=self.degreeDiff(prev,self.planets_degree_ut[i])
			diffb=self.degreeDiff(next,self.planets_degree_ut[i])
			planets_by_pos[e]=[i,diffa,diffb]
			# print "%s %s %s" % (self.planets[i]['label'],diffa,diffb)
			if (diffb < planet_drange):
				if group_open:
					groups[-1].append([e,diffa,diffb,self.planets[planets_degut[keys[e]]]["label"]])
				else:
					group_open=True
					groups.append([])
					groups[-1].append([e, diffa, diffb, self.planets[planets_degut[keys[e]]]["label"]])
			else:
				if group_open:
					groups[-1].append([e, diffa, diffb, self.planets[planets_degut[keys[e]]]["label"]])
				group_open=False
		def zero(x): return 0
		planets_delta = list(map(zero,range(len(self.planets))))
		# print groups
		# print planets_by_pos
		for a in range(len(groups)):
			#Two grouped planets
			if len(groups[a]) == 2:
				next_to_a = groups[a][0][0]-1
				if groups[a][1][0] == (len(planets_by_pos)-1):
					next_to_b = 0
				else:
					next_to_b = groups[a][1][0]+1
				# if both planets have room
				if (groups[a][0][1] > (2*planet_drange))&(groups[a][1][2] > (2*planet_drange)):
					planets_delta[groups[a][0][0]]=-(planet_drange-groups[a][0][2])/2
					planets_delta[groups[a][1][0]]=+(planet_drange-groups[a][0][2])/2
				# if planet a has room
				elif (groups[a][0][1] > (2*planet_drange)):
					planets_delta[groups[a][0][0]]=-planet_drange
				#if planet b has room
				elif (groups[a][1][2] > (2*planet_drange)):
					planets_delta[groups[a][1][0]]=+planet_drange
				# if planets next to a and b have room move them
				elif (planets_by_pos[next_to_a][1] > (2.4*planet_drange))&(planets_by_pos[next_to_b][2] > (2.4*planet_drange)):
					planets_delta[(next_to_a)]=(groups[a][0][1]-planet_drange*2)
					planets_delta[groups[a][0][0]]=-planet_drange*.5
					planets_delta[next_to_b]=-(groups[a][1][2]-planet_drange*2)
					planets_delta[groups[a][1][0]]=+planet_drange*.5
				# if planet next to a has room move them
				elif (planets_by_pos[next_to_a][1] > (2*planet_drange)):
					planets_delta[(next_to_a)]=(groups[a][0][1]-planet_drange*2.5)
					planets_delta[groups[a][0][0]]=-planet_drange*1.2
				# if planet next to b has room move them
				elif (planets_by_pos[next_to_b][2] > (2*planet_drange)):
					planets_delta[next_to_b]=-(groups[a][1][2]-planet_drange*2.5)
					planets_delta[groups[a][1][0]]=+planet_drange*1.2
			# Three grouped planets or more
			xl = len(groups[a])
			if xl >= 3:
				available = groups[a][0][1]
				for f in range(xl):
					available += groups[a][f][2]
				need = (3*planet_drange)+(1.2*(xl-1)*planet_drange)
				leftover = available - need
				xa=groups[a][0][1]
				xb=groups[a][(xl-1)][2]
				# center
				if (xa > (need*.5)) & (xb > (need*.5)):
					startA = xa - (need*.5)
				# position relative to next planets
				else:
					startA = (leftover/(xa+xb))*xa
					startB = (leftover/(xa+xb))*xb
				if available > need:
					planets_delta[groups[a][0][0]] = startA-groups[a][0][1]+(1.5*planet_drange)
					for f in range(xl-1):
						planets_delta[groups[a][(f+1)][0]] = 1.2*planet_drange+planets_delta[groups[a][f][0]]-groups[a][f][2]
		for e in range(len(keys)):
			i = planets_degut[keys[e]]
			#coordinates
			if self.type == "Transit":
				if 22 < i < 27:
					rplanet = 76
				elif switch == 1:
					rplanet=110
					switch = 0
				else:
					rplanet=130
					switch = 1
			else:
				# if 22 < i < 27 it is asc, mc, dsc, ic (angles of chart)
				# put on special line (rplanet is range from outer ring)
				amin, bmin, cmin = 0, 0, 0
				if self.db.astrocfg["chartview"] == "european":
					amin = 74-10
					bmin = 94-10
					cmin = 40-10
				if 22 < i < 27:
					rplanet = 40-cmin
				elif switch == 1:
					rplanet=74-amin
					switch = 0
				else:
					rplanet=94-bmin
					switch = 1
			rtext=45
			if self.db.astrocfg['houses_system'] == "G":
				offset = (int(self.houses_degree_ut[18]) / -1) + int(self.planets_degree_ut[i])
			else:
				offset = (int(self.houses_degree_ut[6]) / -1) + int(self.planets_degree_ut[i]+planets_delta[e])
				trueoffset = (int(self.houses_degree_ut[6]) / -1) + int(self.planets_degree_ut[i])
			planet_x = self.sliceToX( 0 , (r-rplanet) , offset ) + rplanet
			planet_y = self.sliceToY( 0 , (r-rplanet) , offset ) + rplanet
			if self.type == "Transit":
				scale=0.8
			elif self.db.astrocfg["chartview"] == "european":
				scale=0.8
				# line1
				x1=self.sliceToX( 0 , (r-self.c3) , trueoffset ) + self.c3
				y1=self.sliceToY( 0 , (r-self.c3) , trueoffset ) + self.c3
				x2=self.sliceToX( 0 , (r-rplanet-30) , trueoffset ) + rplanet + 30
				y2=self.sliceToY( 0 , (r-rplanet-30) , trueoffset ) + rplanet + 30
				color=self.planets[i]["color"]
				output += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke-width:1px;stroke:%s;stroke-opacity:.3;"/>\n' % (x1,y1,x2,y2,color)
				# line2
				x1=self.sliceToX( 0 , (r-rplanet-30) , trueoffset ) + rplanet + 30
				y1=self.sliceToY( 0 , (r-rplanet-30) , trueoffset ) + rplanet + 30
				x2=self.sliceToX( 0 , (r-rplanet-10) , offset ) + rplanet + 10
				y2=self.sliceToY( 0 , (r-rplanet-10) , offset ) + rplanet + 10
				output += '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke-width:1px;stroke:%s;stroke-opacity:.5;"/>\n' % (x1,y1,x2,y2,color)
			else:
				scale=1
			# output planet
			output = output + '<g transform="translate(-'+str(12*scale)+',-'+str(12*scale)+')"><g transform="scale('+str(scale)+')"><use x="' + str(planet_x*(1/scale)) + '" y="' + str(planet_y*(1/scale)) + '" xlink:href="#' + self.svgSafeHref(self.planets[i]['name']) + '" /></g></g>\n'
		#make transit degut and display planets
		if self.type == "Transit":
			group_offset={}
			t_planets_degut={}
			for i in range(len(self.planets)):
				group_offset[i]=0
				if self.planets[i]['visible'] == 1:
					t_planets_degut[self.t_planets_degree_ut[i]]=i
			t_keys = list(t_planets_degut.keys())
			t_keys.sort()
			# grab closely grouped planets
			groups=[]
			in_group=False
			for e in range(len(t_keys)):
				i_a=t_planets_degut[t_keys[e]]
				if e == (len(t_keys)-1):
					i_b=t_planets_degut[t_keys[0]]
				else:
					i_b=t_planets_degut[t_keys[e+1]]
				a=self.t_planets_degree_ut[i_a]
				b=self.t_planets_degree_ut[i_b]
				diff = self.degreeDiff(a,b)
				if diff <= 2.5:
					if in_group:
						groups[-1].append(i_b)
					else:
						groups.append([i_a])
						groups[-1].append(i_b)
						in_group=True
				else:
					in_group=False
			#loop groups and set degrees display adjustment
			for i in range(len(groups)):
				if len(groups[i]) == 2:
					group_offset[groups[i][0]]=-1.0
					group_offset[groups[i][1]]=1.0
				elif len(groups[i]) == 3:
					group_offset[groups[i][0]]=-1.5
					group_offset[groups[i][1]]=0
					group_offset[groups[i][2]]=1.5
				elif len(groups[i]) == 4:
					group_offset[groups[i][0]]=-2.0
					group_offset[groups[i][1]]=-1.0
					group_offset[groups[i][2]]=1.0
					group_offset[groups[i][3]]=2.0
			switch = 0
			for e in range(len(t_keys)):
				i = t_planets_degut[t_keys[e]]
				if 22 < i < 27:
					rplanet = 9
				elif switch == 1:
					rplanet=18
					switch = 0
				else:
					rplanet=26
					switch = 1
				zeropoint = 360 - self.houses_degree_ut[6]
				t_offset = zeropoint + self.t_planets_degree_ut[i]
				if t_offset > 360:
					t_offset = t_offset - 360
				planet_x = self.sliceToX( 0 , (r-rplanet) , t_offset ) + rplanet
				planet_y = self.sliceToY( 0 , (r-rplanet) , t_offset ) + rplanet
				output = output + '<g transform="translate(-6,-6)"><g transform="scale(0.5)"><use x="' + str(planet_x*2) + '" y="' + str(planet_y*2) + '" xlink:href="#' + self.svgSafeHref(self.planets[i]['name']) + '" /></g></g>\n'
				#transit planet line
				x1 = self.sliceToX( 0 , r+3 , t_offset ) - 3
				y1 = self.sliceToY( 0 , r+3 , t_offset ) - 3
				x2 = self.sliceToX( 0 , r-3 , t_offset ) + 3
				y2 = self.sliceToY( 0 , r-3 , t_offset ) + 3
				output = output + '<line x1="'+str(x1)+'" y1="'+str(y1)+'" x2="'+str(x2)+'" y2="'+str(y2)+'" style="stroke: '+self.planets[i]['color']+'; stroke-width: 1px; stroke-opacity:.8;"/>\n'
				#transit planet degree text
				rotate = self.houses_degree_ut[0] - self.t_planets_degree_ut[i]
				textanchor="end"
				t_offset += group_offset[i]
				rtext=-3.0
				if -90 > rotate > -270:
					rotate = rotate + 180.0
					textanchor="start"
				if 270 > rotate > 90:
					rotate = rotate - 180.0
					textanchor="start"
				if textanchor == "end":
					xo=1
				else:
					xo=-1
				deg_x = self.sliceToX( 0 , (r-rtext) , t_offset + xo ) + rtext
				deg_y = self.sliceToY( 0 , (r-rtext) , t_offset + xo ) + rtext
				degree=int(t_offset)
				output += '<g transform="translate(%s,%s)">' % (deg_x,deg_y)
				output += '<text transform="rotate(%s)" text-anchor="%s' % (rotate,textanchor)
				output += '" style="fill: '+self.planets[i]['color']+'; font-size: 10px;">'+self.dec2deg(self.t_planets_degree[i],type="1")
				output += '</text></g>\n'
			#check transit
			if self.type == "Transit":
				dropin=36
			else:
				dropin=0
			#planet line
			x1 = self.sliceToX( 0 , r-(dropin+3) , offset ) + (dropin+3)
			y1 = self.sliceToY( 0 , r-(dropin+3) , offset ) + (dropin+3)
			x2 = self.sliceToX( 0 , (r-(dropin-3)) , offset ) + (dropin-3)
			y2 = self.sliceToY( 0 , (r-(dropin-3)) , offset ) + (dropin-3)
			output = output + '<line x1="'+str(x1)+'" y1="'+str(y1)+'" x2="'+str(x2)+'" y2="'+str(y2)+'" style="stroke: '+self.planets[i]['color']+'; stroke-width: 2px; stroke-opacity:.6;"/>\n'
			#check transit
			if self.type == "Transit":
				dropin=160
			else:
				dropin=120
			x1 = self.sliceToX( 0 , r-dropin , offset ) + dropin
			y1 = self.sliceToY( 0 , r-dropin , offset ) + dropin
			x2 = self.sliceToX( 0 , (r-(dropin-3)) , offset ) + (dropin-3)
			y2 = self.sliceToY( 0 , (r-(dropin-3)) , offset ) + (dropin-3)
			output = output + '<line x1="'+str(x1)+'" y1="'+str(y1)+'" x2="'+str(x2)+'" y2="'+str(y2)+'" style="stroke: '+self.planets[i]['color']+'; stroke-width: 2px; stroke-opacity:.6;"/>\n'
		return output

	def makePatterns( self ):
		"""
		* Stellium: At least four planets linked together in a series of continuous conjunctions.
    	* Grand trine: Three trine aspects together.
		* Grand cross: Two pairs of opposing planets squared to each other.
		* T-Square: Two planets in opposition squared to a third. 
		* Yod: Two qunicunxes together joined by a sextile. 
		"""
		conj = {} #0
		opp = {} #10
		sq = {} #5
		tr = {} #6
		qc = {} #9
		sext = {} #3
		for i in range(len(self.planets)):
			a=self.planets_degree_ut[i]
			qc[i]={}
			sext[i]={}
			opp[i]={}
			sq[i]={}
			tr[i]={}
			conj[i]={}
			#skip some points
			n = self.planets[i]['name']
			if n == 'earth' or n == 'true node' or n == 'osc. apogee' or n == 'intp. apogee' or n == 'intp. perigee':
				continue
			if n == 'Dsc' or n == 'Ic':
				continue
			for j in range(len(self.planets)):
				#skip some points
				n = self.planets[j]['name']
				if n == 'earth' or n == 'true node' or n == 'osc. apogee' or n == 'intp. apogee' or n == 'intp. perigee':
					continue
				if n == 'Dsc' or n == 'Ic':
					continue
				b = self.planets_degree_ut[j]
				delta=float(self.degreeDiff(a,b))
				#check for opposition
				xa = float(self.aspects[10]['degree']) - float(self.aspects[10]['orb'])
				xb = float(self.aspects[10]['degree']) + float(self.aspects[10]['orb'])
				if (xa <= delta <= xb):
					opp[i][j]=True
				#check for conjunction
				xa = float(self.aspects[0]['degree']) - float(self.aspects[0]['orb'])
				xb = float(self.aspects[0]['degree']) + float(self.aspects[0]['orb'])
				if (xa <= delta <= xb):
					conj[i][j]=True
				#check for squares
				xa = float(self.aspects[5]['degree']) - float(self.aspects[5]['orb'])
				xb = float(self.aspects[5]['degree']) + float(self.aspects[5]['orb'])
				if (xa <= delta <= xb):
					sq[i][j]=True
				#check for qunicunxes
				xa = float(self.aspects[9]['degree']) - float(self.aspects[9]['orb'])
				xb = float(self.aspects[9]['degree']) + float(self.aspects[9]['orb'])
				if (xa <= delta <= xb):
					qc[i][j]=True
				#check for sextiles
				xa = float(self.aspects[3]['degree']) - float(self.aspects[3]['orb'])
				xb = float(self.aspects[3]['degree']) + float(self.aspects[3]['orb'])
				if (xa <= delta <= xb):
					sext[i][j]=True
		yot={}
		#check for double qunicunxes
		for k,v in qc.items():
			if len(qc[k]) >= 2:
				#check for sextile
				for l,w in qc[k].items():
					for m,x in qc[k].items():
						if m in sext[l]:
							if l > m:
								yot['%s,%s,%s' % (k,m,l)] = [k,m,l]
							else:
								yot['%s,%s,%s' % (k,l,m)] = [k,l,m]
		tsquare={}
		# check for opposition
		for k,v in opp.items():
			if len(opp[k]) >= 1:
				# check for square
				for l,w in opp[k].items():
						for a,b in sq.items():
							if k in sq[a] and l in sq[a]:
								#print 'got tsquare %s %s %s' % (a,k,l)
								if k > l:
									tsquare['%s,%s,%s' % (a,l,k)] = '%s => %s, %s' % (
										self.planets[a]['label'],self.planets[l]['label'],self.planets[k]['label'])
								else:
									tsquare['%s,%s,%s' % (a,k,l)] = '%s => %s, %s' % (
										self.planets[a]['label'],self.planets[k]['label'],self.planets[l]['label'])
		stellium={}
		# check for 4 continuous conjunctions
		for k,v in conj.items():
			if len(conj[k]) >= 1:
				# first conjunction
				for l,m in conj[k].items():
					if len(conj[l]) >= 1:
						for n,o in conj[l].items():
							# skip 1st conj
							if n == k:
								continue
							if len(conj[n]) >= 1:
								# third conjunction
								for p,q in conj[n].items():
									# skip first and second conj
									if p == k or p == n:
										continue
									if len(conj[p]) >= 1:
										# fourth conjunction
										for r,s in conj[p].items():
											# skip conj 1,2,3
											if r == k or r == n or r == p:
												continue
											l=[k,n,p,r]
											l.sort()
											stellium['%s %s %s %s' % (l[0],l[1],l[2],l[3])]='%s %s %s %s' % (self.planets[l[0]]['label'], self.planets[l[1]]['label'], self.planets[l[2]]['label'], self.planets[l[3]]['label'])
		# print yots
		out='<g transform="translate(-30,380)">'
		if len(yot) >= 1:
			y=0
			for k,v in yot.items():
				out += '<text y="%s" style="fill:%s; font-size: 12px;">%s</text>\n' % (y,self.colors['paper_0'],_("Yot"))
				# first planet symbol
				out += '<g transform="translate(20,%s)">' % (y)
				out += '<use transform="scale(0.4)" x="0" y="-20" xlink:href="#%s" /></g>\n' % (
					self.svgSafeHref(self.planets[yot[k][0]]['name']))
				# second planet symbol
				out += '<g transform="translate(30,%s)">'  % (y)
				out += '<use transform="scale(0.4)" x="0" y="-20" xlink:href="#%s" /></g>\n' % (
					self.svgSafeHref(self.planets[yot[k][1]]['name']))
				# third planet symbol
				out += '<g transform="translate(40,%s)">'  % (y)
				out += '<use transform="scale(0.4)" x="0" y="-20" xlink:href="#%s" /></g>\n' % (
					self.svgSafeHref(self.planets[yot[k][2]]['name']))
				y=y+14
		# finalize
		out += '</g>'
		# return out
		return ''

	def makeAspects( self , r , ar ):
		out=""
		for i in range(len(self.planets)):
			start=self.planets_degree_ut[i]
			for x in range(i):
				end=self.planets_degree_ut[x]
				diff=float(self.degreeDiff(start,end))
				# loop orbs
				if (self.planets[i]['visible_aspect_line'] == 1) & (self.planets[x]['visible_aspect_line'] == 1):
					for z in range(len(self.aspects)):
						if	( float(self.aspects[z]['degree']) - float(self.aspects[z]['orb']) ) <= diff <= ( float(self.aspects[z]['degree']) + float(self.aspects[z]['orb']) ):
							# check if we want to display this aspect
							if self.aspects[z]['visible'] == 1:
								out = out + self.drawAspect( r , ar , self.planets_degree_ut[i] , self.planets_degree_ut[x] , self.colors["aspect_%s" %(self.aspects[z]['degree'])] )
		return out

	def makeAspectsTransit( self , r , ar ):
		out = ""
		self.atgrid=[]
		for i in range(len(self.planets)):
			start=self.planets_degree_ut[i]
			for x in range(i+1):
				end=self.t_planets_degree_ut[x]
				diff=float(self.degreeDiff(start,end))
				# loop orbs
				if (self.planets[i]['visible'] == 1) & (self.planets[x]['visible'] == 1):
					for z in range(len(self.aspects)):
						# check for personal planets and determine orb
						if 0 <= i <= 4 or 0 <= x <= 4:
							orb_before = 1.0
						else:
							orb_before = 2.0
						# check if we want to display this aspect
						if	( float(self.aspects[z]['degree']) - orb_before ) <= diff <= ( float(self.aspects[z]['degree']) + 1.0 ):
							if self.aspects[z]['visible'] == 1:
								out = out + self.drawAspect( r , ar , self.planets_degree_ut[i] , self.t_planets_degree_ut[x] , self.colors["aspect_%s" %(self.aspects[z]['degree'])] )
							# aspect grid dictionary
							if self.aspects[z]['visible_grid'] == 1:
								self.atgrid.append({})
								self.atgrid[-1]['p1']=i
								self.atgrid[-1]['p2']=x
								self.atgrid[-1]['aid']=z
								self.atgrid[-1]['diff']=diff
		return out

	def makeAspectTransitGrid( self , r ):
		out = '<g transform="translate(500,310)">'
		out += '<text y="-15" x="0" style="fill:%s; font-size: 12px;">%s</text>\n' % (self.colors['paper_0'],_("Planets in Transit"))
		line = 0
		nl = 0
		for i in range(len(self.atgrid)):
			if i == 12:
				nl = 100
				if len(self.atgrid) > 24:
					line = -1 * ( len(self.atgrid) - 24) * 14
				else:
					line = 0
			out += '<g transform="translate(%s,%s)">' % (nl,line)
			# first planet symbol
			out += '<use transform="scale(0.4)" x="0" y="3" xlink:href="#%s" />\n' % (
				self.planets[self.atgrid[i]['p2']]['name'])
			# aspect symbol
			out += '<use  x="15" y="0" xlink:href="#orb%s" />\n' % (
				self.aspects[self.atgrid[i]['aid']]['degree'])
			# second planet symbol
			out += '<g transform="translate(30,0)">'
			out += '<use transform="scale(0.4)" x="0" y="3" xlink:href="#%s" />\n' % (
				self.svgSafeHref(self.planets[self.atgrid[i]['p1']]['name']))
			out += '</g>'
			# difference in degrees
			out += '<text y="8" x="45" style="fill:%s; font-size: 10px;">%s</text>' % (
				self.colors['paper_0'],
				self.dec2deg(self.atgrid[i]['diff']) )
			# line
			out += '</g>'
			line = line + 14
		out += '</g>'
		return out

	def makeAspectGrid( self , r ):
		out=""
		style='stroke:%s; stroke-width: 1px; stroke-opacity:.6; fill:none' % (self.colors['paper_0'])
		xindent=380
		yindent=468
		box=14
		revr=list(range(len(self.planets)))
		revr.reverse()
		for a in revr:
			if self.planets[a]['visible_aspect_grid'] == 1:
				start=self.planets_degree_ut[a]
				# first planet 
				out = out + '<rect x="'+str(xindent)+'" y="'+str(yindent)+'" width="'+str(box)+'" height="'+str(box)+'" style="'+style+'"/>\n'
				out = out + '<use transform="scale(0.4)" x="'+str((xindent+2)*2.5)+'" y="'+str((yindent+1)*2.5)+'" xlink:href="#'+self.svgSafeHref(self.planets[a]['name'])+'" />\n'
				xindent = xindent + box
				yindent = yindent - box
				revr2=list(range(a))
				revr2.reverse()
				xorb=xindent
				yorb=yindent + box
				for b in revr2:
					if self.planets[b]['visible_aspect_grid'] == 1:
						end=self.planets_degree_ut[b]
						diff=self.degreeDiff(start,end)
						out = out + '<rect x="'+str(xorb)+'" y="'+str(yorb)+'" width="'+str(box)+'" height="'+str(box)+'" style="'+style+'"/>\n'
						xorb=xorb+box
						for z in range(len(self.aspects)):
							if	( float(self.aspects[z]['degree']) - float(self.aspects[z]['orb']) ) <= diff <= ( float(self.aspects[z]['degree']) + float(self.aspects[z]['orb']) ) and self.aspects[z]['visible_grid'] == 1:
									out = out + '<use  x="'+str(xorb-box+1)+'" y="'+str(yorb+1)+'" xlink:href="#orb'+str(self.aspects[z]['degree'])+'" />\n'
		return out

	def makeElements( self , r ):
		total = self.fire + self.earth + self.air + self.water
		pf = int(round(100*self.fire/total))
		pe = int(round(100*self.earth/total))
		pa = int(round(100*self.air/total))
		pw = int(round(100*self.water/total))
		out = '<g transform="translate(-30,79)">\n'
		out = out + '<text y="0" style="fill:#ff6600; font-size: 10px;">'+self.label['fire']+'  '+str(pf)+'%</text>\n'
		out = out + '<text y="12" style="fill:#6a2d04; font-size: 10px;">'+self.label['earth']+' '+str(pe)+'%</text>\n'
		out = out + '<text y="24" style="fill:#6f76d1; font-size: 10px;">'+self.label['air']+'   '+str(pa)+'%</text>\n'
		out = out + '<text y="36" style="fill:#630e73; font-size: 10px;">'+self.label['water']+' '+str(pw)+'%</text>\n'
		out = out + '</g>\n'
		return out

	def makeLegend( self ):
		out = '<g transform="translate(632,256)">\n'
		out = out + '<text x="0" y="0" style="fill:#000000; font-size: 12px;">'
		signs = _('Zodiac signs:')
		out = out + signs + '</text>\n'
		out = out + '<g transform="translate(0,4)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[0]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="12" style="fill:#482900; font-size: 10px;"> Aries</text>\n'
		out = out + '<g transform="translate(0,16)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[1]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="24" style="fill:#6b3d00; font-size: 10px;"> Taurus</text>\n'
		out = out + '<g transform="translate(0,28)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[2]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="36" style="fill:#5995e7; font-size: 10px;"> Gemini</text>\n'
		out = out + '<g transform="translate(0,40)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[3]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="48" style="fill:#2b4972; font-size: 10px;"> Cancer</text>\n'
		out = out + '<g transform="translate(0,52)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[4]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="60" style="fill:#c54100; font-size: 10px;"> Leo</text>\n'
		out = out + '<g transform="translate(0,64)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[5]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="72" style="fill:#2b286f; font-size: 10px;"> Virgo</text>\n'
		out = out + '<g transform="translate(0,76)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[6]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="84" style="fill:#69acf1; font-size: 10px;"> Libra</text>\n'
		out = out + '<g transform="translate(0,88)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[7]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="96" style="fill:#ffd237; font-size: 10px;"> Scorpio</text>\n'
		out = out + '<g transform="translate(0,100)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[8]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="108" style="fill:#ff7200; font-size: 10px;"> Sagittarius</text>\n'
		out = out + '<g transform="translate(0,112)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[9]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="120" style="fill:#863c00; font-size: 10px;"> Capricorn</text>\n'
		out = out + '<g transform="translate(0,124)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[10]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="132" style="fill:#4f0377; font-size: 10px;"> Aquarius</text>\n'
		out = out + '<g transform="translate(0,136)">\n'
		out = out + '<use transform="scale(0.3)" xlink:href="#'+self.zodiac[11]+'" />\n'
		out = out + '</g>\n'
		out = out + '<text x="12" y="144" style="fill:#6cbfff; font-size: 10px;"> Pisces</text>\n'
		out = out + '</g>\n'
		return out

	def makePlanetGrid( self ):
		out = '<g transform="translate(510,-40)">'
		# loop over all planets
		li=10
		offset=0
		for i in range(len(self.planets)):
			if i == 27:
				li = 10
				offset = -120
			if self.planets[i]['visible'] == 1:
				# start of line
				out = out + '<g transform="translate(%s,%s)">' % (offset,li)
				# planet text
				out = out + '<text text-anchor="end" style="fill:%s; font-size: 10px;">%s</text>' % (self.colors['paper_0'],self.planets[i]['label'])
				# planet symbol
				out = out + '<g transform="translate(5,-8)"><use transform="scale(0.4)" xlink:href="#'+self.svgSafeHref(self.planets[i]['name'])+'" /></g>'
				# planet degree
				out = out + '<text text-anchor="start" x="19" style="fill:%s; font-size: 10px;">%s</text>' % (self.colors['paper_0'],self.dec2deg(self.planets_degree[i]))
				# zodiac
				out = out + '<g transform="translate(60,-8)"><use transform="scale(0.3)" xlink:href="#'+self.zodiac[self.planets_sign[i]]+'" /></g>'
				# planet retrograde
				if self.planets_retrograde[i]:
					out = out + '<g transform="translate(74,-8)"><use transform="scale(0.7)" xlink:href="#retrograde" /></g>'
				# end of line
				out = out + '</g>\n'
				# offset between lines
				li = li + 14
		out = out + '</g>\n'
		return out

	def makeHousesGrid( self ):
		out = '<g transform="translate(624,-40)">'
		li=10
		for i in range(12):
			if i < 9:
				cusp = '&#160;&#160;'+str(i+1)
			else:
				cusp = str(i+1)
			out += '<g transform="translate(0,'+str(li)+')">'
			out += '<text text-anchor="end" x="40" style="fill:%s; font-size: 10px;">%s %s:</text>' % (self.colors['paper_0'],self.label['cusp'],cusp)
			out += '<g transform="translate(40,-8)"><use transform="scale(0.3)" xlink:href="#'+self.zodiac[self.houses_sign[i]]+'" /></g>'
			out += '<text x="53" style="fill:%s; font-size: 10px;"> %s</text>' % (self.colors['paper_0'], self.dec2deg(self.houses_degree[i]))
			out += '</g>\n'
			li = li + 14
		out += '</g>\n'
		return out

	"""
	 Export/Import Functions situated in AstroApplication
	  exportOAC(filename)
	  importOAC(filename)
	  importOroboros(filename)
	"""
	def exportOAC(self,filename):
		template = """<?xml version='1.0' encoding='UTF-8'?>
<openastrochart>
	<name>$name</name>
	<datetime>$datetime</datetime>
	<location>$location</location>
	<altitude>$altitude</altitude>
	<latitude>$latitude</latitude>
	<longitude>$longitude</longitude>
	<countrycode>$countrycode</countrycode>
	<timezone>$timezone</timezone>
	<geonameid>$geonameid</geonameid>
	<timezonestr>$timezonestr</timezonestr>
	<extra>$extra</extra>
</openastrochart>"""
		h,m,s = self.decHour(self.hour)
		dt = datetime.datetime(self.year,self.month,self.day,h,m,s)
		substitute = {}
		substitute['name'] = self.name
		substitute['datetime'] = dt.strftime("%Y-%m-%d %H:%M:%S")
		substitute['location'] = self.location
		substitute['altitude'] = self.altitude
		substitute['latitude'] = self.geolat
		substitute['longitude'] = self.geolon
		substitute['countrycode'] = self.countrycode
		substitute['timezone'] = self.timezone
		substitute['timezonestr'] = self.timezonestr
		substitute['geonameid'] = self.geonameid
		substitute['extra'] = ''
		#write the results to the template
		output = Template(template).substitute(substitute)
		f = open(filename,"w")
		f.write(output)
		f.close()

		dprint("exporting OAC: %s" % filename)

		return

	def importOAC(self, filename):
		r = importfile.getOAC(filename)[0]
		dt = datetime.datetime.strptime(r['datetime'],"%Y-%m-%d %H:%M:%S")
		self.name = r['name']
		self.countrycode = r['countrycode']
		self.altitude = int(r['altitude'])
		self.geolat = float(r['latitude'])
		self.geolon = float(r['longitude'])
		self.timezone = float(r['timezone'])
		self.geonameid = r['geonameid']
		if "timezonestr" in r:
			self.timezonestr = r['timezonestr']
		else:
			self.timezonestr = self.db.gnearest(self.geolat,self.geolon)['timezonestr']
		self.location = r['location']
		self.year = dt.year
		self.month = dt.month
		self.day = dt.day
		self.hour = self.decHourJoin(dt.hour,dt.minute,dt.second)
		# make locals
		self.utcToLocal()

		# debug print
		dprint('importOAC: %s' % filename)

		return

	def importOroboros(self, filename):
		r = importfile.getOroboros(filename)[0]
		# naive local datetime
		naive = datetime.datetime.strptime(r['datetime'],"%Y-%m-%d %H:%M:%S")
		# aware datetime object
		dt_input = datetime.datetime(naive.year, naive.month, naive.day, naive.hour, naive.minute, naive.second)
		dt = pytz.timezone(r['zoneinfo']).localize(dt_input)
		# naive utc datetime object
		dt_utc = dt.replace(tzinfo=None) - dt.utcoffset()
		# process latitude/longitude
		deg,type,min,sec = r['latitude'].split(":")
		lat = float(deg)+( float(min) / 60.0 )+( float(sec) / 3600.0 )
		if type == "S":
			lat = decimal / -1.0
		deg,type,min,sec = r['longitude'].split(":")
		lon = float(deg)+( float(min) / 60.0 )+( float(sec) / 3600.0 )
		if type == "W":
			lon = decimal / -1.0
		geon = self.db.gnearest(float(lat),float(lon))
		self.timezonestr = geon['timezonestr']
		self.geonameid = geon['geonameid']
		self.name = r['name']
		self.countrycode = ''
		self.altitude = int(r['altitude'])
		self.geolat = lat
		self.geolon = lon
		self.timezone = self.offsetToTz(dt.utcoffset())
		self.location = '%s, %s' % (r['location'],r['countryname'])
		self.year = dt_utc.year
		self.month = dt_utc.month
		self.day = dt_utc.day
		self.hour = self.decHourJoin(dt_utc.hour,dt_utc.minute,dt_utc.second)
		# make locals
		self.utcToLocal()

		# debug print
		dprint('importOroboros: UTC: %s file: %s' % (dt_utc,filename))

		return

	def importSkylendar(self, filename):
		r = importfile.getSkylendar(filename)[0]
		# naive local datetime
		naive = datetime.datetime(int(r['year']),int(r['month']),int(r['day']),int(r['hour']),int(r['minute']))
		# aware datetime object
		dt_input = datetime.datetime(naive.year, naive.month, naive.day, naive.hour, naive.minute, naive.second)
		dt = pytz.timezone(r['zoneinfofile']).localize(dt_input)
		# naive utc datetime object
		dt_utc = dt.replace(tzinfo=None) - dt.utcoffset()
		geon = self.db.gnearest(float(r['latitude']),float(r['longitude']))
		self.timezonestr=geon['timezonestr']
		self.geonameid=geon['geonameid']
		self.name=r['name']
		self.countrycode=''
		self.altitude=25
		self.geolat=float(r['latitude'])
		self.geolon=float(r['longitude'])
		self.timezone=float(r['timezone'])
		self.location='%s, %s' % (r['location'],r['countryname'])
		self.year=dt_utc.year
		self.month=dt_utc.month
		self.day=dt_utc.day
		self.hour=self.decHourJoin(dt_utc.hour,dt_utc.minute,dt_utc.second)
		# make locals
		self.utcToLocal()
		return

	"""
	 Check Timezone in case of Daylight Saving
	"""
	def specialTimeZone(self, tz):
		# create a new window
		self.win_TZ = Gtk.Window(title=_("Daylight Saving Time Detected"))
		""" set_icon """
		#self.win_TZ.set_icon_from_file(app.cfg.iconWindow)
		#self.win_TZ.connect("delete_event", lambda w,e: self.win_TZ.destroy())
		#self.win_TZ.move(150, 150)
		#self.win_TZ.set_border_width(5)
		self.win_TZ.set_default_size(300,100)
		self.win_TZ.set_modal()
		tz_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		tz_box.set_spacing(12)
		header = Gtk.Label(label=_("Change Timezone ?"))
		tz_box.append(header)
		entry_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		_label = Gtk.Label(label=_("Actual Timezone:"))
		entry_box.append(_label)
		tz_split = tz.split('/')
		_entry = Gtk.Entry()
		_entry.set_max_length(16)
		_entry.set_width_chars(12)
		_entry.set_alignment(xalign=1)
		_entry.set_editable(False)
		_entry.set_text(tz_split[0])
		entry_box.append(_entry)
		_label = Gtk.Label(label=_(" / "))
		entry_box.append(_label)
		tz_entry = Gtk.Entry()
		tz_entry.set_max_length(32)
		tz_entry.set_width_chars(24)
		tz_entry.set_text(tz_split[1])
		tz_entry.connect("activate", self.specialTimeZoneSubmit, tz_entry)
		entry_box.append(tz_entry)
		tz_box.append(entry_box)
		hints = Gtk.Label(label=_("Change Timezone and press <Enter>"))
		tz_box.append(hints)
		button = Gtk.Button.new_with_mnemonic(label = _("Cancel"))
		#button.set_can_default(True)
		button.connect("clicked", lambda w: self.win_TZ.destroy())
		self.win_TZ.set_child(tz_box)
		#self.win_TZ.action_area.pack_end(child=button, expand=False, fill=False, padding=16)
		#self.win_TZ.action_area.pack_start(button, True, True, 0)
		self.win_TZ.present()
		tz_entry.grab_focus()
		#self.win_TZ.run()

	def specialTimeZoneSubmit(self, widged, entry):
		s = self.timezone_str
		self.timezone_str = s[:s.find('/')+1] + entry.get_text()
		self.win_TZ.destroy()

	def importAstrolog(self, filename):
		r = importfile.getAstrolog32(filename)[0]
		#timezone string
		self.timezone_str = zonetab.nearest_tz(float(r['latitude']),float(r['longitude']),zonetab.timezones())[2]
		"""
		  Above looks for nearest noted continent/city, but sometimes
		  this is a city with deviating daylight saving time
		"""
		if r['daylight']:
			self.specialTimeZone(self.timezone_str)
		# naive local datetime
		naive = datetime.datetime(int(r['year']),int(r['month']),int(r['day']),int(r['hour']),int(r['minute']),int(r['second']))
		# aware datetime object
		dt_input = datetime.datetime(naive.year, naive.month, naive.day, naive.hour, naive.minute, naive.second)
		dt = pytz.timezone(self.timezone_str).localize(dt_input)
		# naive utc datetime object
		dt_utc = dt.replace(tzinfo=None) - dt.utcoffset()
		geon = self.db.gnearest(float(r['latitude']),float(r['longitude']))
		self.timezonestr=geon['timezonestr']
		self.geonameid=geon['geonameid']
		self.name=r['name']
		self.countrycode=''
		self.altitude=25
		self.geolat=float(r['latitude'])
		self.geolon=float(r['longitude'])
		self.timezone=self.offsetToTz(dt.utcoffset())
		self.location=r['location']
		self.year=dt_utc.year
		self.month=dt_utc.month
		self.day=dt_utc.day
		self.hour=self.decHourJoin(dt_utc.hour,dt_utc.minute,dt_utc.second)
		# make locals
		self.utcToLocal()
		return

	def importZet8(self, filename):
		h=open(filename)
		f=codecs.EncodedFile(h,"utf-8","latin-1")
		data=[]
		for line in f.readlines():
			s=line.split(";")
			if s[0] == line:
				continue
			data.append({})
			data[-1]['name']=s[0].strip()
			day=int( s[1].strip().split('.')[0] )
			month=int( s[1].strip().split('.')[1] )
			year=int( s[1].strip().split('.')[2] )
			hour=int(  s[2].strip().split(':')[0] )
			minute=int( s[2].strip().split(':')[1] )
			if len(s[3].strip()) > 3:
				data[-1]['timezone']=float( s[3].strip().split(":")[0] )
				if data[-1]['timezone'] < 0:
					data[-1]['timezone']-= float( s[3].strip().split(":")[1] ) / 60.0
				else:
					data[-1]['timezone']+= float( s[3].strip().split(":")[1] ) / 60.0
			elif len(s[3].strip()) > 0:
				data[-1]['timezone']=int(s[3].strip())
			else:
				data[-1]['timezone']=0
			# substract timezone from date
			dt = datetime.datetime(year,month,day,hour,minute)
			dt = dt - datetime.timedelta(seconds=float(data[-1]['timezone'])*float(3600))
			data[-1]['year'] = dt.year
			data[-1]['month'] = dt.month
			data[-1]['day'] = dt.day
			data[-1]['hour'] =  float(dt.hour) + float(dt.minute/60.0)
			data[-1]['location']=s[4].strip()
			# latitude
			p=s[5].strip()
			if p.find("°") != -1:
				# later version of zet8
				if p.find("S") == -1:
					deg=p.split("°")[0] #\xc2
					min=p[p.find("°")+2:p.find("'")]
					sec=p[p.find("'")+1:p.find('"')]
					data[-1]['latitude']=float(deg)+(float(min)/60.0)
				else:
					deg=p.split("°")[0] #\xc2
					min=p[p.find("°")+2:p.find("'")]
					sec=p[p.find("'")+1:p.find('"')]
					data[-1]['latitude']=( float(deg)+(float(min)/60.0) ) / -1.0
			else:
				# earlier version of zet8
				if p.find("s") == -1:
					i=p.find("n")
					data[-1]['latitude']=float(p[:i])+(float(p[i+1:])/60.0)
				else:
					i=p.find("s")
					data[-1]['latitude']=( float(p[:i])+(float(p[i+1:])/60.0) ) / -1.0
			# longitude
			p=s[6].strip()
			if p.find("°") != -1:
				#later version of zet8
				if p.find("W") == -1:
					deg = p.split("°")[0] #\xc2
					min = p[p.find("°")+2:p.find("'")]
					sec = p[p.find("'")+1:p.find('"')]
					data[-1]['longitude'] = float(deg)+(float(min)/60.0)
				else:
					deg = p.split("°")[0] #\xc2
					min = p[p.find("°")+2:p.find("'")]
					sec = p[p.find("'")+1:p.find('"')]
					data[-1]['longitude'] = ( float(deg)+(float(min)/60.0) ) / -1.0
			else:
				# earlier version of zet8
				if p.find("w") == -1:
					i=p.find("e")
					data[-1]['longitude'] = float(p[:i])+(float(p[i+1:])/60.0)
				else:
					i=p.find("w")
					data[-1]['longitude'] = ( float(p[:i])+(float(p[i+1:])/60.0) ) / -1.0
		self.db.importZet8(app.cfg.peopledb , data)

		dprint('importZet8: database with %s entries: %s' % (len(data),filename))

		f.close()
		return

	def svgSafeHref(self, name):
		name=name.replace(' ','_')
		return name

	def do_command_line(self, command_line):
		options = command_line.get_options_dict()
		# convert GVariantDict -> GVariant -> dict
		options = options.end().unpack()
		if "local" in options:
			LOCAL = True
			pass
		self.activate()
		return 0

	def on_quit(self, action, parameter):
		self.quit()

if __name__ == "__main__":
	app = AstroApplication()
	exit_status = app.run(sys.argv)
	sys.exit(exit_status)

