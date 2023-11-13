import pyautogui
import time

position = pyautogui.position()
pesan ="hello word"
for a in range(20):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.1)
    pyautogui.typewrite(["enter"])