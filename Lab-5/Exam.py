import requests
import bs4

data = requests.get("https://www.darshan.ac.in/exam")

res = bs4.BeautifulSoup(data.text,'lxml')

dates = res.select("#nav-tabContent-1 > div > div > div.masonry-grid.row > div > article > div > div > div.col-12.col-md-auto.text-left.text-md-center.g-brd-1.g-brd-gray-light-v1.g-brd-right--md > span")

exams = res.select("#nav-tabContent-1 > div > div > div.masonry-grid.row > div > article > div > div > div.col > p > a")

# print(allDate)

for (exam,date) in zip(exams,dates): 
    print(exam.text.strip())