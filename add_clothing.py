import sqlite3


def add_clothing(brand, category, sub_category, color, material, season, thrifted):
    conn = sqlite3.connect('clothing_tracker.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM category WHERE name = ?", (category,))
    category_row = cursor.fetchone()

    if category_row is None:
        print(f"Category '{category}' not found in the database.")
        conn.close()
        return

    category_id = category_row[0]  # Get the ID

    cursor.execute("""
        INSERT INTO clothing (brand, category_id, sub_category, color, material, season, is_thrifted)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (brand, category_id, sub_category, color, material, season, thrifted))

    conn.commit()
    conn.close()
    print(f"Added {brand} {category} to the database.")

if __name__ == "__main__":
    # brand = input("Enter brand: ").lower()
    # category = input("Enter category: ").lower()
    # sub_category = input("Enter sub-category: ").lower()
    # color = input("Enter color: ").lower()
    # size = input("Enter size: ").lower()
    # material = input("Enter material: ").lower()
    # season = input("Enter season: ").lower()
    # thrifted = int(input("Enter season: "))
    # add_clothing(brand, category, sub_category, color, material, season)
    add_clothing("thatvalleygirl","tops","tank tops","pink,white","","spring,summer",0)