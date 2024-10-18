import sqlite3

def display_by_brand(brand, category_id = 0):
    conn = sqlite3.connect('clothing_tracker.db')
    cursor = conn.cursor()

    if category_id == 0:
        # select all items of the specified brand
        cursor.execute("""
            SELECT id, brand, category_id, sub_category, color, material, season, is_thrifted
            FROM clothing
            WHERE brand = ?;
        """, (brand,))
    else:
        cursor.execute("""
            SELECT id, brand, category_id, sub_category, color, material, season, is_thrifted
            FROM clothing
            WHERE brand = ?
            AND category_id = ?;
        """, (brand, category_id))

    # Fetch all matching rows
    items = cursor.fetchall()

    if items:
        print(f"Items for brand '{brand}':")
        for item in items:
            print(item)
    else:
        print(f"No items found for brand '{brand}'.")

    conn.close()

def display_all():
    conn = sqlite3.connect('clothing_tracker.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, brand, category_id, sub_category, color, material, season, is_thrifted
        FROM clothing;
    """)

    items = cursor.fetchall()

    if items:
        print("All items:")
        for item in items:
            print(item)
    else:
        print("No items found.")

    conn.close()

if __name__ == "__main__":
    option = input("Type 1 for all items, 2 for items by brand: ")
    if option == "1":
        display_all()
    if option == "2":
        option = input("Which brand? ").lower()
        display_by_brand(option, 0)