%define base_name trackballs
%define name %{base_name}-music
%define version 1.4
%define release %mkrel 5

Name: %{name}
Version: %{version}
Release: %{release}
Summary: In-game music for Trackballs - A Marble Madness-like game
Requires: %{base_name} >= 0.5.0
Source: http://downloads.sourceforge.net/trackballs/trackballs-music-1.4.tar.bz2
Group: Games/Arcade
License: GPL, Ethymos Free Music Licence
URL: http://sourceforge.net/projects/trackballs
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Some great music to listen to while playing Trackballs.

Some songs are licensed under the GPL :
    * hrluebke, by M3 (Marco Göbl)
    * Plinkeplanke, by M3 (Marco Göbe)
    * Schizophrenia, by Attila Boros (Attila Boros)
    * Sorrow.ogg, by Attila Boros (Attila Boros)

Others are licensed under the Ethymos Free Music Licence 
( http://www.ethymonics.co.uk/fml.html ) :
    * C64 Revival, by Paul Leach
    * Crazy, by Paul Leach
    * Eurovision Winner!, by Paul Leach

%prep
%setup -n %{name} -q

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{base_name}/music
install -m 644 *.ogg %{buildroot}%{_gamesdatadir}/%{base_name}/music

%files
%defattr(-,root,root)
%doc README fml.html
%{_gamesdatadir}/%{base_name}/music/*

%clean
rm -rf %{buildroot}

