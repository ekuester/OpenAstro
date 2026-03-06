%global revision 1
%global alias openastro.org

Name:           OpenAstro
Version:        1.1.70
Release:        1.11
Summary:        Astrology charts
License:        GPLv3+
#distro:        http://ppa.launchpad.net/pellesimon/ubuntu/pool/main/o/openastro.org/
URL:            http://www.github.com/ekuester/OpenAstro
#Source:        https://github.com/ekuester/OpenAstro/archive/refs/tags/v0.1.59.tar.gz
Source0:        http://www.github.com/ekuester/OpenAstro/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-swisseph
#Patch0:         openastro_sqlite.patch

%description
The open source astrology program openastro.org by Pelle van der Scheer.

%prep
# applies patch automatically
%autosetup -n %{name}-%{version}
# change desktop file
rm -fv openastro.desktop
# write desktop file
cat > ./openastro.desktop <<EOF
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
Exec=openastro
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
cp -a data/*.* $RPM_BUILD_ROOT%{_datadir}/%{alias}/
cp -a 'about.xpm' COMMENTS LICENSE $RPM_BUILD_ROOT%{_datadir}/%{alias}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -m 644 icons/openastro.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/swisseph/
install -m 644 swisseph/*.* $RPM_BUILD_ROOT%{_datadir}/swisseph/

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_DIR}/%{alias}-%{version}

%files
%license LICENSE
%doc README.md
%{_bindir}/openastro
%{_datadir}/applications/openastro.desktop
%{_datadir}/openastro.org/*
%{_datadir}/pixmaps/*.svg
%{_datadir}/swisseph/*.*
%{_datadir}/locale/*
%{python3_sitelib}/*

%changelog
* Fri Mar  5 2026 Erich Kuester <erich.kuester«arcor.de> - 1.1.70-1
- further optimization
* Tue Feb 24 2026 Erich Kuester <erich.kuester«arcor.de> - 1.1.66-1
- some dprecations removed, displaying optimized, general revision
* Thu Feb 19 2026 Erich Kuester <erich.kuester«arcor.de> - 1.1.64-1
- added README, built for pyswisseph-2.10.3.2
* Thu Dec 25 2025 Erich Kuester <erich.kuester«arcor.de> - 1.1.59-2
- added README, built for pyswisseph-2.00.01
* Sun Dec 21 2025 Erich Kuester <erich.kuester«arcor.de> - 1.1.59-1
- merged with openastro-data-1.11, pyswisseph-2.00
* Sat Nov 22 2025 Erich Kuester <erich.kuester«arcor.de> - 1.1.57-6
- Rebuild for Fedora 43 and Python 3.14, pyswisseph-2.00
* Mon Nov 28 2022 Erich Kuester <erich.kuester«arcor.de> - 1.1.57-4
- Rebuild for Fedora 37 and Python 3.11
* Thu Dec  2 2021 Erich Kuester <erich.kuester«arcor.de> - 1.1.57-3
- Rebuild for Fedora 35 and Python 3.10
* Fri Nov  6 2020 Erich Kuester <erich.kuester«arcor.de> - 1.1.57-2
- Rebuild for Fedora 33 and Python 3.9
* Mon Aug 17 2020 Erich Kuester <erich.kuester«arcor.de> - 1.1.57-1
- Build for Fedora 32, Python 3.8, pyswisseph-2.08
* Fri Jul 17 2020 Erich Kuester <erich.kuester«arcor.de> - 1.1.57
- Rebuild for Fedora 32 and Python 3.8
* Mon Oct 15 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.57
- Rebuild for Fedora
* Thu Feb 11 2016 Jens Petersen <petersen@redhat.com>
- Initial package
