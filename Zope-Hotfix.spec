%define 	zope_subname	Hotfix
Summary:	This hotfix product fixes a security bug in Page Templates on Zope
Summary(pl):	Ta poprawka naprawia b³êdy bezpieczeñstwa w szablonach stron Zope
Name:		Zope-%{zope_subname}
Version:	050405
Release:	1
License:	ZPL 2.1
Group:		Development/Tools
Source0:	http://zope.org/Products/Zope/Hotfix-2005-04-05/%{zope_subname}-20050405/%{zope_subname}_20%{version}.tar.gz
# Source0-md5:	c91c6fa42bfcfed24826d0cd4d69419b
URL:		http://www.zope.org/Products/Zope/Hotfix-2005-04-05/announce-Hotfix_20050405/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
Obsoletes:	Zope-Hotfix = 040713
Obsoletes:	Zope-Hotfix = 040714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This hotfix product fixes a security bug on Zope.

%description -l pl
Ta poprawka naprawia b³êdy bezpieczeñstwa w Zope.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af %{zope_subname}_20050405/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/LICENSE.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}_20050405/README.txt
%{_datadir}/%{name}
