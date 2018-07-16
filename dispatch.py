#! python3

import sys, requests, pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
browser.get('http://gmail.com')
loginElem = browser.find_element_by_name('identifier')
loginElem.send_keys('postovitvera@gmail.com')
loginElem.send_keys(Keys.ENTER)

element = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.NAME, 'password')))

passwElem = browser.find_element_by_name('password')
passwElem.send_keys('verochka321')
passwElem.send_keys(Keys.ENTER)

a = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='Написать']")))

write_let = browser.find_element_by_xpath("//div[text()='Написать']")
write_let.click()

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

genMail = browser.find_element_by_tag_name('textarea')
genMail.send_keys(address)
genMail.send_keys(Keys.ENTER)

el = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Тело письма']")))

textSMS = browser.find_element_by_xpath("//div[@aria-label='Тело письма']")
textSMS.send_keys(input('Введите сообщение'))

cl_send = browser.find_element_by_xpath("//div[text()='Отправить']")
cl_send.click()
