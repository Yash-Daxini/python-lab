import bs4
import requests

data = requests.get("https://www.darshan.ac.in/circular")

res = bs4.BeautifulSoup(data.text,'lxml')

circulars = res.fetchNextSiblings("#SearchResult")

print(circulars)