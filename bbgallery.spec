Summary:	HTML Gallery Creator Script
Name:		bbgallery
Version:	1.1.0
Release:	1
License:	GPL
Group:		BB/html
Source0:	ftp://ftp.bb-zone.com/pub/bbgallery/%{name}-%{version}.tar.bz2
URL:		http://www.bb-zone.com/zope/bbzone/projects/bbgallery/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bbpic

%description
BBGallery is a small Perl script generating a number of HTML files
from jpeg images that make up a image gallery to browse with any html
browser. It uses The Gimp and Gimp-Perl</A> to create thumbnails and
to scale the images. It offers the following features:

- Thumbnail creation (size can be configured)
- Scaling images to a configurable size (optional)
- Links to full size image
- Meta galleries (optional) (Galleries of galleries)
- Labels or text can be assigned to images and/or galleries using
  simple text files.
- Easy installation and use
- No extra software needed to view galleries and images on any
  plattform (ideal for archiving images)
- Automatic slideshow

Requires Perl, Gimp and Perl-Gimp.

%prep
%setup -q

%build
%{__make} bbgallery

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install instroot=$RPM_BUILD_ROOT prefix=%{_prefix}

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/bbgallery
%attr(755,root,root) %{_bindir}/JPG2jpg
%{_libdir}/bbgallery

%clean
rm -rf $RPM_BUILD_ROOT
