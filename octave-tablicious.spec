%global octpkg tablicious

Summary:	A table (relational, tabular data) implementation for GNU Octave 
Name:		octave-tablicious
Version:	0.4.2
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/tablicious/
Url:		https://github.com/apjanke/octave-tablicious/
Source0:	https://github.com/apjanke/octave-tablicious/archive/v%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	octave-statistics >= 1.0.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-statistics >= 1.0.0

Requires(post): octave
Requires(postun): octave

%description
Matlab-compatible Octave table class for storing tabular/relational
data. Similar to R and Python Pandas DataFrames.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

