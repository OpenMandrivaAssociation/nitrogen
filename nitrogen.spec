Summary:	A wallpaper setter
Name:		nitrogen
Version:	1.5.2
Release:	2
License:	GPLv2
Group:		Graphical desktop/Other
URL:		http://projects.l3ib.org/nitrogen/
Source0:	http://projects.l3ib.org/nitrogen/files/%{name}-%{version}.tar.gz

BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkmm-2.4)

%description
Nitrogen is a background browser and setter for X. It is written in C++
using the gtkmm toolkit. It can be used in two modes: browser and recall.
It is multi-head friendly and can even work in GNOME.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -lX11 -ldl -lXext"
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Nitrogen
Comment=Change wallpapers
Exec=nitrogen
Icon=graphics_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Settings;DesktopSettings;X-MandrivaLinux-System-Configuration;
EOF

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*



%changelog
* Tue May 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.5.2-2
+ Revision: 801182
- imported package nitrogen


* Wed Jan 25 2012 KDulcimer <kdulcimer@unity-linux.org> 1.5.2-2
- Rebuild
- Bring spec up to spec

* Sat Sep 17 2011 KDulcimer <kdulcimer@unity-linux.org> 1.5.2-1
- 1.5.2

* Mon May 31 2010 KDulcimer <kdulcimer@unity-linux.org> 1.5.1-2
- fix desktop file

* Tue Feb 09 2010 KDulcimer <kdulcimer@unity-linux.org> 1.5.1-1
- 1.5.1

* Sat Jan 23 2010 KDulcimer <kdulcimer@unity-linux.org> 1.5-1
- 1.5

* Mon May 18 2009 Gianvacca <gianvacca@unity-linux.org> 1.4-1unity2009
- New version for Unity

* Thu Jan 10 2008 KDulcimer <kdulcimer@gmail.com> 1.2-1tinyme2008
- 1.2

* Tue Nov 27 2007 KDulcimer <kdulcimer@gmail.com> 1.0-3pclos_tinyme2007
- Adjusted Build and BuildRequires

* Thu Nov 15 2007 KDulcimer <kdulcimer@gmail.com> 1.0-2pclos_tinyme2007
- Added menu entry

* Tue Oct 2 2007 KDulcimer <kdulcimer@gmail.com> 1.0-1pclos_tinyme2007
- Build for TinyMe/PCLinuxOS 2007
