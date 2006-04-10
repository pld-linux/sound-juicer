Summary:	CD ripper
Summary(pl):	Ripper p³yt CD
Name:		sound-juicer
Version:	2.14.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/sound-juicer/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	b7f849eecc18cd8e534bd305742aaa19
Patch0:		%{name}-desktop.patch
URL:		http://www.burtonini.com/blog/computers/sound-juicer/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.9
BuildRequires:	gnome-doc-utils >= 0.3.1-2
BuildRequires:	gnome-media-devel >= 2.11.91
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.3
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libcdio-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.13.0
BuildRequires:	libmusicbrainz-devel >= 2.1.0
BuildRequires:	libtool
BuildRequires:	nautilus-cd-burner-devel >= 2.13.93
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	gstreamer-cdparanoia >= 0.10
Requires:	hicolor-icon-theme
Requires:	nautilus-cd-burner-libs >= 2.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%description -l pl
Sound Juicer, ripper p³yt CD u¿ywaj±cy GTK+ i GStreamera.

%prep
%setup -q
%patch0 -p1

%build
gnome-doc-prepare --copy --force
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install sound-juicer.schemas
%scrollkeeper_update_post
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/gconf/schemas/sound-juicer.schemas
