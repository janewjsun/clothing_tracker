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

def add_clothing(brand,category,sub_category,color,material,thrifted):
    if material != "":
        clothing_item = {
            "_id": clothing_collection.count_documents({})+1,
            "brand": brand,
            "category": category,
            "sub_category": sub_category,
            "color": color,
            "material": material,
            "thrifted": thrifted
        }
    else:
        clothing_item = {
            "_id": clothing_collection.count_documents({}) + 1,
            "brand": brand,
            "category": category,
            "sub_category": sub_category,
            "color": color,
            "thrifted": thrifted
        }
    clothing_collection.insert_one(clothing_item)


if __name__ == "__main__":
    brand = input("Enter brand: ").lower()
    category = input("Enter category: ").lower()
    while category not in {"tops", "bottoms", "accessories", "shoes", "outerwear", "one pieces"}:
        category = input("that was not a category! try again: ").lower()
    sub_category = input("Enter sub-category: ").lower()
    color = input("Separate colors by space. Enter color: ").lower().split()
    material = input("Enter material: ").lower()
    thrifted = bool(int(input("0 for not thrifted, 1 for thrifted: ")))
    add_clothing(brand, category, sub_category, color, material, thrifted)
client.close()