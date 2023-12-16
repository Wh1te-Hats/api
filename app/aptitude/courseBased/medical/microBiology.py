import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={user_agent}')

def remove_html_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text

def extract_question_range(text):
    # Use regular expression to find the range
    match1 = re.search(r'Q\.Nos\. (\d+)(?: - (\d+))?', text)
    match2 = re.search(r'Q\.No\. (\d+)', text)

    if match1:
        start = int(match1.group(1))
        end = int(match1.group(2)) if match1.group(2) else None
        return start, end
    elif match2:
        start = int(match2.group(1))
        return start,None
    else:
        return None, None

def microbiology_aptitude():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    # Step 1: Visit the website
    driver.get("https://www.indiabix.com/online-test/microbiology-test/random")
    time.sleep(3)

    # Step 2: Click the "Start Test" button
    start_test_button = driver.find_element(By.ID, "btnStartTest")
    driver.execute_script("arguments[0].click();", start_test_button)
    time.sleep(3)

    # SCRAPPING THE QUESTIONS

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')


    bix_div_containers = soup.find_all('div', class_='bix-div-container')
    direction_divs = soup.find_all('div', class_='direction-div')

    direction_div_list = []
    
    i = 0
    for j in direction_divs:
        # print(i)
        sentence = j.get_text().replace("\n","")
        sentence = " ".join(sentence.split())
        start ,end = extract_question_range(sentence)
        if start is not None and end is None:
            if(i+1<=start):
                while(i+1 <= start):
                    if i+1 == start:
                        direction_div_list.append(sentence)
                        i += 1  
                    else:
                        direction_div_list.append("")
                        i+=1
        else:
            if i+1 < start:
                while(i+1 == start):
                    i+=1
            n = end-start + 1
            while(n!=0):
                direction_div_list.append(sentence)
                n -= 1
                i +=1
    
    if len(direction_div_list) < 20:
        while (len(direction_div_list) <= 20):
            direction_div_list.append("")

    question_data_list = []
    direction_question_list = [None] * 20

    for index, bix_div_container in enumerate(bix_div_containers, start=0):
        # Find the question number
        question_number = bix_div_container.find('div', class_='bix-td-qno').text.strip()

        # Find all <img> tags
        img_tags = bix_div_container.find_all('img')

        for img_tag in img_tags:
            src = img_tag.get('src')

            if src and src.startswith('/'):
                img_tag['src'] = 'https://www.indiabix.com' + src

        # Find the question text HTML as a string
        question_text_html = bix_div_container.find('div', class_='bix-td-qtxt').get_text()

        # Find all options HTML as strings
        option_divs = [option.get_text() for option in bix_div_container.find_all('div', class_='flex-wrap')]

        question_data = {
            "question_number": question_number,
            "question_text_html": direction_div_list[index] + '\n '+ question_text_html,
            "options_html": option_divs
        }

        # for option in option_divs:
        question_data_list.append(question_data)


    for direction_div in direction_divs:
        # Extract the value of xx from "Direction (Q.No. {xx})"
        direction_text = direction_div.find('div', class_='h5 w-100').text
        xx = int(direction_text.split(' ')[-1].strip(')'))

        direction_text_html = direction_div.find('div', class_='direction-text')
        direction_question_list[xx - 1] = direction_text_html


    time.sleep(3)

    # Step 3: Click the "Submit Test" button and press Enter
    submit_test_button = driver.find_element(By.ID, "btnSubmitTest")
    driver.execute_script("arguments[0].click();", submit_test_button)

    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(3)

    # SCRAPPING THE EXPLANATIONS

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    explanation_list = []

    bix_div_containers = soup.find_all('div', class_='bix-div-answer')

    for index, bix_div_container in enumerate(bix_div_containers, start=1):

        # Exclude divs with class 'explain-link' within 'bix-div-answer'
        explain_links = bix_div_container.find_all('div', class_='explain-link')
        for explain_link in explain_links:
            explain_link.extract()
    
        img_tags = bix_div_container.find_all('img')

        for img_tag in img_tags:
            src = img_tag.get('src')

            if src and src.startswith('/'):
                img_tag['src'] = 'https://www.indiabix.com' + src

        html = str(bix_div_container).split("</div>")
        # print(html)
        # print(html[4])
        pattern = r'<span class="mdi mdi-alpha-(\w+)-circle-outline">\s*</span>'

        correct_option = re.search(pattern, html[4])
        if correct_option:
            correct_option = correct_option.group(1)
            # print(correct_option)
        else:
            raise("CORRECT OPTION ERROR")

        true_explaination = remove_html_tags(html[-3])
        # print(true_explaination)
      
        explanation_list.append({"correct_option": correct_option,"explaination":true_explaination})

    driver.quit()
    data = []
    for i,ques in enumerate(question_data_list):
        data.append(
            {
                "question_number": ques["question_number"],
                "question": ques["question_text_html"],
                "options": ques["options_html"],
                "correct_option": explanation_list[i]["correct_option"],
                "explaination":  explanation_list[i]["explaination"]
            }
        )
    return data

# print(microbiology_aptitude())