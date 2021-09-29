from adafruit_ble import BLERadio
import _bleio
from _bleio import adapter
import board
import digitalio
import time
from beacons import *

# turning the blue led ON
led = digitalio.DigitalInOut(board.BLUE_LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

ble = BLERadio()
adp = adapter

## Setting up the adapter now
m = Flag() + CompleteName("nrf52 som")

adp.start_advertising(m,
                      connectable=True,
                      anonymous=True,
                      timeout=30,
                      interval=0.1,
                      tx_power=4)

while True:
    time.sleep(0.1)
