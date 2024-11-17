Name:           bitwarden-polkit-policy

Version:        1.0
Release:        %autorelease
Summary:        Bitwarden Polkit Policy
Provides:       %{name} == %{version}
Obsoletes:      %{name} < %{version}

License:        GPL-3.0
URL:            https://github.com/bitwarden/clients/blob/main/apps/desktop/src/key-management/biometrics/biometric.unix.main.ts
Source0:        
ExcludeArch:    s390 s390x

%description
%{name} installs Bitwarden Polkit Policy into /usr/share/polkit-1/actions which is restricted for immutable distros such as Fedora Kinoite.

%prep
%setup -q -n %{name}

%install
install -p -d -o root -g root -m 0755 %{buildroot}%{_datadir}/polkit-1/actions
install -p -o root -g root -m 0644 com.bitwarden.Bitwarden.policy %{buildroot}%{_datadir}/polkit-1/actions/com.bitwarden.Bitwarden.policy
chcon system_u:object_r:usr_t:s0 %{buildroot}%{_datadir}/polkit-1/actions/com.bitwarden.Bitwarden.policy

%files
%defattr(0644, root, root, 0755)
%{_datadir}/polkit-1/actions/com.bitwarden.Bitwarden.policy

%changelog
* Sun Nov 17 2024 Quan Trinh <qt.quantrinh@zohomail.com> 1.0-1
- Initial
