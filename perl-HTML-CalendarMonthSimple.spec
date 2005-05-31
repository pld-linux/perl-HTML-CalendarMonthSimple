#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	CalendarMonthSimple
Summary:	HTML::CalendarMonthSimple - generating HTML calendars
Summary(pl):	HTML::CalendarMonthSimple - generowanie kalendarzy w HTML
Name:		perl-HTML-CalendarMonthSimple
Version:	1.25
Release:	1
License:	free (see README)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f9fcad2627890cc11ab5c3cd3c986cf
%if %{with tests}
BuildRequires:	perl-Date-Calc
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::CalendarMonthSimple is a Perl module for generating,
manipulating, and printing a HTML calendar grid for a specified month.
It is intended as a faster and easier-to-use alternative to
HTML::CalendarMonth.

%description -l pl
HTML::CalendarMonthSimple to modu³ Perla do generowania, obrabiania i
drukowania tabelek HTML z kalendarzem dla okre¶lonego miesi±ca.
Powinien byæ szybsz± i ³atwiejsz± w u¿yciu alternatyw± dla
HTML::CalendarMonth.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/HTML/CalendarMonthSimple.pm
%{_mandir}/man3/*
