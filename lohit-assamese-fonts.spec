%global fontname lohit-assamese
%global fontconf 65-0-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.4.3
Release:        4%{?dist}
Summary:        Free Assamese font

Group:          User Interface/X
License:        GPLv2 with exceptions
URL:            https://fedorahosted.org/lohit/
Source0:        http://pravins.fedorapeople.org/lohit/assamese/%{fontname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Patch1: bug-549319-586852.patch
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Assamese truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 
%patch1 -p1 -b .1-fix-font-conf


%build
./generate.pe *.sfd
mv 66-%{fontname}.conf 65-0-lohit-assamese.conf

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT COPYING AUTHORS README ChangeLog.old


%changelog
* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-4
- Resolves: bug 586897
- Resolves: bug 586852

* Mon Dec 28 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-3
- Rebase Update to RHEL 6
- Resolves: bug 550972

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.4.3-2.1
- Rebuilt for RHEL 6

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs

* Wed Sep 09 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
