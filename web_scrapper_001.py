#Python program to scrape website
#and save quotes from website
import requests
# This is a sample web scrapper that I am constructing using an outline from the GeeksForGeeks.com website 
#This script is going to work in conjunction with a website I host for testing purposes 
##code name : scrappy. This is some ugly code 
from bs4 import BeautifulSoup
import csv

URL = "http://www.values.com/inspirational-quotes"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
r = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(r.content, 'html5lib')

lesson =[] # a list to store lessons

table = soup.find('div', attrs = {'id':'all_lessons'})

for row in table.findAll('div',
						attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
	quote = {}
	quote['theme'] = row.h5.text
	quote['url'] = row.a['href']
	quote['img'] = row.img['src']
	quote['lines'] = row.img['alt'].split(" #")[0]
	quote['author'] = row.img['alt'].split(" #")[1]
	quotes.append(quote)

filename = 'motivational_lessons.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['theme','url','img','lines','author'])
	w.writeheader()
	for quote in quotes:
		w.writerow(quote)
