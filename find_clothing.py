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

category_list = ['accessories', 'bottoms', 'one pieces', 'outerwear', 'shoes', 'tops']
def gather_inputs():
    input_dict = {}
    input_str = f"""Which keys would you like to search? Enter:
    1 for brand        2 for category
    3 for sub_category 4 for color
    5 for thrifted     6 for material
    and q to quit\n"""
    to_search = input(input_str)
    while to_search != 'q':
        key = int(to_search)
        if key in input_dict:
            to_search = input('this key is already searched and added! try again\n')
            continue


        if key == 1:
            input_dict["brand"] = input('enter brand: ').lower()
        if key == 2:
            print(", ".join(
                f"{category} ({i + 1})" for i, category in enumerate(category_list)))
            category = category_list[int(input("enter category: "))-1]
            input_dict["category"] = category
        if key == 3:
            if "category" in input_dict:
                subcategories = clothing_collection.distinct("sub_category", {"category": input_dict["category"]})
                print(", ".join(
                    f"{sub} ({i + 1})" for i, sub in enumerate(subcategories)))
            inp = input("enter subcategory: ")
            if inp.isdigit():
                input_dict["sub_category"] = subcategories[int(inp)-1]
            else:
                input_dict["sub_category"] = inp.lower()
        if key == 4:
            color_list = sorted(input('enter color(s), separated by a comma: ').split(","))
            input_dict["color"] = color_list
        if key == 5:
            str_bool = input('enter t for thrifted and f for not: ')
            input_dict["thrifted"] = "1" if str_bool.lower() == 't' else "0"
        if key == 6:
            input_dict["material"] = input("enter material: ").lower()

        to_search = input('enter a next key to search: ')
    return input_dict

if __name__ == "__main__":
    inputs = gather_inputs()
    find_clothing(**inputs)

client.close()

#today
#218,53,165,153,5