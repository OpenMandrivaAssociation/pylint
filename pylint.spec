%undefine _debugsource_packages

Summary: 	Extensible Python source code checker
Name:		pylint
Version:	3.2.7
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pylint/pylint-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Python
Url:		https://pylint.org/
Requires:	tkinter
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)

%patchlist
https://github.com/pylint-dev/pylint/pull/9851.patch

%description
PyLint is an extensible tool for checking whether Python
code satisfies a specified coding standard. It is similar to PyChecker
insofar that it can perform nearly all tests supported by
PyChecker. Pylint, however, can check many other things such as
line-code length, variable name adherence to a coding standard,
whether interfaces defined in code are actually implemented, and much
more. One can easily extend PyLint with plugins.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%__install -d -m 755 %{buildroot}%{_sysconfdir}
%__install -m 644 ./examples/pylintrc %{buildroot}%{_sysconfdir}

%files
%doc examples/
%_bindir/*
%config(noreplace) %_sysconfdir/pylintrc
%py_puresitedir/pylint/*
%py_puresitedir/*.*-info
