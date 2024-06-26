#!/usr/bin/python3
"""
Author: Steve N.
REST API program
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.dominos.com/en/")
    time.sleep(5)

    elem = driver.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/a[2]")
    elem.click()
    time.sleep(5)

    elem = driver.find_element(By.XPATH, "//*[@id='City']")
    elem.send_keys("Lebanon")
    time.sleep(5)

main()
