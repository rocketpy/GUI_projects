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
    
    meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_button.png')
    
    pyautogui.click()
    pyautogui.write(meetingid)

    media_button = pyautogui.locateAllOnScreen('media_btn.png')
    
    for button in media_button:
        pyautogui.moveTo(button)
        pyautogui.click()
        time.sleep(3)

