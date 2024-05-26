import mysql.connector

config = {
    'user': 'root',
    'password': 'Amal1234',
    'host': 'localhost',
    'database': 'course'
}

def add_menu_items(menu_items):
    conn = None
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO menu (restaurant_id, name, price, available) 
        VALUES (%s, %s, %s, %s)
        """
        
        cursor.executemany(insert_query, menu_items)
        conn.commit()
        print(f"{cursor.rowcount} menu items successfully added.")

    except mysql.connector.Error as error:
        print("MySQL Error:", error)

    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

def main():
    menu_items = [
    (6, 'Meatball', 26.81, 1),
    (6, 'Kebab', 17.12, 1),
    (6, 'Rice', 27.07, 1),
    (6, 'Salad', 21.94, 1),
    (6, 'Pizza', 45.87, 1),
    (6, 'Pasta', 15.74, 1),
    (7, 'Drink', 25.39, 1),
    (7, 'Meatball', 49.08, 1),
    (7, 'Kebab', 28.12, 1),
    (7, 'Rice', 42.08, 1),
    (7, 'Salad', 23.23, 1),
    (7, 'Pizza', 22.06, 1),
    (7, 'Pasta', 13.50, 1),
    (8, 'Drink', 9.56, 1),
    (8, 'Meatball', 26.27, 1),
    (8, 'Kebab', 13.62, 1),
    (8, 'Rice', 5.78, 1),
    (8, 'Salad', 45.27, 1),
    (8, 'Pizza', 41.61, 1),
    (8, 'Pasta', 2.15, 1),
    (9, 'Drink', 7.42, 1),
    (9, 'Meatball', 43.97, 1),
    (9, 'Kebab', 14.66, 1),
    (9, 'Rice', 43.73, 1),
    (9, 'Salad', 6.36, 1),
    (9, 'Pizza', 35.27, 1),
    (9, 'Pasta', 29.92, 1),
    (10, 'Drink', 4.23, 1),
    (10, 'Meatball', 32.70, 1),
    (10, 'Kebab', 13.75, 1),
    (10, 'Rice', 35.14, 1),
    (10, 'Salad', 17.39, 1),
    (10, 'Pizza', 33.87, 1),
    (10, 'Pasta', 1.42, 1),
    (11, 'Drink', 38.74, 1),
    (11, 'Meatball', 40.18, 1),
    (11, 'Kebab', 31.32, 1),
    (11, 'Rice', 31.22, 1),
    (11, 'Salad', 40.72, 1),
    (11, 'Pizza', 46.62, 1),
    (11, 'Pasta', 43.18, 1),
    (12, 'Meatball', 31.10, 1),
    (12, 'Kebab', 7.74, 1),
    (12, 'Rice', 17.01, 1),
    (12, 'Salad', 27.75, 1),
    (12, 'Pizza', 25.13, 1),
    (12, 'Pasta', 7.13, 1),
    (12, 'Drink', 17.83, 1),
    (13, 'Kebab', 2.80, 1),
    (13, 'Rice', 47.04, 1),
    (13, 'Salad', 18.35, 1),
    (13, 'Pizza', 8.26, 1),
    (13, 'Pasta', 18.33, 1)
        # Daha fazla yemek verisi buraya ekleyin
    ]

    add_menu_items(menu_items)

if __name__ == "__main__":
    main()