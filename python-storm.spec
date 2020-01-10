%define oname	storm

Summary:	Object Relational Mapper for Python

Name:		python2-%{oname}
Version:	0.20
Release:	7
Group:		Development/Python
License:	GPLv2
Url:		http://storm.canonical.com/
Source0:	https://launchpad.net/storm/trunk/0.20/+download/storm-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
Patch1:		storm-0.20-exclude-tests.patch
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
Requires:	python2
Requires:	python2-psycopg2
%rename		python-%{oname}

%description
Storm is an object-relation mapper (ORM) for the Python language. It allows
rows from a relational database to be seen as objects in an object-oriented
language like Python.

- Storm lets you efficiently access and update large datasets by allowing you
  to formulate complex queries spanning multiple tables using Python.

- Storm allows you to fallback to SQL if needed (or if you just prefer),
  allowing you to mix "old school" code and ORM code

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1

%build
%__python2 setup.py build

%install
%__python2 setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc TODO LICENSE README tests/tutorial.txt tests/
%{py2_platsitedir}/*


