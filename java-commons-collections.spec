Summary:	Jakarta Commons Collections - Java Collections enhancements
Summary(pl):	Jakarta Commons Collections - rozszerzenia Java Collections
Name:		jakarta-commons-collections
Version:	3.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/collections/source/commons-collections-%{version}-src.tar.gz
# Source0-md5:	2da710d9c81ae85ee3a386e7ed1b1fe8
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Collections package contains a set of Java classes that extend or
augment the Java Collections Framework.

%description -l pl
Pakiet Collections zawiera zestaw klas Javy rozszerzaj±cych lub
powiêkszaj±cych szkielet Java Collections.

%package doc
Summary:	Jakarta Commons Collections documentation
Summary(pl):	Dokumentacja do Jakarta Commons Collections
Group:		Development/Languages/Java

%description doc
Jakarta Commons Collections documentation.

%description doc -l pl
Dokumentacja do Jakarta Commons Collections.

%prep
%setup -q -n commons-collections-%{version}

%build
echo 'junit.jar=/usr/share/java/junit.jar' > build.properties
ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc build/docs
