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

