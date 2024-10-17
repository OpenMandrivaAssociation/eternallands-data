%define oname eternallands

# data package version
%define dversion 193
# sound package version
%define sversion 191

Summary:	Data files to play Eternal Lands
Name:		%{oname}-data
Version:	1.9.3
Release:	3
License:	QTPL-based
Group:		Games/Adventure
Url:		https://www.eternal-lands.com
Source0:	http://www.eternal-lands.com/el_linux_%{dversion}.zip
Source1:	http://www.eternallands.co.uk/EL_sound_%{sversion}.zip
Source10:	http://www.eternallands.co.uk/music_full.zip
BuildRequires:	unzip
BuildArch:	noarch

%description
Data files to play Eternal Lands. Graphics, music, sounds etc.

%files
%doc license.txt
%{_gamesdatadir}/%{oname}

#----------------------------------------------------------------------------

%prep
%setup -q -n el_linux -a 1

%build

%install
# game data and sound files
install -d %{buildroot}%{_gamesdatadir}/%{oname}
rm -f *.bin *.exe
cp -r * %{buildroot}%{_gamesdatadir}/%{oname}/

# game music
install -d %{buildroot}%{_gamesdatadir}/%{oname}/music
unzip %{SOURCE10} -d %{buildroot}%{_gamesdatadir}/%{oname}/music

