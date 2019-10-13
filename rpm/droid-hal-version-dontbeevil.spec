# rpm_device is the name of the ported device
%define rpm_device dontbeevil
# rpm_vendor is used in the rpm space
%define rpm_vendor pine64
# Manufacturer and device name to be shown in UI
%define vendor_pretty Pine64
%define device_pretty Pinephone
# See ../droid-hal-version/droid-hal-device.inc
%define have_ffmemless 1
%define have_led 1
%define native_build 1
%include droid-hal-version/droid-hal-version.inc
