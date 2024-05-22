Summary: 	Extensible Python source code checker
Name:		pylint
Version:	3.2.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/0c/4c/b561478a1ccb91e9b02965cb999d2281894d43e68c0bf3777d023af15f11/pylint-3.2.2.tar.gz
License:	GPLv2+
Group:		Development/Python
Url:		http://pylint.org/
Requires:	tkinter
BuildArch:	noarch
BuildRequires:	python(pip)

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
