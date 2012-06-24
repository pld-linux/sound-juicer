Summary:	CD ripper
Summary(pl):	Ripper p�yt CD
Name:		sound-juicer
Version:	2.15.5.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/sound-juicer/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	ff54cb0d4414a4305674117cb374735c
Patch0:		%{name}-desktop.patch
URL:		http://www.burtonini.com/blog/computers/sound-juicer/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.9
BuildRequires:	gnome-doc-utils >= 0.7.2
BuildRequires:	gnome-media-devel >= 2.14.2
BuildRequires:	gnome-vfs2-devel >= 2.15.92
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.9
BuildRequires:	gtk+2-devel >= 2:2.10.2
BuildRequires:	intltool >= 0.35
BuildRequires:	libcdio-devel
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.15.90
BuildRequires:	libmusicbrainz-devel >= 2.1.0
BuildRequires:	libtool
BuildRequires:	nautilus-cd-burner-devel >= 2.15.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	gtk+2 >= 2:2.10.2
Requires(post,postun):	scrollkeeper
Requires:	gstreamer-cdparanoia >= 0.10.9
Requires:	hicolor-icon-theme
Requires:	libgnomeui >= 2.15.91
Requires:	nautilus-cd-burner-libs >= 2.15.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%description -l pl
Sound Juicer, ripper p�yt CD u�ywaj�cy GTK+ i GStreamera.

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ug

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
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_sysconfdir}/gconf/schemas/sound-juicer.schemas
