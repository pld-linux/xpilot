Summary:	An X Window System based multiplayer aerial combat game
Summary(pl):	Sieciowa gra symuluj±ca walki powietrzne
Name:		xpilot
Version:	4.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.cs.uit.no/pub/games/xpilot/%{name}-%{version}.tar.gz
Patch0:		%{name}-config.patch
URL:		http://www.cs.uit.no/XPilot/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xpilot is an X Window System based multiplayer game of aerial combat.
The object of the game is to shoot each other down, or you can use the
race mode to just fly around. Xpilot resembles the Commodore 64 Thrust
game, which is similar to Atari's Gravitar and Asteriods (note: this
is not misspelled). Unless you already have an xpilot server on your
network, you'll need to set up the server on one machine, and then set
up xpilot clients on all of the players' machines.

%description -l pl
Xpilot jest sieciow± gr± dla wielu u¿ytkowników symuluj±c± walki
powietrzne. Celem gry jest zestrzeliæ przeciwnika lub rekreacyjne
latanie podczas gry w trybie ,,wycieczki''.

%prep
%setup -q
%patch0 -p1

%build
%{__make} Makefiles
%{__make} \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	INSTLIBDIR=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTLIBDIR=%{_datadir}/%{name}

gzip -9nf README.txt doc/{TODO,README*,F*,C*,B*}	

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xpilot
%{_mandir}/man?/*gz
