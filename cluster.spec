#
# INFO:
# This is work taken from the gfs2.spec and moved into a cluster-3 generation. Some of
# the old work was dropped as it had no interest to the commiter, so if You're 
# missing something, please look into gfs2.spec and update.
#

Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Name:		cluster
Version:	3.0.13
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/c/l/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	d13aac279519af926894cc25722b1f9f
URL:		http://sources.redhat.com/cluster/
BuildRequires:	corosync-devel
BuildRequires:	libvirt-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
BuildRequires:	openais-devel
BuildRequires:	openldap-devel
BuildRequires:	ncurses-devel
BuildRequires:	nss-devel
BuildRequires:	nspr-devel
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	python-pexpect
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
%description -l pl.UTF-8

%package ccs
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System
Requires:	libxml2-progs

%description ccs
%description ccs -l pl.UTF-u

%package ccs-devel
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System
Requires:	%{name}-ccs-libs = %{version}-%{release}	

%description ccs-devel
%description ccs-devel -l pl.UTF-u

%package ccs-libs
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description ccs-libs
%description ccs-libs -l pl.UTF-u

%package ccs-static
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description ccs-static
%description ccs-static -l pl.UTF-u

%package cman
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System
Requires:	corosync
Requires:	openais

%description cman
%description cman -l pl.UTF-u

%package cman-devel
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System
Requires:	%{name}-cman-libs = %{version}-%{release}	

%description cman-devel
%description cman-devel -l pl.UTF-u

%package cman-libs
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description cman-libs
%description cman-libs -l pl.UTF-u

%package cman-static
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description cman-static
%description cman-static -l pl.UTF-u

%package dlm
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description dlm
%description dlm -l pl.UTF-u

%package dlm-devel
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System
Requires:	%{name}-dlm-libs = %{version}-%{release}	

%description dlm-devel
%description dlm-devel -l pl.UTF-u

%package dlm-libs
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description dlm-libs
%description dlm-libs -l pl.UTF-u

%package dlm-static
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description dlm-static
%description dlm-static -l pl.UTF-u

%package fence
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description fence
%description fence -l pl.UTF-u

%package fence-devel
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System
Requires:	%{name}-fence-libs = %{version}-%{release}	

%description fence-devel
%description fence-devel -l pl.UTF-u

%package fence-libs
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description fence-libs
%description fence-libs -l pl.UTF-u

%package fence-static
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description fence-static
%description fence-static -l pl.UTF-u

%package group
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description group
%description group -l pl.UTF-u

%package gfs2
Summary:	Shared-disk cluster filesystem
Summary(pl.UTF-8):	Klastrowy system plików na współdzielonym dysku
Group:		Application/System

%description gfs2
GFS (Global File System) is a cluster file system. It allows a cluster
of computers to simultaneously use a block device that is shared
between them (with FC, iSCSI, NBD, etc...). GFS reads and writes to
the block device like a local filesystem, but also uses a lock module
to allow the computers coordinate their I/O so filesystem consistency
is maintained. One of the nifty features of GFS is perfect consistency
-- changes made to the filesystem on one machine show up immediately on all
other machines in the cluster.

%description gfs2 -l pl.UTF-8
GFS (Global File System) to klastrowy system plików. Pozwala klastrowi
komputerów na jednoczesne korzystanie z urządzenia blokowego
dzielonego między nimi (poprzez FC, iSCSI, NBD itp.). GFS odczytuje i
zapisuje urządzenie blokowe jak lokalny system plików, ale używa
dodatkowo modułu blokującego, aby umożliwić komputerom koordynowanie
ich operacji I/O w celu zachowania spójności systemu plików. Jedną z
szykownych możliwości GFS-a jest idealna spójność - zmiany wykonane w
systemie plików na jednej maszynie natychmiast pokazują się na
wszystkich innych maszynach w klastrze.

%package rgmanager
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Application/System

%description rgmanager
%description rgmanager -l pl.UTF-u

%prep
%setup -q

sed -i -e 's,-Wall,%{rpmcflags} -I/usr/include/ncurses -Wall,' make/defines.mk.input
sed -i -e 's/ -ggdb / %{rpmcflags} /' gfs2/libgfs2/Makefile
sed -i -e 's/ -O2 -ggdb / %{rpmcflags} /' gfs2/mkfs/Makefile

