#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%include	/usr/lib/rpm/macros.java
Summary:	Commons Collections - Java Collections enhancements
Summary(pl.UTF-8):	Commons Collections - rozszerzenia Java Collections
Name:		jakarta-commons-collections
Version:	3.2
Release:	2
License:	Apache
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/collections/source/commons-collections-%{version}-src.tar.gz
# Source0-md5:	dbf80727b384bfb9c220d78af30ebc14
Source1:	jakarta-commons-collections-tomcat5-build.xml
Patch0:		jakarta-commons-collections-target.patch
URL:		http://commons.apache.org/collections/
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
Obsoletes:	jakarta-commons-collections
Provides:	jakarta-commons-collections
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Collections package contains a set of Java classes that extend or
augment the Java Collections Framework.

%description -l pl.UTF-8
Pakiet Collections zawiera zestaw klas Javy rozszerzających lub
powiększających szkielet Java Collections.

%package tomcat5
Summary:	Commons Collections dependency for Tomcat5
Summary(pl.UTF-8):	Elementy Commons Collections dla Tomcata 5
Group:		Development/Languages/Java
Obsoletes:	jakarta-commons-collections-source

%description tomcat5
Commons Collections dependency for Tomcat5.

%description tomcat5 -l pl.UTF-8
Elementy Commons Collections dla Tomcata 5.

%package javadoc
Summary:	Commons Collections documentation
Summary(pl.UTF-8):	Dokumentacja do Commons Collections
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-collections-doc

%description javadoc
Commons Collections documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Commons Collections.

%prep
%setup -q -n commons-collections-%{version}-src
%{__sed} -i -e 's,\r$,,' build.xml
%patch0 -p1
cp %{SOURCE1} tomcat5-build.xml
find -name '*.jar' | xargs rm -vf

%build
%ant jar %{?with_javadoc:javadoc}

# commons-collections-tomcat5
%ant -f tomcat5-build.xml

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d $RPM_BUILD_ROOT%{_javadir}
install build/commons-collections-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-collections-%{version}.jar
ln -sf commons-collections-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-collections.jar

install collections-tomcat5/commons-collections-tomcat5.jar $RPM_BUILD_ROOT%{_javadir}/commons-collections-tomcat5-%{version}.jar
ln -sf commons-collections-tomcat5-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-collections-tomcat5.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/commons-collections.jar
%{_javadir}/commons-collections-%{version}.jar

%files tomcat5
%defattr(644,root,root,755)
%{_javadir}/commons-collections-tomcat5.jar
%{_javadir}/commons-collections-tomcat5-%{version}.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
