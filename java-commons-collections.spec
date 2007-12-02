%include	/usr/lib/rpm/macros.java
Summary:	Jakarta Commons Collections - Java Collections enhancements
Summary(pl.UTF-8):	Jakarta Commons Collections - rozszerzenia Java Collections
Name:		jakarta-commons-collections
Version:	3.1
Release:	4.1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/collections/source/commons-collections-%{version}-src.tar.gz
# Source0-md5:	2da710d9c81ae85ee3a386e7ed1b1fe8
Source1:	%{name}-tomcat5-build.xml
Patch0:		%{name}-target.patch
URL:		http://jakarta.apache.org/commons/collections/
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Collections package contains a set of Java classes that extend or
augment the Java Collections Framework.

%description -l pl.UTF-8
Pakiet Collections zawiera zestaw klas Javy rozszerzających lub
powiększających szkielet Java Collections.

%package javadoc
Summary:	Jakarta Commons Collections documentation
Summary(pl.UTF-8):	Dokumentacja do Jakarta Commons Collections
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-collections-doc

%description javadoc
Jakarta Commons Collections documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Jakarta Commons Collections.

%package tomcat5
Summary:	Collection dependency for Tomcat5
Group:		Development/Languages/Java
Obsoletes:	jakarta-commons-collections-source

%description tomcat5
Collections dependency for Tomcat5

%prep
%setup -q -n commons-collections-%{version}
%{__sed} -i -e 's,\r$,,' build.xml
%patch0 -p1
cp %{SOURCE1} tomcat5-build.xml
find -name '*.jar' | xargs rm -vf

%build
cat <<EOF > build.properties
junit.jar=$(build-classpath junit)
EOF
%ant jar javadoc

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
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

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

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
