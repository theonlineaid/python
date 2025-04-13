import pymongo
from pprint import pprint
import pandas as pd

from dotenv import load_dotenv
import os

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

myclient = pymongo.MongoClient(mongo_uri)
mydb = myclient['chat-app']
ca = mydb['messages']

documents = list(ca.find())

data =  pd.DataFrame(documents)

pprint(data)