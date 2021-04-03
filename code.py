import time
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
shifter_pins = [board.GP18, board.GP19, board.GP20, board.GP21, board.GP10, board.GP11, board.GP12]
gears = [gear(digitalio.DigitalInOut(pin)) for pin in shifter_pins]

pressedButton = 0
prevButton = 0
while True:
    buttonvalue = (int)(not gears[0].pin.value)*2 + (int)(not gears[1].pin.value)*3 + (int)(not gears[2].pin.value)*5 + (int)(not gears[3].pin.value)*7 + (int)(not gears[4].pin.value)*11 + (int)(not gears[5].pin.value)*13 + (int)(not gears[6].pin.value)*17
    if pressedButton > prevButton:
        shifter.press_buttons((prevButton-pressedButton)*-1)
        prevButton = pressedButton
    elif pressedButton < prevButton:
        shifter.release_buttons(prevButton-pressedButton)
        prevButton = pressedButton
    pressedButton = (buttonvalue != 0)*(1*(buttonvalue%2 == 0) + 2*(buttonvalue%3 == 0) + 3*(buttonvalue%5 == 0) + 4*(buttonvalue%7 == 0) + 5*(buttonvalue%11 == 0) + 6*(buttonvalue%13 == 0) + 7*(buttonvalue%17 == 0))
