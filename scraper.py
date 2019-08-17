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
    headlines_list = []
    for headline in content.find_all("a", attrs={"class": "js-headline-text"}):
        headlines_list.append(headline.text.strip())

    return headlines_list    

def get_abc_headlines():
    content = send_http_request("https://abcnews.go.com/")
    headlines_list = []
    for container in content.find_all(attrs={"id": "main-container"}):
        for headline in container.find_all("a", attrs={"class": "black-ln"}):
            headlines_list.append(headline.text.strip())

    return list(set(headlines_list))

def get_fox_headlines():
    content = send_http_request("https://www.foxnews.com/")   
    headlines_list = []
    for main_content in content.find_all(attrs={"class":"main-content"}):
        for headline in main_content.find_all(attrs={"class": "content"}):
            for link in headline.find_all("a"):     
                headlines_list.append(link.text.strip())
        
    return list(set(headlines_list)) 

if __name__ == "__main__":
    headlines = []
    headlines.extend(get_fox_headlines())
    headlines.extend(get_abc_headlines())
    headlines.extend(get_guardian_headlines())
    headlines = [val for val in headlines if len(val) > 12]
    for h in headlines:
        print(h)