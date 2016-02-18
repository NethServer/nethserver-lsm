Summary: NethServer Link Status Monitor configuration
Name: nethserver-lsm
Version: 1.1.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-base
Requires: lsm >= 0.190

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
NethServer LSM (Link Status Monitor) configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Thu Feb 18 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- Latency monitoring in multiwan - Enhancement #3351

* Wed Nov 11 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- MultiWAN: remove static routes for checkip - Enhancement #3289 [NethServer]

* Thu Apr 09 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- LSM: configuration tuning - Enhancement #3098 [NethServer]

* Thu Oct 02 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- Handle nethserver-firewall-base uninstallation - Enhancement #2873 [NethServer]

* Wed Aug 20 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- Link monitor daemon - Feature #2333 [NethServer]
- Firewall-base: add support for multi-wan - Feature #2332 [NethServer]

