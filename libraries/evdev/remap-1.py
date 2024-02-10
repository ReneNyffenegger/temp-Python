#!/usr/bin/python3

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


# Import necessary libraries.
import atexit
# You need to install evdev with a package manager or pip3.
import evdev  # (sudo pip3 install evdev)


# Define an example dictionary describing the remaps.
REMAP_TABLE = {
  # Let's swap A and B...
    evdev.ecodes.KEY_A: evdev.ecodes.KEY_B,
    evdev.ecodes.KEY_B: evdev.ecodes.KEY_A,
    # ... and make the right Shift into a second Space.
    evdev.ecodes.KEY_RIGHTSHIFT: evdev.ecodes.KEY_SPACE,
    # We'll also remap CapsLock to Control when held ...
    evdev.ecodes.KEY_CAPSLOCK: evdev.ecodes.KEY_LEFTCTRL,
    # ... but to Esc when pressed solo, xcape style! See below.
}
# The names can be found with evtest or in evdev docs.


# The keyboard name we will intercept the events for. Obtainable with evtest.
MATCH = 'LITEON Technology USB Multimedia Keyboard'
MATCH = 'AT Translated Set 2 keyboard'

# Find all input devices.
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

# Limit the list to those containing MATCH and pick the first one.
kbd = [d for d in devices if MATCH in d.name][0]
print(type(kbd.leds()))
print(kbd.leds())
#quit()

atexit.register(kbd.ungrab)  # Don't forget to ungrab the keyboard on exit!
kbd.grab()  # Grab, i.e. prevent the keyboard from emitting original events.


soloing_caps = False  # A flag needed for CapsLock example later.

# Create a new keyboard mimicking the original one.
with evdev.UInput.from_device(kbd, name='kbdremap') as ui:

  # Read events from original keyboard.
    for ev in kbd.read_loop():
    #   print(type(ev))
        print(kbd.active_keys())

        if ev.type == evdev.ecodes.EV_KEY:  # Process key events.

            if ev.code == evdev.ecodes.KEY_PAUSE and ev.value == 1:
              # Exit on pressing PAUSE.
              # Useful if that is your only keyboard. =)
              # Also if you bind that script to PAUSE, it'll be a toggle.
                break

            elif ev.code in REMAP_TABLE:

              # Lookup the key we want to press/release instead...
                remapped_code = REMAP_TABLE[ev.code]

              # And do it.
                ui.write(evdev.ecodes.EV_KEY, remapped_code, ev.value)

              # Also, remap a 'solo CapsLock' into an Escape as promised.
                if ev.code == evdev.ecodes.KEY_CAPSLOCK and ev.value == 0:
                    if soloing_caps:
                      # Single-press Escape.
                        ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_ESC, 1)
                        ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_ESC, 0)
            else:
                # Passthrough other key events unmodified.
                ui.write(evdev.ecodes.EV_KEY, ev.code, ev.value)

            # If we just pressed (or held) CapsLock, remember it.
            # Other keys will reset this flag.
            soloing_caps = (ev.code == evdev.ecodes.KEY_CAPSLOCK and ev.value)
        else:
            # Passthrough other events unmodified (e.g. SYNs).
            ui.write(ev.type, ev.code, ev.value)
