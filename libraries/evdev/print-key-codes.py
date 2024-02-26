import evdev

# devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

#
# Find device object for device with a given name
#
devname = 'LITEON Technology USB Multimedia Keyboard'
# devname = 'AT Translated Set 2 keyboard'

devobjs = [ devobj for devobj  in [ evdev.InputDevice(devpath) 
                   for devpath in evdev.list_devices() ]
              if devobj.name == devname
          ]

if devobjs == []:
   print('no device found')
   quit()

devobj=devobjs[0]

for ev in devobj.read_loop():
    if ev.type == evdev.ecodes.EV_KEY and ev.value == 1:
       print(evdev.ecodes.KEY[ev.code])
