Summary:	HTML Gallery Creator Script
Summary(pl.UTF-8):   Skrypt do tworzenia galerii w HTML-u
Name:		bbgallery
Version:	1.1.0
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ftp.bb-zone.com/pub/bbgallery/%{name}-%{version}.tar.bz2
# Source0-md5:	783536b3b01b19b578ac96ea923214a8
Patch0:		%{name}-etc_dir.patch
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

%description -l pl.UTF-8
BBGallery to mały skrypt Perla tworzący pliki HTML z obrazków JPEG,
które tworzą galerię do przeglądania dowolną przeglądarką HTML-a.
Skrypt używa programu Gimp i modułów Gimp-Perl do tworzenia miniaturek
oraz skalowania obrazków. Oferuje następujące możliwości:
- tworzenie miniaturek (rozmiar jest konfigurowalny)
- skalowanie obrazków do konfigurowalnego rozmiaru (opcjonalne)
- odnośniki do obrazków w pełnym rozmiarze
- meta-galerie (galerie galerii)
- etykiety lub tekst mogą być przypisywane do obrazków i/lub galerii
  przy użyciu prostych plików tekstowych
- łatwa instalacja i używanie
- nie wymaga dodatkowego oprogramowania do przeglądania galerii i
 obrazków na dowolnej platformie (idealne do archiwizowania
  obrazków)
 - automatyczne przeglądanie slajdów.

%prep
%setup -q
%patch0 -p1

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
