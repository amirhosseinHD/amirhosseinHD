#import the library's we need
import time , pyautogui
#get the text and number of text
inp = input("enter your text for spam : ")
inp2 = input("how much? ")
inp2 = int(inp2)
inp2 = inp2 + 1
#*if you want too change sleep time change the number*
time.sleep(5)
for i in range(1,inp2):
    pyautogui.typewrite(inp)
    pyautogui.press("enter")    
