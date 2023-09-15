from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options




def scrape_video(query):

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument(f'user-agent={user_agent}')
    
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.get("https://www.youtube.com/results?search_query={}".format(query))

    user_data = driver.find_elements(by=By.XPATH, value='//*[@id="video-title"]')
    imgs = driver.find_elements(by=By.XPATH, value='//*[@id="img"]')

    links = []

    for i, (data, img) in enumerate(zip(user_data, imgs)):

        if data.get_attribute('href') != None and data.get_attribute('title') != None:
            # links.append({0: data.get_attribute('href'), 1: data.get_attribute('title'), 2: img.get_attribute('src')})
            links.append('video')
            links.append(data.get_attribute('href'))
            links.append(data.get_attribute('title'))
            break
    driver.quit()
    return links

# link = scrape_video('Can I get a video on kmp algorithm')
# for _ in link:
#     print(_)


