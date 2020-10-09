#imports libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException 

#creates a xpath detection function
def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
'''
def check_for_textErrors(text) :
    try:
        username.send_keys('') #Choose the receiving email
    except:
'''       

#starts the webscrapping
i = 0
while i <= 9:
    browser = webdriver.Chrome() #opens chrome
    browser.get(('https://mail.google.com/mail/#inbox')) #goes to gmail website
    print("We are in Gmail!")
    browser.implicitly_wait(2)
    username = browser.find_element_by_id('identifierId')
    username.send_keys('') #Signing into an email
    print("Email entered!")
    nextButton = browser.find_element_by_id('identifierNext')
    nextButton.click() #clicks next after entering a email address
    time.sleep(5)
    username = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    username.send_keys('') # Email Password
    nextButton = browser.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
    nextButton.click() #clicks entering after entering a password
    time.sleep(5)
    
    #created multiple if statements to see which xpath element Gmail would generate for the compose button
    if check_exists_by_xpath('//*[@id=":3z"]/div/div'):
        print("true")
        nextButton = browser.find_element_by_xpath('//*[@id=":3z"]/div/div')
        nextButton.click() #composes a email button is clicked
        print("Compose button clicked")
        time.sleep(15)
    elif check_exists_by_xpath('//*[@id=":3o"]/div/div'):
        print("true")
        nextButton = browser.find_element_by_xpath('//*[@id=":3o"]/div/div')
        nextButton.click() #composes a email button is clicked
        print("Compose button clicked")
        time.sleep(15)
    elif check_exists_by_xpath('//*[@id=":40"]/div/div'):
        print("true")
        nextButton = browser.find_element_by_xpath('//*[@id=":40"]/div/div')
        nextButton.click() #composes a email button is clicked
        print("Compose button clicked")
        time.sleep(15)
        if check_exists_by_xpath('//*[@id=":9e"]'): 
            print("true")
            username = browser.find_element_by_xpath('//*[@id=":9e"]')
            username.send_keys('') #Choose receiving email
            print("Typed in email address")
            if check_exists_by_xpath('//*[@id=":8w"]'):
                print("true")
                username = browser.find_element_by_xpath('//*[@id=":8w"]')
                username.send_keys('THE END IS NEAR RESPOND ASAP') #types in subject of the email
                print("Typed in subject")
                if check_exists_by_xpath('//*[@id=":a1"]'):
                    print("true")
                    username = browser.find_element_by_xpath('//*[@id=":a1"]')
                    username.send_keys('THE END IS NEAR RESPOND ASAP') #types in the content of the email
                    print("Typed in text")
                    if check_exists_by_xpath('//*[@id=":8m"]'):
                        print("true")
                        nextButton = browser.find_element_by_xpath('//*[@id=":8m"]')
                        nextButton.click() #clicks the send button on the email
                        print("SENT EMAIL")
                    else:
                        print("False")
                        pass
                else:
                    print("False")
                    pass
            else:
                print("False")
                pass
        else:
            print("False")
            pass
    else:
        print("False")
        pass
    time.sleep(5)
    i += 1
    browser.close()
    print("RESTARTING PROCESS")
print("PROCESS END")



 
   

