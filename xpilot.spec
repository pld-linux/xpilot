#
# TODO:
# - separate clent, server and map edit subpackages,
# - maybe move all xpilot desktop files to Games/Arcade/XPilot ?
#
Summary:	An X Window System based multiplayer aerial combat game
Summary(es.UTF-8):	Juego de vuelo en estilo arcade
Summary(pl.UTF-8):	Gra sieciowa symulująca walki powietrzne
Summary(pt_BR.UTF-8):	Jogo de vôo no estilo arcade
Name:		xpilot
Version:	4.5.4
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.xpilot.org/pub/%{name}-%{version}.tar.gz
# Source0-md5:	f2774fda5938629001ed65a311554c01
Source1:	%{name}.png
Source2:	%{name}.desktop
Source3:	%{name}-server.desktop
Source4:	%{name}-mapedit.desktop
Patch0:		%{name}-config.patch
URL:		http://www.xpilot.org/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xpilot is an X Window System based multiplayer game of aerial combat.
The object of the game is to shoot each other down, or you can use the
race mode to just fly around. Xpilot resembles the Commodore 64 Thrust
game, which is similar to Atari's Gravitar and Asteriods (note: this
is not misspelled). Unless you already have an xpilot server on your
network, you'll need to set up the server on one machine, and then set
up xpilot clients on all of the players' machines.

%description -l es.UTF-8
xpilot es un juego de ación que permite diversos jugadores en red.
Esto le hace óptimo para horas de diversión. El objetivo básico del
juego es volar y matar - ¿Hace falta decir algo más?

%description -l pl.UTF-8
Xpilot jest grą sieciową dla wielu użytkowników symulującą walki
powietrzne. Celem gry jest zestrzelić przeciwnika lub rekreacyjne
latanie podczas gry w trybie ,,wycieczki''.

%description -l pt_BR.UTF-8
xpilot é um jogo de ação que permite diversos jogadores em rede. Isto
torna-o ótimo para horas de diversão. O objetivo básico do jogo é voar
e matar - precisa dizer mais?

%prep
%setup -q
%patch0 -p1

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	PREFIX=/usr \
	INSTLIBDIR=%{_datadir}/%{name} \
	INSTBINDIR=%{_bindir} \
	INSTMANDIR=%{_mandir}/man6

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=/usr \
	INSTLIBDIR=%{_datadir}/%{name} \
	INSTBINDIR=%{_bindir} \
	INSTMANDIR=%{_mandir}/man6

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/{TODO,README*,C*}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xpilot
%{_mandir}/man?/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
