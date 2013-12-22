Summary:	ITS-based XML translation tool
Name:		itstool
Version:	2.0.2
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2
# Source0-md5:	d472d877a7bc49899a73d442085b2f93
URL:		http://itstool.org/
Requires:	python-libxml2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ITS Tool allows you to translate XML documents with PO files, using
rules from the W3C Internationalization Tag Set (ITS) to determine
what to translate and how to separate it into PO file messages.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_bindir}/itstool
%{_datadir}/itstool
%{_mandir}/man1/itstool.1*

