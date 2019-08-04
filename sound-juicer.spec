Summary:	CD ripper
Summary(pl.UTF-8):	Ripper płyt CD
Name:		sound-juicer
Version:	3.24.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sound-juicer/3.24/%{name}-%{version}.tar.xz
# Source0-md5:	09e1f132339c81e64a7a25620569b5c3
URL:		https://wiki.gnome.org/Apps/SoundJuicer
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
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
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.49.5
Requires(post,postun):	gtk-update-icon-cache
Requires:	desktop-file-utils
Requires:	glib2 >= 1:2.49.5
Requires:	gsettings-desktop-schemas
Requires:	gstreamer-cdparanoia >= 1.0.0
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

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/sound-juicer
%{_datadir}/GConf/gsettings/sound-juicer.convert
%{_datadir}/appdata/org.gnome.SoundJuicer.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.SoundJuicer.service
%{_datadir}/glib-2.0/schemas/org.gnome.sound-juicer.gschema.xml
%{_datadir}/sound-juicer
%{_desktopdir}/org.gnome.SoundJuicer.desktop
%{_iconsdir}/hicolor/*x*/apps/sound-juicer.png
%{_mandir}/man1/sound-juicer.1*
