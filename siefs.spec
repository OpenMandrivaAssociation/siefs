%define debug_package %{nil}

Summary:	SieFS - virtual filesystem for Siemens mobile phones' memory
Name:		siefs
Version:	0.5
Release:	1
License:	GPL, partially free (see COPYRIGHT.vmo2wav)
Group:		System/Base
Source0:	http://chaos.allsiemens.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	974328fc20b99e975d03a312a2814ed8
Patch0:		%{name}-fuse-from-flags.patch
URL:		http://chaos.allsiemens.com/siefs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig(fuse) >= 2.2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This is SieFS - a virtual filesystem for accessing Siemens mobile
phones' memory via datacable. Now you can mount your phone to a Linux
box and browse it like a simple directory! The program was tested on
S45/ME45/SL45/S55/M55/MC60, but should work also on C55/M50/MT50/SL55/C60.

%description -l pl
SieFS - wirtualny system plików udostêpniaj±cy pamiêæ telefonów
komórkowych Siemens pod³±czonych kablem. Pozwala podmontowaæ telefon
spod Linuksa i przegl±daæ go tak, jak zwyk³y katalog. Program by³
testowany na S45/ME45/SL45/S55/MC60, ale powinien dzia³aæ tak¿e z
C55/M50/MT50/SL55/C60.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fiv
CFLAGS="$(pkg-config --cflags fuse) -DFUSE_USE_VERSION=22"
LDFLAGS="$(pkg-config --libs fuse)"
%configure \
	--with-fuse=%{_prefix}
%make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp converter/README README.vmo2wav
cp converter/COPYRIGHT COPYRIGHT.vmo2wav
ln -s ..%{_bindir}/siefs $RPM_BUILD_ROOT%{_sbindir}/mount.siefs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS README* ChangeLog COPYRIGHT.vmo2wav
%attr(755,root,root) %{_bindir}/*
/sbin/mount.siefs

