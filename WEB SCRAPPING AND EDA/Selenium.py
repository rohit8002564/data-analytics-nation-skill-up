''' Selenium: To handle this, we use Selenium that can automate browsers like Chrome or Firefox, wait for content to load, click buttons, scroll and extract fully rendered web pages just like a real user.'''
''' WebDriver is a software component that Selenium uses to interact with a web browser. It acts as the bridge between your Python script and the actual browser window.'''

# -> Searching on Google with Firfox
# import webdriver
from selenium import webdriver 

# create webdriver object 
driver = webdriver.Firefox() 

# get google.co.in 
driver.get("https://www.google.co.in/ / search?q = geeksforgeeks")

# ->Scrape Laptop Details from a Test Site using Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

element_list = []

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Use a proper Service object
service = Service(ChromeDriverManager().install())

for page in range(1, 3):
    # Initialize driver properly
    driver = webdriver.Chrome(service=service, options=options)

    # Load the URL
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=%7Bpage%7D"
    driver.get(url)
    time.sleep(2)  # Optional wait to ensure page loads

    # Extract product details
    titles = driver.find_elements(By.CLASS_NAME, "title")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    descriptions = driver.find_elements(By.CLASS_NAME, "description")
    ratings = driver.find_elements(By.CLASS_NAME, "ratings")

    # Store results in a list
    for i in range(len(titles)):
        element_list.append([
            titles[i].text,
            prices[i].text,
            descriptions[i].text,
            ratings[i].text
        ])

    driver.quit()

# Display extracted data
for row in element_list:
    print(row)

    # -> Parsing HTML with lxml and Xpath
    from lxml import html
import requests

url = 'https://example.com/'
response = requests.get(url)
tree = html.fromstring(response.content)

# Extract all link texts
link_titles = tree.xpath('//a/text()')

for title in link_titles:
    print(title)


# Extract all link URLs
link_urls = tree.xpath('//a/@href')

for url in link_urls:
    print(url)

# Automateing UI Task with PyAutoGUI

import pyautogui

# moves to (519,1060) in 1 sec
pyautogui.moveTo(519, 1060, duration = 1)

# simulates a click at the present mouse position 
pyautogui.click()

pyautogui.moveTo(1717, 352, duration = 1) 

pyautogui.click()