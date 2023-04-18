import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

#使用selenium
chrome_options = Options() 
chrome_options.add_argument('--headless')  # 啟動Headless 無頭
chrome_options.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.tmrt.com.tw/metro-life/ride-time-and-fare") # 更改網址以前往不同網頁

location = driver.find_element_by_name("stationSelection")
select_location = Select(location) #找尋"單一車站至所有車站"下拉式選單
select_location.select_by_value("95ea9819-79c6-4069-bee9-80e09f9ceb75") #選擇四維國小

time.sleep(2) #loading時間

#爬蟲
MRT_table = pd.read_html(driver.page_source)


title = MRT_table[0]
title.columns = ["起站", "訖站", "單程票票價", "電子票證", "敬老卡、愛心卡、愛心陪伴卡", "乘車時間(分鐘)"]
print(MRT_table)


