#!/usr/bin/env python3
"""Module task 10
"""


# if __name__ == "__main__":
def update_topics(mongo_collection, name, topics):
    """Function that changes all topics of a school document based on the name
    """
    query = {'name': name}
    new_values = {'$set': {'topics': topics}}
    mongo_collection.update_one(query, new_values)