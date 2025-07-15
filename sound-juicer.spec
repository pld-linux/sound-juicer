Summary:	CD ripper
Summary(pl.UTF-8):	Ripper płyt CD
Name:		sound-juicer
Version:	3.40.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	https://download.gnome.org/sources/sound-juicer/3.40/%{name}-%{version}.tar.xz
# Source0-md5:	c648769f8310a43c4b98970cc5d9a7ba
Patch0:		%{name}-no-gst-modules-check.patch
URL:		https://wiki.gnome.org/Apps/SoundJuicer
BuildRequires:	appstream-glib
# libbrasero-media3
BuildRequires:	brasero-devel >= 3.0.0
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.49.5
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.21.6
BuildRequires:	iso-codes
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libdiscid-devel >= 0.4.0
BuildRequires:	libmusicbrainz5-devel >= 5.0.1
BuildRequires:	meson >= 0.57.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.49.5
Requires(post,postun):	gtk-update-icon-cache
Requires:	desktop-file-utils
Requires:	glib2 >= 1:2.49.5
Requires:	gsettings-desktop-schemas
Requires:	gstreamer-cdparanoia >= 1.0
Requires:	gstreamer-plugins-base >= 1.0
Requires:	gtk+3 >= 3.21.6
Requires:	hicolor-icon-theme
Requires:	iso-codes
Requires:	libdiscid >= 0.4.0
Requires:	libmusicbrainz5 >= 5.0.1
Suggests:	gstreamer-audio-formats >= 1.0
Suggests:	gstreamer-flac >= 1.0
Suggests:	gstreamer-lame >= 1.0
Suggests:	gstreamer-taglib >= 1.0
Suggests:	gstreamer-vorbis >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%description -l pl.UTF-8
Sound Juicer, ripper płyt CD używający GTK+ i GStreamera.

%prep
%setup -q
%patch -P0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/sound-juicer

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/sound-juicer
%{_datadir}/GConf/gsettings/sound-juicer.convert
%{_datadir}/dbus-1/services/org.gnome.SoundJuicer.service
%{_datadir}/glib-2.0/schemas/org.gnome.sound-juicer.gschema.xml
%{_datadir}/metainfo/org.gnome.SoundJuicer.metainfo.xml
%{_datadir}/sound-juicer
%{_desktopdir}/org.gnome.SoundJuicer.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.SoundJuicer.png
%{_mandir}/man1/sound-juicer.1*
