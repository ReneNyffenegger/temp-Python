import evdev

# device = evdev.InputDevice('/dev/input/event8')
# device = evdev.InputDevice('/dev/input/event0')
device = evdev.InputDevice('/dev/input/event7')
print(device)

for event in device.read_loop():
    if   event.type == evdev.ecodes.EV_KEY:
         print(evdev.categorize(event))
    elif event.type == evdev.ecodes.EV_SYN:
         print('SYN event')
         print(evdev.categorize(event))
    else:
        print('Event type: ' + str(event.type))
