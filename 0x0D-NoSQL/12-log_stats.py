#!/usr/bin/env python3
"""Module task 12
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    count_docs = nginx_collection.count_documents({})
    


    print('{} logs'.format(count_docs))
