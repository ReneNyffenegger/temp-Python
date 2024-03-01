  python3 -m venv py-virt-env

  . py-virt-env/bin/activate

  pip3 install evdev
# pip3 install ansi-escapes


#
#      The intention of the following was to change group ownership of dev/uinput to «uinput»
#      It didn't work.
# #
# # https://github.com/chrippa/ds4drv/issues/93
# # 
#   sudo sh -c 'echo SUBSYSTEM=="misc", KERNEL=="uinput", MODE="0660", GROUP="uinput"  > /etc/udev/rules.d/tq4-uinput.rules'
#   sudo sh -c 'echo uinput > /etc/modules-load.d/uinput.conf'
#   sudo sh -c 'udevadm control --reload-rules && udevadm trigger'
