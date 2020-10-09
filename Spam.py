#imports the selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException 

#creates an array of the letters of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#creates a function for finding elements in a webpage using xpath
def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

#start of the webscrapping
browser = webdriver.Chrome() #opens a chrome browser
browser.get(('https://mail.google.com/mail/#inbox')) #navigates to the gmail website
print("We are in Gmail!")
browser.implicitly_wait(2)
username = browser.find_element_by_id('identifierId') #tries to find the html identifierID for the email textbox
username.send_keys('') #send keys should be your email 
print("Email entered!")
nextButton = browser.find_element_by_id('identifierNext') #tries to find the html identifierID for the next button after entering a email address
nextButton.click() #clicks the button
browser.implicitly_wait(2)

username = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input') #finds the password textbox using xpath
username.send_keys('') #send keys should be your gmail password

nextButton = browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span') #finds the next button after entering your password using xpath
nextButton.click() #clicks the button

time.sleep(5)

#composes a new message and enters subject, recipients, and contents as well as sending the message
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
    username.send_keys('') #recipient email
    username = browser.find_element_by_xpath('//*[@id=":8w"]')
    username.send_keys('THE END IS NEAR RESPOND ASAP') #email subject
    username = browser.find_element_by_xpath('//*[@id=":a1"]')
    username.send_keys('THE END IS NEAR RESPOND ASAP') #email content
    nextButton = browser.find_element_by_xpath('//*[@id=":8m"]')
    nextButton.click() #sends the email
    time.sleep(5)
    browser.refresh()
    a = 0
    i += 1








 
   
