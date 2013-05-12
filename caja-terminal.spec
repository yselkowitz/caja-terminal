Name:           caja-terminal
Version:        1.6.0
Release:        1%{?dist}
Summary:        Terminal embedded in Caja

Group:          System Environment/Shells
License:        GPLv3+
URL:            https://github.com/NiceandGently/caja-terminal
Source0:        https://github.com/downloads/NiceandGently/caja-terminal/caja-terminal-%{version}.tar.gz


BuildRequires:  gettext python2-devel

Requires:       pygtk2 python-caja vte pyxdg

%description
Caja Terminal is a terminal embedded in Caja, the MATE's file browser.
It is always open in the current folder, and follows the navigation
(like an automated "cd" command).

%prep
%setup -q
chmod -x AUTHORS
sed -i 's|/usr/lib/caja/extensions-2.0|%{_libdir}/caja/extensions-2.0|g' install.sh

%build

%install
mkdir -p $RPM_BUILD_ROOT
bash install.sh --package $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS README
%{_datadir}/%{name}
%{_datadir}/python-caja/extensions/%{name}.py*

%changelog
* Fri Nov 16 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-1
- test build
- ported to gir

* Fri Nov 16 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7-0101
- build against fedora official mate-desktop
- remove epoch
- add python-devel as BR

* Mon Aug 27 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7-0100
- build for f18

* Tue Apr 10 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7-2
- switch to python-caja instead of caja-python

* Wed Jan 04 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7-1
- caja-terminal.spec based on nautilus-terminal-0.7-2.fc15 spec

