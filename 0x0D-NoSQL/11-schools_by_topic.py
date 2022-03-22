#!/usr/bin/env python3
"""Module task 11
"""


# if __name__ == "__main__":
def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a specific topic
    """
    return mongo_collection.find({'topics': topic})
