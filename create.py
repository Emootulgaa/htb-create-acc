import requests
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import string
def Create(Email,Username,Fullname,Password):
    display = Display(visible=0, size=(1024, 768))
    display.start()
    driver = webdriver.Chrome()
    driver.get('https://app.hackthebox.com/invite')
    send = driver.find_element_by_id('input-35')
    send.send_keys(Username)
    send = driver.find_element_by_id('input-38')
    send.send_keys(Email)
    send = driver.find_element_by_id('input-41')
    send.send_keys(Fullname)
    send = driver.find_element_by_id('input-44')
    send.send_keys(Password)
    send = driver.find_element_by_id('input-48')
    send.send_keys(Password)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/form/div[5]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/form/div[6]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/form/button').click()
def getFakeMail():
    url = 'https://email-fake.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    mail = soup.find_all("span", {"id": "email_ch_text"})
    return mail[0].contents
ner = input("neree oruul 14 oos baga temdegt oroogu !!! : ")
Username = ner + '0'+''.join(random.choice(string.printable[0:62]) for i in range(14-(len(ner)+2)))+'0'
Email = getFakeMail()[0]
Fullname = "Tulgaa sda"
Password = "Tulgaa123"
Create(Email,Username,Fullname,Password)
print('Email:',Email+'\nPassword:',Password)
print('\n\nwish luck on your battleground')

