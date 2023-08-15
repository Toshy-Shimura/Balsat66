import time, os, usb_hid, board, digitalio
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

if 'run' in os.listdir():
    time.sleep(8)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    layout.write("\n")
    time.sleep(4)
    layout.write("\n")
    time.sleep(4)
    keyboard.send(Keycode.WINDOWS)
    time.sleep(4)
    layout.write("terminal")
    time.sleep(3)
    layout.write("\n")
    time.sleep(4)
    layout.write("cd ..\n")
    time.sleep(2)
    layout.write("cd ..\n")
    time.sleep(2)
    layout.write("cd ..\n")
    time.sleep(2)
    layout.write("cd ..\n")
    time.sleep(2)
    layout.write("cd home\n")
    time.sleep(2)
    layout.write("cd pi\n")
    time.sleep(2)
    layout.write("cd Desktop\n")
    time.sleep(2)
    layout.write("cd Balsat\n")
    time.sleep(2)
    layout.write("python3 main.py\n")
    
    led.value = True
    time.sleep(15)
    led.value = False

while not 'run' in os.listdir():
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
