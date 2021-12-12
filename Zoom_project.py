import time
import pandas as pd
from datetime import datetime

import subprocess
import pyautogui


def zoom_sign_in(id, password):
    subprocess.call('C:\\Users\AppData\Roaming\Zoom\bin\Zoom.exe')
    time.sleep(8)
    join_button = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_button)
    pyautogui.click()


