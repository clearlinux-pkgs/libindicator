#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7EA53E6D798DB404 (charles.kerr@canonical.com)
#
Name     : libindicator
Version  : 12.10.1
Release  : 1
URL      : https://launchpad.net/libindicator/12.10/12.10.1/+download/libindicator-12.10.1.tar.gz
Source0  : https://launchpad.net/libindicator/12.10/12.10.1/+download/libindicator-12.10.1.tar.gz
Source99 : https://launchpad.net/libindicator/12.10/12.10.1/+download/libindicator-12.10.1.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: libindicator-lib
Requires: libindicator-bin
Requires: libindicator-license
Requires: libindicator-data
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
Patch1: libm.patch

%description


%package bin
Summary: bin components for the libindicator package.
Group: Binaries
Requires: libindicator-data
Requires: libindicator-license

%description bin
bin components for the libindicator package.


%package data
Summary: data components for the libindicator package.
Group: Data

%description data
data components for the libindicator package.


%package dev
Summary: dev components for the libindicator package.
Group: Development
Requires: libindicator-lib
Requires: libindicator-bin
Requires: libindicator-data
Provides: libindicator-devel

%description dev
dev components for the libindicator package.


%package lib
Summary: lib components for the libindicator package.
Group: Libraries
Requires: libindicator-data
Requires: libindicator-license

%description lib
lib components for the libindicator package.


%package license
Summary: license components for the libindicator package.
Group: Default

%description license
license components for the libindicator package.


%prep
%setup -q -n libindicator-12.10.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534965361
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1534965361
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libindicator
cp COPYING %{buildroot}/usr/share/doc/libindicator/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/indicator-loader3

%files data
%defattr(-,root,root,-)
/usr/share/libindicator/80indicator-debugging

%files dev
%defattr(-,root,root,-)
/usr/include/libindicator3-0.4/libindicator/indicator-desktop-shortcuts.h
/usr/include/libindicator3-0.4/libindicator/indicator-image-helper.h
/usr/include/libindicator3-0.4/libindicator/indicator-object.h
/usr/include/libindicator3-0.4/libindicator/indicator-service-manager.h
/usr/include/libindicator3-0.4/libindicator/indicator-service.h
/usr/include/libindicator3-0.4/libindicator/indicator.h
/usr/lib64/libdummy-indicator-blank.so
/usr/lib64/libdummy-indicator-entry-func.so
/usr/lib64/libdummy-indicator-null.so
/usr/lib64/libdummy-indicator-signaler.so
/usr/lib64/libdummy-indicator-simple.so
/usr/lib64/libdummy-indicator-visible.so
/usr/lib64/libindicator3.so
/usr/lib64/pkgconfig/indicator3-0.4.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libindicator3.so.7
/usr/lib64/libindicator3.so.7.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/libindicator/COPYING
