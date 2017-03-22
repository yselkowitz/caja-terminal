Name:           caja-terminal
Version:        0.10
Release:        1%{?dist}
Summary:        Terminal embedded in Caja

Group:          System Environment/Shells
License:        GPLv3+
URL:            http://software.flogisoft.com/nautilus-terminal/en/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext

Requires:       python-gobject python-caja vte291 pyxdg

%description
Caja Terminal is a terminal embedded in Caja, the MATE's file browser.
It is always open in the current folder, and follows the navigation
(like an automated "cd" command).

%prep
%setup -q
chmod -x AUTHORS

%build

%install
mkdir -p $RPM_BUILD_ROOT
bash install.sh --package $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS README
%{_datadir}/%{name}
%{_datadir}/caja-python/extensions/%{name}.py*


%changelog
* Wed Mar 22 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 0.10-1
- new version for GTK+3

* Tue Mar 29 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.1-1
- new version

* Mon Aug 24 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9-1
- bump version to 0.9

* Sat Jun 15 2013 Wolfgang Ulbrich <info@raveit.de> - 0.8-1
- bump version to 0.8

* Tue Apr 10 2012 Wolfgang Ulbrich <info@raveit.de> - 0.7-2
- switch to python-caja instead of caja-python

* Wed Jan 04 2012 Wolfgang Ulbrich <info@raveit.de> - 0.7-1
- caja-terminal.spec based on nautilus-terminal-0.7-2.fc15 spec

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 24 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.7-1
- New upstream release

* Mon Sep 20 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 0.6-1
- Initial package
