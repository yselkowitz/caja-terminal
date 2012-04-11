Name:           caja-terminal
Version:        0.7
Release:        2%{?dist}
Summary:        Terminal embedded in Caja

Group:          System Environment/Shells
License:        GPLv3+
URL:            http://software.flogisoft.com/nautilus-terminal/en/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gettext

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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
bash install.sh --package $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{_datadir}/%{name}
%{_libdir}/caja/extensions-2.0/python/%{name}.py*

%changelog
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
