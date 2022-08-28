from operator import indexOf
import requests
import bs4

branch = ['computer','mechanical','electrical','civil']

for b in branch:
    url = 'https://www.darshan.ac.in/engineering/' + b +'/faculty'
    data = requests.get(url)

    soap = bs4.BeautifulSoup(data.text,'lxml')

    allh2 = soap.select("body > main > div > div > div > div > div > div > div > div > div > div > h2")

    print("--------------",b,"-------------")

    for h1 in allh2:
        print(h1.text.strip())
    print()


