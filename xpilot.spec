Summary: An X Window System based multiplayer aerial combat game.
Name: xpilot
Version: 3.6.2
Release: 6
Copyright: GPL
Group: Amusements/Games
Source: ftp://ftp.cs.uit.no/pub/games/xpilot/xpilot-3.6.2.tar.gz
Url: http://www.cs.uit.no/XPilot/
Patch: xpilot-3.6.1-config.patch
Exclusivearch: i386 sparc
BuildRoot: /var/tmp/xpilot-root

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
make Makefiles
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man

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
%defattr(-,root,root)
%doc README LICENSE README.msub 
%doc doc
/usr/X11R6/bin/xpilots
/usr/X11R6/bin/xpilot
/usr/X11R6/bin/xp-replay
/usr/X11R6/lib/X11/xpilot
/usr/X11R6/man/man1/xpilot.1x
/usr/X11R6/man/man1/xpilots.1x
/usr/X11R6/man/man1/xp-replay.1x
%config /etc/X11/wmconfig/xpilot
%config /etc/X11/wmconfig/xpilots
