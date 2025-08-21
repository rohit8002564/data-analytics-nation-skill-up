import requests


# print the HTML using BeautifulSoup
from bs4 import BeautifulSoup

response = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())

soup = BeautifulSoup(response.text, 'html.parser')

# Extract Title
print(soup.title.string) # prints the page title 

# Extract all headings
for heading in soup.find_all(['h1', 'h2', 'h3']):
    print(heading.get_text(strip=True))
# Extract all links
for link in soup.find_all('a', href=True):
    print(link['href'])

    # Fetch page
url = 'https://www.geeksforgeeks.org/python/python-programming-language-tutorial/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extrat content by tag and class
# Example: article content inside <div class"entry-content">
content = soup.find("div", class_="entry-content")
if content:
    print(content.get_text(strip=True))


#Extract all paragraphs from a specific class
for para in soup.find_all("p", class_="text"):
    print(para.get_text(strip=True))

# Extract all paragraphs (without needing class="text")
for para in soup.find_all("p"):
    print(para.get_text(strip=True))
