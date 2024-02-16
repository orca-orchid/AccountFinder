from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import logging
import time
import re

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(r"D:\Poly_Work\Code\AccountCrawler\chromedriver_win32\chromedriver.exe")
cr_id = "orca0orchid"
cr_pw = "qjarhfosksch"

def login(browser, id, pw):
    input_id = browser.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[1]/div[1]/label[1]/input[1]")
    input_id.send_keys(id)
    input_pw = browser.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[2]/div[1]/label[1]/input[1]")
    input_pw.send_keys(pw)
    input_pw.send_keys(Keys.RETURN)
    time.sleep(5)
    #나중에 하기
    btn_later1 = browser.find_element(By.XPATH, "//*[@role='button']")
    btn_later1.click()
    time.sleep(5)
    btn_later2 = browser.find_element(By.XPATH, "//*[@role='dialog']//button[contains(text(), '나중에')]")
    btn_later2.click()
    time.sleep(10)


def word_url(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    return url

def select_first(driver):
    first = driver.find_elements(By.XPATH, "//article//a[@role='link']")
    first[0].click()
    time.sleep(5)

def get_content(driver):
    html=driver.page_source
    soup=BeautifulSoup(html, 'lxml')
    try:
        content = soup.select('div.C')
    except:
        content = ''

    tags = re.findall(r"#[^s#,\\]+", content)
    #date
    #like
    #place
    
    data = [content, tags]
    return data

#here
def move_next(driver):
    right = driver.find_element(By.XPATH, "//dialog//svg[@aria-label='다음']")
    right.click()
    time.sleep(3)
        

def main():
    logging.basicConfig(filename='CheckLog.log', level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s')
    
    word = "beautytips"
    results = []
    targetNum = 10
    
    #실행부
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)
    login(browser, cr_id, cr_pw)
    browser.get(word_url(word))
    time.sleep(10)
    select_first(browser)

    for i in range(targetNum):
        try:
            data = get_content(browser)
            results.append(data)
            move_next(browser)
        except:
            time.sleep(2)
            move_next(browser)
        time.sleep(5)

    print(results)
  




if __name__ == "__main__":
    main()

    
    
    
    
    


    

