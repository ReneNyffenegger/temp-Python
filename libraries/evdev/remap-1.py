#/usr/bin/python3

#  https://gist.github.com/t184256/f4994037a2a204774ef3b9a2b38736dc

# CC0, originally written by t184256.

# This is an example Python program for Linux that remaps a keyboard.
# The events (key presses releases and repeats), are captured with evdev,
# and then injected back with uinput.

# This approach should work in X, Wayland, anywhere!

# Also it is not limited to keyboards, may be adapted to any input devices.

# The program should be easily portable to other languages or extendable to
# run really any code in 'macros', e.g., fetching and typing current weather.

# The ones eager to do it in C can take a look at (overengineered) caps2esc:
# https://gitlab.com/interception/linux/plugins/caps2esc


import atexit
import evdev
# from ansi_escapes import ansiEscapes

# print(evdev.ecodes.KEY_ESC)
# quit()

# The keyboard name we will intercept the events for. Obtainable with evtest.
keyboard_name   = 'LITEON Technology USB Multimedia Keyboard'
# keyboard_name = 'AT Translated Set 2 keyboard'

# Find all input devices.
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

# Limit the list to those containing keyboard_name and pick the first one.
kbd = [d for d in devices if keyboard_name in d.name][0]
# print(type(kbd.leds()))
# print(kbd.leds())
#quit()

atexit.register(kbd.ungrab)  # Don't forget to ungrab the keyboard on exit!
kbd.grab()  # Grab, i.e. prevent the keyboard from emitting original events.

left_alt_suppressed = False

# print(ansiEscapes.clearTerminal)

# Create a new keyboard mimicking the original one.
with evdev.UInput.from_device(kbd, name='kbdremap') as ui:

  # Read events from original keyboard.
    for ev in kbd.read_loop():
    #   print(type(ev))
    #   print(kbd.active_keys())

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

                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL , 1)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 1)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_U        , 1)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_U        , 0)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL , 0)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 0)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_E        , 1) # https://www.utf8-zeichentabelle.de/unicode-utf8-table.pl?names=-&unicodeinhtml=hex
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_E        , 0)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_4        , 1)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_4        , 0)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_SPACE    , 1)
                 ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_SPACE    , 0)
          

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
  #        elif ev.code == evdev.ecodes.KEY_BACKSPACE and ev.value == 0:
  #                print('yes')
# #             if ev.value == 1:
# #                print('  1')
# #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTALT  , 0)
# #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_SEMICOLON, 0)

  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL , 1)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 1)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_U        , 1)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_U        , 0)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL , 0)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 0)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_E        , 1) # https://www.utf8-zeichentabelle.de/unicode-utf8-table.pl?names=-&unicodeinhtml=hex
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_E        , 0)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_4        , 1)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_4        , 0)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_SPACE    , 1)
  #                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_SPACE    , 0)

           else:
                ui.write(evdev.ecodes.EV_KEY, ev.code, ev.value)

        else:
          # Passthrough other events unmodified (e.g. SYNs).
            ui.write(ev.type, ev.code, ev.value)
