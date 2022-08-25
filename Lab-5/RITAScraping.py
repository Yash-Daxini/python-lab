import requests
import bs4

data = requests.get("https://ritaindia.org/Member")

res = bs4.BeautifulSoup(data.text,'lxml')

alltr = res.select("body > section > div > div > div > div > table > tbody > tr")

for tr in alltr:
    print(tr.select("td")[1].text)