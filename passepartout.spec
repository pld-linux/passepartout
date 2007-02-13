Summary:	Passepartout - a DTP application for X
Summary(pl.UTF-8):	Passepartout - aplikacja DTP dla X
Name:		passepartout
Version:	0.6
Release:	1
License:	BSD
Group:		X11/Applications/Publishing
Source0:	http://www.stacken.kth.se/project/pptout/files/%{name}-%{version}.tar.bz2
# Source0-md5:	5d35d32dce802a627e48531207db62ce
Patch0:		%{name}-cvs.patch
Patch1:		%{name}-libxml++.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-gcc4.patch
URL:		http://www.stacken.kth.se/project/pptout/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	libgnomecanvasmm-devel >= 2.6.0
BuildRequires:	libxml++-devel >= 2.6.0
BuildRequires:	libsigc++-devel >= 2.0
Requires:	ghostscript
Requires:	libxslt-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Passepartout is an Open Source Desktop Publishing application for the
X Window System environment. The goal of this project is to create a
system capable of producing pre-press material of professional
quality, but also a useful tool for any enthusiast with access to a
printer. The main focus is on making it easy for the user to create
publications with a flexible layout, typical examples being magazines,
brochures and leaflets.

%description -l pl.UTF-8
Passepartout to aplikacja DTP z otwartymi źródłami dla środowiska X
Window System. Celem projektu jest stworzenie systemu będącego w
stanie wytwarzać materiał profesjonalnej jakości, ale także narzędzia
użytecznego dla entuzjastów z dostępem do drukarki. Głównym celem jest
ułatwienie użytkownikom tworzenia publikacji z elastycznym układem,
których typowymi przykładami są magazyny, broszury i druczki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README doc/*.html doc/examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xml/%{name}
%{_mandir}/man1/*
