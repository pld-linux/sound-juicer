Summary:	CD ripper
Summary(pl):	Ripper p³yt CD
Name:		sound-juicer
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.burtonini.com/computing/%{name}-%{version}.tar.gz
URL:		http://www.burtonini.com
BuildRequires:	GConf2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gstreamer-cdparanoia >= 0.6.0
BuildRequires:	gstreamer-devel >= 0.6.0
BuildRequires:	gstreamer-vorbis >= 0.6.0
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libmusicbrainz-devel >= 2.0.0
Requires:	gstreamer-cdparanoia >= 0.6.0
Requires:	gstreamer-vorbis >= 0.6.0
Requires(post):	GConf2
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

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_pixmapsdir}/*
