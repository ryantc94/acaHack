#!/usr/bin/env python
# -*- coding: utf-8 -*-import json

import pymongo
import json
import urllib
import datetime
import pyexcel as pe
import pyexcel.ext.xlsx 


client = pymongo.MongoClient()

today = datetime.date.today()
today = today.strftime("%Y%m%d")
client = pymongo.MongoClient()
#creat database and collection
db = client['ACAHack']
col = 'formulary_'+ today


#open file
records = pe.get_records(file_name="machine-readable-url-puf.xlsx")
counter = 0
for record in records:
	url = record["URL Submitted"]
	if ".json" in url:

		response = urllib.urlopen(url)
		data = json.loads(response.read())

		for url2 in data["formulary_urls"]:
			response2 = urllib.urlopen(url2)
			dic = json.loads(response2.read())
			db[col].insert(dic)
			counter+=1
			print ("importing...",counter," to Mongo")
