caja-terminal
======================

embedded terminal in caja

Caja terminal is a fork of nautilus terminal.
Orginal:
WEB SITE : http://software.flogisoft.com/nautilus-terminal/
VERSION : 0.8

caja-terminal is an embedded terminal in caja, the MATE's file browser.
It is always open in the current folder, and follows the navigation.

Dependencies:
    * PyGTK 2.x <http://pygtk.org/>
	* Caja Python <http://pub.mate-desktop.org/releases/1.4/python-caja>
    * python-caja-1.4.0 needs to be patched for removing python-mate dependencies
    * for MATE-1.6.0, don't use python-caja-1.6.0
    * https://dl.dropboxusercontent.com/u/49862637/Mate-desktop/patches/python-caja_removal_of_mate-python_usage.patch
	* Python VTE <http://ftp.gnome.org/pub/GNOME/sources/vte/>
	* Python XDG <http://freedesktop.org/wiki/Software/pyxdg>

Building dependencies:
    * GNU gettext <http://www.gnu.org/software/gettext/>
	* Bash

Install:
    For install Caja Terminal on 32 bit machines (x86), run './install.sh --install' as root.
    For install Caja Terminal on 64 bit machines (x86_64), run './install-64.sh --install' as root.

Uninstall:
    For uninstall Caja Terminal on 32 bit machines (x86), run 
    '/usr/share/caja-terminal/install.sh --remove' as root.
    For uninstall Caja Terminal on 64 bit machines (x86_64), run 
    '/usr/share/caja-terminal/install-64.sh --remove' as root.
