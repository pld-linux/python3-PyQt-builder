%define		pypi_name	PyQt-builder
Summary:	The PEP 517 compliant PyQt build system
Name:		python3-PyQt-builder
Version:	1.15.1
Release:	1
License:	BSD
#Source0Download: https://pypi.org/simple/PyQt-builder
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt-builder/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	bbb1ab98658f0f8d7f7d612eb6499376
URL:		https://www.riverbankcomputing.com/software/pyqt/
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and
projects that extend PyQt. It extends the sip build system and uses
Qt's qmake to perform the actual compilation and installation of
extension modules.Projects that use PyQt- builder provide an
appropriate pyproject.toml file and an optional project.py.

%prep
%setup -q -n %{pypi_name}-%{version}

%{__rm} -r PyQt_builder.egg-info

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/pyqtbuild/bundle/dlls

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyqt-bundle
%attr(755,root,root) %{_bindir}/pyqt-qt-wheel
%{py3_sitescriptdir}/pyqtbuild
%{py3_sitescriptdir}/PyQt_builder-%{version}-py*.egg-info
