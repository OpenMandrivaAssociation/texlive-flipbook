# revision 25584
# category Package
# catalog-ctan /macros/latex/contrib/flipbook
# catalog-date 2012-03-07 15:39:23 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-flipbook
Version:	0.2
Release:	10
Summary:	Typeset flipbook animations, in the corners of documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flipbook
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flipbook.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flipbook.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides techniques for adding flip book animations
in the corner of your LaTeX documents (using images or ASCII
art). Animations are defined as a set of numbered files (e.g.,
"im1.pdf", "im2.pdf", "im3.pdf", ...). The package relies on
fancyhdr to control the corners.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/flipbook/flipbook.sty
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im01.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im01.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im01.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im02.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im02.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im02.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im03.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im03.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im03.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im04.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im04.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im04.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im05.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im05.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im05.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im06.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im06.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an1b/im06.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/an2.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/an2.xcf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im0.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im0.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im00.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im01.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im01.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im02.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im02.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im03.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im03.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im04.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im04.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im05.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im05.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im06.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im06.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im07.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im07.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im08.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im08.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im09.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im09.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im1.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im1.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im10.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im10.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im10.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im10.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im11.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im11.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im11.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im11.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im12.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im12.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im12.gif
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im12.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im13.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im13.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im13.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im14.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im14.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im14.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im15.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im15.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im15.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im16.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im16.fig
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im16.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im2.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im2.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im3.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im3.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im4.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im4.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im5.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im5.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im6.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im6.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im7.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im7.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im8.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im8.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im9.eps
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an2/im9.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/an3.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/an3.pnm
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/an3.xcf
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im1.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im10.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im11.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im12.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im13.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im14.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im15.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im16.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im17.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im18.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im19.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im2.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im20.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im21.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im22.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im23.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im24.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im25.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im26.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im27.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im28.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im29.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im3.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im30.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im31.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im32.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im33.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im34.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im35.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im36.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im37.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im38.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im39.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im4.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im40.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im41.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im42.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im43.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im44.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im45.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im46.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im5.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im6.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im7.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im8.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/an3/im9.png
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/anASCII/an0.tex
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/anASCII/an1.tex
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/anASCII/an2.tex
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/anASCII/an3.tex
%doc %{_texmfdistdir}/doc/latex/flipbook/Images/Anims/anASCII/an4.tex
%doc %{_texmfdistdir}/doc/latex/flipbook/Makefile
%doc %{_texmfdistdir}/doc/latex/flipbook/README
%doc %{_texmfdistdir}/doc/latex/flipbook/flipbook-doc.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/flipbook-doc.tex
%doc %{_texmfdistdir}/doc/latex/flipbook/flipbook-ex.pdf
%doc %{_texmfdistdir}/doc/latex/flipbook/flipbook-ex.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 787612
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 751925
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 739615
- texlive-flipbook
- texlive-flipbook

