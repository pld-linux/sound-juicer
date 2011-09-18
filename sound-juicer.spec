Summary:	CD ripper
Summary(pl.UTF-8):	Ripper płyt CD
Name:		sound-juicer
Version:	2.32.0
Release:	5
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sound-juicer/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	8261bd1f450d7056d15828ed2a69ef65
# https://bugzilla.gnome.org/show_bug.cgi?id=630868
Patch0:		%{name}-gtk.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=631887
Patch1:		%{name}-drawable.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=634729
Patch2:		%{name}-profiles.patch
URL:		http://www.burtonini.com/blog/computers/sound-juicer/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	brasero-devel >= 3.0.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.15
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libgnome-media-profiles-devel
BuildRequires:	libmusicbrainz3-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gstreamer-cdparanoia >= 0.10.10
Requires:	hicolor-icon-theme
Suggests:	gstreamer-audio-formats
Suggests:	gstreamer-flac
Suggests:	gstreamer-lame
Suggests:	gstreamer-taglib
Suggests:	gstreamer-vorbis
Requires:	desktop-file-utils
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%description -l pl.UTF-8
Sound Juicer, ripper płyt CD używający GTK+ i GStreamera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--disable-silent-rules \
	--with-gtk=3.0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install sound-juicer.schemas
%scrollkeeper_update_post
%update_desktop_database
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall sound-juicer.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/sound-juicer
%{_datadir}/%{name}
%{_mandir}/man1/sound-juicer.1*
%{_desktopdir}/sound-juicer.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/gconf/schemas/sound-juicer.schemas
