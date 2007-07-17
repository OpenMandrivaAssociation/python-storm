%define oname storm
%define name python-%{oname}
%define version 0.9
%define release %mkrel 1

Summary: Storm is an Object Relational Mapper for Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://launchpad.net/storm/trunk/0.9/+download/%{oname}-%{version}.tar.bz2
License: GPL
URL: http://storm.canonical.com/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
BuildRequires: libpython-devel
Requires:  python >= 2.4
Requires: python-psycopg2 python-sqlite2

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc TODO LICENSE tests/tutorial.txt tests/
%{py_puresitedir}/*
