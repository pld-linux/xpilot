Summary:	An X Window System based multiplayer aerial combat game.
Name:		xpilot
Version:	3.6.2
Release:	6
Copyright:	GPL
Group:		Games
Source:		ftp://ftp.cs.uit.no/pub/games/xpilot/%{name}-%{version}.tar.gz
Url:		http://www.cs.uit.no/XPilot/
Patch:		xpilot-3.6.1-config.patch
Exclusivearch:	%{ix86} sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xpilot is an X Window System based multiplayer game of aerial combat.
The object of the game is to shoot each other down, or you can use
the race mode to just fly around.  Xpilot resembles the Commodore 64
Thrust game, which is similar to Atari's Gravitar and Asteriods (note:
this is not misspelled).  Unless you already have an xpilot server on
your network, you'll need to set up the server on one machine, and then
set up xpilot clients on all of the players' machines.

%prep
%setup -q
%patch -p1

%build
xmkmf
%{__make} Makefiles
%{__make} CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS" \
	INSTLIBDIR=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT \
	INSTLIBDIR=%{_datadir}/%{name}

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README README.msub doc/{BUGS,CREDITS,ChangeLog,FAQ,FIXED,README*}

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpilot <<EOF
xpilot name "xpilot (requires server)"
xpilot description "Fly/Shoot Arcade Game"
xpilot group Games/Video
xpilot exec "xterm -e xpilot -join &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpilots <<EOF
xpilots name "xpilots server"
xpilots description "Fly/Shoot Arcade Game"
xpilots group Games/Video
xpilots exec "xterm -e xpilots &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,README.msub,doc/{BUGS,CREDITS,ChangeLog,FAQ,FIXED,README*}}.gz
%attr(755,root,root) %{_bindir}/xpilots
%attr(755,root,root) %{_bindir}/xpilot
%attr(755,root,root) %{_bindir}/xp-replay
%{_datadir}/xpilot
%{_mandir}/man1/xpilot.1x.gz
%{_mandir}/man1/xpilots.1x.gz
%{_mandir}/man1/xp-replay.1x.gz
%config /etc/X11/wmconfig/xpilot
%config /etc/X11/wmconfig/xpilots
