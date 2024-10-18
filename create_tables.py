import sqlite3

def create_tables():
    conn = sqlite3.connect('clothing_tracker.db')
    cursor = conn.cursor()

    # Create category table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    """)

    # Insert allowed categories into the category table
    categories = [('bottoms',), ('tops',), ('outerwear',), ('accessories',), ('shoes',)]
    cursor.executemany("INSERT OR IGNORE INTO category (name) VALUES (?);", categories)

    # Create clothing table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clothing (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT,
        category_id INTEGER,
        sub_category TEXT,
        color TEXT,
        material TEXT,
        season TEXT,
        is_thrifted INTEGER,
        FOREIGN KEY (category_id) REFERENCES category(id)
    );
    """)

    # Create daily_log table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        log_date DATE,
        clothing_id INTEGER,
        FOREIGN KEY (clothing_id) REFERENCES clothing(id)
    );
    """)

    conn.commit()
    conn.close()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
