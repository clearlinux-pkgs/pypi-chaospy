#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-chaospy
Version  : 4.3.7
Release  : 7
URL      : https://files.pythonhosted.org/packages/60/96/5d6d6d0a4832c422a9d12c97940824ed0f3080cc24baf900e476fab5a19d/chaospy-4.3.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/60/96/5d6d6d0a4832c422a9d12c97940824ed0f3080cc24baf900e476fab5a19d/chaospy-4.3.7.tar.gz
Summary  : "Numerical tool for perfroming uncertainty quantification"
Group    : Development/Tools
License  : MIT
Requires: pypi-chaospy-license = %{version}-%{release}
Requires: pypi-chaospy-python = %{version}-%{release}
Requires: pypi-chaospy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(chaospy)
BuildRequires : pypi(matplotlib)
BuildRequires : pypi(numpoly)
BuildRequires : pypi(numpy)
BuildRequires : pypi(scipy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(setuptools_scm_git_archive)

%description
.. image:: https://github.com/jonathf/chaospy/raw/master/docs/_static/chaospy_logo.svg
:height: 200 px
:width: 200 px
:align: center

%package license
Summary: license components for the pypi-chaospy package.
Group: Default

%description license
license components for the pypi-chaospy package.


%package python
Summary: python components for the pypi-chaospy package.
Group: Default
Requires: pypi-chaospy-python3 = %{version}-%{release}

%description python
python components for the pypi-chaospy package.


%package python3
Summary: python3 components for the pypi-chaospy package.
Group: Default
Requires: python3-core
Provides: pypi(chaospy)
Requires: pypi(chaospy)
Requires: pypi(matplotlib)
Requires: pypi(numpoly)
Requires: pypi(numpy)
Requires: pypi(scipy)

%description python3
python3 components for the pypi-chaospy package.


%prep
%setup -q -n chaospy-4.3.7
cd %{_builddir}/chaospy-4.3.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649726255
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-chaospy
cp %{_builddir}/chaospy-4.3.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-chaospy/8eed8b719245ab4840f724d06277670b21ea38ba
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-chaospy/8eed8b719245ab4840f724d06277670b21ea38ba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
