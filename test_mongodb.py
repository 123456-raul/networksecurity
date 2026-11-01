import os

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()
uri = os.getenv("MONGO_DB_URL")

# Send a ping to confirm a successful connection
try:
    # Create a new client and connect to the server
    client = MongoClient(uri)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
