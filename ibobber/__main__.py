import asyncio

from bleak import BleakScanner


async def main():
    devices = await BleakScanner.discover(return_adv=True)

    for d, a in devices.values():
        print()
        print(d)
        print("-" * len(str(d)))
        print(a)


asyncio.run(main())
