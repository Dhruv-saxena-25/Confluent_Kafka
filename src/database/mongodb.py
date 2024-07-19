import pymongo
import os
from dotenv import load_dotenv
load_dotenv() 


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:

        self.client = pymongo.MongoClient(os.getenv('MONGO_DB_URL', None),tlsCAFile=ca)
        self.db_name="sensor"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
