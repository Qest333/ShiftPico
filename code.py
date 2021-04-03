import board
import digitalio
import usb_hid
from adafruit_hid.gamepad import Gamepad

class gear:
    def __init__(self, pin):
        self.pin = pin
        self.pin.direction = digitalio.Direction.INPUT
        self.pin.pull = digitalio.Pull.UP

shifter = Gamepad(usb_hid.devices)
gears = list()
prevButt = 1
shifter_pins = [board.GP18, board.GP19, board.GP20, board.GP21, board.GP10, board.GP11, board.GP12]

for pins in shifter_pins:
    gears.append(gear(digitalio.DigitalInOut(pins)))

while True:
    buttonvalue = (int)(not gears[0].pin.value) + (int)(not gears[1].pin.value)*2 + (int)(not gears[2].pin.value)*3 + (int)(not gears[3].pin.value)*4 + (int)(not gears[4].pin.value)*5 + (int)(not gears[5].pin.value)*6 + (int)(not gears[6].pin.value)*7
    if buttonvalue != 0:
        shifter.press_buttons(buttonvalue)
        prevButt = buttonvalue
    else: shifter.release_buttons(prevButt)
