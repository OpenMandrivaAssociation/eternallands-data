%define 	oname eternallands

# data package version
%define		dversion 192
# sound package version
%define		sversion 191

Name:		%{oname}-data
Summary:	Data files to play Eternal Lands
Version:	1.9.2
Release:	%mkrel 1
License:	QTPL-based
Group:		Games/Adventure
URL:		http://www.eternal-lands.com
Source0:	http://www.eternal-lands.com/el_linux_%{dversion}.zip
Source1:	http://www.eternallands.co.uk/EL_sound_%{sversion}.zip
Source10:	http://www.eternallands.co.uk/music_full.zip
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot

%description
Data files to play Eternal Lands. Graphics, music, sounds etc.

%prep
%setup -q -n el_linux -a 1

%build

%install
rm -rf %{buildroot}

# game data and sound files
install -d %{buildroot}%{_gamesdatadir}/%{oname}
rm -f *.bin
cp -r * %{buildroot}%{_gamesdatadir}/%{oname}/

# game music
install -d %{buildroot}%{_gamesdatadir}/%{oname}/music
unzip %{SOURCE10} -d %{buildroot}%{_gamesdatadir}/%{oname}/music

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc license.txt
%{_gamesdatadir}/%{oname}