%build
./configure \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--mandir=%{_mandir} \
	--prefix=%{_prefix} \
	--sbindir=%{_sbindir} \
	--ncursesincdir=/usr/include/ncurses \
	--nsprincdir=/usr/include/nspr \
	--nssincdir=/usr/include/nss \
	--without_kernel_modules --disable_kernel_check

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/cluster
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT/var/log/cluster
mv $RPM_BUILD_ROOT/''etc/init.d/* $RPM_BUILD_ROOT/etc/rc.d/init.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files ccs
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/confdb2ldif
%attr(755,root,root) %{_sbindir}/ccs_config_dump
%attr(755,root,root) %{_sbindir}/ccs_config_validate
%attr(755,root,root) %{_sbindir}/ccs_test
%attr(755,root,root) %{_sbindir}/ccs_tool
%attr(755,root,root) %{_libdir}/lcrso/*.lcrso
%{_mandir}/man8/ccs_config_dump.*
%{_mandir}/man8/ccs_config_validate.*
%{_mandir}/man8/ccs_tool.*
%{_mandir}/man8/confdb2ldif.*

%files ccs-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libccs.so.3.0
%attr(755,root,root) %ghost %{_libdir}/libccs.so.3

%files ccs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libccs.so
%{_includedir}/ccs.h
%{_pkgconfigdir}/libccs.pc

%files ccs-static
%defattr(644,root,root,755)
%{_libdir}/libccs.a


%files cman
%defattr(644,root,root,755)
%{_sysconfdir}/cluster
/etc/logrotate.d/cluster
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/cman
%attr(755,root,root) %{_sbindir}/cman_notify
%attr(755,root,root) %{_sbindir}/cman_tool
%attr(755,root,root) %{_sbindir}/cmannotifyd
%attr(755,root,root) %{_sbindir}/mkqdisk
%attr(755,root,root) %{_sbindir}/qdiskd
%{_datadir}/cluster
%{_docdir}/cluster
%{_mandir}/man5/cluster.conf.*
%{_mandir}/man5/cman.*
%{_mandir}/man5/qdisk.*
%{_mandir}/man8/cman_tool.*
%{_mandir}/man8/cman_notify.*
%{_mandir}/man8/cmannotifyd.*
%{_mandir}/man8/mkqdisk.*
%{_mandir}/man8/qdiskd.*
/var/log/cluster

%files cman-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcman.so
%attr(755,root,root) %{_libdir}/liblogthread.so
%{_includedir}/libcman.h
%{_includedir}/liblogthread.h
%{_pkgconfigdir}/libcman.pc
%{_pkgconfigdir}/liblogthread.pc

%files cman-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcman.so.3.0
%attr(755,root,root) %ghost %{_libdir}/libcman.so.3
%attr(755,root,root) %{_libdir}/liblogthread.so.3.0
%attr(755,root,root) %ghost %{_libdir}/liblogthread.so.3

%files cman-static
%defattr(644,root,root,755)
%{_libdir}/libcman.a
%{_libdir}/liblogthread.a


%files dlm
%defattr(644,root,root,755)
/etc/udev/rules.d/51-dlm.rules
%attr(755,root,root) %{_sbindir}/dlm_tool
%{_mandir}/man8/dlm_tool.*

%files dlm-devel
%defattr(644,root,root,755)
%{_includedir}/libdlm.h
%{_includedir}/libdlmcontrol.h
%{_pkgconfigdir}/libdlm.pc
%{_pkgconfigdir}/libdlm_lt.pc
%{_pkgconfigdir}/libdlmcontrol.pc
%attr(755,root,root) %{_libdir}/libdlm.so
%attr(755,root,root) %{_libdir}/libdlm_lt.so
%attr(755,root,root) %{_libdir}/libdlmcontrol.so
%{_mandir}/man3/dlm_*.*
%{_mandir}/man3/libdlm.*

%files dlm-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdlm.so.3.0
%attr(755,root,root) %ghost %{_libdir}/libdlm.so.3
%attr(755,root,root) %{_libdir}/libdlm_lt.so.3.0
%attr(755,root,root) %ghost %{_libdir}/libdlm_lt.so.3
%attr(755,root,root) %{_libdir}/libdlmcontrol.so.3.1
%attr(755,root,root) %ghost %{_libdir}/libdlmcontrol.so.3

%files dlm-static
%defattr(644,root,root,755)
%{_libdir}/libdlm.a
%{_libdir}/libdlm_lt.a
%{_libdir}/libdlmcontrol.a


%files fence
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/fence_*
%attr(755,root,root) %{_sbindir}/fenced
%{_mandir}/man8/fence_*.*
%{_mandir}/man8/fenced.*

%files fence-devel
%defattr(644,root,root,755)
%{_includedir}/libfence.h
%{_includedir}/libfenced.h
%{_pkgconfigdir}/libfence.pc
%{_pkgconfigdir}/libfenced.pc
%attr(755,root,root) %{_libdir}/libfence.so
%attr(755,root,root) %{_libdir}/libfenced.so

%files fence-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfence.so.4.0
%attr(755,root,root) %ghost %{_libdir}/libfence.so.4
%attr(755,root,root) %{_libdir}/libfenced.so.3.0
%attr(755,root,root) %ghost %{_libdir}/libfenced.so.3

%files fence-static
%defattr(644,root,root,755)
%{_libdir}/libfence.a
%{_libdir}/libfenced.a

%files group
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/dlm_controld
%attr(755,root,root) %{_sbindir}/gfs_control
%attr(755,root,root) %{_sbindir}/gfs_controld
%attr(755,root,root) %{_sbindir}/group_tool
%attr(755,root,root) %{_sbindir}/groupd
%{_mandir}/man8/dlm_controld.*
%{_mandir}/man8/gfs_control.*
%{_mandir}/man8/gfs_controld.*
%{_mandir}/man8/group_tool.*
%{_mandir}/man8/groupd.*

%files gfs2
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/gfs2
%attr(755,root,root) %{_sbindir}/fsck.gfs2
%attr(755,root,root) %{_sbindir}/gfs2_convert
%attr(755,root,root) %{_sbindir}/gfs2_edit
%attr(755,root,root) %{_sbindir}/gfs2_grow
%attr(755,root,root) %{_sbindir}/gfs2_jadd
%attr(755,root,root) %{_sbindir}/gfs2_quota
%attr(755,root,root) %{_sbindir}/gfs2_tool
%attr(755,root,root) %{_sbindir}/mkfs.gfs2
%attr(755,root,root) %{_sbindir}/mount.gfs2
%{_mandir}/man8/fsck.gfs2.*
%{_mandir}/man8/gfs2.*
%{_mandir}/man8/gfs2_convert.*
%{_mandir}/man8/gfs2_edit.*
%{_mandir}/man8/gfs2_grow.*
%{_mandir}/man8/gfs2_jadd.*
%{_mandir}/man8/gfs2_quota.*
%{_mandir}/man8/gfs2_tool.*
%{_mandir}/man8/mkfs.gfs2.*
%{_mandir}/man8/mount.gfs2.*

%files rgmanager
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/rgmanager
%attr(755,root,root) %{_sbindir}/clubufflush
%attr(755,root,root) %{_sbindir}/clufindhostname
%attr(755,root,root) %{_sbindir}/clulog
%attr(755,root,root) %{_sbindir}/clunfslock
%attr(755,root,root) %{_sbindir}/clurgmgrd
#%attr(755,root,root) %{_sbindir}/clurmtabd
%attr(755,root,root) %{_sbindir}/clustat
%attr(755,root,root) %{_sbindir}/clusvcadm
%attr(755,root,root) %{_sbindir}/rg_test
%attr(755,root,root) %{_sbindir}/rgmanager
%{_mandir}/man8/clubufflush.*
%{_mandir}/man8/clufindhostname.*
%{_mandir}/man8/clulog.*
#%{_mandir}/man8/clunfslock.*
%{_mandir}/man8/clurgmgrd.*
#%{_mandir}/man8/clurmtabd.*
%{_mandir}/man8/clustat.*
%{_mandir}/man8/clusvcadm.*
%{_mandir}/man8/rgmanager.*
