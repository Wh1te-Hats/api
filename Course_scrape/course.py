from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helper import *
import time

final_data = []


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={user_agent}')

def intialize_driver(chrome_options,start_url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(start_url)
    return driver

def count_words(text):
    words = text.split()
    return len(words)

# https://www.simplilearn.com/skillup-search?sortBy=Relevance&tag=java
# https://www.simplilearn.com/skillup-search?sortBy=Relevance&tag=management+skill


def course(course):
    final_data=[]
    no_of_words = count_words(course)
    if no_of_words == 1:
         q = course
    else:
         q = "+".join(course.split())
    print(q)

    start_url = f"https://www.simplilearn.com/skillup-search?sortBy=Relevance&tag={q}"
    driver = intialize_driver(chrome_options=chrome_options,start_url=start_url)
    for i in range(0,6):
        data = {}
        data['img']=check_exists_by_xpath_src(driver,f'//*[@id="skillup-search-results"]/div/div[{i+2}]/a/div/div[2]/img')

        data['course_name'] = check_exists_by_xpath_text(driver,f'//*[@id="skillup-search-results"]/div/div[{i+2}]/a/div/div[1]/div[2]')

        data['course_rating'] = check_exists_by_xpath_text(driver,f'//*[@id="skillup-search-results"]/div/div[{i+2}]/a/div/div[1]/div[3]/ul/li[1]/span')
        
        data['course_duration'] =  check_exists_by_xpath_text(driver,f'//*[@id="skillup-search-results"]/div/div[{i+2}]/a/div/div[1]/div[3]/ul/li[3]')   

        data['course_link'] = check_exists_by_xpath_href(driver,f'//*[@id="skillup-search-results"]/div/div[{i+1}]/a')

        final_data.append(data)
     #    save(final_data)
     

    return final_data


# print(course("Java"))

