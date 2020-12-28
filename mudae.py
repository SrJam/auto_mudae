from pyautogui import moveTo, dragTo, hotkey, click
import keyboard
from tkinter import Tk
from time import sleep

minimo = int(373)


sleep(2)

def irRank(minimo):

    sleep(2)

    try:
        moveTo(400, 341)
        dragTo(354, 341, 0.2, button='left')   
        hotkey('ctrl', 'c')
        root = Tk()
        root.withdraw()
        number = root.clipboard_get()
        number = number.split("#")
        number = number[1]

    except IndexError:
        moveTo(400, 327)
        dragTo(356, 327, 0.2, button='left')   
        hotkey('ctrl', 'c')
        root = Tk()
        root.withdraw()
        number = root.clipboard_get()
        number = number.split("#")
        number = number[1]

    number = int(number)
    if number >= minimo:
        return False
    else:
        return True 


for i in range(10):
    keyboard.write('$wa')
    keyboard.press_and_release('enter')
    result = irRank(minimo)    
    if result == True:
        moveTo(326, 650)
        click()
    else:
        pass


    

    