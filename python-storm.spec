%define oname	storm

Summary:	Object Relational Mapper for Python
Name:		python-%{oname}
Version:	0.19
Release:	3
Group:		Development/Python
License:	GPLv2
Url:		http://storm.canonical.com/
Source0:	https://launchpad.net/storm/trunk/0.19/+download/storm-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
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
%setup -qn %{oname}-%{version}

%build

%install
install -d %{buildroot}%{py_puresitedir}
cp -af storm/ %{buildroot}%{py_puresitedir}

%files
%doc TODO LICENSE README tests/tutorial.txt tests/
%{py_puresitedir}/*

