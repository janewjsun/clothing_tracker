from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_USER = quote_plus(os.getenv("MONGO_USERNAME"))
MONGODB_PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD"))

client = MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@clothing-tracker.hruqs.mongodb.net/")
db = client.ClothingTracker
clothing_collection=db.clothing
daily_log = db.daily_log

for item in daily_log.find():
    if 'accessories' not in item:
        daily_log.update_one(
            {'_id': item['_id']},
            {'$set': {'accessories': [206, 207, 208, 209, 210, 211]}}
        )
    else:
        daily_log.update_one(
            {"_id": item['_id']},
            {"$addToSet": {'accessories': {"$each": [206,207,208,209,210,211]}}}
        )


client.close()