# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       kf5-kdelibs4support
Summary:    KDE Frameworks 5 Tier 4 module with porting aid from KDELibs 4
Version:    4.99.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kf5-kdelibs4support.yaml
Source101:  kf5-kdelibs4support-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  libX11-devel
BuildRequires:  libSM-devel
BuildRequires:  openssl-devel
BuildRequires:  gettext-devel
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdesignerplugin-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kunitconversion-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel


%description
KDE Frameworks 5 Tier 4 module with porting aid from KDELibs 4



%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kf5-kauth-devel
Requires:   kf5-kconfigwidgets-devel
Requires:   kf5-kcoreaddons-devel
Requires:   kf5-kcrash-devel
Requires:   kf5-kdesignerplugin-devel
Requires:   kf5-kdoctools-devel
Requires:   kf5-kemoticons-devel
Requires:   kf5-kguiaddons-devel
Requires:   kf5-kiconthemes-devel
Requires:   kf5-kitemmodels-devel
Requires:   kf5-kinit-devel
Requires:   kf5-knotifications-devel
Requires:   kf5-kparts-devel
Requires:   kf5-ktextwidgets-devel
Requires:   kf5-kunitconversion-devel
Requires:   kf5-kwindowsystem-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.



%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post









%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_bindir}/kf5-config
%{_kf5_bindir}/kdebugdialog5
%{_kf5_libdir}/libKF5KDELibs4Support.so.*
%{_kf5_libexecdir}/fileshareset
%{_kf5_qtplugindir}/kf5/*.so
%{_kf5_qtplugindir}/designer/*.so
%{_kf5_mandir}/man1/*
%{_kf5_datadir}/kservices5/*.protocol
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/qimageioplugins/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/kservices5/kded/networkstatus.desktop
%{_kf5_datadir}/kf5/kdoctools/customization
%{_kf5_datadir}/kf5/locale/*
%{_kf5_datadir}/locale/en_US/kf5_entry.desktop
%{_kf5_datadir}/locale/kf5_all_languages
%{_kf5_datadir}/kf5/widgets/
%{_kf5_datadir}/kf5/kssl/ca-bundle.crt
%{_kf5_sysconfdir}/xdg/colors
%{_kf5_sysconfdir}/xdg/kdebug.areas
%{_kf5_sysconfdir}/xdg/kdebugrc
%{_kf5_sysconfdir}/xdg/ksslcalist
%{_kf5_docdir}/HTML/en/kdebugdialog5
# >> files
# << files


%files devel
%defattr(-,root,root,-)
%{_kf5_libdir}/libKF5KDELibs4Support.so
%{_kf5_libdir}/cmake/KF5KDELibs4Support/
%{_kf5_libdir}/cmake/KF5KDE4Support/
%{_kf5_libdir}/cmake/KDELibs4/
%{_kf5_includedir}/kdelibs4support_version.h
%{_kf5_includedir}/KDELibs4Support/
%{_kf5_datadir}/dbus-1/interfaces/*.xml
# >> files devel
# << files devel

