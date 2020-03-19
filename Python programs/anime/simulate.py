from pynput.mouse import Button,Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as Control
import time

def open_u_know_what():
    mouse=Controller()
    keyboard=Control()
    keyboard.press(Key.cmd)
    keyboard.press('e')
    keyboard.release(Key.cmd)
    keyboard.release('e')
    time.sleep(3)


    mouse.position=(100,560)
    mouse.click(Button.left,1)
    time.sleep(1)
    mouse.position=(575,240)
    mouse.click(Button.left,2)
    time.sleep(1)
    mouse.position=(875,240)
    mouse.click(Button.left,2)
    time.sleep(1)
    mouse.position=(1020,240)
    mouse.click(Button.left,2)
    time.sleep(1)
def coding():
    keyboard=Control()
    with open('gui.py','r',encoding='utf-8') as reader:
        code=reader.read().split('\n')
    length=len(code)
    print(code)


    time.sleep(2)

    for j in range(length):
        for k in code[j]:
            time.sleep(0.1)
            keyboard.press(k)
            keyboard.release(k)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
"""
    mouse.position=(850,240)
    mouse.click(Button.left,2)
    time.sleep(1)
    mouse.position=(950,240)
    mouse.click(Button.left,1)
"""
open_u_know_what()

