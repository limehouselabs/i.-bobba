import asyncio
import logging

from bleak import BleakClient, BleakScanner

DEVICE_NAME = "iBobber"
IBOBBER_ADDR = "34:14:B5:4B:B9:15"
ACCEL_SERVICE_UUID = "1791FFA0-3853-11E3-AA6E-0800200C9A66"
CUSTOM_SERVICE_UUID = "1791FF90-3853-11E3-AA6E-0800200C9A66"
BATT_SERVICE_UUID = "0000180F-0000-1000-8000-00805F9B34FB"
DEVICE_SERVICE_UUID = "0000180A-0000-1000-8000-00805F9B34FB"
OAD_SERVICE_UUID = "F000FFC0-0451-4000-B000-000000000000"

ALL_SERVICES = [
    ACCEL_SERVICE_UUID,
    CUSTOM_SERVICE_UUID,
    BATT_SERVICE_UUID,
    DEVICE_SERVICE_UUID,
    OAD_SERVICE_UUID,
]


log = logging.getLogger("iBobber")
log.setLevel(logging.DEBUG)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        # level=logging.DEBUG,
        format="%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
        # datefmt="%Y-%m-%d %H:%M:%S",
    )
    log.debug("meow")
    for device, advert in sorted(
        (await BleakScanner.discover(return_adv=True)).values(),
        key=lambda d: -d[1].rssi,
    ):
        if not (device.name == DEVICE_NAME or advert.local_name == DEVICE_NAME):
            continue
        log.debug("Got a bobber at %s", device.address)
        log.debug("services be like %s", advert.service_uuids)

        async with BleakClient(
            device.address,
            # services=ALL_SERVICES,
            timeout=9999,
        ) as client:
            log.info("Connected!")
            for service in client.services:
                log.debug("%s: %s", service.handle, service.description)
                for characteristic in service.characteristics:
                    log.debug(
                        "  %s: %s",
                        characteristic.handle,
                        characteristic.description,
                    )


asyncio.run(main())
