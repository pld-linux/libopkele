#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries

Summary:	C++ OpenID support library
Name:		libopkele
Version:	2.0.4
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://kin.klever.net/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	47a7efbdd2c9caaaa8e4360eb2beea21
URL:		http://kin.klever.net/libopkele/
BuildRequires:	boost-devel
BuildRequires:	curl-devel
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	pkgconfig
BuildRequires:	tidy-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libopkele is a C++ implementation of an OpenID decentralized identity
system. It provides OpenID protocol handling, leaving authentication
and user interaction to the implementor.

%package devel
Summary:	Header files for libopkele library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libopkele
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libopkele library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libopkele.

%package static
Summary:	Static libopkele library
Summary(pl.UTF-8):	Statyczna biblioteka libopkele
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libopkele library.

%description static -l pl.UTF-8
Statyczna biblioteka libopkele.

%package apidocs
Summary:	libopkele API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libopkele
Group:		Documentation

%description apidocs
API and internal documentation for libopkele library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libopkele.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%{?with_apidocs:doxygen}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libopkele.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopkele.so.3

%files devel
%defattr(644,root,root,755)
%{_libdir}/libopkele.so
%{_libdir}/libopkele.la
%{_includedir}/opkele
%{_pkgconfigdir}/libopkele.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libopkele.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doxydox/html/*
%endif
