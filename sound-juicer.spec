Summary:	CD ripper
Summary(pl.UTF-8):	Ripper płyt CD
Name:		sound-juicer
Version:	2.20.1
Release:	2
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sound-juicer/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	cea3c67215c99acf513ee7ea4b5eba7b
Patch0:		%{name}-desktop.patch
URL:		http://www.burtonini.com/blog/computers/sound-juicer/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.9
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-media-devel >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	hal-devel >= 0.5.9
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libcdio-devel >= 0.70
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libmusicbrainz-devel >= 2.1.0
BuildRequires:	libtool
BuildRequires:	nautilus-cd-burner-devel >= 2.20.0
BuildRequires:	pkgconfig
# support for --with-omf in find_lang.sh
BuildRequires:	rpm-build >= 4.4.9-10
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gstreamer-cdparanoia >= 0.10.10
Requires:	hicolor-icon-theme
Requires:	libgnomeui >= 2.20.0
Requires:	nautilus-cd-burner-libs >= 2.20.0
Suggests:	gstreamer-audio-formats
Suggests:	gstreamer-flac
Suggests:	gstreamer-lame
Suggests:	gstreamer-taglib
Suggests:	gstreamer-vorbis
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

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install sound-juicer.schemas
%scrollkeeper_update_post
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
