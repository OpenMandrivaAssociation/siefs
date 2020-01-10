%define debug_package %{nil}

Summary:	SieFS - virtual filesystem for Siemens mobile phones' memory
Name:		siefs
Version:	0.5
Release:	2
License:	GPL, partially free (see COPYRIGHT.vmo2wav)
Group:		System/Base
Source0:	http://chaos.allsiemens.com/download/%{name}-%{version}.tar.gz
Patch0:		siefs-0.5-qa-fixes.patch
URL:		http://chaos.allsiemens.com/siefs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig(fuse) >= 2.2
BuildRequires:	pkgconfig

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
%autopatch -p1

%build
autoreconf -fiv
CFLAGS="$(pkg-config --cflags fuse) -DFUSE_USE_VERSION=22"
LDFLAGS="$(pkg-config --libs fuse)"
%configure \
	--with-fuse=%{_prefix}
%make

%install
%makeinstall_std

cp converter/README README.vmo2wav
cp converter/COPYRIGHT COPYRIGHT.vmo2wav

%files
%doc AUTHORS README* ChangeLog COPYRIGHT.vmo2wav
%attr(755,root,root) %{_bindir}/*
/sbin/mount.siefs
