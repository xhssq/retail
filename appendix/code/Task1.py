from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://movie.douban.com/subject/26100958/comments?status=P')
time.sleep(1)
driver.find_element_by_class_name('nav-login').click()
driver.find_element_by_class_name('account-tab-account').click()

driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys(['18158648069'])
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys(['xuhong326035..'])
driver.find_element_by_class_name('account-form-field-submit ').click()
time.sleep(1)
driver.refresh()
user_info = []
citys = []
names = []
content = []
scores = []
evaluate = []
labs = []
votes = []
times = []
count = 0
while count < 25:

    for i in range(1, 21):
        xpath6 = '//*[@id="comments"]/div['+str(i)+']/div[2]/h3/span[2]/span[3]'
        xpath7 = '//*[@id="comments"]/div['+str(i)+']/div[2]/h3/span[2]/span[2]'
        try:
            times.append(driver.find_element_by_xpath(xpath6).get_attribute('title'))
        except:
            times.append(driver.find_element_by_xpath(xpath7).get_attribute('title'))
            continue

    for i in range(1,21):
        xpath5 = '//*[@id="comments"]/div[' + str(i) + ']/div[2]/h3/span[1]/span'
        votes.append(driver.find_element_by_xpath(xpath5).text)

        xpath4 = '//*[@id="comments"]/div[' + str(i) + ']/div[2]/h3/span[2]/span[1]'
        labs.append(driver.find_element_by_xpath(xpath4).text)

        xpath3 = '//*[@id="comments"]/div[' + str(i) + ']/div[2]/h3/span[2]/span[2]'
        scores.append(re.findall(r"\d+\.?\d*", (driver.find_element_by_xpath(xpath3).get_attribute('class'))))
        evaluate.append(driver.find_element_by_xpath(xpath3).get_attribute('title'))

        xpath2 = '//*[@id="comments"]/div[' + str(i) + ']/div[2]/p/span'
        content.append(driver.find_element_by_xpath(xpath2).text)

        xpath1 = '//*[@id="comments"]/div[' + str(i) + ']/div[2]/h3/span[2]/a'
        names.append(driver.find_element_by_xpath(xpath1).text)

        xpath = '//*[@id="comments"]/div[' + str(i) + ']/div[1]/a/img'
        driver.find_element_by_xpath(xpath).click()

        try:
            user_info.append(driver.find_element_by_xpath('//*[@id="profile"]/div/div[2]/div[1]/div/div').text)
            citys.append(driver.find_element_by_xpath('//*[@id="profile"]/div/div[2]/div[1]/div/a').text)
        except:
            citys.append('')
            driver.back()
            continue
        driver.back()
    driver.find_element_by_class_name('next').click()
    driver.refresh()
    count = count + 1
driver.close()

df = pd.DataFrame(list(zip(citys, content, evaluate, labs, names, scores,times, user_info, votes)),
                  columns=['citys', 'content', 'evaluate', 'labs', 'names', 'scores','times', 'user-info', 'votes'])
df.to_csv('fulian4Data.csv', encoding='utf_8_sig') 
