# OpenAstro
To preserve the great OpenAstro program by Pelle van der Scheer [1] from oblivion, find it here slightly modified and adapted. The former separate files from 'openastro-data' are now fully integrated.</br>
(python / Linux / Gnome / pyGTK / Astrology / Horoscope / Swiss Ephemeris)

### Features
- Natal/Radix Charts
- Transit Charts
- Synastry/Combine/Composite Charts
- Solar Return / Secondary Progressions
- Customizeable Planets & Aspects
- Additional celestial bodies: Chiron, Pholus, Ceres, Pallas, Juno, Vesta
- Fictional points: North/South Node, Day/Night Pars
- Cusp Aspects
- Monthly Timeline
- European and Traditional chart view
- Online Atlas (Geocoder) using google maps (virtually every location)
- Offline Atlas (Geonames) with about 80.000 major cities!
- Database export/import, Save as JPG, PNG, SVG, OAC
- Import from skylendar (.skif), oroboros (.xml)
- Import from astrolog32 (.dat), zet8 dbase (.zds)
- Ephemeris files for 1200 AD - 2400 AD (included)

### Enhancements
The published version 1.1.59 is the last release authorized by Pelle van der Scheer and dated from roundabout 2021. Somewhat enhanced versions can be found here. Several deprecations were eliminated (work in progress). The chart window, maximized at start, can be unmaximized without problems with the graphic.<br/>
BUT...the original ideas of Pelle remained untouched.

### Discussion
This program is written in python with use of pyGtk for the Gnome GTK3 environment of Linux. For simplicity the .py ending of the executable is omitted, so start a standalone version with

```
# execute once to make program executable
chmod +x ./openastro
# start program as standalone
./openastro --local
```
The program is localized in 25 languages in folder 'locale'.

Achieve a system-wide installation by copying files accordingly to your distribution. To generate a RPM package (suitable for Red Hat, Fedora, OpenSUSE and so on) a .spec file can be found in directory "packages".<br/>
Generally the program requires installation of 'pyswisseph' [2] aka 'python3-swisseph' on RPM-systems. For this purpose the package 'python3-swisseph' can be generated with the here added, corresponding .spec file. There are some incompatibilities with newer python versions higher 3.8 and pyswisseph higher 2.1 ... which are eliminated in using the here published software <br/>

```
# generate the older way
# a source package
python3 setup.py sdist
# a rpm package
python3 setup.py bdist_rpm
```
CAVEAT: The 'setup.py' method is deprecated.

Manual input of events<br/>
Daylight saving times at natal or other events can cause problems if not entered correctly. OpenAstro uses module 'pytz' which recognized many situations for different locations and timezones. In doubt consulting the program 'astrolog' by Walter D. Pullen is recommended as a very helpful tool.

Printing of Horoscopes<br/>
OpenAstro stores the horoscope SVGs under '$HOME/.openastro.org/tmp/openAstroChart.svg', which can be converted easily to PDF. Look into directory 'script'. The shell script uses 'chromium --headless' mode and was found in [4]. The built-in conversion is equally effective.

