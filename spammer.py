import time , pyautogui
inp = input("enter your text for spam : ")
inp2 = input("how much? ")

inp2 = int(inp2)
inp2 = inp2 + 1
time.sleep(5)
for i in range(1,inp2):
    pyautogui.typewrite(inp)
    pyautogui.press("enter")    