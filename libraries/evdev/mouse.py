import asyncio
import atexit
import evdev
import sys
import time


#
# Find device object for device with a given name
#
nm_kb = 'LITEON Technology USB Multimedia Keyboard'
nm_ms = 'USB OPTICAL MOUSE ' # note the final space

dv_kb = [ devobj for devobj  in [ evdev.InputDevice(devpath) for devpath in evdev.list_devices() ] if devobj.name == nm_kb ][0]
dv_ms = [ devobj for devobj  in [ evdev.InputDevice(devpath) for devpath in evdev.list_devices() ] if devobj.name == nm_ms ][0]

print( "[2J") # Clear screen
print(f'[1;1HKeyboard at {dv_kb.path}')
print(f'[2;1HMouse    at {dv_ms.path}')

dv_kb.grab()                   # Grab, i.e. prevent the keyboard from emitting original events.
atexit.register(dv_kb.ungrab)  # Don't forget to ungrab the keyboard on exit!
dv_ms.grab()                   # Grab, i.e. prevent the keyboard from emitting original events.
atexit.register(dv_kb.ungrab)  # Don't forget to ungrab the keyboard on exit!
left_alt_suppressed = False

# Create a new keyboard mimicking the original one.
ui = evdev.UInput.from_device(dv_kb, dv_ms, name='kbdremap', version=3) 

def write_hex(keys): # {{{

    global ui

    ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL , 1)
    ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 1)
    ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_U        , 1)
    ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_U        , 0)
    ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL , 0)
    ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 0)

    for key in keys:
        ui.write(evdev.ecodes.EV_KEY, key, 1) # https://www.utf8-zeichentabelle.de/unicode-utf8-table.pl?names=-&unicodeinhtml=hex
        ui.write(evdev.ecodes.EV_KEY, key, 0)

    ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_SPACE    , 1)
    ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_SPACE    , 0)
    
# }}}

async def handle_events(dev): # {{{
    global left_alt_suppressed
    global ui

    async for ev in dev.async_read_loop():
        if ev.type == evdev.ecodes.EV_KEY:  # {{{ Process key events.
        
           if   ev.code == evdev.ecodes.KEY_PAUSE and ev.value == 1:
              # Exit on pressing PAUSE.
              # Useful if that is your only keyboard. =)
              # Also if you bind that script to PAUSE, it'll be a toggle.
                break


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
                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTALT, 1)
                ui.syn()
                left_alt_suppressed = False
                print(f'[4;1H     ')
                ui.write(ev.type, ev.code, ev.value)

           elif ev.code == evdev.ecodes.KEY_ESC:
                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_CAPSLOCK, ev.value)

           elif ev.code == evdev.ecodes.KEY_CAPSLOCK:
                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_ESC, ev.value)

           elif ev.code == evdev.ecodes.KEY_RIGHTMETA:
                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_RIGHTCTRL, ev.value)

           elif ev.code == evdev.ecodes.KEY_LEFTMETA:
                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL, ev.value)

           elif left_alt_suppressed:
                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTALT, 1)
                ui.write(evdev.ecodes.EV_KEY, ev.code, ev.value)
                print(f'[4;1H     ')
                left_alt_suppressed = False
                   
           else:
                ui.write(ev.type, ev.code, ev.value)
        # }}}
        
        else:
          # All other events (also SYNs) are passed to uinput without modification:
            ui.write(ev.type, ev.code, ev.value)
# }}}



for dev in dv_ms, dv_kb:
    asyncio.ensure_future(handle_events(dev))

loop = asyncio.get_event_loop()
loop.run_forever()
