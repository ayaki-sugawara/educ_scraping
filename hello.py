# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
INTERVAL = 0.07

driver = webdriver.Chrome(executable_path='./chromedriver')
url = "https://anotepad.com/"
driver.get(url)

title = driver.find_element_by_id("edit_title")
for s in "スクレイピングの世界へようこそ":
    title.send_keys(s)
    sleep(INTERVAL)
sleep(2)
edit_textarea = driver.find_element_by_id("edit_textarea")
with open('./teach.txt') as f:
    for line in f:
        for s in line:
            edit_textarea.send_keys(s)
            sleep(INTERVAL)
sleep(2)
driver.quit()
