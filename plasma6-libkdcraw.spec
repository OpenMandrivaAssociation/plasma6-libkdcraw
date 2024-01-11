%define major 5
%define libname %mklibname KDcrawQt6
%define devname %mklibname KDcrawQt6 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	C++ interface around LibRaw library
Name:		plasma6-libkdcraw
Version:	24.01.90
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libkdcraw-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
%rename	%{name}-common

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files
%doc README AUTHORS
%{_datadir}/qlogging-categories6/libkdcraw.categories

#----------------------------------------------------------------------

%define kdcraw_major 23
%define libkdcraw %mklibname kdcraw %{kdcraw_major}

%package -n %{libname}
Summary:	Kdcraw library
Group:		System/Libraries
Requires:	%{name}-common = %{EVRD}
Obsoletes:	%{_lib}kdcraw20 < 2:4.9.0
Obsoletes:	%{_lib}kdcraw21 < 2:4.10.0
Obsoletes:	%{_lib}kdcraw22 < 2:4.12.0
Obsoletes:	%{_lib}kdcraw23 < 2:16.12.0

%description -n %{libname}
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files -n %{libname}
%{_libdir}/libKDcrawQt6.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90
Obsoletes:	libkdcraw-devel < 2:16.12.0

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devname}
%{_includedir}/KDcrawQt6
%{_libdir}/*.so
%{_libdir}/cmake/KDcrawQt6

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n libkdcraw-%{?git:master}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
