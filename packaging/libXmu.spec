%bcond_with x

Name:           libXmu
Version:        1.1.1
Release:        1
License:        MIT
Summary:        X.org Xmu library
Url:            http://www.x.org
Group:          Graphics/X Window System

Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXmu.manifest

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xt)

%if !%{with x}
ExclusiveArch:
%endif

%description
X.Org X11 libXmu/libXmuu runtime libraries

%package devel
Summary:        X.org Xmu library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X.Org X11 libXmu development package.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXmu.so.6
%{_libdir}/libXmu.so.6.2.0
%{_libdir}/libXmuu.so.1
%{_libdir}/libXmuu.so.1.0.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xmu
%{_includedir}/X11/Xmu/Atoms.h
%{_includedir}/X11/Xmu/CharSet.h
%{_includedir}/X11/Xmu/CloseHook.h
%{_includedir}/X11/Xmu/Converters.h
%{_includedir}/X11/Xmu/CurUtil.h
%{_includedir}/X11/Xmu/CvtCache.h
%{_includedir}/X11/Xmu/DisplayQue.h
%{_includedir}/X11/Xmu/Drawing.h
%{_includedir}/X11/Xmu/Editres.h
%{_includedir}/X11/Xmu/EditresP.h
%{_includedir}/X11/Xmu/Error.h
%{_includedir}/X11/Xmu/ExtAgent.h
%{_includedir}/X11/Xmu/Initer.h
%{_includedir}/X11/Xmu/Lookup.h
%{_includedir}/X11/Xmu/Misc.h
%{_includedir}/X11/Xmu/StdCmap.h
%{_includedir}/X11/Xmu/StdSel.h
%{_includedir}/X11/Xmu/SysUtil.h
%{_includedir}/X11/Xmu/WhitePoint.h
%{_includedir}/X11/Xmu/WidgetNode.h
%{_includedir}/X11/Xmu/WinUtil.h
%{_includedir}/X11/Xmu/Xct.h
%{_includedir}/X11/Xmu/Xmu.h
%{_libdir}/libXmu.so
%{_libdir}/libXmuu.so
%{_libdir}/pkgconfig/xmu.pc
%{_libdir}/pkgconfig/xmuu.pc
