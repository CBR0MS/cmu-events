import requests
import selenium
from requests import get
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver")
#page = requests.get('https://thebridge.cmu.edu/organizations')
page = browser.get('https://thebridge.cmu.edu/organizations')
soup = BeautifulSoup(page.text, 'html.parser')
clubs = soup.find(class_='org-search-results')

print(soup)
print(soup.find_all('a'))

for a in soup.find_all('a',href=True):
    newpage = requests.get(a)
    soup = BeautifulSoup(newpage.text,'html.parser')
    email = soup.findAll(text='^@$')
    print(email)


"""def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url,str(e)))
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1))

def log_error(e):
    print(e)"""
