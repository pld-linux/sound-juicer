Summary:	CD ripper
Summary(pl):	Ripper p³yt CD
Name:		sound-juicer
Version:	2.16.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/sound-juicer/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	2427ed778ab3366b47405af349be3a33
Patch0:		%{name}-desktop.patch
URL:		http://www.burtonini.com/blog/computers/sound-juicer/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.9
BuildRequires:	gnome-doc-utils >= 0.8.0
BuildRequires:	gnome-media-devel >= 2.16.1
BuildRequires:	gnome-vfs2-devel >= 2.16.2
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcdio-devel
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libmusicbrainz-devel >= 2.1.0
BuildRequires:	libtool
BuildRequires:	nautilus-cd-burner-devel >= 2.16.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post,preun):	GConf2 >= 2.16.0
Requires(post,postun):	gtk+2 >= 2:2.10.6
Requires(post,postun):	scrollkeeper
Requires:	gstreamer-cdparanoia >= 0.10.10
Requires:	hicolor-icon-theme
Requires:	libgnomeui >= 2.16.1
Requires:	nautilus-cd-burner-libs >= 2.16.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%description -l pl
Sound Juicer, ripper p³yt CD u¿ywaj±cy GTK+ i GStreamera.

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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install sound-juicer.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor
%banner %{name} -e << EOF
To be able to rip a CD, You need to install appropriate
GStreamer plugins:
- gstreamer-audio-formats (encoding to WAVE)
- gstreamer-flac (encoding to FLAC)
- gstreamer-vorbis (encoding to Ogg Vorbis)
EOF

%preun
%gconf_schema_uninstall sound-juicer.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/gconf/schemas/sound-juicer.schemas
