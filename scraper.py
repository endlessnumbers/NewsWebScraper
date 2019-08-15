from bs4 import BeautifulSoup
import requests
import time

def send_http_request(url):
    response = requests.get(url, timeout=10)
    content = BeautifulSoup(response.content, "html.parser")
    return content

#Gets all guardian headlines
def get_guardian_headlines():
    content = send_http_request("https://www.theguardian.com/uk")
    for headline in content.find_all("a", attrs={"class": "js-headline-text"}):
        print(headline.text)

def get_abc_headlines():
    content = send_http_request("https://abcnews.go.com/")
    for headline in content.find_all("a", attrs={"class": "black-ln"}):
        print(headline.text)

def get_fox_headlines():
    content = send_http_request("https://www.foxnews.com/")    
    for headline in content.find_all(attrs={"class": "content"}):
        for link in headline.find_all("a"):
            print(link.text)

if __name__ == "__main__":
    get_fox_headlines()
    get_abc_headlines()
    get_guardian_headlines()