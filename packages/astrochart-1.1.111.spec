%global revision 1
%global alias openastro

Name:           OpenAstro
Version:        1.1.111
Release:        1.11
Summary:        Astrology charts
License:        GPLv3+
#distro:        http://ppa.launchpad.net/pellesimon/ubuntu/pool/main/o/openastro.org/
URL:            http://www.github.com/ekuester/OpenAstro
#Source:        https://github.com/ekuester/OpenAstro/archive/refs/tags/v0.1.59.tar.gz
Source0:        http://www.github.com/ekuester/OpenAstro/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       gtk4, gtk4-devel python3-swisseph
#Patch0:         openastro_sqlite.patch

%description
The open source astrology program openastro.org by Pelle van der Scheer in enhanced version astrochart..

%prep
# applies patch automatically
%autosetup -n %{name}-%{version}
# change desktop file
rm -fv %{alias}.desktop
# write desktop file
cat > ./%{alias}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Name=Open Source Astrology
Name[de_CH]=Astrologie für alle
Name[de_DE]=Astrologie für alle
Comment=Astrology Program by Pelle van der Scheer
GenericName=Open Source Astrology
Categories=Graphics;2DGraphics;GTK;
Exec=astroChart.py
Icon=openastro
StartupNotify=true
Terminal=false
EOF

%build
%pyproject_wheel

%install
%pyproject_install
cp -a locale $RPM_BUILD_ROOT%{_datadir}/
rm -fr $RPM_BUILD_ROOT%{_datadir}/%{alias}/locale
cp -a data/*.* $RPM_BUILD_ROOT%{_datadir}/%{alias}.org/
#rm -fv openastro.desktop
cp -a openastro.desktop $RPM_BUILD_ROOT%{_datadir}/applications/astrochart.desktop
cp -a 'about.xpm' COMMENTS LICENSE $RPM_BUILD_ROOT%{_datadir}/%{alias}.org/
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/openastro.desktop
rm -f $RPM_BUILD_ROOT%{_bindir}/%{alias}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -m 644 icons/openastro.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/swisseph/
install -m 644 swisseph/*.* $RPM_BUILD_ROOT%{_datadir}/swisseph/

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_DIR}/%{name}-%{version}

%files
%license LICENSE
%doc README.md
%{_bindir}/astroChart.py
%{_datadir}/applications/astrochart.desktop
%{_datadir}/%{alias}.org/*
%{_datadir}/pixmaps/*.svg
%{_datadir}/swisseph/*.*
%{_datadir}/locale/*
%{python3_sitelib}/*

%changelog
* Sun May  3 2026 Erich Kuester <erich.kuester«arcor.de> - 1.1.111-1
- openastro final for Fedora 44 and python 3.14
* Fri Apr 24 2026 Erich Kuester <erich.kuester«arcor.de> - 1.1.110-1
- continuation of openastro for Fedora 43 and python 3.14

