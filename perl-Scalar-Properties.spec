#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Scalar
%define		pnam	Properties
Summary:	Scalar::Properties - run-time properties on scalar variables
Summary(pl):	Scalar::Properties - w³a¶ciwo¶ci skalarów w trakcie wykonywania
Name:		perl-Scalar-Properties
Version:	0.12
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	19aefcff9043f8645d42f0bbe8c39d18
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scalar::Properties attempts to make Perl more object-oriented by
taking an idea from Ruby: Everything you manipulate is an object, and
the results of those manipulations are objects themselves.

%description -l pl
Scalar::Properties próbuje dodaæ do Perla nieco wiêcej obiektowo¶ci
poprzez zaimplementowanie pomys³u z Ruby: wszystko, na czym operujesz,
jest obiektem; tak samo, jak rezultat tych manipulacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%dir %{perl_vendorlib}/Scalar
%{perl_vendorlib}/Scalar/*.pm
%{_mandir}/man3/*
