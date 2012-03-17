#define bzr
%define rev 8
%define rel 1
Name:           caja-terminal
Version:        1.0
Release:        %{rel}%{?bzr:.%{rev}bzr}%{?dist}
Summary:        Terminal embedded in Caja

Group:          System Environment/Shells
License:        GPLv3+
URL:            http://software.flogisoft.com/caja-terminal/en/
%if 0%{?bzr}
# This is a bzr snapshot, to get it
# bzr branch -r %%{rev} lp:caja-terminal
# mv caja-terminal %%{name}-%%{version}
# tar cjf %%{name}-%%{version}-%%{rev}bzr.tar.bz2 %%{name}-%%{version}
Source0:        %{name}-%{version}-%{rev}bzr.tar.bz2
%else
Source0:        http://download.flogisoft.com/files/Software/%{name}/%{name}_%{version}_src.tar.gz
%endif
BuildArch:      noarch

Requires:       caja-python >= 1.0
Requires:       pygobject2
Requires:       vte3

%description
Caja Terminal is a terminal embedded in Caja, the MATE's file browser.
It is always open in the current folder, and follows the navigation.

%prep
%setup -q -n %{name}_%{version}_src
# Remove shebang
sed -i -e '/^#!\//, 1d' src/caja_terminal.py

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 644 src/caja_terminal.py \
                 $RPM_BUILD_ROOT%{_datadir}/caja-python/extensions/caja_terminal.py

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{_datadir}/caja-python/extensions/caja_terminal.py*

%changelog
* Wed Feb 08 2012 Hicham HAOUARI <hicham.haouari@gmail.com> - 1.0-1
- Update to released 1.0

* Tue Sep 27 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 1.0-0.1.8bzr
- Switch to 1.0 branch
