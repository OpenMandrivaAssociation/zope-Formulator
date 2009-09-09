%define Product Formulator
%define product formulator
%define name    zope-%{Product}
%define version 1.11.3
%define release %mkrel 5

%define zope_minver     2.6
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    An extensible framework that eases the creation and validation of web forms
License:    GPL
Group:      System/Servers
URL:        http://www.infrae.com/download/Formulator
Source:     http://www.infrae.com/download/Formulator/%{version}/%{Product}-%{version}.tgz
Requires:   zope >= %{zope_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Formulator is an extensible framework that eases the creation and validation of
web forms.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
