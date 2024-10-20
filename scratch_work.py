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

for item in clothing_collection.find():
    sorted_colors = sorted(item['color'])
    clothing_collection.update_one(
        {'_id': item['_id']},
        {'$set': {'color': sorted_colors}}
    )


client.close()