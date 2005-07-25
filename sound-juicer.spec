Summary:	CD ripper
Summary(pl):	Ripper p�yt CD
Name:		sound-juicer
Version:	2.11.90
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/sound-juicer/2.11/%{name}-%{version}.tar.bz2
# Source0-md5:	b7b997b8377673049da55675f48ae26d
Patch0:		%{name}-desktop.patch
URL:		http://www.burtonini.com/blog/computers/sound-juicer/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	gnome-doc-utils >= 0.3.1-2
BuildRequires:	gnome-media-devel >= 2.10.0-0.2
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gstreamer-GConf-devel >= 0.8.8
BuildRequires:	gstreamer-devel >= 0.8.9
BuildRequires:	gtk+2-devel >= 2:2.6.3
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libmusicbrainz-devel >= 2.1.0
BuildRequires:	libtool
BuildRequires:	nautilus-cd-burner-devel >= 2.11.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	gstreamer-cdparanoia >= 0.8.8
Requires:	nautilus-cd-burner-libs >= 2.11.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%description -l pl
Sound Juicer, ripper p�yt CD u�ywaj�cy GTK+ i GStreamera.

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
	--disable--schemas-install
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
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