Data Bases<br/>
OpenAstro makes intensive use of data bases in sqlite format 3:<br/>
- astrodb.sql | common data of OpenAstro
```
sqlite3 ../astrodb.sql
sqlite> .schema
CREATE TABLE astrocfg (name VARCHAR(150) UNIQUE,value VARCHAR(150));
CREATE TABLE history (id INTEGER PRIMARY KEY,name VARCHAR(50)				 ,year VARCHAR(50),month VARCHAR(50), day VARCHAR(50), hour VARCHAR(50), geolon VARCHAR(50)			 	,geolat VARCHAR(50), altitude VARCHAR(50), location VARCHAR(150), timezone VARCHAR(50)			 	,notes VARCHAR(500), image VARCHAR(250), countrycode VARCHAR(2), geonameid INTEGER, extra VARCHAR(250));
CREATE TABLE settings_aspect (degree INTEGER UNIQUE, name VARCHAR(50)				 ,color VARCHAR(50),visible INTEGER, visible_grid INTEGER				 ,is_major INTEGER, is_minor INTEGER, orb VARCHAR(5));
CREATE TABLE color_codes (name VARCHAR(50) UNIQUE				 ,code VARCHAR(50));
CREATE TABLE label (name VARCHAR(150) UNIQUE				 ,value VARCHAR(200));
CREATE TABLE settings_planet (id INTEGER UNIQUE, name VARCHAR(50)				,color VARCHAR(50),visible INTEGER, element_points INTEGER, zodiac_relation VARCHAR(50)			 	,label VARCHAR(50), label_short VARCHAR(20), visible_aspect_line INTEGER			 	,visible_aspect_grid INTEGER);
sqlite> SELECT * FROM history WHERE id=1;
1|Egon Mustermann|1957|8|15|3.0|6.77616|51.22172|39|Düsseldorf, North Rhine-Westphalia, Germany|2.0|||DE||

```
- famous.sql | data for famous people
```
sqlite3 famous.sql
sqlite> .schema
CREATE TABLE famous (id INTEGER PRIMARY KEY AUTOINCREMENT,cacheid INTEGER UNIQUE,name VARCHAR(200),firstname VARCHAR(100),lastname VARCHAR(100),firstletter VARCHAR(1),city VARCHAR(100),country VARCHAR(100),code VARCHAR(2),type VARCHAR(20),href VARCHAR(20),popularity INTEGER,year INTEGER,month INTEGER,day INTEGER,hour REAL,geoname VARCHAR(80),latitude REAL,longitude REAL,geonameid INTEGER,timezone VARCHAR(40));
CREATE TABLE sqlite_sequence(name,seq);
sqlite> SELECT * FROM famous WHERE id=1;
1|16579|JESUS CHRIST|Jesus christ||J|Bethléem|Israel|IL|Male|E5t7TAxeM4Jt.htm|67659|-6|2|28|3.56666666666667|Bethlehem|31.7166667|35.2|284315|Asia/Gaza
```
- geonames.sql | data for locations on earth
```
sqlite3 geonames.sql
sqlite> .schema
CREATE TABLE geonames (id INTEGER PRIMARY KEY AUTOINCREMENT,geonameid INTEGER UNIQUE,name VARCHAR(200),asciiname VARCHAR(200),alternatenames VARCHAR(5000),latitude REAL,longitude REAL,fclass CHAR(1),fcode VARCHAR(10),country VARCHAR(2),cc2 VARCHAR(60),admin1 VARCHAR(20),admin2 VARCHAR(80),admin3 VARCHAR(20),admin4 VARCHAR(20),population INTEGER,elevation INTEGER,gtopo30 INTEGER,timezone VARCHAR(40),moddate VARCHAR(40));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE countryinfo (id INTEGER PRIMARY KEY AUTOINCREMENT,isoalpha2 VARCHAR(2),isoalpha3 VARCHAR(3),isonum INTEGER,fips VARCHAR(2),name VARCHAR(100),capital VARCHAR(150),areainsqkm VARCHAR(32),population INTEGER,continent VARCHAR(5),tld VARCHAR(30),currencycode VARCHAR(30),currencyname VARCHAR(30),phonepostalcodeformat VARCHAR(30),postalcode VARCHAR(30),regex VARCHAR(30),language VARCHAR(30),geonameid INTEGER UNIQUE,neighbours VARCHAR(30),equivalentfipscode VARCHAR(30) );
CREATE TABLE admin1codes (id INTEGER PRIMARY KEY AUTOINCREMENT,country VARCHAR(2),admin1 VARCHAR(2),province VARCHAR(150));
CREATE TABLE continent (id INTEGER PRIMARY KEY AUTOINCREMENT,code VARCHAR(2),name VARCHAR(20),geonameid INTEGER);
sqlite> SELECT * FROM geonames WHERE id=1;
1|3039154|El Tarter|El Tarter|Ehl Tarter,Эл Тартер|42.57952|1.65362|P|PPL|AD||02||||1052||1721|Europe/Andorra|2012-11-03
```
- peopledb.sql | data for own entries (this is used for quick access)
```
sqlite3 peopledb.sql
SQLite version 3.50.2 2025-06-28 14:00:48
sqlite> .schema
CREATE TABLE event_natal (id INTEGER PRIMARY KEY,name VARCHAR(50),
 year VARCHAR(4),month VARCHAR(2), day VARCHAR(2), hour VARCHAR(50), geolon VARCHAR(50),
 geolat VARCHAR(50), altitude VARCHAR(50), location VARCHAR(150), timezone VARCHAR(50),
 notes VARCHAR(500), image VARCHAR(250), countrycode VARCHAR(2), geonameid INTEGER,
 timezonestr VARCHAR(100), extra VARCHAR(250));
sqlite> SELECT * FROM event_natal WHERE id=1;
1|Erika Mustermann|1954|7|23|2.0|10.972276|50.516770|773|Masserberg, Thüringen|2.0|Geburtshaus Masserberg||DE||Europe/Berlin|
```

### Appreciation
Sole ownership of this fine piece of software belongs to Pelle van der Scheer. 

### Acknowledgements:
Special thanks go to the people in the developer community at StackOverflow. Without their help and answered questions at <https://stackoverflow.com/> and affiliate sites this work would not be possible.

### Literature
[1] The original software website is broken, there exist some "forked" GitHub repositories and a lauchpad folder for Ubuntu:<br/>
<http://ppa.launchpad.net/pellesimon/ubuntu/pool/main/o/openastro.org/><br/>
[2] <https://pypi.org/project/pyswisseph>\
[3] <https://www.astrolog.org/><br/>
[4] <https://gist.github.com/s417-lama/84bf66de1096c4587e8187092fb41684><br/>

### Disclaimer
Use the program for what purpose you like, but hold in mind, that there is no guaranty for any harm it will cause to your hard- or software. It was your decision to use this piece of software.

