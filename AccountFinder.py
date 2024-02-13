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

def login(id, pw):
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)
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
    first.click()
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

def move_next(driver):
    right = driver.find_element(By.CSS_SELECTOR('a.coreSpriteRightPaginationArrow'))
    right.click()
    time.sleep(3)
        

def main():
    logging.basicConfig(filename='CheckLog.log', level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s')
    #실행부
    login(cr_id, cr_pw)
    




if __name__ == "__main__":
    main()

    
    
    
    
    


    

