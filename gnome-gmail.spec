Summary:	Integrate GMail into the GNOME desktop
Summary(fr.UTF-8):	Intègre GMail dans l'environnement de bureau GNOME
Name:		gnome-gmail
Version:	1.8.1
Release:	1
License:	GPL v2
Group:		Applications/Networking
URL:		http://gnome-gmail.sourceforge.net/
Source0:	http://downloads.sourceforge.net/gnome-gmail/%{name}-%{version}.tar.gz
# Source0-md5:	d8dbb7954e6ebf8553d2cf6c417404d9
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
Requires:	control-center
Requires:	gconf-editor
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	hicolor-icon-theme
Requires:	python >= 1:2.6
Requires:	python-dbus
Requires:	python-gnome-desktop-keyring
Requires:	python-gnome-gconf
Requires:	python-pygobject
Requires:	python-pygtk-glade
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

%build
%configure \
	--with-gconf-schema-file-dir=%{_sysconfdir}/gconf/schemas

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ta_LK/LC_MESSAGES

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
%gconf_schema_install %{name}.schemas
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/setOOmailer
%{_desktopdir}/%{name}.desktop
# gnome2:
#%{_datadir}/gnome-control-center/default-apps/%{name}.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/gnomegmail.glade
%attr(755,root,root) %{_datadir}/%{name}/evolution
%{_datadir}/gnome/autostart/setOOmailer.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man1/setOOmailer*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
