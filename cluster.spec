#
# Conditional build:
%bcond_without	ldap		# do not include ldap support

Summary:	Linux Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra linuksowego
Name:		cluster
Version:	3.2.0
Release:	1
License:	LGPL v2.1+ (libraries), GPL v2+ (applications)
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/c/l/cluster/%{name}-%{version}.tar.xz
# Source0-md5:	300d83dbbc525c3da21c2e961271c84b
Source1:	%{name}.tmpfiles
Patch0:		%{name}-no_ldap.patch
URL:		https://fedorahosted.org/cluster/wiki/HomePage
BuildRequires:	corosync-devel >= 1.4.1
BuildRequires:	corosync-devel < 2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
BuildRequires:	ncurses-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	openais-devel >= 1.1.4
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	slang-devel
Requires:	%{name}-cman = %{version}-%{release}
Requires:	%{name}-rgmanager = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Linux Cluster infrastructure.

%description -l pl.UTF-8
Infrastruktura klastra linuksowego.

%package ccs
Summary:	Cluster configuration system
Summary(pl.UTF-8):	System konfiguracji klastra
Group:		Applications/System
Requires:	%{name}-ccs-libs = %{version}-%{release}
Requires:	corosync >= 1.4.1
Requires:	libxml2-progs
Obsoletes:	ccs < 3

%description ccs
Cluster configuration system to manage the cluster config file.

%description ccs -l pl.UTF-8
System konfiguracji klastra do zarządzania jego plikiem
konfiguracyjnym.

%package ccs-libs
Summary:	Cluster configuration system library
Summary(pl.UTF-8):	Biblioteka systemu konfiguracji klastra
Group:		Libraries
Requires:	corosync-libs >= 1.4.1

%description ccs-libs
Cluster configuration system library.

%description ccs-libs -l pl.UTF-8
Biblioteka systemu konfiguracji klastra.

%package ccs-devel
Summary:	Header files for ccs library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki ccs
Group:		Development/Libraries
Requires:	%{name}-ccs-libs = %{version}-%{release}
Obsoletes:	ccs-devel < 3

%description ccs-devel
Header files for ccs library.

%description ccs-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki ccs.

%package ccs-static
Summary:	Static ccs library
Summary(pl.UTF-8):	Statyczna biblioteka ccs
Group:		Development/Libraries

%description ccs-static
Static ccs library.

%description ccs-static -l pl.UTF-8
Statyczna biblioteka ccs.

%package cman
Summary:	Cluster infrastructure manager
Summary(pl.UTF-8):	Zarządca infrastruktury klastra
Group:		Applications/System
Requires:	%{name}-ccs = %{version}-%{release}
Requires:	%{name}-cman-libs = %{version}-%{release}
Requires:	%{name}-dlm = %{version}-%{release}
Requires:	%{name}-fence = %{version}-%{release}
Requires:	%{name}-group = %{version}-%{release}
Requires:	corosync >= 1.4.1
Requires:	openais
Obsoletes:	cman < 3

%description cman
MAN is a symmetric, general-purpose, kernel-based cluster manager. It
has two parts. Connection Manager (cnxman) handles membership,
messaging, quorum, event notification and transitions. Service Manager
(sm) handles "service groups" which are a general way of representing
and managing instances of external systems that require cluster
management. The CMAN cluster manager is the foundational system upon
which DLM, GFS, CLVM, and Fence all depend. The CMAN API in the kernel
and userspace is general and available for other programs to use.

%description cman -l pl.UTF-8
MAN to zarządca opartych na jądrze symetrycznych klastrów ogólnego
przeznaczenia. Składa się z dwóch części. Zarządca połączeń
(Connection Manager, cnxman) obsługuje członkostwo, komunikację,
kworum, powiadamianie o zdarzeniach i przejścia. Zarządca usług
(Service Manager, sm) obsługuje "grupy usług", które są ogólnym
sposobem reprezentacji i zarządzania instancjami zewnętrznych systemów
wymagających zarządzania klastrem. Zarządca klastrów CMAN to
podstawowy system, na którym polegają DLM, GFS, CLVM i Fence. API
CMAN-a w jądrze i przestrzeni użytkownika jest ogólne i w całości
dostępne do wykorzystania w innych programach.

