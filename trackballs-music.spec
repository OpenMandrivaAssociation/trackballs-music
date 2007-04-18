%define base_name	trackballs
%define name		%{base_name}-music
%define version		1.2
%define release		%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	In-game music for Trackballs - A Marble Madness-like game
Requires:	%{base_name} >= 0.5.0
Source0:	http://heanet.dl.sourceforge.net/sourceforge/trackballs/tb_design.ogg
Source1:	http://heanet.dl.sourceforge.net/sourceforge/trackballs/tb_genesis.ogg
Source2:	http://heanet.dl.sourceforge.net/sourceforge/trackballs/tb_hrluebke.ogg
Source3:	http://heanet.dl.sourceforge.net/sourceforge/trackballs/tb_plinkeplanke.ogg
Source4:	http://heanet.dl.sourceforge.net/sourceforge/trackballs/tb_schizophrenia.ogg
Source5:	http://heanet.dl.sourceforge.net/sourceforge/trackballs/tb_sorrow.ogg
Group:		Games/Arcade
License:	GPL
URL:		http://sourceforge.net/projects/trackballs
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Some great music to listen to while playing Trackballs.

%prep
cp %{SOURCE0} tb_genesis.ogg
cp %{SOURCE1} tb_design.ogg
cp %{SOURCE2} tb_hrluebke.ogg
cp %{SOURCE3} tb_plinkeplanke.ogg
cp %{SOURCE4} tb_schizophrenia.ogg
cp %{SOURCE5} tb_sorrow.ogg

%build

%install
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{base_name}/music
install -m 644 *.ogg %{buildroot}%{_gamesdatadir}/%{base_name}/music

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{base_name}/music/*

%clean
rm -rf "%{buildroot}"

