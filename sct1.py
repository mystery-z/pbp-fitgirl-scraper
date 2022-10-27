#  sct1.py
#  Copyright 2022 mystery-z <https://github.com/mystery-z/>
# -*- coding: utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup
import json

# ~ this is a tier-one scraper

with open("fitgirl_index.json",'w+') as file:
	base = '''{"fitgirl_index":[]	
}'''
	file.write(base)

def mainScraper():
	startUrl = "https://fitgirl-repacks.site/all-my-repacks-a-z/"
	
	startReq = requests.get(startUrl)
	
	startSoup = BeautifulSoup(startReq.content, 'html.parser')
	
	pageList = startSoup.find('ul', class_='lcp_paginator')
	
	pages = pageList.find_all('a')
	
	listPages = [1,]
	
	for page in pages:
		element = page.text.strip()
		listPages = listPages + [element]
	listPages.remove('Next Page')
	listLength = listPages[-1]
	listLength = int(listLength)
	

	for n in range(1, listLength):
		mainUrl = "https://fitgirl-repacks.site/all-my-repacks-a-z/?lcp_page0=" + str(n)

		mainReq = requests.get(mainUrl)
			
		soup = BeautifulSoup(mainReq.content, 'html.parser')

		gameList = soup.find('ul', class_='lcp_catlist')

		results = gameList.find_all('a')


		def write_json(new_data, filename='fitgirl_index.json'):
			with open(filename,'r+', encoding='utf-8') as file:
				file_data = json.load(file)
				file_data["fitgirl_index"].append(new_data)
				file.seek(0)
				json.dump(file_data, file, indent = 4)

		for result in results:
			link = result.get("href")
			title = result.text.strip()
		
			title1 = title.replace("\u2019","'")
			title2 = title1.replace("\u2018","'")
			title3 = title2.replace("\u2014", "-")
			title4 = title3.replace("\u2013", "-")
			
			print(link, title4)
			entry = {"title": title4,
					 "link": link
					}
			print(entry)
			write_json(entry)

mainScraper()
