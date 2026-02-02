from pynput.mouse import Controller
from pynput.keyboard import Controller
def control_mouse():
    mouse= Controller()
    mouse.position= (100,200)
#control_mouse()
def control_keyboard():
    keyboard= Controller()
    keyboard.type("hello world")

#control_keyboard()

