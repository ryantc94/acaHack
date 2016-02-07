from pymongo import MongoClient
import json

connection = MongoClient()
db = connection['ACAHack']
col = 'formulary_20160206'

users_plan_id = "27833IL0140001"

query = list(db[col].find({"rxnorm_id" : "1000499"}))


for item in query:
	if "27833IL0140001" in item:
		print "value is ", item["27833IL0140001"]