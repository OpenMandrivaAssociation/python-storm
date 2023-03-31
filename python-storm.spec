%define oname	storm

Summary:	Object Relational Mapper for Python

Name:		python2-%{oname}
Version:	0.25
Release:	5
Group:		Development/Python
License:	GPLv2
Url:		http://storm.canonical.com/
Source0:	https://files.pythonhosted.org/packages/c0/f6/4b30697087af83edbc25584938fff7de08645ea6c2addf22420b4a1c70c9/storm-%{version}.tar.gz
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
#{py_platsitedir}/*
%{python_sitearch}/storm-%{version}-py*.*.egg-info
%{python_sitearch}/storm/
