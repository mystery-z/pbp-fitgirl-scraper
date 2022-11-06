import time
import requests
from bs4 import BeautifulSoup
import unidecode, json

def gameLinker(dl_link):
	startUrl = dl_link
	startReq = requests.get(startUrl)
	startSoup = BeautifulSoup(startReq.content, 'html.parser')
	content = startSoup.find('div', class_='entry-content')
	firstList = content.find('ul')
	bulletList = firstList.find_all('a')


	dict1 = {}


	for line in bulletList:
		name = line.text.strip()
		link = line.get("href")
		if link != "http://jdownloader.org/jdownloader2":
			if link != "magnet:":
				dict1[name] = link
	return(dict1)


# ~ usage: 
print(gameLinker("https://fitgirl-repacks.site/borderlands-game-of-the-year-enhanced"))
