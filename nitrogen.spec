Summary:	A wallpaper setter
Name:		nitrogen
Version:	1.6.1
Release:	1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/l3ib/nitrogen
Source0:	https://github.com/l3ib/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:		nitrogen-1.6.1-fix_appdata_path.patch

BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libpng)

%description
Nitrogen is a background browser and setter for X. It is written in C++
using the gtkmm toolkit. It can be used in two modes: browser and recall.
It is multi-head friendly and can even work in GNOME.

%files -f %{name}.lang
%license COPYING
%doc NEWS README AUTHORS ChangeLog
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lX11"
#export CXXFLAGS="%{optflags} -lX11 -ldl -lXext"
%configure
%make_build

%install
%make_install

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

# locales
%find_lang %{name}

