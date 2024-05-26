import mysql.connector
from mysql.connector import Error

def search_menu_item(item_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',        
            user='root',             
            password='Amal1234',     
            database='course'        
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Check the connection of restaurant_id, price, available from menu
            query = "SELECT restaurant_id, price, available FROM menu WHERE name LIKE %s"
            cursor.execute(query, ('%' + item_name + '%',))

            # Get results
            results = cursor.fetchall()

            # Print results
            if results:
                print(f"\n'{item_name}' ile ilgili bulunan sonuçlar:\n")
                for row in results:
                    modified_row = list(row)
                    modified_row[0] = f"restaurant_id {modified_row[0]}"
                    print(tuple(modified_row))
            else:
                print(f"\n'{item_name}' ile ilgili hiçbir sonuç bulunamadı.")

    except Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

