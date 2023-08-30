from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

myclient = MongoClient(config.get("DATABESE_CONNECTION_URL"))