%package cman-libs
Summary:	Cluster infrastructure manager library
Summary(pl.UTF-8):	Biblioteka zarządcy infrastruktury klastra
Group:		Libraries
Obsoletes:	cman-libs < 3
# cluster 1.x packages obsoleted by cman-libs 2.x
Obsoletes:	gulm
Obsoletes:	gulm-devel
Obsoletes:	gulm-static
Obsoletes:	iddev
Obsoletes:	magma
Obsoletes:	magma-devel
Obsoletes:	magma-plugins
Obsoletes:	magma-static

%description cman-libs
Cluster infrastructure manager library.

%description cman-libs -l pl.UTF-8
Biblioteka zarządcy infrastruktury klastra.

%package cman-devel
Summary:	Header filed for cman library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki cman
Group:		Development/Libraries
Requires:	%{name}-cman-libs = %{version}-%{release}
Obsoletes:	cman-devel < 3

%description cman-devel
Header filed for cman library.

%description cman-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki cman.

%package cman-static
Summary:	Static cman library
Summary(pl.UTF-8):	Statyczna biblioteka cman
Group:		Development/Libraries
Obsoletes:	cman-static < 3

%description cman-static
Static cman library.

%description cman-static -l pl.UTF-8
Statyczna biblioteka cman.

%package dlm
Summary:	Distributed lock manager
Summary(pl.UTF-8):	Zarządca rozproszonych blokad
Group:		Applications/System
Requires:	%{name}-dlm-libs = %{version}-%{release}
Obsoletes:	dlm < 3

%description dlm
The DLM lock manager is a kernel-based VMS-like distributed lock
manager. It is general purpose and not specific to only GFS or CLVM.
Kernel and userspace locking API's are available.

%description dlm -l pl.UTF-8
Zarządca blokad DLM to oparty na jądrze zarządca rozproszonych blokad
w stylu VMS. Jest ogólnego przeznaczenia, przeznaczonym nie tylko dla
GFS-a czy CLVM-a. Dostępne są API blokowania w jądrze i przestrzeni
użytkownika.

%package dlm-libs
Summary:	Distributed lock manager library
Summary(pl.UTF-8):	Biblioteka zarządcy rozproszonych blokad
Group:		Libraries
Obsoletes:	dlm-libs < 3

%description dlm-libs
Distributed lock manager library.

%description dlm-libs -l pl.UTF-8
Biblioteka zarządcy rozproszonych blokad.

%package dlm-devel
Summary:	Header filed for dlm library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki dlm
Group:		Development/Libraries
Requires:	%{name}-dlm-libs = %{version}-%{release}
Obsoletes:	dlm-devel < 3

%description dlm-devel
Header filed for dlm library.

%description dlm-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki dlm.

%package dlm-static
Summary:	Static dlm library
Summary(pl.UTF-8):	Statyczna biblioteka dlm
Group:		Development/Libraries
Obsoletes:	dlm-static < 3

%description dlm-static
Static dlm library.

%description dlm-static -l pl.UTF-8
Statyczna biblioteka dlm.

%package fence
Summary:	Cluster infrastructure I/O fencing system
Summary(pl.UTF-8):	System barier I/O infrastruktury klastra
Group:		Applications/System
Requires:	%{name}-ccs-libs = %{version}-%{release}
Requires:	%{name}-cman-libs = %{version}-%{release}
Requires:	%{name}-fence-libs = %{version}-%{release}
Requires:	corosync >= 1.4.1
Suggests:	fence-agents
Obsoletes:	fence < 3

%description fence
The Fence system does I/O fencing of cluster members. Any member may
join the default fence domain after which it will be fenced if it
fails without leaving the fence domain cleanly. The lock_dlm GFS lock
module will not permit GFS to be mounted until the node has joined a
fence domain.

