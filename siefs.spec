# $Revision: 1.12 $, $Date: 2005/04/05 18:52:00 $
Summary:	SieFS - virtual filesystem for Siemens mobile phones' memory
Summary(pl):	SieFS - wirtualny system plików do pamiêci telefonów komórkowych Siemens
Name:		siefs
Version:	0.5
Release:	1
License:	GPL, partially free (see COPYRIGHT.vmo2wav)
Group:		Base/Kernel
Source0:	http://chaos.allsiemens.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	974328fc20b99e975d03a312a2814ed8
Patch0:		%{name}-fuse-from-flags.patch
URL:		http://chaos.allsiemens.com/siefs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 2.2
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} $(pkg-config --cflags fuse) -DFUSE_USE_VERSION=22"
LDFLAGS="%{rpmldflags} $(pkg-config --libs fuse)"
%configure \
	--with-fuse=%{_prefix}
%{__make}

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
%defattr(644,root,root,755)
%doc AUTHORS README* ChangeLog COPYRIGHT.vmo2wav
%attr(755,root,root) %{_bindir}/*
/sbin/mount.siefs

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: siefs.spec,v $
Revision 1.12  2005/04/05 18:52:00  saq
- up to 0.5
- lots of various fixes
- introducing mount.siefs (yes, mount -t siefs works now)

Revision 1.11  2005/01/05 19:46:22  speedo
- rel 1, STBR

Revision 1.10  2004/08/29 21:29:23  darekr
- update to 0.4

Revision 1.9  2004/05/10 18:14:28  pawcioos
- added vmo2wav

Revision 1.8  2004/05/09 22:08:55  pawcioos
- remove fuser*, added comments

Revision 1.7  2004/01/30 04:02:50  pzurowski
- updated to version 0.2, rel. 0.1
- fuse (not emulator) needed => not tested

Revision 1.6  2003/11/11 01:33:24  ankry
- caps unification, other cosmetics

Revision 1.5  2003/06/20 09:39:18  ankry
- md5

Revision 1.4  2003/06/18 14:32:46  qboosh
- URLs, descriptions, some build fixes

Revision 1.3  2003/06/06 12:33:22  qboosh
- updated feedback address

Revision 1.2  2003/05/25 06:26:43  misi3k
- massive attack s/pld.org.pl/pld-linux.org/

Revision 1.1  2003/03/17 12:18:13  cieciwa
- initial.

NFY.
