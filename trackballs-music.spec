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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.4-5mdv2010.0
+ Revision: 434457
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-4mdv2009.0
+ Revision: 261644
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-3mdv2009.0
+ Revision: 254712
- rebuild

* Tue Mar 04 2008 Guillaume Bedot <littletux@mandriva.org> 1.4-1mdv2008.1
+ Revision: 179227
- 1.4

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-5mdv2008.0
+ Revision: 90339
- rebuild

* Wed Apr 18 2007 Guillaume Bedot <littletux@mandriva.org> 1.2-4mdv2008.0
+ Revision: 14715
- 2 new tracks added


* Fri May 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-3mdk
- rebuild

* Sat Mar 05 2005 Guillaume Bedot <guillaume.bedot@cegetel.net> 1.2-2mdk
- 2 new tracks.

* Wed May 26 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.2-1mdk
- new version
- rpmbuildupdate aware

