Summary:	CD ripper
Summary(pl):	Ripper p³yt CD
Name:		sound-juicer
Version:	2.9.92
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/sound-juicer/2.9/%{name}-%{version}.tar.bz2
# Source0-md5:	1b25649be6a65bd6580fe6e8f77fa623
URL:		http://www.burtonini.com/blog/computers/sound-juicer/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	gnome-media-devel >= 2.9.90
BuildRequires:	gnome-vfs2-devel >= 2.9.0
BuildRequires:	gtk+2-devel >= 2:2.6.2
BuildRequires:	gstreamer-cdparanoia >= 0.8.7
BuildRequires:	gstreamer-devel >= 0.8.8
BuildRequires:	gstreamer-vorbis >= 0.8.7
BuildRequires:	intltool >= 0.20
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libmusicbrainz-devel >= 2.1.0
BuildRequires:	nautilus-cd-burner-devel >= 2.9.0
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	gstreamer-cdparanoia >= 0.8.7
Requires:	gstreamer-vorbis >= 0.8.7
Requires:	nautilus-cd-burner-libs >= 2.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%description -l pl
Sound Juicer, ripper p³yt CD u¿ywaj±cy GTK+ i GStreamera.

%prep
%setup -q

%build
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
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
