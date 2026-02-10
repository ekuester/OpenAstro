%global revision 3
%global srcname pyswisseph

Name:           python3-swisseph
Version:        2.10.3.2
Release:        %{revision}%{?dist}
Summary:        Swiss Ephemeris astrology data
License:        GPLv2+
URL:            https://pypi.org/project/%{srcname}
#Download:      https://github.com/astrorigin/pyswisseph/releases/tag/v2.10.03.2
Source0:        %{srcname}-%{version}.tar.gz
BuildRequires:  python3-devel

%description
Python extension to AstroDienst Swiss Ephemeris library.

%global debug_package %{nil}

%prep
# file without -%{revision}
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_DIR}/%{srcname}-%{version}

%files
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/*

%changelog
* Sat Nov 22 2025 Erich Kuester <erich.kuester«arcor.de> - 2.10.3.2-3
- Rebuild for Fedora 43 and Python 3.14
* Fri Nov  7 2025 Erich Kuester <erich.kuester«arcor.de> - 2.10.3.2-2
- Rebuild for Fedora 42 and Python 3.13
* Thu Nov 30 2023 Erich Kuester <erich.kuester«arcor.de> - 2.10.3.2-1
- Rebuild for Fedora 39 and Python 3.12
* Mon Nov 28 2022 Erich Kuester <erich.kuester«arcor.de> - 2.08.00-4
- Rebuild for Fedora 37 and Python 3.11
* Thu Dec  2 2021 Erich Kuester <erich.kuester«arcor.de> - 2.08.00-3
- Rebuild for Fedora 35 and Python 3.10
* Fri Nov  6 2020 Erich Kuester <erich.kuester«arcor.de> - 2.08.00-2
- Rebuild for Fedora 33 and Python 3.9
* Mon Aug 17 2020 Erich Kuester <erich.kuester@arcor.de> - 2.08.00-1
- Build for Fedora 32 and Python 3.8 with new version
* Fri Jul 17 2020 Erich Kuester <erich.kuester@arcor.de> - 2.00.00
- Rebuild for Fedora 32 and Python 3.8
* Mon Jun 19 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.00.00
- Rebuild for Fedora
* Thu Feb 11 2016 Jens Petersen <petersen@redhat.com>
- Initial package
