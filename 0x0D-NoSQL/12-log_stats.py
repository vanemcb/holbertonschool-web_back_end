#!/usr/bin/env python3
"""Module task 12
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    count_docs = nginx_collection.count_documents({})
    count_get = nginx_collection.count_documents({'method': 'GET'})
    count_post = nginx_collection.count_documents({'method': 'POST'})
    count_put = nginx_collection.count_documents({'method': 'PUT'})
    count_patch = nginx_collection.count_documents({'method': 'PATCH'})
    count_del = nginx_collection.count_documents({'method': 'DELETE'})
    count_path = nginx_collection.count_documents({'path': '/status'})

    dict_methods = {'GET': count_get,
                    'POST': count_post,
                    'PUT': count_put,
                    'PATCH': count_patch,
                    'DELETE': count_del
                    }

    print('{} logs\nMethods:'.format(count_docs))
    for key, value in dict_methods.items():
        print('\tmethod {}: {}'.format(key, value))
    print('{} status check'.format(count_path))
