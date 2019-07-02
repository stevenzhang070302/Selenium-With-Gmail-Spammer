from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
       
def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

browser = webdriver.Chrome()
browser.get(('https://mail.google.com/mail/#inbox'))
print("We are in Gmail!")
browser.implicitly_wait(2)
username = browser.find_element_by_id('identifierId')
username.send_keys('roberttzhang2800')
print("Email entered!")
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
print("Password entered!")
browser.implicitly_wait(2)

username = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
username.send_keys('happymath28')

nextButton = browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
nextButton.click()

time.sleep(5)

i = 1
a = 0
xpath_ID1 = '//*[@id=":3'
xpath_ID2 = '"]/div/div'
print(check_exists_by_xpath(xpath_ID1 + alphabet[a] + xpath_ID2))
while i <= 3:
    while a <= 25:
        if check_exists_by_xpath(xpath_ID1 + alphabet[a] + xpath_ID2):
            print("True")
            nextButton = browser.find_element_by_xpath(xpath_ID1 + alphabet[a] + xpath_ID2)
            nextButton.click()
        print("False")
        a = a + 1
    username = browser.find_element_by_xpath('//*[@id=":9e"]')  
    username.send_keys('stevenzhang070302@gmail.com')
    username = browser.find_element_by_xpath('//*[@id=":8w"]')
    username.send_keys('THE END IS NEAR RESPOND ASAP')
    username = browser.find_element_by_xpath('//*[@id=":a1"]')
    username.send_keys('THE END IS NEAR RESPOND ASAP')
    nextButton = browser.find_element_by_xpath('//*[@id=":8m"]')
    nextButton.click()
    time.sleep(5)
    browser.refresh()
    a = 0
    i += 1








 
   
