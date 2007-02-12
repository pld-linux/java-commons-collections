Summary:	Jakarta Commons Collections - Java Collections enhancements
Summary(pl.UTF-8):   Jakarta Commons Collections - rozszerzenia Java Collections
Name:		jakarta-commons-collections
Version:	3.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/collections/source/commons-collections-%{version}-src.tar.gz
# Source0-md5:	2da710d9c81ae85ee3a386e7ed1b1fe8
URL:		http://jakarta.apache.org/commons/collections/
BuildRequires:	ant
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Collections package contains a set of Java classes that extend or
augment the Java Collections Framework.

%description -l pl.UTF-8
Pakiet Collections zawiera zestaw klas Javy rozszerzających lub
powiększających szkielet Java Collections.

%package doc
Summary:	Jakarta Commons Collections documentation
Summary(pl.UTF-8):   Dokumentacja do Jakarta Commons Collections
Group:		Development/Languages/Java

%description doc
Jakarta Commons Collections documentation.

%description doc -l pl.UTF-8
Dokumentacja do Jakarta Commons Collections.

%prep
%setup -q -n commons-collections-%{version}

%build
echo 'junit.jar=%{_datadir}/java/junit.jar' > build.properties
ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/*.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf commons-collections-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-collections.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc build/docs
