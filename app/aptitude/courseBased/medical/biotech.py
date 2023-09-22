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

def aptitude():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    # Step 1: Visit the website
    driver.get("https://www.indiabix.com/online-test/biotechnology-test/")
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

    question_data_list = []
    direction_question_list = [None] * 20

    for index, bix_div_container in enumerate(bix_div_containers, start=1):
        # Find the question number
        question_number = bix_div_container.find('div', class_='bix-td-qno').text.strip()

        # Find all <img> tags
        img_tags = bix_div_container.find_all('img')

        for img_tag in img_tags:
            src = img_tag.get('src')

            if src and src.startswith('/'):
                img_tag['src'] = 'https://www.indiabix.com' + src

        # Find the question text HTML as a string
        question_text_html = str(bix_div_container.find('div', class_='bix-td-qtxt'))

        # Find all options HTML as strings
        option_divs = bix_div_container.find_all('div', class_='flex-wrap')

        question_data = {
            "question_number": question_number,
            "question_text_html": question_text_html,
            "options_html": []
        }

        for option in option_divs:
            question_data['options_html'].append(str(option))
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

        # Find the <span> tag with class 'mdi-alpha-xx-circle-outline' mapping of class names to corresponding alphabets
        span_tag = bix_div_container.find('span', class_=lambda x: 'mdi-alpha' in x and 'circle-outline' in x)

        if span_tag:
            class_attr = span_tag.get('class')
            for class_name in class_attr:
                if 'mdi-alpha' in class_name and 'circle-outline' in class_name:
                    # Extract the 'xx' value from the class name
                    xx = class_name.split('-')[2]
                    # Map 'xx' to the corresponding alphabet
                    alphabet = {
                        'a': 'A',
                        'b': 'B',
                        'c': 'C',
                        'd': 'D',
                    }.get(xx, '')  # Default to empty string if 'xx' is not in the mapping
                    # Update the content of the <span> tag with the corresponding alphabet
                    span_tag.string = alphabet

        # Find all <img> tags
        img_tags = bix_div_container.find_all('img')

        for img_tag in img_tags:
            src = img_tag.get('src')

            if src and src.startswith('/'):
                img_tag['src'] = 'https://www.indiabix.com' + src

        html = str(bix_div_container).split("</div>")
        pattern = r'<span class="mdi mdi-alpha-(\w+)-circle-outline">(\w+)</span>'
        try:
            correct_option = re.search(pattern, html[4]).group(1)
        except:
            correct_option = ""
        true_explaination = ""
        for i in html[3:]:
            true_explaination += i.replace("\n","")
        true_explaination = true_explaination.split("Explanation:")[1]
        true_explaination += "</div>" 
        explanation_list.append({"correct_option": correct_option,"explaination":true_explaination})

    # for question_data, direction_question in zip(question_data_list, direction_question_list):
    #     print(f"Question {question_data['question_number']}:")
    #     print("Question Text HTML:")
    #     print(question_data['question_text_html'])
    #     print("Options HTML:")
    #     for option in question_data['options_html']:
    #         print(option)
    #     if direction_question is not None:
    #         print("Direction Text HTML:")
    #         print(direction_question)
    #     print("--------------------")

    # for explanation in explanation_list:
    #     print(explanation)
    #     print("--------------------")


    driver.quit()
    data = []
    for i,ques in enumerate(question_data_list):
        data.append(
            {
                "question_number": ques["question_number"],
                "question_text_html": ques["question_text_html"],
                "options_html": ques["options_html"],
                "correct_option": explanation_list[i]["correct_option"],
                "explaination":  explanation_list[i]["explaination"]
            }
        )
    return data


# aptitude()