#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from random import choice, sample
from details import details

zonal_url = 'https://healingstreams.tv/3days/online_reg.php?r=2TCG3'
options = Options()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
driver.get(zonal_url)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")

driver.find_element(By.XPATH, '//*[@id="firstname"]').clear()
driver.find_element(By.XPATH, '//*[@id="firstname"]').send_keys("Olagoke")

driver.find_element(By.XPATH,'//*[@id="lastname"]').clear()
driver.find_element(By.XPATH, '//*[@id="lastname"]').send_keys("Midas")

driver.find_element(By.XPATH, '//*[@id="email"]').clear()
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('midasgoke@outlook.com')

Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/form/div[4]/div/select')).select_by_value('Nigeria')

Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/form/div[5]/div[1]/select')).select_by_value('Edo')

driver.find_element(By.CSS_SELECTOR, '#city').clear()
driver.find_element(By.CSS_SELECTOR, '#city').send_keys('Benin')

# if not driver.find_element(By.CSS_SELECTOR, '#need_healing2').is_selected:
driver.find_element(By.CSS_SELECTOR, '#need_healing2').send_keys(Keys.SPACE)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
# driver.find_element_by_css_selector('//*[@id="form2"]/input').click()
driver.find_element(By.XPATH, '//*[@id="form2"]').submit()

driver.get(zonal_url)

print("Done")