from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv()

# Set up environment variables for your username and password
MONGODB_USER = quote_plus(os.getenv("MONGO_USERNAME"))
MONGODB_PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD"))

# Connection string

client = MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@clothing-tracker.hruqs.mongodb.net/")
db = client.ClothingTracker
clothing_collection=db.clothing
daily_log = db.daily_log

def log_outfit(clothing_ids):
    dict = {"tops": [], "bottoms": [], "outerwear": [], "accessories": [], "shoes": [], "one pieces": []}

    for id in clothing_ids:
        document = clothing_collection.find_one({"_id": id})

        dict[document["category"]].append(id)

    log = {
        "_id": str(date.today()),
    }
    for k,v in dict.items():
        if v:
            log[k]=v
    daily_log.insert_one(log)


if __name__ == "__main__":
    clothing_ids = input("clothing IDs, separate by commas: ").split(',')
    clothing_ids = [int(cid.strip()) for cid in clothing_ids]

    log_outfit(clothing_ids)
client.close()