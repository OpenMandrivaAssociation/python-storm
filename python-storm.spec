%define oname	storm

Summary:	Object Relational Mapper for Python
Name:		python-%{oname}
Version:	0.18
Release:	2
Source0:	https://launchpad.net/storm/trunk/%{version}/+download/%{oname}-%{version}.tar.bz2
License:	GPLv2
URL:		http://storm.canonical.com/
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	python-devel
Requires:	python
Requires:	python-psycopg2
Requires:	python-sqlite2

%description
Storm is an object-relation mapper (ORM) for the Python language. It allows
rows from a relational database to be seen as objects in an object-oriented
language like Python.

- Storm lets you efficiently access and update large datasets by allowing you
  to formulate complex queries spanning multiple tables using Python.

- Storm allows you to fallback to SQL if needed (or if you just prefer),
  allowing you to mix "old school" code and ORM code

%prep
%setup -q -n %{oname}-%{version}

%build

%install
install -d %{buildroot}%{py_puresitedir}
cp -af storm/ %{buildroot}%{py_puresitedir}

%files
%doc TODO LICENSE README tests/tutorial.txt tests/
%{py_puresitedir}/*


%changelog
* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2011.0
+ Revision: 603076
- update to new version 0.18

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 0.17-2mdv2011.0
+ Revision: 590595
- rebuild for python 2.7

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2011.0
+ Revision: 587731
- update to new version 0.17

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.16.0-1mdv2010.1
+ Revision: 515958
- update to 0.16.0

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.13-3mdv2010.0
+ Revision: 442498
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.13-2mdv2009.1
+ Revision: 323372
- rebuild

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.13-1mdv2009.0
+ Revision: 280473
- New release

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.11-5mdv2009.0
+ Revision: 259825
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.11-4mdv2009.0
+ Revision: 247679
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2008.1
+ Revision: 171068
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 26 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.11-1mdv2008.1
+ Revision: 102257
- new version 0.11

* Tue Jul 17 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.9-1mdv2008.0
+ Revision: 53014
- Import python-storm

