import pyautogui, keyboard, os
from pathlib import Path
from datetime import datetime as dt

pictures = str(Path.home()) + "/Pictures/Python-ScreenShotter/"

while   True:
    if keyboard.is_pressed('f8'):
        if not os.path.exists(pictures):
            os.makedirs(pictures)
        file = "{0}{1}.png".format(pictures, dt.now().strftime("%Y-%m-%d %H-%M-%S"))
        screenshot = pyautogui.screenshot(file)
        print("Screenshot Taken")