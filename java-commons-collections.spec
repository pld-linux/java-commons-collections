Summary:	Jakarta Commons Collections
Name:		jakarta-commons-collections
Version:	2.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-collections/v%{version}/commons-collections-%{version}-src.tar.gz
URL:		http://jakarta.apache.org/
Requires:	jre
BuildRequires:	jakarta-ant
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Jakarta Commons Collections.

%package doc
Summary:	Jakarta Commons Collections
Group:		Development/Languages/Java

%description doc
Jakarta Commons Collections.

%prep
%setup -q -n commons-collections-%{version}-src

%build
ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/*.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs dist/*.html
