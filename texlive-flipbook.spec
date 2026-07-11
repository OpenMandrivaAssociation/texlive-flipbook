%global tl_name flipbook
%global tl_revision 75878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Typeset flipbook animations, in the corners of documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/flipbook
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flipbook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flipbook.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides techniques for adding flip book animations in the
corner of your LaTeX documents (using images or ASCII art). Animations
are defined as a set of numbered files (e.g., im1.pdf, im2.pdf, im3.pdf,
...). The package relies on fancyhdr to control the corners.

