Summary:	CD ripper
Summary(pl):	Ripper p³yt CD
Name:		sound-juicer
Version:	0.5.10.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.burtonini.com/computing/%{name}-%{version}.tar.gz
# Source0-md5:	a879cce136a1f26274f0cb1906fbec71
URL:		http://www.burtonini.com/blog/computers/sound-juicer/
BuildRequires:	GConf2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gstreamer-cdparanoia >= 0.6.1
BuildRequires:	gstreamer-devel >= 0.6.1
BuildRequires:	gstreamer-vorbis >= 0.6.1
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libmusicbrainz-devel >= 2.0.1
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	gstreamer-cdparanoia >= 0.6.1
Requires:	gstreamer-vorbis >= 0.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%description -l pl
Sound Juicer, ripper p³yt CD u¿ywaj±cy GTK+ i GStreamera.

%prep
%setup -q

%build
%configure \
	--disable--schemas-install

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
