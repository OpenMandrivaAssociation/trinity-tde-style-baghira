%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tde-style-baghira
%define tde_prefix /opt/trinity


# Required for Mageia and PCLinuxOS: removes the ldflag '--no-undefined'
%define _disable_ld_no_undefined 1

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.8
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TDE style for Apple junkies :)
Group:		Graphical desktop/TDE
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/themes/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:          trinity-tdelibs-devel >= %{tde_version}
BuildRequires:          trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# JPEG support
BuildRequires:  pkgconfig(libjpeg)

BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

%description
Based upon mosfet-liquid0.9.6pre4... the last heir of mosfet.
Baghira includes both an style (custom widgets) and twin decoration as
well as colour schemes.

Baghira (panther, in german) makes TDE resemble Apple's MacOS X's Aqua,
Panther and Jaguar looks, and also includes its own 'Baghira' look


%files
%defattr(-,root,root)
%{tde_prefix}/bin/bab
%{tde_prefix}/%{_lib}/libbaghirastarter.la
%{tde_prefix}/%{_lib}/libbaghirastarter.so
%{tde_prefix}/%{_lib}/trinity/b_menu_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/b_menu_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/plugins/styles/baghira.la
%{tde_prefix}/%{_lib}/trinity/plugins/styles/baghira.so
%{tde_prefix}/%{_lib}/trinity/tdestyle_baghira_config.la
%{tde_prefix}/%{_lib}/trinity/tdestyle_baghira_config.so
%{tde_prefix}/%{_lib}/trinity/twin3_baghira.la
%{tde_prefix}/%{_lib}/trinity/twin3_baghira.so
%{tde_prefix}/%{_lib}/trinity/twin_baghira_config.la
%{tde_prefix}/%{_lib}/trinity/twin_baghira_config.so
%{tde_prefix}/%{_lib}/usermanager_panelapplet.la
%{tde_prefix}/%{_lib}/usermanager_panelapplet.so
%{tde_prefix}/share/applications/tde/bab.desktop
%{tde_prefix}/share/apps/baghira/
%{tde_prefix}/share/apps/kicker/applets/baghira-starter.desktop
%{tde_prefix}/share/apps/kicker/applets/baghira-usermanager.desktop
%{tde_prefix}/share/apps/tdedisplay/color-schemes/AquaBlue.kcsrc
%{tde_prefix}/share/apps/tdedisplay/color-schemes/AquaGraphite.kcsrc
%{tde_prefix}/share/apps/tdestyle/themes/baghira.themerc
%{tde_prefix}/share/apps/twin/baghira.desktop
%{tde_prefix}/share/icons/crystalsvg/128x128/apps/baghira.png
%{tde_prefix}/share/icons/crystalsvg/128x128/apps/baghira_blue.png
%{tde_prefix}/share/icons/crystalsvg/128x128/apps/baghira_grey.png
%{tde_prefix}/share/icons/crystalsvg/128x128/apps/baghira_white.png
%{tde_prefix}/share/icons/crystalsvg/128x128/apps/baghira_yellow.png
%{tde_prefix}/share/icons/crystalsvg/16x16/apps/baghira.png
%{tde_prefix}/share/icons/crystalsvg/16x16/apps/baghira_blue.png
%{tde_prefix}/share/icons/crystalsvg/16x16/apps/baghira_grey.png
%{tde_prefix}/share/icons/crystalsvg/16x16/apps/baghira_white.png
%{tde_prefix}/share/icons/crystalsvg/16x16/apps/baghira_yellow.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/bStarter.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/bStarter_down.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/bStarter_hover.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/bab_itunes.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/bab_jaguar.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/bab_milk.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/bab_panther.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/bab_tiger.png
%{tde_prefix}/share/icons/crystalsvg/22x22/apps/baghira.png
%{tde_prefix}/share/icons/crystalsvg/22x22/apps/baghira_blue.png
%{tde_prefix}/share/icons/crystalsvg/22x22/apps/baghira_grey.png
%{tde_prefix}/share/icons/crystalsvg/22x22/apps/baghira_white.png
%{tde_prefix}/share/icons/crystalsvg/22x22/apps/baghira_yellow.png
%{tde_prefix}/share/icons/crystalsvg/32x32/apps/baghira.png
%{tde_prefix}/share/icons/crystalsvg/32x32/apps/baghira_blue.png
%{tde_prefix}/share/icons/crystalsvg/32x32/apps/baghira_grey.png
%{tde_prefix}/share/icons/crystalsvg/32x32/apps/baghira_white.png
%{tde_prefix}/share/icons/crystalsvg/32x32/apps/baghira_yellow.png
%{tde_prefix}/share/icons/crystalsvg/48x48/apps/baghira.png
%{tde_prefix}/share/icons/crystalsvg/48x48/apps/baghira_blue.png
%{tde_prefix}/share/icons/crystalsvg/48x48/apps/baghira_grey.png
%{tde_prefix}/share/icons/crystalsvg/48x48/apps/baghira_white.png
%{tde_prefix}/share/icons/crystalsvg/48x48/apps/baghira_yellow.png
%{tde_prefix}/share/icons/crystalsvg/64x64/apps/baghira.png
%{tde_prefix}/share/icons/crystalsvg/64x64/apps/baghira_blue.png
%{tde_prefix}/share/icons/crystalsvg/64x64/apps/baghira_grey.png
%{tde_prefix}/share/icons/crystalsvg/64x64/apps/baghira_white.png
%{tde_prefix}/share/icons/crystalsvg/64x64/apps/baghira_yellow.png
%lang(de) %{tde_prefix}/share/locale/de/LC_MESSAGES/*.mo
%lang(it) %{tde_prefix}/share/locale/it/LC_MESSAGES/*.mo
%lang(ka) %{tde_prefix}/share/locale/ka/LC_MESSAGES/*.mo
%lang(nl) %{tde_prefix}/share/locale/nl/LC_MESSAGES/*.mo
%lang(pl) %{tde_prefix}/share/locale/pl/LC_MESSAGES/*.mo
%lang(pt_BR) %{tde_prefix}/share/locale/pt_BR/LC_MESSAGES/*.mo
%lang(ru) %{tde_prefix}/share/locale/ru/LC_MESSAGES/*.mo
%{tde_prefix}/share/man/man1/bab.1*

