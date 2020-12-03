%define oname	storm

Summary:	Object Relational Mapper for Python

Name:		python2-%{oname}
Version:	0.24
Release:	2
Group:		Development/Python
License:	GPLv2
Url:		http://storm.canonical.com/
Source0:	https://files.pythonhosted.org/packages/23/1e/5376de4541fede4ceb0598b103f89a85a16f9fa7da06548cdf5455e340f2/storm-0.24.tar.gz
Source100:	%{name}.rpmlintrc
Patch1:		storm-0.20-exclude-tests.patch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
Requires:	python-psycopg2
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
%py_build

%install
%py_install

%files
%doc TODO LICENSE README
%{py_platsitedir}/*
