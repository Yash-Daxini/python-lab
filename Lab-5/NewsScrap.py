import requests
import bs4

data = requests.get("https://www.darshan.ac.in/circular")

res = bs4.BeautifulSoup(data.text,'lxml')

allDate = res.select("#SearchResult > div > div > div > div.masonry-grid.row > div > article > div > div > div.col.g-brd-1.g-brd-gray-light-v1.g-brd-left--md > p.g-font-size-15.g-font-weight-600.g-mb-10")

print(allDate)