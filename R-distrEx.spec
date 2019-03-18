#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-distrEx
Version  : 2.7.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/distrEx_2.7.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/distrEx_2.7.0.tar.gz
Summary  : Extensions of Package 'distr'
Group    : Development/Tools
License  : LGPL-3.0
Requires: R-distrEx-lib = %{version}-%{release}
BuildRequires : R-distr
BuildRequires : R-robustbase
BuildRequires : R-startupmsg
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-distrEx package.
Group: Libraries

%description lib
lib components for the R-distrEx package.


%prep
%setup -q -c -n distrEx

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552905134

%install
export SOURCE_DATE_EPOCH=1552905134
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library distrEx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library distrEx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library distrEx
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  distrEx || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/distrEx/CITATION
/usr/lib64/R/library/distrEx/DESCRIPTION
/usr/lib64/R/library/distrEx/INDEX
/usr/lib64/R/library/distrEx/MASKING
/usr/lib64/R/library/distrEx/MOVED
/usr/lib64/R/library/distrEx/Meta/Rd.rds
/usr/lib64/R/library/distrEx/Meta/demo.rds
/usr/lib64/R/library/distrEx/Meta/features.rds
/usr/lib64/R/library/distrEx/Meta/hsearch.rds
/usr/lib64/R/library/distrEx/Meta/links.rds
/usr/lib64/R/library/distrEx/Meta/nsInfo.rds
/usr/lib64/R/library/distrEx/Meta/package.rds
/usr/lib64/R/library/distrEx/NAMESPACE
/usr/lib64/R/library/distrEx/NEWS
/usr/lib64/R/library/distrEx/R/distrEx
/usr/lib64/R/library/distrEx/R/distrEx.rdb
/usr/lib64/R/library/distrEx/R/distrEx.rdx
/usr/lib64/R/library/distrEx/R/sysdata.rdb
/usr/lib64/R/library/distrEx/R/sysdata.rdx
/usr/lib64/R/library/distrEx/TOBEDONE
/usr/lib64/R/library/distrEx/demo/Prognose.R
/usr/lib64/R/library/distrEx/demo/distrExUse.R
/usr/lib64/R/library/distrEx/help/AnIndex
/usr/lib64/R/library/distrEx/help/aliases.rds
/usr/lib64/R/library/distrEx/help/distrEx.rdb
/usr/lib64/R/library/distrEx/help/distrEx.rdx
/usr/lib64/R/library/distrEx/help/paths.rds
/usr/lib64/R/library/distrEx/html/00Index.html
/usr/lib64/R/library/distrEx/html/R.css
/usr/lib64/R/library/distrEx/tests/Examples/distrEx-Ex_i386.Rout.save
/usr/lib64/R/library/distrEx/tests/Examples/distrEx-Ex_x64.Rout.save
/usr/lib64/R/library/distrEx/tests/Tests.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/distrEx/libs/distrEx.so
/usr/lib64/R/library/distrEx/libs/distrEx.so.avx2