#
# Conditional build:
%bcond_without	ldap		# do not include ldap support

Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Name:		cluster
Version:	3.1.8
Release:	1.aos1
License:	GPL v2
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/c/l/cluster/%{name}-%{version}.tar.bz2
# Source0-md5:	25699384c42c28bbec2998c25e7a8300
Source1:	%{name}.tmpfiles
Patch0:		%{name}-no_ldap.patch
URL:		http://sources.redhat.com/cluster/wiki
BuildRequires:	corosync-devel >= 1.4.1
BuildRequires:	libxml2-devel
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
%description -l pl.UTF-8

%package ccs
Summary:	Cluster configuration system
Summary(pl.UTF-8):	System konfiguracji klastra
Group:		Applications/System
Requires:	libxml2-progs

%description ccs
Cluster configuration system to manage the cluster config file.

%description ccs -l pl.UTF-8
System konfiguracji klastra do zarządzania jego plikiem
konfiguracyjnym.

%package ccs-devel
Summary:	Header filed for ccs library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki ccs
Group:		Applications/System
Requires:	%{name}-ccs-libs = %{version}-%{release}

%description ccs-devel
Header filed for ccs library.

%description ccs-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki ccs.

%package ccs-libs
Summary:	Cluster configuration system library
Summary(pl.UTF-8):	Biblioteka systemu konfiguracji klastra
Group:		Applications/System

%description ccs-libs
Cluster configuration system library.

%description ccs-libs -l pl.UTF-8
Biblioteka systemu konfiguracji klastra.

%package ccs-static
Summary:	Static ccs library
Summary(pl.UTF-8):	Statyczna biblioteka ccs
Group:		Applications/System

%description ccs-static
Static ccs library.

%description ccs-static -l pl.UTF-8
Statyczna biblioteka ccs.

%package cman
Summary:	Cluster infrastructure manager
Summary(pl.UTF-8):	Zarządca infrastruktury klastra
Group:		Applications/System
Requires:	%{name}-ccs = %{version}-%{release}
Requires:	%{name}-dlm = %{version}-%{release}
Requires:	%{name}-fence = %{version}-%{release}
Requires:	%{name}-group = %{version}-%{release}
Requires:	corosync
Requires:	openais
Obsoletes:	cman

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

%package cman-devel
Summary:	Header filed for cman library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki cman
Group:		Applications/System
Requires:	%{name}-cman-libs = %{version}-%{release}
Obsoletes:	cman-devel

%description cman-devel
Header filed for cman library.

%description cman-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki cman.

%package cman-libs
Summary:	Cluster infrastructure manager library
Summary(pl.UTF-8):	Biblioteka zarządcy infrastruktury klastra
Group:		Applications/System

%description cman-libs
Cluster infrastructure manager library.

%description cman-libs -l pl.UTF-8
Biblioteka zarządcy infrastruktury klastra.

%package cman-static
Summary:	Static cman library
Summary(pl.UTF-8):	Statyczna biblioteka cman
Group:		Applications/System
Obsoletes:	cman-static

%description cman-static
Static cman library.

%description cman-static -l pl.UTF-8
Statyczna biblioteka cman.

%package dlm
Summary:	Distributed lock manager
Summary(pl.UTF-8):	Zarządca rozporoszonych blokad
Group:		Applications/System
Obsoletes:	dlm

%description dlm
The DLM lock manager is a kernel-based VMS-like distributed lock
manager. It is general purpose and not specific to only GFS or CLVM.
Kernel and userspace locking API's are available.

%description dlm -l pl.UTF-8
Zarządca blokad DLM to oparty na jądrze zarządca rozproszonych blokad
w stylu VMS. Jest ogólnego przeznaczenia, przeznaczonym nie tylko dla
GFS-a czy CLVM-a. Dostępne są API blokowania w jądrze i przestrzeni
użytkownika.

%package dlm-devel
Summary:	Header filed for dlm library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki dlm
Group:		Applications/System
Requires:	%{name}-dlm-libs = %{version}-%{release}
Obsoletes:	dlm-devel

%description dlm-devel
Header filed for dlm library.

%description dlm-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki dlm.

%package dlm-libs
Summary:	Distributed lock manager library
Summary(pl.UTF-8):	Biblioteka zarządca rozporoszonych blokad
Group:		Applications/System

