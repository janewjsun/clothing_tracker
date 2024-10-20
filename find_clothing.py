from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

# Set up environment variables for your username and password
MONGODB_USER = quote_plus(os.getenv("MONGO_USERNAME"))
MONGODB_PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD"))

# Connection string

client = MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@clothing-tracker.hruqs.mongodb.net/")
db = client.ClothingTracker
clothing_collection=db.clothing

def find_clothing(**kwargs):
    # Build the query based on the provided keyword arguments
    query = {}

    # Add only the parameters that were provided
    for key, value in kwargs.items():
        query[key] = value

    # Use the query to find matching clothing items
    results = clothing_collection.find(query)

    # Return all matching documents as a list
    ctr=1
    for item in list(results):
        print(f"item {ctr}")
        print("-"*34)
        for k,v in item.items():
            if type(v) == list:
                v = ", ".join(v)
            if type(v)==str and len(v) > 15:
                print(f"| {k:<12} | {v:<15}")
            else:
                print(f"| {k:<12} | {v:<15} |")
        print("-" * 34)
        print()
        ctr += 1


if __name__ == "__main__":
    find_clothing(color = ["brown"])

client.close()