import evdev
print(evdev.InputDevice('/dev/input/event0'))

# print('<\n>'.join([evdev.InputDevice(devpath).name for devpath in evdev.list_devices()]))
# quit()

# devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

#
# Find device object for device with a given name
#
# devname = 'LITEON Technology USB Multimedia Keyboard'
devname = 'USB OPTICAL MOUSE ' # note the final space

devobjs = [ devobj for devobj  in [ evdev.InputDevice(devpath) 
                   for devpath in evdev.list_devices() ]
              if devobj.name == devname
          ]

if devobjs == []:
   print('no device found')
   quit()

devobj=devobjs[0]

for ev in devobj.read_loop():
    if ev.type == evdev.ecodes.EV_KEY: #  and ev.value == 1:
#      print(evdev.categorize(ev))
#      print(ev.code)
#      print('y')
       print(evdev.ecodes.BTN[ev.code])
