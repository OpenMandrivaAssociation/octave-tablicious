%global octpkg tablicious

Summary:	A table (relational, tabular data) implementation for GNU Octave 
Name:		octave-%{octpkg}
Version:	0.3.6
Release:	1
Url:		https://github.com/apjanke/octave-%{octpkg}
Source0:	%{url}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics

BuildRequires:	octave-devel >= 3.6.0
BuildRequires:	octave-statistics >= 1.0.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-statistics >= 1.0.0

Requires(post): octave
Requires(postun): octave

%description
Tablicious provides tabular/relational data structures for Octave. You can
think of it as "pandas for Octave".

%files
%license COPYING
#doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

# remove backup files
#find . -name \*~ -delete

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

