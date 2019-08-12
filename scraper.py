from bs4 import BeautifulSoup
import requests
import time


#Gets all guardian headlines

url = 'https://www.theguardian.com/uk'
time.sleep(5)
response = requests.get(url, timeout=10)
content = BeautifulSoup(response.content, "html.parser")
for headline in content.find_all('a', attrs={"class": "js-headline-text"}):
    print(headline.text)


