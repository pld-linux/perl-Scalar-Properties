%include	/usr/lib/rpm/macros.perl
%define	pdir	Scalar
%define	pnam	Properties
Summary:	Scalar::Properties -- run-time properties on scalar variables.
Summary(pl):	Scalar::Properties -- w�a�ciwo�ci skalar�w w trakcie wykonywania.
Name:		perl-%{pdir}-%{pnam}
Version:	0.10
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scalar::Properties attempts to make Perl more object-oriented by taking
an idea from Ruby: Everything you manipulate is an object, and the
results of those manipulations are objects themselves.

%description -l pl
Scalar::Properties pr�buje doda� do Perla nieco wi�cej obiektowo�ci
poprzez zaimplementowanie pomys�u z Ruby: wszystko, na czym operujesz,
jest obiektem; tak samo, jak rezultat tych manipulacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
