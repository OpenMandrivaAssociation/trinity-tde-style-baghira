#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define tde_pkg tde-style-baghira
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

# Required for Mageia and PCLinuxOS: removes the ldflag '--no-undefined'
%define _disable_ld_no_undefined 1

%if 0%{?mdkversion}
%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1
%endif

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity
%global toolchain %(readlink /usr/bin/cc)

Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.8
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TDE style for Apple junkies :)
Group:		Graphical desktop/TDE
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/themes/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildRequires:  cmake make
BuildRequires:          trinity-tdelibs-devel >= %{tde_version}
BuildRequires:          trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}
%if "%{?toolchain}" != "clang"
BuildRequires:	gcc-c++
%endif
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


%if 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif


%prep
%autosetup -n %{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}


%build
if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DDATA_INSTALL_DIR=%{tde_datadir}/apps \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__make install DESTDIR=%{buildroot} -C build


%files
%defattr(-,root,root)
%{tde_bindir}/bab
%{tde_libdir}/libbaghirastarter.la
%{tde_libdir}/libbaghirastarter.so
%{tde_tdelibdir}/b_menu_panelapplet.la
%{tde_tdelibdir}/b_menu_panelapplet.so
%{tde_tdelibdir}/plugins/styles/baghira.la
%{tde_tdelibdir}/plugins/styles/baghira.so
%{tde_tdelibdir}/tdestyle_baghira_config.la
%{tde_tdelibdir}/tdestyle_baghira_config.so
%{tde_tdelibdir}/twin3_baghira.la
%{tde_tdelibdir}/twin3_baghira.so
%{tde_tdelibdir}/twin_baghira_config.la
%{tde_tdelibdir}/twin_baghira_config.so
%{tde_libdir}/usermanager_panelapplet.la
%{tde_libdir}/usermanager_panelapplet.so
%{tde_tdeappdir}/bab.desktop
%{tde_datadir}/apps/baghira/
%{tde_datadir}/apps/kicker/applets/baghira-starter.desktop
%{tde_datadir}/apps/kicker/applets/baghira-usermanager.desktop
%{tde_datadir}/apps/tdedisplay/color-schemes/AquaBlue.kcsrc
%{tde_datadir}/apps/tdedisplay/color-schemes/AquaGraphite.kcsrc
%{tde_datadir}/apps/tdestyle/themes/baghira.themerc
%{tde_datadir}/apps/twin/baghira.desktop
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bStarter.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bStarter_down.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bStarter_hover.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_itunes.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_jaguar.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_milk.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_panther.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_tiger.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira_yellow.png
%lang(de) %{tde_datadir}/locale/de/LC_MESSAGES/*.mo
%lang(it) %{tde_datadir}/locale/it/LC_MESSAGES/*.mo
%lang(ka) %{tde_datadir}/locale/ka/LC_MESSAGES/*.mo
%lang(nl) %{tde_datadir}/locale/nl/LC_MESSAGES/*.mo
%lang(pl) %{tde_datadir}/locale/pl/LC_MESSAGES/*.mo
%lang(pt_BR) %{tde_datadir}/locale/pt_BR/LC_MESSAGES/*.mo
%lang(ru) %{tde_datadir}/locale/ru/LC_MESSAGES/*.mo
%{tde_mandir}/man1/bab.1*

