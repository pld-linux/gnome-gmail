Summary:	Integrate GMail into the GNOME desktop
Summary(fr.UTF-8):	Intègre GMail dans l'environnement de bureau GNOME
Name:		gnome-gmail
Version:	1.7.2
Release:	1
License:	GPL v2
Group:		Applications/Networking
URL:		http://gnome-gmail.sourceforge.net/
Source0:	http://downloads.sourceforge.net/gnome-gmail/%{name}-%{version}.tar.gz
# Source0-md5:	3d9eb34d8f143f40125e1f6063edc15f
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
Requires:	control-center
Requires:	gconf-editor
Requires:	gnome-python2-gconf
Requires:	gnome-python2-gnomekeyring
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	hicolor-icon-theme
Requires:	pygtk2-libglade
Requires:	python >= 1:2.6
Requires:	python-dbus
Requires:	python-pygobject
BuildArch:	noarch
Requires(post):	GConf2
Requires(postun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package makes Gmail a choice in the Gnome control panel for the
default mail handler. It opens in the default web browser.

%description -l fr.UTF-8
Ce paquet rajoute Gmail comme choix possible de logiciel de messagerie
par défaut de Gnome dans le contrôle des applications préférées. Gmail
sera ensuite ouvert dans le navigateur web préféré.

%prep
%setup -q
echo "MimeType=application/mbox;message/rfc822;x-scheme-handler/mailto" >> \
    %{name}.desktop.in

%build
%configure \
	--with-gconf-schema-file-dir=%{_sysconfdir}/gconf/schemas

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

desktop-file-install \
    --dir=$RPM_BUILD_ROOT%{_desktopdir} \
    --add-category Network \
    --remove-category System \
    --remove-category ContactManagement \
    %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}
%update_desktop_database
%update_icon_cache_post hicolor

%postun
%update_desktop_database
%update_icon_cache_post hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/setOOmailer
%{_desktopdir}/%{name}.desktop
%{_datadir}/gnome-control-center/default-apps/%{name}.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/gnomegmail.glade
%{_datadir}/%{name}/evolution
%{_datadir}/gnome/autostart/setOOmailer.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man1/setOOmailer*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
