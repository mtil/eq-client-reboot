import pygetwindow as gw
import pywinauto
import time
import keyboard

token = ""

def login(color):


    # EULA Window Accept Button
    # (Assuming coordinates are correct, you may need to adjust)
    pywinauto.mouse.click(button='left', coords=(963, 673))
    time.sleep(.1)

    # SOE Splash Screen Click
    pywinauto.mouse.click(button='left', coords=(963, 673))

    # Wait time for splash screen transition
    time.sleep(.1)

    # Login button
    pywinauto.mouse.click(button='left', coords=(915, 415))
    pywinauto.mouse.click(button='left', coords=(886, 491))
    for letter in token:
        keyboard.send(letter)
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('enter')