Name:           nethserver-docker
Version: 1.0.10
Release: 1%{?dist}
Summary:        NethServer Docker configuration

License:        GPLv3+
URL: %{url_prefix}/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  nethserver-devtools
Requires:       docker-ce
Requires: nethserver-httpd-admin-service

%description
NethServer configuration for Docker CE

%prep
%setup

%build
%{makedocs}
perl createlinks


%install
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist
mkdir -p %{buildroot}%{_nsstatedir}/portainer
mkdir -p ${RPM_BUILD_ROOT}/var/log/docker


%files -f %{name}-%{version}-filelist
%doc COPYING
%doc README.rst
%config(noreplace) %attr (0644,root,root) %{_sysconfdir}/docker/docker.conf
%attr(0750,root,root) %dir /var/log/docker
%dir %{_nseventsdir}/%{name}-update
%dir %{_nsstatedir}/portainer

%changelog
* Thu Jan 28 2021 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.10-1
- Merge pull request #25 from stephdl/RequiresNethserver-httpd-admin-service
- Requires nethserver-httpd-admin-service

* Sat Nov 28 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.9-1
- Merge pull request #23 from stephdl:fixShorewall
- Restart docker with the event firewall-adjust
- Restart docker when systemd restart shorewall

* Mon Oct 26 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.8-1
- Merge pull request #22 from stephdl/FixFreeDevice
- Fix static path to /dev/sdb

* Wed Jul 01 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.7-1
- Merge pull request #21 from stephdl/EnableRepoForSubscription
- Enable docker repository for subscription
- Debug command of aeria network

* Mon Jun 22 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.6-1
  - Merge pull request #20 from stephdl/bridgeCannotBeShared
  - The bridge cannot be shared among aeria and macvlan

* Tue Jun 16 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.5-1
- Merge pull request #15 from stephdl/portainerEndpointLost
- Create portainer after docker restart
- After docker restart, portainer is restarted

* Sat Jun 13 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.4-1
- Docker must be up before to restart macvlan container

* Sat Jun 13 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.3-1
- Merge pull request #12 from stephdl/macvlan
- Network macvlan for containers

* Sat Jun 13 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.2-1
  - Merge pull request #13 from stephdl/docker0
  - Merge pull request #14 from stephdl/disableUpdate
  - Disable by default docker-ce-stable
  - Enable default bridge docker0

* Sat May 16 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.1-1 
  - Merge pull request #11 from stephdl/fixRuletemplate
  - Rule template must output a comment

* Fri May 15 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-1
- First stable release to NethForge
- Code from mrmarkuz & stephdl

* Mon Sep 10 2018 Davide Principi <davide.principi@nethesis.it> - 0.0.0
- Initial version
