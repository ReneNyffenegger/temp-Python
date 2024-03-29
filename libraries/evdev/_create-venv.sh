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
#   https://tkcheng.wordpress.com/2013/11/11/changing-uinput-device-permission/
# 
#   sudo touch /etc/udev/rules.d/99-input.rules
    sudo addgroup uinput
    sudo sh -c 'echo SUBSYSTEM==\"misc\", KERNEL==\"uinput\",   MODE=\"0660\", GROUP=\"uinput\" > /etc/udev/rules.d/99-input.rules' # https://github.com/chrippa/ds4drv/issues/93 , https://github.com/tuomasjjrasanen/python-uinput/blob/master/udev-rules/40-uinput.rules
  # sudo sh -c                     ' echo KERNEL==\"uinput\", MODE:=\"0660\", GROUP=\"uinput\" > /etc/udev/rules.d/99-input.rules'
  # sudo sh -c 'echo KERNEL==\"uinput\", MODE=\"0660\", GROUP=\"uinput\" > /etc/udev/rules.d/99-input.rules'
    sudo sh -c 'echo uinput > /etc/modules-load.d/uinput.conf' # https://github.com/chrippa/ds4drv/issues/93
  # sudo udevadm control --reload-rules
    sudo usermod -a -G  input rene
    sudo usermod -a -G uinput rene
#   sudo chmode 0660 /dev/uinput
#   sudo chgrp input /dev/uinput


#
# https://forum.xfce.org/viewtopic.php?id=5550
# https://askubuntu.com/questions/971105/what-is-the-difference-between-config-autostart-and-config-autostart-scrip
# 
mkdir -p ~/.config/autostart
cat <<TF > ~/.config/autostart/evdev.desktop
[Desktop Entry]
Type=Application
Name=Python evdev keyboard mapper
Version=1.5
Exec= /home/rene/github/dev/python/temp/libraries/evdev/start
Terminal=true
StartupNotify=false
TF

# Version=1.5
# Terminal=false
# Encoding=UTF-8
# Hidden=false

# [Desktop Entry]
# Version=1.0
# Encoding=UTF-8
# Name=Script
# Type=Application
# Exec= /home/rene/github/temp/Python/libraries/evdev/start
# Icon=
# Terminal=false
# StartupNotify=false
# Hidden=false
# GenericName=
# GenericName[en_US]=
