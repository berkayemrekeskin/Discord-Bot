import requests
from bs4 import BeautifulSoup

url = '--'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
data = soup.find_all('--', class_='--')

for inf in data:
    print(inf.data)