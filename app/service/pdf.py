from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time



def get_pdf_links(x):
	if x is not None:
		return x[-4:] == ".pdf"
	return False

def pdf_search(site):
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.get("https://www.google.com")

    search_bar = driver.find_element(by=By.XPATH, value="//*[@id=\"APjFqb\"]")
    search_expr = "{} filetype:pdf "
    search_bar.send_keys(search_expr.format(site))
    search_bar.send_keys(Keys.RETURN)

    pdf_links = []
    try:
       links = [x.get_attribute("href") for x in driver.find_elements(by=By.TAG_NAME, value="a")]
       print(links)
       print(x.get_attribute("href") for x in driver.find_elements(by=By.TAG_NAME, value="a"))
       pdf_links += list(filter(get_pdf_links, links))
       time.sleep(0.25)
       driver.find_element(by=By.ID, value="pnnext").click()
       driver.quit()
       return pdf_links

    except Exception as e:
        pass

# link = pdf_search('dsce.edu.in')
# for _ in link:
#     print(_)