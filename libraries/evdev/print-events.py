#/usr/bin/env python3
import asyncio, evdev

nm_kb = 'LITEON Technology USB Multimedia Keyboard'
nm_ms = 'USB OPTICAL MOUSE ' # note the final space

dv_kb = [ devobj for devobj  in [ evdev.InputDevice(devpath) for devpath in evdev.list_devices() ] if devobj.name == nm_kb ][0]
dv_ms = [ devobj for devobj  in [ evdev.InputDevice(devpath) for devpath in evdev.list_devices() ] if devobj.name == nm_ms ][0]

async def print_events(dev):
    async for ev in dev.async_read_loop():
       if ev.type == evdev.ecodes.EV_SYN:
          print(f'EV_SYN {ev.code} {ev.value}')
       else:
          print(dev.path, evdev.categorize(ev), sep=': ')

for dv in dv_ms, dv_kb:
    asyncio.ensure_future(print_events(dv))

loop = asyncio.get_event_loop()
loop.run_forever()
