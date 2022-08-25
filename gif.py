# coding:utf-8
from selenium import webdriver
import re
import os
import psutil
import imageio.v2 as imageio
from PIL import Image

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
dir_name = 'gif'

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

print('------------------------------')

# 依序截圖
for i in url_lists:
    driver.get(i)
    print(driver.title)
    name = re.sub(r'\/|\.', "-", re.sub(
        r'https://www\.|http://www\.|https://www|http://|https://|www\.|.com|.tw|.io|.org|.webflow|events\.|event\.|', "", i).strip('/'))

    # save GIF
    gif_width = 685
    gif_quality = 50
    gif_fps = 20
    gif_dur = int(1000/gif_fps)

    # mode: “I” for multiple images
    # TODO: GIF duration
    with imageio.get_writer(dir_name+'/'+name+'.gif', mode="I") as writer:
        for i in range(gif_fps):
            # TODO: 暫存?
            img_path = dir_name+'/'+name+'_'+str(i+1)+'.png'
            driver.save_screenshot(img_path)
            width, height = Image.open(img_path).size
            rate = 685 / width
            Image.open(img_path).resize(
                (int(width * rate), int(height * rate))).save(img_path, optimize=True)
            writer.append_data(imageio.imread(img_path))

# TODO: GIF 壓縮

driver.quit()

print('------------------------------')

# delete png
for item in os.listdir(dir_name):
    if item.endswith(".png"):
        os.remove(os.path.join(dir_name, item))

print('DONE :) see in '+dir_name+'/')

# 刪除背景 `chromedriver`
PROCNAME = "chromedriver"
for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()
        print('Kill '+PROCNAME)
