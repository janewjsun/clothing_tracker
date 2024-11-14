from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

# Set up environment variables for your username and password
MONGODB_USER = quote_plus(os.getenv("MONGO_USERNAME"))
MONGODB_PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD"))

# Connection string

client = MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@clothing-tracker.hruqs.mongodb.net/")
db = client.ClothingTracker
clothing_collection=db.clothing
daily_log = db.daily_log

def get_clothing_stats():
    # Retrieve all clothing items
    clothing_items = list(clothing_collection.find())
    df = pd.DataFrame(clothing_items)
    df = df[df['brand'] != ""]

    # Count each brand, color, and type
    brand_counts = df['brand'].value_counts()
    color_counts = df['color'].explode().value_counts()
    category_counts = df['category'].value_counts()

    print("Brand Counts:\n", brand_counts.head(10))
    print("\nColor Counts:\n", color_counts.head(5))
    print("\nCategory Counts:\n", category_counts)

if __name__ == "__main__":
    get_clothing_stats()
