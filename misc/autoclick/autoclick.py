import pyautogui
import time
import sys

print("You have 10 seconds to move your mouse to the position you want clicked\nMove mouse to top left of screen to exit")
time.sleep(10)
while 1:
    try:
        pyautogui.click()
    except:
        sys.exit()        