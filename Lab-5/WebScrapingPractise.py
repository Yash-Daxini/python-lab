from operator import indexOf
import requests
import bs4

data = requests.get('https://www.darshan.ac.in/engineering/computer/faculty')

soap = bs4.BeautifulSoup(data.text,'lxml')

allh2 = soap.select("body > main > div > div > div > div > div > div > div > div > div > div > h2")

print(allh2)

for h1 in allh2:
    print(h1.text.strip())