import sqlite3
from datetime import date


def log_outfit(clothing_ids):
    conn = sqlite3.connect('clothing_tracker.db')
    cursor = conn.cursor()

    for clothing_id in clothing_ids:
        cursor.execute("""
            INSERT INTO daily_log (log_date, clothing_id)
            VALUES (?, ?)
        """, (date.today(), clothing_id))

    conn.commit()
    conn.close()
    print("Logged today's outfit.")


if __name__ == "__main__":
    clothing_ids = input("clothing IDs, separate by commas: ").split(',')
    clothing_ids = [int(cid.strip()) for cid in clothing_ids]

    log_outfit(clothing_ids)