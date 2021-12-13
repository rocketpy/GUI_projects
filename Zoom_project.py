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

    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(5)
    password_button = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(password_button)
    pyautogui.click()
    pyautogui.write(password)
    pyautogui.press('enter')
    time.sleep(20)
    frame = 2
    while frame==2:
        join_window = pyautogui.locateCenterOnScreen('join_mic.png')
        if window_mic == join_window:
            frame = 3

    pyautogui.moveTo(join_with_micro)
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey('alt','f')
    time.sleep(5)
    pyautogui.hotkey('alt','a')

