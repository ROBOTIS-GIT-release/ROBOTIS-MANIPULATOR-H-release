Name:           ros-kinetic-manipulator-h
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS manipulator_h package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ROBOTIS-MANIPULATOR-H
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-manipulator-h-base-module
Requires:       ros-kinetic-manipulator-h-base-module-msgs
Requires:       ros-kinetic-manipulator-h-bringup
Requires:       ros-kinetic-manipulator-h-description
Requires:       ros-kinetic-manipulator-h-gazebo
Requires:       ros-kinetic-manipulator-h-gui
Requires:       ros-kinetic-manipulator-h-kinematics-dynamics
Requires:       ros-kinetic-manipulator-h-manager
BuildRequires:  ros-kinetic-catkin

%description
ROS packages for the ROBOTIS MANIPULATOR-H (meta package)

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
* Fri Aug 19 2016 pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

* Wed Aug 17 2016 pyo <pyo@robotis.com> - 0.1.1-0
- Autogenerated by Bloom

