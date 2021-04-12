from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
from datetime import datetime
import pandas as pd
import time

opt = webdriver.ChromeOptions()


#watch in youtube how to download the chrome web driver

def sign_in(meetingid, pswd):
    #webdriver.Chrome("Enter the path of your chrome web driver.")
    #for our pc we get C:\users\. we get single slash, make that as double slash
    #after pasiting the path make the slash as double slash and in last entert the file name,for clarity check my path
 Browser = webdriver.Chrome("C:\\Users\\sasha\\Downloads\\chromedriver_win32 (1)\\chromedriver")
 Browser.get('https://zoom.us/join')
 pyautogui.write(meetingid)
 pyautogui.press('enter') 
 time.sleep(5)
 #here also change the path,keep that screenshot path in this place
 openzoom = pyautogui.locateCenterOnScreen(r"C:\\Users\\sasha\\OneDrive\\Documents\\Python\\My bot\\allow.png",grayscale=True,confidence=.9)
 pyautogui.moveTo(openzoom)
 pyautogui.click()
 print(openzoom)
 time.sleep(5)
 pyautogui.write(pswd)
 time.sleep(2)
 pyautogui.press('enter')

#here also change the path, and keep the path for the monday.csv
df = pd.read_csv(r"C:\\Users\\sasha\\OneDrive\\Documents\\Python\\My bot\\monday.csv")

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(5)
       print('signed in')
