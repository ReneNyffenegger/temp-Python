import asyncio
import atexit
import evdev
import sys

def grab_device(dev_name): # {{{

    dev = [ devobj for devobj in [ evdev.InputDevice(devpath) for devpath in evdev.list_devices() ] if devobj.name == dev_name ][0]
  #
  # We want to handle the device's original events ourselves and
  # thus do not want the device to emit these events:
  #
    dev.grab()
  #
  # When this script stope, the device is allowed (yea, even should)
  # emit the events again:
  #
    atexit.register(dev.ungrab)
    return dev

# }}}


dv_kb = grab_device('LITEON Technology USB Multimedia Keyboard')
dv_ms = grab_device('USB OPTICAL MOUSE '                       ) # Note the final space

print( "[2J") # Clear screen
print(f'[1;1HKeyboard at {dv_kb.path}')
print(f'[2;1HMouse    at {dv_ms.path}')

left_alt_suppressed = False

vdev = evdev.UInput.from_device(dv_kb, dv_ms, name='virt-device', version=3) 

def write_hex(keys): # {{{

    global vdev

    vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL , 1)
    vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 1)
    vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_U        , 1)
    vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_U        , 0)
    vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL , 0)
    vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 0)

    for key in keys:
        vdev.write(evdev.ecodes.EV_KEY, key, 1)
        vdev.write(evdev.ecodes.EV_KEY, key, 0)

    vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_SPACE    , 1)
    vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_SPACE    , 0)
    
# }}}

async def handle_events(dev): # {{{
    global left_alt_suppressed
    global vdev

    async for ev in dev.async_read_loop():
        if ev.type == evdev.ecodes.EV_KEY:  # {{{ Process key events.
        
           if   ev.code == evdev.ecodes.KEY_PAUSE and ev.value == 1:
              #
              # Exit on pressing PAUSE.
              # Useful if that is your only keyboard. =)
              # Also if you bind that script to PAUSE, it'll be a toggle.
              #
                sys.exit()
              # break


           if   ev.code == evdev.ecodes.KEY_LEFTALT and ev.value == 1:
                print(f'[4;1HL-ALT')
                left_alt_suppressed = True

           elif left_alt_suppressed and ev.code == evdev.ecodes.KEY_SEMICOLON and ev.value == 1:
                print(f'[4;1H     ')
                left_alt_suppressed = False
                write_hex([evdev.ecodes.KEY_F, evdev.ecodes.KEY_6]) # ö

           elif left_alt_suppressed and ev.code == evdev.ecodes.KEY_APOSTROPHE and ev.value == 1:
                print(f'[4;1H     ')
                left_alt_suppressed = False
                write_hex([evdev.ecodes.KEY_E, evdev.ecodes.KEY_4]) # ä
          
           elif left_alt_suppressed and ev.code == evdev.ecodes.KEY_LEFTBRACE and ev.value == 1:
                print(f'[4;1H     ')
                left_alt_suppressed = False
                write_hex([evdev.ecodes.KEY_F, evdev.ecodes.KEY_C]) # ü

           elif left_alt_suppressed and ev.code == evdev.ecodes.BTN_LEFT and ev.value == 1:
                vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTALT, 1)
                vdev.syn()
                left_alt_suppressed = False
                print(f'[4;1H     ')
                vdev.write(ev.type, ev.code, ev.value)

           elif ev.code == evdev.ecodes.KEY_ESC:
                vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_CAPSLOCK, ev.value)

           elif ev.code == evdev.ecodes.KEY_CAPSLOCK:
                vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_ESC, ev.value)

           elif ev.code == evdev.ecodes.KEY_RIGHTMETA:
                vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_RIGHTCTRL, ev.value)

           elif ev.code == evdev.ecodes.KEY_LEFTMETA:
                vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL, ev.value)

           elif left_alt_suppressed:
                vdev.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTALT, 1)
                vdev.write(evdev.ecodes.EV_KEY, ev.code, ev.value)
                print(f'[4;1H     ')
                left_alt_suppressed = False
                   
           else:
                vdev.write(ev.type, ev.code, ev.value)
        # }}}
        
        else:
          # All other events (also SYNs) are passed to uinput without modification:
            vdev.write(ev.type, ev.code, ev.value)
# }}}


for dev in dv_ms, dv_kb:
    asyncio.ensure_future(handle_events(dev))

loop = asyncio.get_event_loop()
loop.run_forever()
