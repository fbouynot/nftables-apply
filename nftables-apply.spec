Name:           nftables-apply
Version:        1.2.8
Release:        1%{?dist}
Summary:        A safer way to use nftables remotely

License:        GPLv3
URL:            https://github.com/fbouynot/nftables-apply
Source0:        https://github.com/fbouynot/nftables-apply/archive/refs/heads/main.zip

Requires:       bash nftables coreutils systemd sed

%description
A program to apply nftables rules, and automatically rollback if your new ruleset disconnects you

%global debug_package %{nil}
%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/ $RPM_BUILD_ROOT%{_datadir}/license/%{name}/
cp %{name} $RPM_BUILD_ROOT%{_bindir}
cp LICENSE $RPM_BUILD_ROOT%{_datadir}/license/%{name}/
cp README.md $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/README

%files
%license %{_datadir}/license/%{name}/LICENSE
%doc %{_datadir}/doc/%{name}/README
%{_bindir}/%{name}

%changelog
* Thu Jul 31 2025 Félix Bouynot <felix.bouynot@setenforce.one>
- First version being packaged
