#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_cache
Version  : 0.5.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/b3/07/feded9f29b7ae087e5b49b6f93f74c59f444300c2b226801e8417ae83a17/jupyter-cache-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b3/07/feded9f29b7ae087e5b49b6f93f74c59f444300c2b226801e8417ae83a17/jupyter-cache-0.5.0.tar.gz
Summary  : A defined interface for working with a cache of jupyter notebooks.
Group    : Development/Tools
License  : MIT
Requires: pypi-jupyter_cache-bin = %{version}-%{release}
Requires: pypi-jupyter_cache-license = %{version}-%{release}
Requires: pypi-jupyter_cache-python = %{version}-%{release}
Requires: pypi-jupyter_cache-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(attrs)
BuildRequires : pypi(click)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(nbclient)
BuildRequires : pypi(nbformat)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(sqlalchemy)
BuildRequires : pypi(tabulate)
BuildRequires : pypi(wheel)

%description
# jupyter-cache
[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]

%package bin
Summary: bin components for the pypi-jupyter_cache package.
Group: Binaries
Requires: pypi-jupyter_cache-license = %{version}-%{release}

%description bin
bin components for the pypi-jupyter_cache package.


%package license
Summary: license components for the pypi-jupyter_cache package.
Group: Default

%description license
license components for the pypi-jupyter_cache package.


%package python
Summary: python components for the pypi-jupyter_cache package.
Group: Default
Requires: pypi-jupyter_cache-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_cache package.


%package python3
Summary: python3 components for the pypi-jupyter_cache package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_cache)
Requires: pypi(attrs)
Requires: pypi(click)
Requires: pypi(importlib_metadata)
Requires: pypi(nbclient)
Requires: pypi(nbformat)
Requires: pypi(pyyaml)
Requires: pypi(sqlalchemy)
Requires: pypi(tabulate)

%description python3
python3 components for the pypi-jupyter_cache package.


%prep
%setup -q -n jupyter-cache-0.5.0
cd %{_builddir}/jupyter-cache-0.5.0
pushd ..
cp -a jupyter-cache-0.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656397108
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_cache
cp %{_builddir}/jupyter-cache-0.5.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyter_cache/ab5a711cce75e49bdbd08bbcb728262e30580e5d
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jcache

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_cache/ab5a711cce75e49bdbd08bbcb728262e30580e5d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
