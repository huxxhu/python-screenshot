# coding:utf-8
from selenium import webdriver
import re
import os
import psutil

# 載入 lists.txt
url_lists = []
with open('lists.txt') as f:
    for line in f:
        line = line.strip()
        url_lists.append(line)

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1440,900")
options.add_argument("--hide-scrollbars")

# 建立 Chrome Driver
driver = webdriver.Chrome(options=options)

# 建立圖片資料夾
dir_name = 'images'

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

print('------------------------------')

# 依序截圖
for i in url_lists:
    driver.get(i)
    print(driver.title)
    name = re.sub(r'\/|\.', "-", re.sub(
        r'https://www\.|http://www\.|https://www|http://|https://|www\.|.com|.tw|.io|.org|.webflow|events\.|event\.|', "", i).strip('/'))
    driver.save_screenshot(dir_name+'/'+name+'.png')

driver.quit()

print('------------------------------')
print('DONE :) see in '+dir_name+'/')

# 刪除背景 `chromedriver`
PROCNAME = "chromedriver"
for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()
        print('Kill '+PROCNAME)
