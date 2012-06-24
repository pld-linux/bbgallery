Summary:	HTML Gallery Creator Script
Summary(pl):	Skrypt do tworzenia galerii w HTML-u
Name:		bbgallery
Version:	1.1.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ftp.bb-zone.com/pub/bbgallery/%{name}-%{version}.tar.bz2
URL:		http://www.bb-zone.com/zope/bbzone/projects/bbgallery/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bbpic

%description
BBGallery is a small Perl script generating a number of HTML files
from JPEG images that make up a image gallery to browse with any HTML
browser. It uses The Gimp and Gimp-Perl to create thumbnails and to
scale the images. It offers the following features:

- Thumbnail creation (size can be configured)
- Scaling images to a configurable size (optional)
- Links to full size image
- Meta galleries (optional) (Galleries of galleries)
- Labels or text can be assigned to images and/or galleries using
  simple text files
- Easy installation and use
- No extra software needed to view galleries and images on any
  platform (ideal for archiving images)
- Automatic slideshow

Requires Perl, Gimp and Perl-Gimp.

%description -l pl
BBGallery to ma�y skrypt Perla tworz�cy pliki HTML z obrazk�w JPEG,
kt�re tworz� galeri� do przegl�dania dowoln� przegl�dark� HTML. Skrypt
u�ywa programu Gimp i modu��w Gimp-Perl do tworzenia miniaturek oraz
skalowania obrazk�w. Oferuje nast�puj�ce mo�liwo�ci:
 - tworzenie miniaturek (rozmiar jest konfigurowalny)
 - skalowanie obrazk�w do konfigurowalnego rozmiaru (opcjonalne)
 - odno�niki do obrazk�w w pe�nym rozmiarze
 - meta-galerie (galerie galerii)
 - etykiety lub tekst mog� by� przypisywane do obrazk�w i/lub galerii
   przy u�yciu prostych plik�w tekstowych
 - �atwa instalacja i u�ywanie
 - nie wymaga dodatkowego oprogramowania do przegl�dania galerii i
   obrazk�w na dowolnej platformie (idealne do archiwizowania
   obrazk�w)
  - automatyczne przegl�danie slajd�w.

%prep
%setup -q

%build
%{__make} bbgallery

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install instroot=$RPM_BUILD_ROOT prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/bbgallery
%attr(755,root,root) %{_bindir}/JPG2jpg
%{_libdir}/bbgallery
