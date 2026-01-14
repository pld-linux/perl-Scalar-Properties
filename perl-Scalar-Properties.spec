#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Scalar
%define		pnam	Properties
Summary:	Scalar::Properties - run-time properties on scalar variables
Summary(pl.UTF-8):	Scalar::Properties - właściwości skalarów w trakcie wykonywania
Name:		perl-Scalar-Properties
Version:	1.100860
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Scalar/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f144203205f0a60026b82f32e51c595
URL:		http://search.cpan.org/dist/Scalar-Properties/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.11
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scalar::Properties attempts to make Perl more object-oriented by
taking an idea from Ruby: Everything you manipulate is an object, and
the results of those manipulations are objects themselves.

%description -l pl.UTF-8
Scalar::Properties próbuje dodać do Perla nieco więcej obiektowości
poprzez zaimplementowanie pomysłu z Ruby: wszystko, na czym operujesz,
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
%doc Changes
%dir %{perl_vendorlib}/Scalar
%{perl_vendorlib}/Scalar/Properties.pm
%{_mandir}/man3/Scalar::Properties.3pm*
