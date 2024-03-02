import asyncio
import atexit
import evdev



# print(evdev.InputDevice('/dev/input/event0'))

# print('<\n>'.join([evdev.InputDevice(devpath).name for devpath in evdev.list_devices()]))
# quit()

# devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

#
# Find device object for device with a given name
#
nm_kb = 'LITEON Technology USB Multimedia Keyboard'
nm_ms = 'USB OPTICAL MOUSE ' # note the final space

dv_kb = [devobj for devobj  in [ evdev.InputDevice(devpath) for devpath in evdev.list_devices() ] if devobj.name == nm_kb ][0]
dv_ms = [devobj for devobj  in [ evdev.InputDevice(devpath) for devpath in evdev.list_devices() ] if devobj.name == nm_ms ][0]

# print(type(dv_kb))
# print(type(dv_ms))

print(f'Keyboard at {dv_kb.path}')
print(f'Mouse    at {dv_ms.path}')



# --- rempa-1.py -----------------------------------------------------------

atexit.register(dv_kb.ungrab)  # Don't forget to ungrab the keyboard on exit!
dv_kb.grab()                   # Grab, i.e. prevent the keyboard from emitting original events.
left_alt_suppressed = False

# Create a new keyboard mimicking the original one.
ui = evdev.UInput.from_device(dv_kb, name='kbdremap') 

async def handle_events(dev): # {{{
    global left_alt_suppressed
    global ui

  # Read events from original keyboard.
    for ev in dev.async_read_loop():
     #  print(type(ev))
     #  print(dev.active_keys())
        print(dev.path, evdev.categorize(ev), sep=': ')

        if ev.type == evdev.ecodes.EV_KEY:  # Process key events.
        
#          print(kbd.active_keys())

           if   ev.code == evdev.ecodes.KEY_PAUSE and ev.value == 1:
              # Exit on pressing PAUSE.
              # Useful if that is your only keyboard. =)
              # Also if you bind that script to PAUSE, it'll be a toggle.
                break


           if    ev.code == evdev.ecodes.KEY_LEFTALT and ev.value == 1:
                 left_alt_suppressed = True

           elif  left_alt_suppressed and ev.code == evdev.ecodes.KEY_SEMICOLON and ev.value == 1:
                 left_alt_suppressed = False
                 write_hex([evdev.ecodes.KEY_F, evdev.ecodes.KEY_6]) # ö

           elif  left_alt_suppressed and ev.code == evdev.ecodes.KEY_APOSTROPHE and ev.value == 1:
                 left_alt_suppressed = False
                 write_hex([evdev.ecodes.KEY_E, evdev.ecodes.KEY_4]) # ä
          
           elif  left_alt_suppressed and ev.code == evdev.ecodes.KEY_LEFTBRACE and ev.value == 1:
                 left_alt_suppressed = False
                 write_hex([evdev.ecodes.KEY_F, evdev.ecodes.KEY_C]) # ü

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
                left_alt_suppressed = False
                   
#          elif evdev.ecodes.KEY_LEFTALT in kbd.active_keys() and evdev.ecodes.KEY_SEMICOLON in kbd.active_keys():

           else:
                ui.write(evdev.ecodes.EV_KEY, ev.code, ev.value)

        else:
          # Passthrough other events unmodified (e.g. SYNs).
            ui.write(ev.type, ev.code, ev.value)
# }}}



for dev in dv_ms, dv_kb:
    asyncio.ensure_future(handle_events(dev))

loop = asyncio.get_event_loop()
loop.run_forever()



def write_hex(keys): # {{{

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

# --------------------------------------------------------------------------

# async def print_events(device): # {{{
# 
#     async for ev in device.async_read_loop():
#         if ev.type == evdev.ecodes.EV_KEY:
#         #  print(device.path, evdev.categorize(ev), sep=': ')
#         #  print(dir(ev))
#         #  print(f'code: {ev.code}, value: {ev.value}')
#            if ev.code in [evdev.ecodes.BTN_RIGHT, evdev.ecodes.BTN_MIDDLE, evdev.ecodes.BTN_LEFT]:
#               print('btn')
#         #  print(evdev.ecodes.KEY[ev.code])
#        #if ev.type == evdev.ecodes.EV_BTN:
#        #   print(device.path, evdev.categorize(ev), sep=': ')
# 
# # }}}


# loop = asyncio.get_event_loop()
# loop.run_forever()

# if devobjs == []:
#    print('no device found')
#    quit()
# 
# devobj=devobjs[0]
# 
# for ev in devobj.read_loop():
#     if ev.type == evdev.ecodes.EV_KEY: #  and ev.value == 1:
# #      print(evdev.categorize(ev))
# #      print(ev.code)
# #      print('y')
#        print(evdev.ecodes.BTN[ev.code])
