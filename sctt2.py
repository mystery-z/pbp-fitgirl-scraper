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


	dict = {}


	for line in bulletList:
		name = line.text.strip()
		link = line.get("href")
		if link != "http://jdownloader.org/jdownloader2":
			if link != "magnet:":
				dict[name] = link
	print(dict)


	with open("fitgirl_index.json","a",encoding='utf-8') as filemygod:
		file_data = json.load(filemygod)
		megalist = file_data["fitgirl_index"]
		print(megalist)
		

with open("fitgirl_index.json","r",encoding='utf-8') as readfile:
	data = json.load(readfile)
	
	for item in data['fitgirl_index']:
		dl_link = item['link']
		print(dl_link)
		gameLinker(dl_link)


