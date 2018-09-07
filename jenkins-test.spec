Name: jenkins-test
Version: 1.0
Release: 2%{?dist}
Summary: This is a test rpm package for study

Group: Application/file
License: GPL
URL: http://pelway.com

BuildArch: noarch
#BuildRequires:
Requires: python >= 2.7.0

#%define SRC_DIR /home/jenkins-test
%define SRC_DIR /var/lib/jenkins/workspace/jenkins-test

%description
This is a test.

%prep
mkdir -p %SRC_DIR
#%setup -q

#%build

%install
#tar zxvf %SRC_FILE -C %SRC_DIR
mkdir -p %{buildroot}/etc/jenkins-test/conf/
cp %SRC_DIR/jenkins-test.conf %{buildroot}/etc/jenkins-test/conf/
mkdir -p %{buildroot}/usr/local/jenkins-test/
cp %SRC_DIR/jenkins-test.sh %{buildroot}/usr/local/jenkins-test/

%files
/etc/jenkins-test/conf/
/usr/local/jenkins-test/

%doc

%pre

%post
chmod +x /usr/local/jenkins-test/jenkins-test.sh
ln -s /usr/local/jenkins-test/jenkins-test.py /usr/local/bin/jenkins-test

%preun
if [ $1 == 0 ]; then # uninstall
    unlink /usr/local/bin/test
fi

%postun

%changelog
* Tue May 31 2016 jenkins-test <jenkins-test@test.test> - 1.0-1
- Test package
- Example second item in the changelog for version-release 1.0-1
- Haha Nothing has been Changed
