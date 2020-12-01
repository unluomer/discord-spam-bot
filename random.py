import mouseinfo
import time
import platform
import random2
import pyautogui
liste = ['i', 'v', 'm', 'l', 'b', 'd', "d", "e", "f", "w", "u", "y", "s", "a", "z", "x", "2", "3", "j", "r", "p"]
print(random2.choice(liste))
time.sleep(5)
a = 1
while a == 1:
	pyautogui.typewrite(random2.choice(liste))
	pyautogui.typewrite(random2.choice(liste))
	pyautogui.typewrite(random2.choice(liste))
	time.sleep(0.2)
	pyautogui.press('enter')
