Name: docker-ce-cli
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Docker CLI (loong64)
License: Apache-2.0
URL: https://github.com/kubernetes-loong64/cli-loong64
BugURL: https://github.com/kubernetes-loong64/cli-loong64/issues
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>

# Disable strip and build-id links for cross-compiled loongarch64 binary
%global _build_id_links none
%define __strip /bin/true

%description
Docker CLI binary for the loong64 (LoongArch) architecture.

%prep
# This example has no source, so nothing here

%build
# Generate the script directly

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 docker %{buildroot}/usr/bin/docker

mkdir -p %{buildroot}/usr/share/bash-completion/completions/
install -m 644 completions/docker.bash %{buildroot}/usr/share/bash-completion/completions/docker

mkdir -p %{buildroot}/usr/share/fish/vendor_completions.d/
install -m 644 completions/docker.fish %{buildroot}/usr/share/fish/vendor_completions.d/docker.fish

mkdir -p %{buildroot}/usr/share/zsh/site-functions/
install -m 644 completions/_docker.zsh %{buildroot}/usr/share/zsh/site-functions/_docker

mkdir -p %{buildroot}/usr/share/man/man1/
install -m 644 man/docker.1 %{buildroot}/usr/share/man/man1/docker.1

mkdir -p %{buildroot}/usr/share/licenses/%{name}/
install -m 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

%files
%license /usr/share/licenses/%{name}/LICENSE
/usr/bin/docker
/usr/share/man/man1/docker.1*
/usr/share/bash-completion/completions/docker
/usr/share/fish/vendor_completions.d/docker.fish
/usr/share/zsh/site-functions/_docker

%changelog
