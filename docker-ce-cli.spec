Name: docker-ce-cli
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Docker CLI (loong64)
License: Apache-2.0
URL: https://github.com/kubernetes-loong64/cli-loong64
BugURL: https://github.com/kubernetes-loong64/cli-loong64/issues
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>
%define ref_name release-loong64-v%{version}
Source0: https://github.com/kubernetes-loong64/cli-loong64/archive/refs/tags/%{ref_name}.tar.gz

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

%files
/usr/bin/docker
/usr/share/bash-completion/completions/docker
/usr/share/fish/vendor_completions.d/docker.fish
/usr/share/zsh/site-functions/_docker

%changelog
#
