Summary:	Passepartout - a DTP application for X
Summary(pl):	Passepartout - aplikacja DTP dla X
Name:		passepartout
Version:	0.3
Release:	1
License:	BSD
Group:		X11/Applications/Publishing
Source0:	http://www.stacken.kth.se/project/pptout/files/%{name}-%{version}.tar.bz2
# Source0-md5:	84ca77ac477b3ae53b841023e78adc44
URL:		http://www.stacken.kth.se/project/pptout/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.2.0
BuildRequires:	libxml++-devel >= 0.22
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

%description -l pl
Passepartout to aplikacja DTP z otwartymi ¼ród³ami dla ¶rodowiska X
Window System. Celem projektu jest stworzenie systemu bêd±cego w
stanie wytwarzaæ materia³ profesjonalnej jako¶ci, ale tak¿e narzêdzia
u¿ytecznego dla entuzjastów z dostêpem do drukarki. G³ównym celem jest
u³atwienie u¿ytkownikom tworzenia publikacji z elastycznym uk³adem,
których typowymi przyk³adami s± magazyny, broszury i druczki.

%prep
%setup -q

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
%doc AUTHORS BUGS NEWS README doc/*.html 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xml/%{name}
%{_mandir}/man1/*
