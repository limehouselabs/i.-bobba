import asyncio
from pprint import pprint

from bleak import BleakScanner


async def main():
    print("\n\n\n")
    for device, advert in sorted(
        (await BleakScanner.discover(return_adv=True)).values(),
        key=lambda d: -d[1].rssi,
    ):
        print(f"{device.name}/{advert.local_name}: {device.address} at {advert.rssi}db")
        print("services:", advert.service_uuids)
        print("service data:")
        pprint(advert.service_data)
        print("\n\n")
    print("\n")


if __name__ == "__main__":
    asyncio.run(main())
