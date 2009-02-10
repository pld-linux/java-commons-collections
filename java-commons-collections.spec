#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%include	/usr/lib/rpm/macros.java

%define		srcname	commons-collections
Summary:	Commons Collections - Java Collections enhancements
Summary(pl.UTF-8):	Commons Collections - rozszerzenia Java Collections
Name:		java-commons-collections
Version:	3.2
Release:	3
License:	Apache
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/collections/source/commons-collections-%{version}-src.tar.gz
# Source0-md5:	dbf80727b384bfb9c220d78af30ebc14
Source1:	jakarta-commons-collections-tomcat5-build.xml
Patch0:		jakarta-commons-collections-target.patch
URL:		http://commons.apache.org/collections/
BuildRequires:	ant
BuildRequires:	java-gcj-compat-devel
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
Provides:	jakarta-commons-collections
Obsoletes:	jakarta-commons-collections
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
Provides:	jakarta-commons-collections-tomcat5
Obsoletes:	jakarta-commons-collections-source
Obsoletes:	jakarta-commons-collections-tomcat5

%description tomcat5
Commons Collections dependency for Tomcat5.

%description tomcat5 -l pl.UTF-8
Elementy Commons Collections dla Tomcata 5.

%package javadoc
Summary:	Commons Collections documentation
Summary(pl.UTF-8):	Dokumentacja do Commons Collections
Group:		Documentation
Requires:	jpackage-utils
Provides:	jakarta-commons-collections-javadoc
Obsoletes:	jakarta-commons-collections-doc
Obsoletes:	jakarta-commons-collections-javadoc

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
%ant -Dbuild.compiler=extJavac jar

%if %{with javadoc}
export SHELL=/bin/sh
%ant javadoc
%endif

# commons-collections-tomcat5
%ant -Dbuild.compiler=extJavac -f tomcat5-build.xml

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d $RPM_BUILD_ROOT%{_javadir}
install build/%{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -sf %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

install collections-tomcat5/%{srcname}-tomcat5.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-tomcat5-%{version}.jar
ln -sf %{srcname}-tomcat5-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-tomcat5.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}.jar
%{_javadir}/%{srcname}-%{version}.jar

%files tomcat5
%defattr(644,root,root,755)
%{_javadir}/%{srcname}-tomcat5.jar
%{_javadir}/%{srcname}-tomcat5-%{version}.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
