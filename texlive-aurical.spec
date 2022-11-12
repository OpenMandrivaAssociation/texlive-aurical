Name:		texlive-aurical
Version:	15878
Release:	1
Summary:	Calligraphic fonts for use with LaTeX in T1 encoding
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/aurical
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aurical.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aurical.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package that implements a set (AuriocusKalligraphicus) of
three calligraphic fonts derived from the author's handwriting
in Adobe Type 1 Format, T1 (Cork) encoding for use with LaTeX:
- Auriocus Kalligraphicus; - Lukas Svatba; and - Jana Skrivana.
Each font features oldstyle digits and (machine-generated)
boldface and slanted versions. A variant of Lukas Svatba offers
a 'long s'.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogo.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoBold.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoBoldRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoBoldSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicus.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusBold.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusBoldRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusBoldSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivana.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaBold.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaBoldRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaBoldSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatba.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaBold.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaBoldRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaBoldSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaSlant.afm
%{_texmfdistdir}/fonts/map/dvips/aurical/aurical.map
%{_texmfdistdir}/fonts/source/public/aurical/aurical_source.zip
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogo.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoBold.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoBoldRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoBoldSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicus.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusBold.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusBoldRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusBoldSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivana.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaBold.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaBoldRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaBoldSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatba.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaBold.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaBoldRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaBoldSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaSlant.tfm
%{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogo.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoBold.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoBoldRslant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoBoldSlant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoRslant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoSlant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicus.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusBold.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusBoldRslant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusBoldSlant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusRslant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusSlant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivana.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaBold.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaBoldRslant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaBoldSlant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaRslant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaSlant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatba.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaBold.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaBoldRslant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaBoldSlant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaRslant.pfb
%{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaSlant.pfb
%{_texmfdistdir}/tex/latex/aurical/T1AmiciLogo.fd
%{_texmfdistdir}/tex/latex/aurical/T1AuriocusKalligraphicus.fd
%{_texmfdistdir}/tex/latex/aurical/T1JanaSkrivana.fd
%{_texmfdistdir}/tex/latex/aurical/T1LukasSvatba.fd
%{_texmfdistdir}/tex/latex/aurical/aurical.sty
%doc %{_texmfdistdir}/doc/latex/aurical/aurical.pdf
%doc %{_texmfdistdir}/doc/latex/aurical/aurical.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
