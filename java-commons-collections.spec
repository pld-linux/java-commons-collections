%include	/usr/lib/rpm/macros.java
Summary:	Jakarta Commons Collections - Java Collections enhancements
Summary(pl.UTF-8):	Jakarta Commons Collections - rozszerzenia Java Collections
Name:		jakarta-commons-collections
Version:	3.1
Release:	2
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/collections/source/commons-collections-%{version}-src.tar.gz
# Source0-md5:	2da710d9c81ae85ee3a386e7ed1b1fe8
URL:		http://jakarta.apache.org/commons/collections/
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
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

%package source
Summary:	Jakarta Commons Collections source code
Summary(pl.UTF-8):	Kod źródłowy Jakarta Commons Collections
Group:		Development/Languages/Java
AutoReq:	no
AutoProv:	no

%description source
Jakarta Commons Collections source code.

%description source -l pl.UTF-8
Kod źródłowy Jakarta Commons Collections.

%prep
%setup -q -n commons-collections-%{version}

%build
cat <<EOF > build.properties
junit.jar=$(build-classpath junit)
EOF
%ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d $RPM_BUILD_ROOT%{_javadir}
install build/commons-collections-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-collections-%{version}.jar
ln -sf commons-collections-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-collections.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# source code
install -d $RPM_BUILD_ROOT%{_prefix}/src/%{name}-%{version}
cp -a src $RPM_BUILD_ROOT%{_prefix}/src/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files source
%defattr(644,root,root,755)
%{_prefix}/src/%{name}-%{version}
