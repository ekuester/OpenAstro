%global srcname python3-swisseph
# this is python3-swisseph.spec
# for Fedora higher as 32 use python3-swisseph-2.10.3.2.spec

Name:           python3-swisseph
Version:        2.00.01
Release:        2.1
Summary:        Swiss Ephemeris astrology data
License:        GPLv2+
URL:            http://pypi.python.org/pypi/pyswisseph
Source0:        https://pypi.python.org/packages/source/p/pyswisseph/%{srcname}_%{version}.orig.tar.gz
BuildRequires:  python3-devel python3-setuptools

%description
Python extension to AstroDienst Swiss Ephemeris library.

%global debug_package %{nil}

%prep
# use old file for revision 1
%autosetup -n %{srcname}-%{version}
sed -i s/'PyUnicode_AS_DATA'/PyUnicode_DATA/g pyswisseph.c

%build
%pyproject_wheel

%install
%pyproject_install

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_DIR}/%{srcname}-%{version}

%files
%license COPYING.TXT
%doc README.TXT
%{python3_sitearch}/*

%changelog
* Tue Feb 10 2026 Erich Kuester <erich.kuester@arcor.de> - 2.00.01
- Rebuild for Fedora 43 and Python 3.14 needed for Pelle's latest openastro'
* Fri Jul 17 2020 Erich Kuester <erich.kuester@arcor.de> - 2.00.00
- Rebuild for Fedora 32 and Python 3.8
* Mon Jun 19 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.00.00
- Rebuild for Fedora
* Thu Feb 11 2016 Jens Petersen <petersen@redhat.com>
- Initial package
