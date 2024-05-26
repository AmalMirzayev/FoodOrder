import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Amal1234',
            database='course'
        )
        self.cursor = self.connection.cursor()

    def place_order(self, item_id):
        query = "UPDATE menu SET available = False WHERE id = %s"
        self.cursor.execute(query, (item_id,))
        self.connection.commit()
    def show_all_restaurants(self):
        query = "SELECT id, name, city FROM restaurant"
        self.cursor.execute(query)
        restaurants = self.cursor.fetchall()
        if restaurants:
            print("All Restaurants:")
            for restaurant in restaurants:
                print(f"ID: {restaurant[0]}, Name: {restaurant[1]}, City: {restaurant[2]}")
        else:
            print("No restaurants found.")
    def show_all_menu_items(self, restaurant_id):
        query = "SELECT id, name, price FROM menu WHERE restaurant_id = %s"
        self.cursor.execute(query, (restaurant_id,))
        items = self.cursor.fetchall()
        if items:
            print("All Menu Items:")
            for item in items:
                print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]}")
        else:
            print("No menu items found for this restaurant.")