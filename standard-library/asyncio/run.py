import asyncio

async def take_a_nap(s):
    print(f'I am going to snap for {s} seconds')
    await asyncio.sleep(s)
    print(f'I slept for {s} seconds')
    

asyncio.run(take_a_nap(1))
asyncio.run(take_a_nap(2))

