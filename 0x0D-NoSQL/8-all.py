#!/usr/bin/env python3
"""Module task 8
"""


def list_all(mongo_collection):
    """Function that lists all documents in a collection
    """
    list_docs = []
    for doc in mongo_collection.find({}):
        list_docs.append(doc)

    return list_docs
