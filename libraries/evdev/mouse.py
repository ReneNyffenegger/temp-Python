import asyncio
# import atexit
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

dv_kb = [ devobj for devobj  in [ evdev.InputDevice(devpath) for devpath in evdev.list_devices() ] if devobj.name == nm_kb ][0]
dv_ms = [ devobj for devobj  in [ evdev.InputDevice(devpath) for devpath in evdev.list_devices() ] if devobj.name == nm_ms ][0]

# print(type(dv_kb))
# print(type(dv_ms))

print(f'Keyboard at {dv_kb.path}')
print(f'Mouse    at {dv_ms.path}')

async def handle_events(device):
    async for ev in device.async_read_loop():
        if ev.type == evdev.ecodes.EV_KEY:
           print(device.path, evdev.categorize(ev), sep=': ')
           if ev.code in [evdev.ecodes.BTN_LEFT, evdev.ecodes.BTN_MIDDLE, evdev.ecodes.BTN_RIGHT]:
              print('btn')


for dev in dv_ms, dv_kb:
    asyncio.ensure_future(handle_events(dev))

loop = asyncio.get_event_loop()
loop.run_forever()

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
