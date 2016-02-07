#!/usr/bin/env python
# -*- coding: utf-8 -*-import json

import pymongo
import json
import urllib
import datetime
import ujson
import pyexcel as pe
import pyexcel.ext.xlsx
import socket
import errno


client = pymongo.MongoClient()
today = datetime.date.today()
today = today.strftime("%Y%m%d")
# creat database and collection
db1 = client['ACAHack']
col = 'plan_' + today


#open file
records = pe.get_records(file_name="a.xlsx")
counter = 0
for record in records:
    try:
        url = record["URL Submitted"]
        if ".json" in url and url!="http://www.healthnet.com/static/hhs_az_json_20439/index.json":
            #print url
            response = urllib.urlopen(url)
            data = json.loads(response.read())

            for url2 in data["plan_urls"]:
                try:
                    if ".json" in url2:
                        response2 = urllib.urlopen(url2)
                        dic = ujson.loads(response2.read())

                        for item in dic:
                            try:
                                    ILLINOISCHECKER = item["plan_id"]
                                    if "IL" in ILLINOISCHECKER:
                                        newdic = {"plan_id": item["plan_id"]}
                                        newdic ["marketing_name"]= item["marketing_name"]
                                        newdic["summary_url"]= item["summary_url"]
                                        newdic["plan_contact"] = item["plan_contact"]
                                        db1[col].insert(newdic)

                            except ValueError:
                                print url2
                            except socket.error as e: 
                                continue
                except:
                    continue
    except:
        continue


            #     try:
            #         ILLINOISCHECKER = item["plan_id"]
            #         newdic = {"plan_id": item["plan_id"]}
            #         for plan in item["plans"]:
            #             ILLINOISCHECKER = plan["plan_id"]
            #             if "IL" in ILLINOISCHECKER:
            #                 oneplan = True
            #                 if plan["drug_tier"] == "PREFERRED-GENERIC":
            #                     newdic[plan["plan_id"]] = 7
            #
            #                 elif plan["drug_tier"] == "GENERIC-BRAND":
            #                     newdic[plan["plan_id"]]=6
            #
            #                 elif plan["drug_tier"] == "NON-PREFERRED-GENERIC":
            #                     newdic[plan["plan_id"]] = 5
            #
            #                 elif plan["drug_tier"] == "PREFERRED-BRAND":
            #                     newdic[plan["plan_id"]] = 4
            #                 elif plan["drug_tier"] == "NON-PREFERRED-BRAND":
            #                     newdic[plan["plan_id"]] = 3
            #                 elif plan["drug_tier"] == "GENERIC-BRAND-SPECIALITY":
            #                     newdic[plan["plan_id"]] = 2
            #                 elif plan["drug_tier"] == "GENERIC-BRAND-SPECIALITY-DRUGS":
            #                     newdic[plan["plan_id"]] = 2
            #                 elif plan["drug_tier"] == "SPECIALITY-DRUGS":
            #                     newdic[plan["plan_id"]] = 1
            #                 elif plan["drug_tier"] == "SPECIALITY BRAND":
            #                     newdic[plan["plan_id"]] = 1
            #                 else:
            #                     print plan["drug_tier"]
            #         if oneplan:
            #             print newdic
            #             db1[col].insert(newdic)
            #             print "inserted"
            #     except:
            #         print "ITEM WITHOUT ID"
            #         continue
            # counter += 1
            # print ("importing...", counter, " to Mongo")
