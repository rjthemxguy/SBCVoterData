# -*- coding: utf-8 -*-

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://rj:Hapkido123@cluster0.iiuhn.mongodb.net/?retryWrites=true&w=majority")
db = cluster["SBC2023"]
voters = db["voters"]

print (voters.distinct("01 11/08/2022 november 8, 2022, general election 4136"))


