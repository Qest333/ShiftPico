import time
import board
import digitalio
import usb_hid
from adafruit_hid.gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

btn_a = digitalio.DigitalInOut(board.GP19)
btn_a.direction = digitalio.Direction.INPUT
btn_a.pull = digitalio.Pull.UP

while True:
    buttonavalue = btn_a.value
    if buttonavalue == 0:
        gp.click_buttons(1)
        time.sleep(0.2)