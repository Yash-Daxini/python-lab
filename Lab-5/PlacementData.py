import bs4
import requests

year = input("Enter year :")

url = "https://www.darshan.ac.in/placement/list/engineering/computer/"+year

data = requests.get(url)

getdata = bs4.BeautifulSoup(data.text,'lxml')

allName = getdata.select("body > main > div:nth-child(5) > div > div > div.col-lg-8.col-xl-9.g-font-size-14.g-mb-30 > div > div.row.g-px-4.g-px-5--sm.g-px-5--md > div > article > div > h2 > span")

allAmount = getdata.select("body > main > div:nth-child(5) > div > div > div.col-lg-8.col-xl-9.g-font-size-14.g-mb-30 > div.g-pt-20 > div.row.g-px-4.g-px-5--sm.g-px-5--md > div > article > div > p.g-color-gray-light-v1.g-font-weight-600.g-font-size-14.g-mb-0 > span")

# print(allAmount)

for (name,amount) in zip(allName,allAmount):
    print(name.text.strip(),end="")
    print('  -----  ',end="")
    print(amount.text.strip())



