from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException 

def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
'''
def check_for_textErrors(text) :
    try:
        username.send_keys('stevenzhang070302@gmail.com')
    except:
'''       

i = 0
while i <= 9:
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
    time.sleep(5)
    username = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    username.send_keys('happymath28')
    nextButton = browser.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
    nextButton.click()
    time.sleep(5)

    if check_exists_by_xpath('//*[@id=":3z"]/div/div'):
        print("true")
        nextButton = browser.find_element_by_xpath('//*[@id=":3z"]/div/div')
        nextButton.click()
        print("Compose button clicked")
        time.sleep(15)
    elif check_exists_by_xpath('//*[@id=":3o"]/div/div'):
        print("true")
        nextButton = browser.find_element_by_xpath('//*[@id=":3o"]/div/div')
        nextButton.click()
        print("Compose button clicked")
        time.sleep(15)
    elif check_exists_by_xpath('//*[@id=":40"]/div/div'):
        print("true")
        nextButton = browser.find_element_by_xpath('//*[@id=":40"]/div/div')
        nextButton.click()
        print("Compose button clicked")
        time.sleep(15)
        if check_exists_by_xpath('//*[@id=":9e"]'): 
            print("true")
            username = browser.find_element_by_xpath('//*[@id=":9e"]')
            username.send_keys('robertzhang2800@gmail.com')
            print("Typed in email address")
            if check_exists_by_xpath('//*[@id=":8w"]'):
                print("true")
                username = browser.find_element_by_xpath('//*[@id=":8w"]')
                username.send_keys('THE END IS NEAR RESPOND ASAP')
                print("Typed in subject")
                if check_exists_by_xpath('//*[@id=":a1"]'):
                    print("true")
                    username = browser.find_element_by_xpath('//*[@id=":a1"]')
                    username.send_keys('THE END IS NEAR RESPOND ASAP')
                    print("Typed in text")
                    if check_exists_by_xpath('//*[@id=":8m"]'):
                        print("true")
                        nextButton = browser.find_element_by_xpath('//*[@id=":8m"]')
                        nextButton.click()
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



 
   

