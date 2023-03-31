Summary:	Truetype's Poltawski-Antiqua fonts
Name:		fonts-ttf-poltawski-antiqua
Version:	1.101
Release:	9
License:	GUST Font License
Group:		System/Fonts/True type
URL:		http://jmn.pl/antykwa-poltawskiego/
Source0:	http://jmn.pl/pliki/ap%{version}ttf.zip
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description
This font was designed in the 'twenties and the 'thirties
of XX century by a Polish graphic artist and a typographer 
Adam PÃÅÅtawski.
It was widely used by Polish printing houses as long as metal
types were in use (until ca the 'sixties).

%prep
%setup -qc

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/antpolt

install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/antpolt
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/antpolt > %{buildroot}%{_datadir}/fonts/TTF/antpolt/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/antpolt/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/antpolt \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-antpolt:pri=50

%files
%dir %{_datadir}/fonts/TTF/antpolt
%{_datadir}/fonts/TTF/antpolt/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/antpolt/fonts.dir
%{_datadir}/fonts/TTF/antpolt/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-antpolt:pri=50