%description dlm-libs
Distributed lock manager library.

%description dlm-libs -l pl.UTF-8
Biblioteka zarządca rozporoszonych blokad.

%package dlm-static
Summary:	Static dlm library
Summary(pl.UTF-8):	Statyczna biblioteka dlm
Group:		Applications/System
Obsoletes:	dlm-static

%description dlm-static
Static dlm library.

%description dlm-static -l pl.UTF-8
Statyczna biblioteka dlm.

%package fence
Summary:	Cluster infrastructure I/O fencing system
Summary(pl.UTF-8):	System barier I/O infrastruktury klastra
Group:		Applications/System
Suggests:	fence-agents

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

%package fence-devel
Summary:	Header filed for fence library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki fence
Group:		Applications/System
Requires:	%{name}-fence-libs = %{version}-%{release}

%description fence-devel
Header filed for fence library.

%description fence-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki fence.

%package fence-libs
Summary:	Cluster infrastructure I/O fencing system library
Summary(pl.UTF-8):	Biblioteka systemu barier I/O infrastruktury klastra
Group:		Applications/System

%description fence-libs
Cluster infrastructure I/O fencing system library.

%description fence-libs -l pl.UTF-8
Biblioteka systemu barier I/O infrastruktury klastra.

%package fence-static
Summary:	Static fence library
Summary(pl.UTF-8):	Statyczna biblioteka fence
Group:		Applications/System

%description fence-static
Static fence library.

%description fence-static -l pl.UTF-8
Statyczna biblioteka fence.

%package group
Summary:	Cluster infrastructure
Summary(pl.UTF-8):	Infrastruktura klastra
Group:		Applications/System

%description group
Cluster infrastructure.

%description group -l pl.UTF-8
Infrastruktura klastra.

%package rgmanager
Summary:	HA resource group failover
Summary(pl.UTF-8):	Failover dla grupy zasobów wysokiej dostępności
Group:		Applications/System
Suggests:	resource-agents

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

sed -i -e 's,-Wall,%{rpmcflags} -I/usr/include/ncurses -Wall,' make/defines.mk.input

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

%clean
rm -rf $RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/lcrso/*.lcrso
%{_mandir}/man8/ccs_config_dump.*
%{_mandir}/man8/ccs_config_validate.*
%{_mandir}/man8/ccs_tool.*
%{_mandir}/man8/ccs_update_schema.*
%if %{with ldap}
%{_mandir}/man8/confdb2ldif.*
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
%{_sysconfdir}/cluster
/etc/logrotate.d/cluster
%attr(754,root,root) /etc/rc.d/init.d/cman
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
%{_mandir}/man8/checkquorum.*
%{_mandir}/man8/cman_notify.*
%{_mandir}/man8/cman_tool.*
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
/lib/udev/rules.d/51-dlm.rules
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
%{perl_vendorarch}/Cluster
%{perl_vendorarch}/auto/Cluster
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
%{_mandir}/man3/Cluster::CCS.3pm.*

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
%attr(755,root,root) %{_sbindir}/group_tool
%attr(755,root,root) %{_sbindir}/groupd
%{_mandir}/man8/dlm_controld.*
%{_mandir}/man8/group_tool.*
%{_mandir}/man8/groupd.*

%files rgmanager
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/rgmanager
%attr(755,root,root) %{_sbindir}/clubufflush
%attr(755,root,root) %{_sbindir}/clufindhostname
%attr(755,root,root) %{_sbindir}/clulog
%attr(755,root,root) %{_sbindir}/clunfslock
%attr(755,root,root) %{_sbindir}/clurgmgrd
%attr(755,root,root) %{_sbindir}/clustat
%attr(755,root,root) %{_sbindir}/clusvcadm
%attr(755,root,root) %{_sbindir}/rg_test
%attr(755,root,root) %{_sbindir}/rgmanager
%{_mandir}/man8/clubufflush.*
%{_mandir}/man8/clufindhostname.*
%{_mandir}/man8/clulog.*
%{_mandir}/man8/clurgmgrd.*
%{_mandir}/man8/clustat.*
%{_mandir}/man8/clusvcadm.*
%{_mandir}/man8/rgmanager.*
