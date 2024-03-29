#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-chaospy
Version  : 4.3.13
Release  : 26
URL      : https://files.pythonhosted.org/packages/1c/84/e2ed2ad3d1098368b89083663f0ecdac7fe397803fd33820926c66264ade/chaospy-4.3.13.tar.gz
Source0  : https://files.pythonhosted.org/packages/1c/84/e2ed2ad3d1098368b89083663f0ecdac7fe397803fd33820926c66264ade/chaospy-4.3.13.tar.gz
Summary  : Numerical tool for performing uncertainty quantification
Group    : Development/Tools
License  : MIT
Requires: pypi-chaospy-license = %{version}-%{release}
Requires: pypi-chaospy-python = %{version}-%{release}
Requires: pypi-chaospy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: pypi(importlib_metadata)
Requires: pypi(numpoly)
Requires: pypi(numpy)
Requires: pypi(scipy)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-chaospy package.


%prep
%setup -q -n chaospy-4.3.13
cd %{_builddir}/chaospy-4.3.13
pushd ..
cp -a chaospy-4.3.13 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685978352
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-chaospy
cp %{_builddir}/chaospy-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-chaospy/8eed8b719245ab4840f724d06277670b21ea38ba || :
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-chaospy/8eed8b719245ab4840f724d06277670b21ea38ba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
