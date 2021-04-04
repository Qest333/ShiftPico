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

pressedButtons = [False, False, False, False, False, False, False]
while True:
    for i, button in enumerate(buttons):
        if pressedButtons[i] != button.value:
            if button.value:
                shifter.release_buttons(shifter_buttons[i])
            else:
                shifter.press_buttons(shifter_buttons[i])
            pressedButtons[i] = button.value
