import pyautogui
import math
import sys
import pyperclip

#1660, 1060 gizli simgeler
#1610, 1000 steam
#1665, 870 arkadaşlar
#402, 182 utku
#800, 720 chat

def main():
	pyautogui.moveTo(1660,1060,duration=0.5)
	pyautogui.click()
	pyautogui.moveTo(1610,1000,duration=0.5)
	pyautogui.click(button="right")
	pyautogui.moveTo(1665,870,duration=0.5)
	pyautogui.click()
	pyautogui.moveTo(402,182,duration=0.5)
	pyautogui.click()
	pyautogui.moveTo(800,720,duration=0.5)
	pyautogui.click()
	
	old = pyperclip.paste()

	for x in sys.argv[1:]:
		#pyautogui.write(str(x),interval=0.2)
		pyperclip.copy(x)
		pyautogui.hotkey("ctrl", "v")
		pyautogui.press('enter')

	pyperclip.copy(old)

if __name__ == '__main__':
	main()