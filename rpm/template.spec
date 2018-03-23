Name:           ros-kinetic-manipulator-h-bringup
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS manipulator_h_bringup package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/manipulator_h_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-joint-state-publisher
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-rviz
BuildRequires:  ros-kinetic-catkin

%description
The manipulator_h_bringup package This package includes launch file to describe
robotis in Rviz.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Mar 23 2018 Pyo <pyo@robotis.com> - 0.3.0-0
- Autogenerated by Bloom

* Fri Jun 09 2017 Pyo <pyo@robotis.com> - 0.2.3-0
- Autogenerated by Bloom

* Wed May 24 2017 Pyo <pyo@robotis.com> - 0.2.2-0
- Autogenerated by Bloom

* Thu Sep 22 2016 pyo <pyo@robotis.com> - 0.2.1-0
- Autogenerated by Bloom

* Fri Aug 19 2016 pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

* Wed Aug 17 2016 pyo <pyo@robotis.com> - 0.1.1-0
- Autogenerated by Bloom

