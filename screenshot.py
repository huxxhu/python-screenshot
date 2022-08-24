# coding:utf-8
from selenium import webdriver
import re

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

for i in url_lists:
    driver.get(i)
    print(driver.title)
    str = re.sub(
        r'https://www\.|http://www\.|https://www|http://|https://|www\.|.com|.tw|.io|.org|.webflow|events\.|event\.|', "", i).strip('/')
    str = re.sub(
        r'\/|\.', "-", str)
    driver.save_screenshot('images/'+str+'.png')

driver.close()
print('DONE')
