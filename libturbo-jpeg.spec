%define name    libturbo-jpeg
%define version 1.1.90
%define release 2

%define libname %mklibname jpeg-turbo
%define develname %mklibname -d -s jpeg-turbo

Name:           %{name}

Summary:        A derivative of libjpeg that uses SIMD instructions
Version:        %{version}
Release:        %{release}
Source0:        http://prdownloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-%{version}.tar.gz
URL:            http://www.libjpeg-turbo.org

Group:          System/Libraries
Summary:        A derivative of libjpeg that uses SIMD instructions
License:        wxWindows Library License v3.1

%description
Builds libjpeg-turbo-static-devel and libjpeg-turbo packages, since
the files required for linking are not included in libjpeg.


%package -n %libname
Summary:        A derivative of libjpeg that uses SIMD instructions
Group:          System/Libraries

Requires: %{_lib}jpeg62
BuildRequires: cmake gcc-c++ glibc-devel jpeg-devel X11-devel nasm
Provides: libjpeg-turbo = %{EVRD}
Provides: turbojpeg = %{EVRD}
Provides: jpeg-turbo = %{EVRD}	

%package -n %develname
Summary:        A derivative of libjpeg that uses SIMD instructions
Group:          System/Libraries

Requires:	%{libname} >= %{EVRD} jpeg-devel
Provides:	turbojpeg-devel = %{EVRD}
Provides:	libturbojpeg-devel = %{EVRD}
Provides:	jpeg-turbo = %{EVRD}

%description -n %libname
This package contains the library needed to run programs dynamically
linked with libjpeg-turbo.

%description -n %develname
This package contains theheaders that programmers will need to develop
applications which will use the libjpeg-turbo library.

%prep
%setup -q -n libjpeg-turbo-%{version}

%build
autoreconf -fi
%configure
%make

%install
%makeinstall
rm -rf %{buildroot}/%{_libdir}/libjpeg*
rm -rf %{buildroot}/%{_includedir}/j*.h
rm -rf %{buildroot}/%{_bindir}/*
rm -rf %{buildroot}/%{_mandir}/*
rm -rf %{buildroot}/%{_libdir}/*.la

%files -n %libname
%{_libdir}/libturbojpeg.so

%files -n %develname
%{_includedir}/turbojpeg.h
