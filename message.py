


import webbrowser as web
from urllib.parse import quote
import pyautogui as pg
import time


# for specific person
# Details of preson
phone_no = "User mobile number"
message = "Well Done!"

# webbrowser window open
web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
time.sleep(7)

# clicking at the middile of screen
screenWidth, screenHeight = pg.size() 
print(screenWidth, screenHeight)
pg.click(screenWidth/2, screenHeight/2)
pg.press("enter")




# # for group 
# code = "Resources"
# message = "Well done!"

# web.open("https://web.whatsapp.com/")

# time.sleep(3)
# # clicking at the middile of screen
# screenWidth, screenHeight = pg.size() 
# pg.click(screenWidth/2, screenHeight/2)
# time.sleep(2)
# print(screenHeight,screenWidth)
# # arguments img.click work for my screen adjust according to yours 
# pg.click(215,215)  #scwidth/9, scheight/5
# pg.typewrite(code,0.5)
# time.sleep(5)
# pg.press("enter")
# for char in message:
#     if char == "\n":
#         pg.hotkey("shift", "enter")
#     else:
#         pg.typewrite(char)
# pg.press("enter")

