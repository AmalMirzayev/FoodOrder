import mysql.connector
config = {
    'user': 'root',
    'password': 'Amal1234',
    'host': 'localhost',
    'database': 'course'
}




def add_restaurants(restaurants):
    conn = None
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO restaurant (name, city, available) 
        VALUES (%s, %s, %s)
        """
        
        cursor.executemany(insert_query, restaurants)
        conn.commit()
        print(f"{cursor.rowcount} restaurants successfully added.")

    except mysql.connector.Error as error:
        print("MySQL Error:", error)

    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    restaurants = [
        ("MC DONALDS", "GENCE", "100"),
        ("KFC", "BAKU", "100"),
        ("KFC", "GENCE", "100"),
        ("MADO", "SUMQAYIT", "100"),
        ("Alinea", "BAKU", "100"),
        ("Alinea", "GENCE", "100"),
        ("Alinea", "SUMQAYIT", "100"),
        ("Geranium", "BAKU", "100"),
        ("Geranium", "GENCE", "100"),
        ("Geranium", "SUMQAYIT", "100"),
        ("Asador Etxebarri", "BAKU", "100"),
        ("Asador Etxebarri", "GENCE", "100"),
        ("Asador Etxebarri", "SUMQAYIT", "100"),
        # Daha fazla veri buraya ekleyin
    ]

    add_restaurants(restaurants)
