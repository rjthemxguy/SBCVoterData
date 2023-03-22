# -*- coding: utf-8 -*-

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://rj:Hapkido123@cluster0.iiuhn.mongodb.net/?retryWrites=true&w=majority")
db = cluster["SBC2023"]
voters = db["voters"]

print ("--- Getting Precincts ---")
precinctList = (voters.distinct("precinct"))

pipeline = [
   {
      "$match": {
         "precinct": "1458",
         "party":"AI"
      }
   },
   {
    "$count": "total"
  }
]


results = voters.aggregate(pipeline)

for rec in results:
    print(rec["total"])

    
