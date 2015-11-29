%define 	module	django-profiles
Summary:	A fairly simple user-profile management application for Django
Name:		python-%{module}
Version:	0.2
Release:	1
License:	MIT
Group:		Libraries/Python
# wget https://bitbucket.org/ubernostrum/django-profiles/get/default.tar.bz2 -O django-profiles.tar.bz2
Source0:	django-profiles.tar.bz2
# Source0-md5:	5a94560b95f64dc3b786701647876484
URL:		https://bitbucket.org/ubernostrum/django-profiles/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-django >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fairly simple user-profile management application for Django,
designed to make the management of site-specific user profiles as
painless as possible. It requires a functional installation of Django
1.0 or newer and provides a useful complement to
`django-registration`, but has no other dependencies.

%prep
%setup -q -n ubernostrum-django-profiles-default

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt INSTALL.txt README.txt docs/*
%dir %{py_sitescriptdir}/profiles
%{py_sitescriptdir}/profiles/*.py[co]
%{py_sitescriptdir}/django_profiles-%{version}-py*.egg-info
