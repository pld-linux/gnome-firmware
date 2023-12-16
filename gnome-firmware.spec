# TODO: switch to gtk4-update-icon-cache
Summary:	GNOME Firmware - install firmware on devices
Summary(pl.UTF-8):	GNOME Firmware - instalowanie firmware'u w urządzeniach
Name:		gnome-firmware
Version:	45.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	169ccd79b918a5ed2485810253fc1155
Patch0:		%{name}-man.patch
URL:		https://gitlab.gnome.org/hughsie/gnome-firmware-updater
BuildRequires:	ConsoleKit-devel
BuildRequires:	appstream-glib
BuildRequires:	desktop-file-utils
BuildRequires:	fwupd-devel >= 1.8.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.74.0
BuildRequires:	gtk4-devel >= 4.2
BuildRequires:	help2man
BuildRequires:	libadwaita-devel >= 1.4
BuildRequires:	libsoup-devel >= 2.52
BuildRequires:	libxmlb-devel >= 0.1.7
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel >= 1:211
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	fwupd >= 1.8.11
Requires:	glib2 >= 1:2.74.0
Requires:	gtk4 >= 4.2
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.4
Requires:	libsoup >= 2.52
Requires:	libxmlb >= 0.1.7
Obsoletes:	gnome-firmware-updater < 3.36
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application can:
- Upgrade, Downgrade, & Reinstall firmware on devices supported by
  fwupd.
- Unlock locked fwupd devices
- Verify firmware on supported devices
- Display all releases for a fwupd device

%description -l pl.UTF-8
Ta aplikacja potrafi:
- uaktualniać, cofać do starszej wersji i reinstalować firmware w
  urządzeniach obsługiwanych przez fwupd
- odblokowywać zablokowanie urządzenia fwupd
- weryfikować firmware w obsługiwanych urządzeniach
- wyświetlać wszystkie wydania dla urządzenia fwupd

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	-Dman=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc MAINTAINERS README.md
%attr(755,root,root) %{_bindir}/gnome-firmware
%{_datadir}/metainfo/org.gnome.Firmware.metainfo.xml
%{_desktopdir}/org.gnome.Firmware.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Firmware.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Firmware-symbolic.svg
%{_mandir}/man1/gnome-firmware.1*
