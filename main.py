# -*- coding: utf-8 -*-

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://rj:Hapkido123@cluster0.iiuhn.mongodb.net/?retryWrites=true&w=majority")
db = cluster["SBC2023"]
voters = db["Voters"]

