from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import logging
import json
# from dotenv import load_dotenv
from pymongo import MongoClient
import shutil
import requests
import time


# Define the path to chrome driver


def _build_query(query:str):
    return f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"

def _get_info(query):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument(f'user-agent={user_agent}')

        wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        # This searches images from google.com
        wd.get('https://google.com')
        # image_urls = set()

        wd.get(_build_query(query))

        # img.Q4LuWd is the google tumbnail selector
        thumbnails = wd.find_elements(by=By.CSS_SELECTOR, value="img.Q4LuWd")
        urls = []
        for img in thumbnails[:10]:
            try:
                img.click()
                time.sleep(1)
                page_source = wd.page_source
                soup = BeautifulSoup(page_source, 'html.parser')
                images = soup.find_all('img', class_='r48jcc pT0Scc iPVvYb')
                for image in images:
                    src_value = image.get('src')
                    urls.append(src_value)
            except Exception as e:
                continue
        return urls


def scrape_images(query):
    image_info = _get_info(query)
    return image_info

# url = scrape_images('what is depth first search')
# print(url)




# imagePath = "https://edumilestones.com/blog/images/What-after-12th.png"

def img_download(imagePath):
    '''
    OPEN BROWSER AND GET IMAGE LINK TO BE DOWNLOADED
    '''
    response = requests.get(imagePath, stream = True)
    path = "app/images/" + imagePath.split("/")[-1]
    with open(path, 'wb') as f:
        print("Image Saved")
        shutil.copyfileobj(response.raw, f)
        return path

def check_exists_by_xpath_text(driver,xpath):
    try:
        value = driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        logging.debug(f'XPATH NOT FOUND ---- || {xpath}')
        return "null"
    return value.text

def check_exists_by_xpath_src(driver,xpath):
    try:
        value = driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        logging.debug(f'XPATH NOT FOUND ---- || {xpath}')
        return "null"
    return value.get_attribute('src')

def check_exists_by_xpath_href(driver,xpath:str,required_link:str=None):
    try:
       link = required_link
       value = driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        logging.debug(f'XPATH NOT FOUND ---- || {xpath}')
        return "null"
    # if link == "registration_link" and urlparse(value.get_attribute('href')).netloc != "www.naukri.com" :
    #     return value.get_attribute('href')
    # else:
    return value.get_attribute('href')

def check_exists_by_classname(driver,xpath):
    try:
        value = driver.find_element(By.CLASS_NAME,xpath)
    except NoSuchElementException:
        return "null"
    return value

def find_registration_link(driver,data):
    a = data["job_slug"]
    b = data["company_name"]
    driver.get("https://www.google.com/")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(f"""{a} "{b}" """)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
                
            
    value = check_exists_by_xpath_href(driver,'//*[@id="rso"]/div[1]/div/div/div[1]/div/a',"registration_link")
            # print("REGISTRATION LINK: {}".format(data["registration_link"]))
    driver.back()
    driver.back()
    driver.implicitly_wait(10)
    return value

def save(data):
    f = open('data.json')
    final_data = json.load(f)
    final_data.append(data)
    json_object = json.dumps(final_data, indent=4, ensure_ascii=False)
    with open("data.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)

def get_database(collection_name:str):
    CONNECTION_STRING = "mongodb+srv://samrath:samrath@pragati.oeap8sk.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db = client['pragati']
    return db[f'{collection_name}']
  
def save_db(data:json,collection_name:str):
   dbname = get_database(f'{collection_name}')
   dbname.insert_one(data)

def intialize_driver(chrome_options,link:str):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    start_url = link
    driver.get(start_url)
    return driver

def trigger_first_scrape(driver,data,job_list,i,j):
    
    data["registration_link"] = find_registration_link(driver,data)
               
    data["company_logo"] = check_exists_by_xpath_src(driver,'/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/a/img')

    data["job_duration"] = check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[1]/span')

    data["job_stipend"] = check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[2]/span').replace('₹','')

    data["job_location"] = (check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[3]/span')).split(",")

    data["job_description"] = check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[2]/div[1]')

    data["job_role"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[1]/span/a')

    data["industry_type"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[2]/span/a')

    data["functional_area"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[3]/span/a')

    data["employment_type"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[4]/span/span')

    data["role_category"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[5]/span/span')

    data["education_qualification"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[3]')

    data["about_company"] = check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[3]/div[1]')
            
    data["company_address"] = check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[3]/div[3]/span')

    print(f"{job_list.upper()} || {j} CYCLE || {i} DONE")
    return data

def trigger_second_scrape(driver,data,job_list,i,j):

    data["registration_link"] = find_registration_link(driver,data)
               
    data["company_logo"] = check_exists_by_xpath_src(driver,'/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/a/img')

    data["job_duration"] = check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[1]/span')

    data["job_stipend"] = check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[2]/span')

    data["job_location"] = (check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[3]/span')).split(",")

    data["job_description"] = check_exists_by_xpath_text(driver,'/html/body/div[1]/main/div[2]/div[2]/section[2]/div[1]')

    data["job_role"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[1]/span/a')

    data["industry_type"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[2]/span/a')

    data["functional_area"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[3]/span/a')

    data["employment_type"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[4]/span/span')

    data["role_category"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]/div[5]/span/span')

    data["education_qualification"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[3]')

    data["about_company"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[4]/div[1]')
            
    data["company_address"] = check_exists_by_xpath_text(driver,'//*[@id="root"]/main/div[2]/div[2]/section[4]/div[3]')

    print(f"{job_list.upper()} || {j} CYCLE || {i} DONE")
    return data

def read_json():
    "Return json data"
    f = open("app/dataset/college.json")
    data = json.load(f)
    return data