%define name	pylint
%define version 0.14.0
%define release %mkrel 3

Summary: 	Extensible Python source code checker
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.lzma
License:	GPLv2+
Group:		Development/Python
Url:		http://www.logilab.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-logilab-common >= 0.19.0
Requires:	python-logilab-astng >= 0.16.1
Requires:	tkinter
BuildRequires:	python-devel
BuildArch:	noarch

%description 
PyLint is an extensible tool for checking whether Python
code satisfies a specified coding standard. It is similar to PyChecker
insofar that it can perform nearly all tests supported by
PyChecker. Pylint, however, can check many other things such as
line-code length, variable name adherence to a coding standard,
whether interfaces defined in code are actually implemented, and much
more. One can easily extend PyLint with plugins.

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%__lzma -z man/pylint.1
%__install -d -m 755 %{buildroot}%{_mandir}/man1
%__install -m 644 man/pylint.1.lzma %{buildroot}%{_mandir}/man1

%__install -d -m 755 %{buildroot}%{_sysconfdir}
%__install -m 644 ./examples/pylintrc %{buildroot}%{_sysconfdir}

%__install -d -m 755 %{buildroot}%{_sysconfdir}/emacs/site-start.d
%__install -m 644 ./elisp/pylint.el %{buildroot}%{_sysconfdir}/emacs/site-start.d/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog TODO doc/ examples/
%_bindir/*
%config(noreplace) %_sysconfdir/pylintrc
%_sysconfdir/emacs/site-start.d/pylint.el
%_mandir/man1/pylint.*
%py_sitedir/pylint/*
%exclude %py_sitedir/pylint/test*
%if "%py_ver" == "2.5"
%py_sitedir/*.egg-info
%endif

