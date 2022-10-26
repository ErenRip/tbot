from cmath import e
from lib2to3.pgen2.driver import Driver
import click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random


kullanıcıadları = []
parolalar = []

with open("account.txt", "r") as f:
  contents = f.read().split("\n")
  for content in contents:
    if not content == "":
      if (contents.index(content)%2) == 0:
        print(f"Ad: {content}")
        kullanıcıadları.append(content)
      else:
        print(f"Şifre: {content}")
        parolalar.append(content)
print("--------------------------------------------------")
yorumlar = []
with open("yrm.txt", "r") as f:
  contents = f.read().split("\n")
  for content in contents:
    if not content == "":
      if (contents.index(content)%2) == 0:
        print(f"Yorumlar:  {content}")
        yorumlar.append(content)
      else:
        print(f"Yorumlar:  {content}")
        yorumlar.append(content)

yr=random.choice(yorumlar)


account=0
i=0
time.sleep(5)

while True:  
 while i<len(kullanıcıadları):
      driver = webdriver.Chrome()
      driver.get("https://twitter.com/home?lang=tr")
      time.sleep(5)#int
      driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(kullanıcıadları[account])
      time.sleep(2)#int
      driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(Keys.ENTER)
      time.sleep(2)#int
      password=driver.find_element(By.XPATH,"//input[@autocomplete='current-password']")
      password.send_keys(parolalar[account]) 
      time.sleep(2)#int
      password.send_keys(Keys.ENTER)#girişkısmı
      time.sleep(3)#int
      driver.get('https://twitter.com/GSTV') #Tweet çekilicek yorum yapılıcak istenilen kullanıcı
      time.sleep(5)
      a=driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
      time.sleep(0.50)
      driver.find_element(By.XPATH,".//div[@data-testid='reply']").click()
      yr=random.choice(yorumlar)
      print("Yorum: "+yr)
      print(account)
      print("Tur: "+i)
      time.sleep(2)#int
      driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(yr)
      time.sleep(1) #int
      driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]').click()
      #çıkış yok
      
      print(f"Yorum Atıldı {yr}")
      time.sleep(3)#int
      i=i+1
      account=account+1
  #Kontrol   
 driver.get('https://twitter.com/GSTV')
 time.sleep(5)#int
 b=driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
 if(a==b):
    driver.refresh()
    time.sleep(15)#internet bağlantısına göre süreyi uzatın
    b=driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
    if(a!=b):
      account=0
      i=0
    else:
      continue  
 else:
    continue
  