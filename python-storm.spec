%define oname storm

Name:				python-%{oname}
Summary:		Object Relational Mapper for the Python programming language
Version:		1.2
Release:		1
Group:			Development/Python
License:		LGPL-2.1
URL:				https://launchpad.net/storm/
Source0:		https://files.pythonhosted.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz

BuildSystem:		python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(packaging)

Obsoletes: python2-%{oname} < 1.0

%description
Storm is an object-relation mapper (ORM) for the Python language. It allows
rows from a relational database to be seen as objects in an object-oriented
language like Python.

- Storm lets you efficiently access and update large datasets by allowing you
  to formulate complex queries spanning multiple tables using Python.

- Storm allows you to fallback to SQL if needed (or if you just prefer),
  allowing you to mix "old school" code and ORM code

Documentation: https://storm-orm.readthedocs.io

%prep
%autosetup -n storm-1.2 -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%build
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%py_install

%files
%doc README
%license LICENSE
%{python_sitearch}/storm-%{version}-py%{pyver}.egg-info
%{python_sitearch}/storm/