The fence daemon, fenced, is usually started by running "fence_tool
join". Once started, fenced joins the default fence domain and the
node is subject to being fenced if it fails. A collection of fence
agents are used by fenced to interface with hardware devices (usually
to shut off its path to shared storage or cycle its power source.)

%description fence -l pl.UTF-8
System Fence odpowiada za bariery I/O dla członków klastra. Każdy z
członków może dołączyć do domyślnej domeny barier, po czym będzie
odgrodzony jeśli zawiedzie nie opuszczając czysto domeny barier. Moduł
blokujący GFS-a lock_dlm nie pozwoli na podmontowanie GFS-a dopóki
węzeł nie dołączy do domeny barier.

Demon fence, fenced, jest zwykle uruchamiany przez fence_tool join. Po
uruchomieniu fenced dołącza do domyślnej domeny barier, a węzeł jest
przedmiotem odgrodzenia jeśli zawiedzie. fenced wykorzystuje zbiór
agentów fence do komunikacji z urządzeniami sprzętowymi (zwykle do
odcinania drogi do dzielonej pamięci lub wyłączania i włączania
zasilania).

%package fence-libs
Summary:	Cluster infrastructure I/O fencing system libraries
Summary(pl.UTF-8):	Biblioteki systemu barier I/O infrastruktury klastra
Group:		Libraries
Requires:	%{name}-ccs-libs = %{version}-%{release}

%description fence-libs
Cluster infrastructure I/O fencing system libraries.

%description fence-libs -l pl.UTF-8
Biblioteki systemu barier I/O infrastruktury klastra.

%package fence-devel
Summary:	Header filed for fence library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki fence
Group:		Development/Libraries
Requires:	%{name}-fence-libs = %{version}-%{release}

%description fence-devel
Header filed for fence library.

%description fence-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki fence.

%package fence-static
Summary:	Static fence libraries
Summary(pl.UTF-8):	Statyczne biblioteki fence
Group:		Development/Libraries
Requires:	%{name}-fence-devel = %{version}-%{release}

%description fence-static
Static fence libraries.

%description fence-static -l pl.UTF-8
Statyczne biblioteki fence.

%package group
Summary:	Cluster 2 compatibility infrastructure
Summary(pl.UTF-8):	Infrastruktura kompatybilności z klastrem w wersji 2
Group:		Applications/System
Requires:	%{name}-ccs-libs = %{version}-%{release}
Requires:	%{name}-cman-libs = %{version}-%{release}
Requires:	%{name}-dlm-libs = %{version}-%{release}
Requires:	%{name}-fence-libs = %{version}-%{release}

%description group
Cluster 2 compatibility infrastructure.

%description group -l pl.UTF-8
Infrastruktura kompatybilności z klastrem w wersji 2.

%package rgmanager
Summary:	HA resource group failover
Summary(pl.UTF-8):	Failover dla grupy zasobów wysokiej dostępności
Group:		Applications/System
Requires:	%{name}-ccs-libs = %{version}-%{release}
Requires:	%{name}-cman-libs = %{version}-%{release}
Requires:	%{name}-dlm-libs = %{version}-%{release}
Requires:	%{name}-fence-libs = %{version}-%{release}
Suggests:	resource-agents
Obsoletes:	rgmanager < 3

%description rgmanager
Resource Group Manager provides high availability of critical server
applications in the event of planned or unplanned system downtime.

%description rgmanager -l pl.UTF-8
Resource Group Manager daje wysoką dostępność krytycznych aplikacji
serwerowych w przypadku planowanych lub nieplanowanych wyłączeń
serwera.

%prep
%setup -q
%{!?with_ldap:%patch0 -p1}

sed -i -e 's@-Wall@%{rpmcflags} -I/usr/include/ncurses -Wall@' make/defines.mk.input

