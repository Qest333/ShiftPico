import board
import digitalio
import usb_hid

from adafruit_hid.gamepad import Gamepad

shifter = Gamepad(usb_hid.devices)
button_pins = (board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27)
shifter_buttons = (1, 2, 3, 4, 5, 6, 7)
buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

while True:
    for i, button in enumerate(buttons):
        shifter_button_num = shifter_buttons[i]
        if button.value:
            shifter.release_buttons(shifter_button_num)
        else:
            shifter.press_buttons(shifter_button_num)
