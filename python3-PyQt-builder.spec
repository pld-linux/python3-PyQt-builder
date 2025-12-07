%define		pypi_name	pyqt_builder
Summary:	The PEP 517 compliant PyQt build system
Summary(pl.UTF-8):	System budowania PyQt zgodny z PEP 517
Name:		python3-PyQt-builder
Version:	1.19.1
Release:	1
License:	BSD
#Source0Download: https://pypi.org/simple/PyQt-builder
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt-builder/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	17e3748d53cbf6f07484b0eec27a020e
URL:		https://www.riverbankcomputing.com/software/pyqt/
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	python3-installer
BuildRequires:	python3-setuptools >= 1:77
BuildRequires:	python3-setuptools_scm >= 8
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and
projects that extend PyQt. It extends the sip build system and uses
Qt's qmake to perform the actual compilation and installation of
extension modules. Projects that use PyQt-builder provide an
appropriate pyproject.toml file and an optional project.py.

%description -l pl.UTF-8
PyQt-builder to zgodny z PEP 517 system budowania dla PyQt oraz
projektów rozszerzających PyQt. Rozszerza system budowania sip i
wykorzystuje program qmake z Qt, aby wykonać właściwą kompilację i
instalację modułów rozszerzeń. Projekty wykorzystujące pakiet
PyQt-builder dostarczają odpowiedni plik pyproject.toml oraz
opcjonalnie project.py.

%prep
%setup -q -n %{pypi_name}-%{version}

%{__rm} -r PyQt_builder.egg-info

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT
%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyqt-bundle
%attr(755,root,root) %{_bindir}/pyqt-qt-wheel
%{py3_sitescriptdir}/pyqtbuild
%{py3_sitescriptdir}/pyqt_builder-%{version}.dist-info