%build
./configure \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--mandir=%{_mandir} \
	--prefix=%{_prefix} \
	--sbindir=%{_sbindir} \
	--ncursesincdir=/usr/include/ncurses \
	--disable_kernel_check

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/cluster,/etc/rc.d/init.d} \
		$RPM_BUILD_ROOT{/var/log/cluster,%{systemdtmpfilesdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/''etc/init.d/* $RPM_BUILD_ROOT/etc/rc.d/init.d

install %{SOURCE1} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

# let rpm autogenerate dependencies
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post   ccs-libs   -p /sbin/ldconfig
%postun ccs-libs   -p /sbin/ldconfig
%post   cman-libs  -p /sbin/ldconfig
%postun cman-libs  -p /sbin/ldconfig
%post   dlm-libs   -p /sbin/ldconfig
%postun dlm-libs   -p /sbin/ldconfig
%post   fence-libs -p /sbin/ldconfig
%postun fence-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%files ccs
%defattr(644,root,root,755)
%if %{with ldap}
%attr(755,root,root) %{_sbindir}/confdb2ldif
%endif
%attr(755,root,root) %{_sbindir}/ccs_config_dump
%attr(755,root,root) %{_sbindir}/ccs_config_validate
%attr(755,root,root) %{_sbindir}/ccs_test
%attr(755,root,root) %{_sbindir}/ccs_tool
%attr(755,root,root) %{_sbindir}/ccs_update_schema
%attr(755,root,root) %{_libdir}/lcrso/config_cmanpre.lcrso
%{?with_ldap:%attr(755,root,root) %{_libdir}/lcrso/config_ldap.lcrso}
%attr(755,root,root) %{_libdir}/lcrso/config_xml.lcrso
%attr(755,root,root) %{_libdir}/lcrso/service_cman.lcrso
%{_mandir}/man8/ccs_config_dump.8*
%{_mandir}/man8/ccs_config_validate.8*
%{_mandir}/man8/ccs_tool.8*
%{_mandir}/man8/ccs_update_schema.8*
%if %{with ldap}
%{_mandir}/man8/confdb2ldif.8*
%endif
%attr(700,root,root) /var/run/cluster
%{systemdtmpfilesdir}/%{name}.conf

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
%dir %{_sysconfdir}/cluster
%dir %{_sysconfdir}/cluster/cman-notify.d
/etc/logrotate.d/cluster
%attr(754,root,root) /etc/rc.d/init.d/cman
%attr(755,root,root) %{_sbindir}/cman_notify
%attr(755,root,root) %{_sbindir}/cman_tool
%attr(755,root,root) %{_sbindir}/cmannotifyd
%attr(755,root,root) %{_sbindir}/mkqdisk
%attr(755,root,root) %{_sbindir}/qdiskd
%{_datadir}/cluster
%{_docdir}/cluster
%{_mandir}/man5/cluster.conf.5*
%{_mandir}/man5/cman.5*
%{_mandir}/man5/qdisk.5*
%{_mandir}/man8/checkquorum.8*
%{_mandir}/man8/cman_notify.8*
%{_mandir}/man8/cman_tool.8*
%{_mandir}/man8/cmannotifyd.8*
%{_mandir}/man8/mkqdisk.8*
%{_mandir}/man8/qdiskd.8*
/var/log/cluster

%files cman-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcman.so.3.0
%attr(755,root,root) %ghost %{_libdir}/libcman.so.3
%attr(755,root,root) %{_libdir}/liblogthread.so.3.0
%attr(755,root,root) %ghost %{_libdir}/liblogthread.so.3

%files cman-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcman.so
%attr(755,root,root) %{_libdir}/liblogthread.so
%{_includedir}/libcman.h
%{_includedir}/liblogthread.h
%{_pkgconfigdir}/libcman.pc
%{_pkgconfigdir}/liblogthread.pc

%files cman-static
%defattr(644,root,root,755)
%{_libdir}/libcman.a
%{_libdir}/liblogthread.a

%files dlm
%defattr(644,root,root,755)
/lib/udev/rules.d/51-dlm.rules
%attr(755,root,root) %{_sbindir}/dlm_tool
%{_mandir}/man8/dlm_tool.8*

%files dlm-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdlm.so.3.0
%attr(755,root,root) %ghost %{_libdir}/libdlm.so.3
%attr(755,root,root) %{_libdir}/libdlm_lt.so.3.0
%attr(755,root,root) %ghost %{_libdir}/libdlm_lt.so.3
%attr(755,root,root) %{_libdir}/libdlmcontrol.so.3.1
%attr(755,root,root) %ghost %{_libdir}/libdlmcontrol.so.3

%files dlm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdlm.so
%attr(755,root,root) %{_libdir}/libdlm_lt.so
%attr(755,root,root) %{_libdir}/libdlmcontrol.so
%{_includedir}/libdlm.h
%{_includedir}/libdlmcontrol.h
%{_pkgconfigdir}/libdlm.pc
%{_pkgconfigdir}/libdlm_lt.pc
%{_pkgconfigdir}/libdlmcontrol.pc
%{_mandir}/man3/dlm_*.3*
%{_mandir}/man3/libdlm.3*

%files dlm-static
%defattr(644,root,root,755)
%{_libdir}/libdlm.a
%{_libdir}/libdlm_lt.a
%{_libdir}/libdlmcontrol.a

%files fence
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/fence_*
%attr(755,root,root) %{_sbindir}/fenced
%{perl_vendorarch}/Cluster
%dir %{perl_vendorarch}/auto/Cluster
%dir %{perl_vendorarch}/auto/Cluster/CCS
%{perl_vendorarch}/auto/Cluster/CCS/CCS.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Cluster/CCS/CCS.so
%{_mandir}/man3/Cluster::CCS.3pm*
%{_mandir}/man8/fence_*.8*
%{_mandir}/man8/fenced.8*

%files fence-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfence.so.4.0
%attr(755,root,root) %ghost %{_libdir}/libfence.so.4
%attr(755,root,root) %{_libdir}/libfenced.so.3.0
%attr(755,root,root) %ghost %{_libdir}/libfenced.so.3

%files fence-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfence.so
%attr(755,root,root) %{_libdir}/libfenced.so
%{_includedir}/libfence.h
%{_includedir}/libfenced.h
%{_pkgconfigdir}/libfence.pc
%{_pkgconfigdir}/libfenced.pc

%files fence-static
%defattr(644,root,root,755)
%{_libdir}/libfence.a
%{_libdir}/libfenced.a

%files group
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/dlm_controld
%attr(755,root,root) %{_sbindir}/group_tool
%attr(755,root,root) %{_sbindir}/groupd
%{_mandir}/man8/dlm_controld.8*
%{_mandir}/man8/group_tool.8*
%{_mandir}/man8/groupd.8*

%files rgmanager
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/cpglockd
%attr(754,root,root) /etc/rc.d/init.d/rgmanager
%attr(755,root,root) %{_sbindir}/clubufflush
%attr(755,root,root) %{_sbindir}/clufindhostname
%attr(755,root,root) %{_sbindir}/clulog
%attr(755,root,root) %{_sbindir}/clunfslock
%attr(755,root,root) %{_sbindir}/clurgmgrd
%attr(755,root,root) %{_sbindir}/clustat
%attr(755,root,root) %{_sbindir}/clusvcadm
%attr(755,root,root) %{_sbindir}/cpglockd
%attr(755,root,root) %{_sbindir}/cpglockdump
%attr(755,root,root) %{_sbindir}/rg_test
%attr(755,root,root) %{_sbindir}/rgmanager
%{_mandir}/man8/clubufflush.8*
%{_mandir}/man8/clufindhostname.8*
%{_mandir}/man8/clulog.8*
%{_mandir}/man8/clurgmgrd.8*
%{_mandir}/man8/clustat.8*
%{_mandir}/man8/clusvcadm.8*
%{_mandir}/man8/cpglockd.8*
%{_mandir}/man8/rgmanager.8*
