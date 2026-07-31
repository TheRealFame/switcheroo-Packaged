Name:           switcheroo
Version:        2.6.0
Release:        1%{?dist}
Summary:        Convert and manipulate images

%define debug_package %{nil}

License:        GPL-3.0-or-later
URL:            https://gitlab.com/adhami3310/Switcheroo
Source0:        https://gitlab.com/adhami3310/Switcheroo/-/archive/v%{version}/Switcheroo-%{version}.tar.gz

BuildRequires:  meson >= 0.59.0
BuildRequires:  ninja-build

BuildRequires:  pkgconfig
BuildRequires:  gtk4-devel >= 4.6.0
BuildRequires:  libadwaita-devel
BuildRequires:  ImageMagick-devel
BuildRequires:  libheif-devel
BuildRequires:  libjxl-devel
BuildRequires:  libwebp-devel
BuildRequires:  librsvg2-devel
BuildRequires:  ghostscript
BuildRequires:  desktop-file-utils
BuildRequires:  appstream
BuildRequires:  gettext

Requires:       ImageMagick
Requires:       ghostscript

%description
A simple, quick, and easy-to-use tool to convert and manipulate your images
in whatever way you like. Supports JPEG, PNG, WebP, SVG, HEIC, BMP, AVIF,
JXL, PDF, TIFF, GIF, and ICO formats.

%prep
%autosetup -n Switcheroo-%{version}

%build
meson setup builddir --prefix=/usr --buildtype=release
ninja -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%{_bindir}/switcheroo
%{_datadir}/applications/io.gitlab.adhami3310.Converter.desktop
%{_datadir}/metainfo/io.gitlab.adhami3310.Converter.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/io.gitlab.adhami3310.Converter.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.gitlab.adhami3310.Converter-symbolic.svg
%{_datadir}/glib-2.0/schemas/io.gitlab.adhami3310.Converter.gschema.xml
%{_datadir}/dbus-1/services/io.gitlab.adhami3310.Converter.service
%{_datadir}/locale/*/LC_MESSAGES/switcheroo.mo
%{_datadir}/switcheroo/
%license COPYING

%changelog
* Thu Jul 30 2026 Fame <fame@famelinuxpc> - 2.6.0-1
- Initial RPM package release
