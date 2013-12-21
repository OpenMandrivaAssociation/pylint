Summary: 	Extensible Python source code checker
Name:		pylint
Version:	1.0.0
Release:	1
Source0:	http://download.logilab.org/pub/pylint/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Python
Url:		http://www.logilab.org/project/pylint
Requires:	python-logilab-common >= 0.53.0
Requires:	python-logilab-astng >= 0.21.1
Requires:	tkinter
BuildArch:	noarch
BuildRequires:	python-distribute
BuildRequires:  python-devel

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
%__python setup.py install --root=%{buildroot}

%__lzma -z man/pylint.1
%__install -d -m 755 %{buildroot}%{_mandir}/man1
%__install -m 644 man/pylint.1.lzma %{buildroot}%{_mandir}/man1

%__install -d -m 755 %{buildroot}%{_sysconfdir}
%__install -m 644 ./examples/pylintrc %{buildroot}%{_sysconfdir}

%__install -d -m 755 %{buildroot}%{_sysconfdir}/emacs/site-start.d
%__install -m 644 ./elisp/pylint.el %{buildroot}%{_sysconfdir}/emacs/site-start.d/

%files
%doc README COPYING ChangeLog  examples/
%_bindir/*
%config(noreplace) %_sysconfdir/pylintrc
%_sysconfdir/emacs/site-start.d/pylint.el
%_mandir/man1/pylint.*
%py_puresitedir/pylint/*
%py_puresitedir/*.egg-info


%changelog
* Thu Jan 12 2012 Lev Givon <lev@mandriva.org> 0.25.1-1mdv2012.0
+ Revision: 760535
- Update to 0.25.1.

* Wed Oct 26 2011 Andrey Bondrov <abondrov@mandriva.org> 0.25.0-1
+ Revision: 707362
- New version 0.25.0

* Fri Aug 05 2011 Lev Givon <lev@mandriva.org> 0.24.0-1
+ Revision: 693332
- Update to 0.24.0.

* Thu Feb 17 2011 Lev Givon <lev@mandriva.org> 0.23.0-1
+ Revision: 638259
- Update to 0.23.0.

* Tue Nov 30 2010 Lev Givon <lev@mandriva.org> 0.22.0-1mdv2011.0
+ Revision: 603779
- Update to 0.22.0.

* Mon Nov 08 2010 Lev Givon <lev@mandriva.org> 0.21.4-1mdv2011.0
+ Revision: 595120
- Update to 0.21.4.
- Update to 0.21.3.

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.21.2-2mdv2011.0
+ Revision: 592425
- rebuild for python 2.7

* Mon Aug 30 2010 Lev Givon <lev@mandriva.org> 0.21.2-1mdv2011.0
+ Revision: 574479
- Update to 0.21.2.

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 0.21.1-1mdv2011.0
+ Revision: 562815
- Update to 0.21.1.

* Fri May 28 2010 Lev Givon <lev@mandriva.org> 0.21.0-1mdv2011.0
+ Revision: 546544
- Update to 0.21.0.

* Sun Apr 04 2010 Lev Givon <lev@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 531444
- Update to 0.20.0.

* Sun Dec 20 2009 Lev Givon <lev@mandriva.org> 0.19.0-1mdv2010.1
+ Revision: 480426
- Update to 0.19.0.

* Thu Nov 12 2009 Lev Givon <lev@mandriva.org> 0.18.1-1mdv2010.1
+ Revision: 465477
- Update to 0.18.1.

* Wed May 06 2009 Lev Givon <lev@mandriva.org> 0.18.0-3mdv2010.0
+ Revision: 372589
- Make package own %%py_sitedir/pylint.

* Sun Apr 19 2009 Lev Givon <lev@mandriva.org> 0.18.0-2mdv2009.1
+ Revision: 368051
- Bump release.

* Sun Apr 19 2009 Lev Givon <lev@mandriva.org> 0.18.0-1mdv2009.1
+ Revision: 368022
- Update to 0.18.0.

* Tue Feb 17 2009 Jérôme Soyer <saispo@mandriva.org> 0.16.0-1mdv2009.1
+ Revision: 341497
- New upstream release

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.15.2-2mdv2009.1
+ Revision: 325999
- rebuild

* Tue Nov 04 2008 Lev Givon <lev@mandriva.org> 0.15.2-1mdv2009.1
+ Revision: 299695
- Update to 0.15.2.

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.14.0-4mdv2009.0
+ Revision: 259424
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.14.0-3mdv2009.0
+ Revision: 247284
- rebuild

* Tue Feb 19 2008 Lev Givon <lev@mandriva.org> 0.14.0-1mdv2008.1
+ Revision: 172408
- Update to 0.14.0.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 09 2007 Lev Givon <lev@mandriva.org> 0.13.2-1mdv2008.0
+ Revision: 50548
- Update to 0.13.2.

* Wed Apr 18 2007 Lev Givon <lev@mandriva.org> 0.13.1-1mdv2008.0
+ Revision: 14826
- Import pylint



* Wed Mar 21 2007 Lev Givon <lev@mandriva.org> 0.13.1-1mdv2007.0
- Initial Mandriva package.




