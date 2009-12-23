#
# TODO: pl
#
Summary:	Programmable physical simulator and renderer
Name:		techne
Version:	0.1
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://mirror.lihnidos.org/GNU/savannah/techne/%{name}-%{version}.tar.gz
# Source0-md5:	ce836281dd38394f98a919d13ed891a7
Patch0:		%{name}-bin.patch
URL:		http://savannah.nongnu.org/projects/techne/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-objc
BuildRequires:	lua51-devel
BuildRequires:	ode-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Techne is a general purpose, programmable physical simulator and
renderer. It reads in a set of scripts wherein every aspect of a
physical system is specified and then proceeds to simulate and render
the system onscreen. This is the general idea. The main goal is to
decouple computer programming, in its involved low-level form at
least, from digital art creation, shifting effort away from worrying
about graphics library quirks and memory allocation and towards
understanding and modeling the physical and aesthetic aspects of a
given system.

%prep
%setup -q
%patch0 -p1
%{__sed} -i 's/\[lua5.1\]/\[lua51\]/' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/techne.bin $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/techne*
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
