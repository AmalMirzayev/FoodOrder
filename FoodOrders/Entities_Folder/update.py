import mysql.connector

class Update:
    def __init__(self) -> None:
        pass

    def update_restaurant_availability(restaurant_id, config):
        conn = None
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            cursor.execute("SELECT available FROM restaurant WHERE id = %s", (restaurant_id,))
            result = cursor.fetchone()

            if result:
                available = int(result[0])
                if available > 0:
                    cursor.execute("UPDATE restaurant SET available = %s WHERE id = %s", (available - 1, restaurant_id))
                    conn.commit()
                    print("The restaurant has been successfully updated.")
                else:
                    print("This restaurant is no longer available.")
            else:
                print("The restaurant could not be found.")

        except mysql.connector.Error as error:
            print("MySQL Error:", error)

        finally:
            if conn is not None and conn.is_connected():
                cursor.close()
                conn.close() 
    
    def update_menu_item_availability(item_id, config):
        conn = None
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            # Take id of the item
            cursor.execute("SELECT available FROM menu WHERE id = %s", (item_id,))
            result = cursor.fetchone()

            if result:
                available = int(result[0])
                if available > 0:
                    # Decreasing 1 
                    cursor.execute("UPDATE menu SET available = %s WHERE id = %s", (available - 1, item_id))
                    conn.commit()
                    print("The menu item has been successfully updated.")
                else:
                    print("This menu item is no longer available.")
            else:
                print("The menu item could not be found.")

        except mysql.connector.Error as error:
            print("MySQL Error:", error)

        finally:
            if conn is not None and conn.is_connected():
                cursor.close()
                conn.close()

