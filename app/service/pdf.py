from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup



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

    search_bar = driver.find_element(By.NAME, "q")
    search_expr = "{} filetype:pdf "
    search_bar.send_keys(search_expr.format(site))
    search_bar.send_keys(Keys.RETURN)

    pdf_links = []
    try:
        time.sleep(2)  # Allow some time for the search results to load

        # Extract page source using BeautifulSoup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find all hrefs that end with ".pdf" using BeautifulSoup
        pdf_links += [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]

        return pdf_links
    except Exception as e:
        print("An error occurred:", str(e))


# link = pdf_search('dsce.edu.in')
# for _ in link:
#     print(_)