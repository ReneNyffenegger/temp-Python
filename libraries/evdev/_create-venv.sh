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


#
#     2024-03-05  - next trial
#
#   https://www.coderancher.us/2023/04/28/how-to-allow-users-access-to-virtual-devices/
# 
#   sudo touch /etc/udev/rules.d/99-input.rules
    sudo sh -c 'echo KERNEL=="uinput", MODE="0660", GROUP="input" > /etc/udev/rules.d/99-input.rules'
    sudo udevadm control --reload-rules
    sudo usermod -a -G input rene
#   sudo chmode 0660 /dev/uinput
#   sudo chgrp input /dev/uinput
