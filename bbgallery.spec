# ----------------------------------------------------------------------
# Copyright (C) 2001 Bodo Bauer <bb@bb-zone.com>
#
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as 
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version. 
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details. 
#
# You should have received a copy of the GNU General Public License 
# along with this program; if not, write to the Free Software 
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, 
# MA 02111-1307, USA. 
# ----------------------------------------------------------------------

Name:     	bbgallery
Version: 	1.1.0
Release:	0
Vendor:		Bodo Bauer
Distribution:	Bodo Bauer
Copyright:	GPL
Source:		bbgallery-%{version}.tar.bz2
BuildRoot:	/var/tmp/%{name}-%{version}-root
Summary:	HTML Gallery Creator Script
Group:		BB/html

%description
BBGallery is a small Perl script generating a number of HTML files from 
jpeg images that make up a image gallery to browse with any html browser. 
It uses The Gimp and Gimp-Perl</A> to create thumbnails and to scale the 
images. It offers the following features:

* Thumbnail creation (size can be configured)
* Scaling images to a configurable size (optional)
* Links to full size image
* Meta galleries (optional)
  (Galleries of galleries)
* Labels or text can be assigned to images and/or 
  galleries using simple text files.
* Easy installation and use
* No extra software needed to view galleries and 
  images on any plattform (ideal for archiving images)
* Automatic slideshow

Requires Perl, Gimp and Perl-Gimp.

%prep
%setup -n %{name}-%{version}

%build
make bbgallery

%install
make install instroot=$RPM_BUILD_ROOT prefix=/usr

%files
%defattr(-,root,root)
%doc README COPYING CHANGELOG
/usr/bin/bbgallery
/usr/bin/JPG2jpg
/usr/lib/bbgallery/gimp_scale.pl

%clean
rm -rf $RPM_BUILD_ROOT
