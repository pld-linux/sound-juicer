Summary:	CD ripper
Summary(pl.UTF-8):	Ripper płyt CD
Name:		sound-juicer
Version:	3.12.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sound-juicer/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	72eec63540026139d9aa855a2839a5cb
URL:		http://www.burtonini.com/blog/computers/sound-juicer/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	brasero-devel >= 3.0.0
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.2.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	iso-codes
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libdiscid-devel
BuildRequires:	libmusicbrainz5-devel >= 5.0.1
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	desktop-file-utils
Requires:	gsettings-desktop-schemas
Requires:	gstreamer-cdparanoia >= 1.0.0
Requires:	hicolor-icon-theme
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

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
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
%{_datadir}/%{name}
%{_datadir}/GConf/gsettings/sound-juicer.convert
%{_datadir}/glib-2.0/schemas/org.gnome.sound-juicer.gschema.xml
%{_mandir}/man1/sound-juicer.1*
%{_desktopdir}/sound-juicer.desktop
%{_iconsdir}/hicolor/*/apps/*
