
import datetime
import mysql.connector

class FoodOrderSystem:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Amal1234',
            database='course'
        )
        self.cursor = self.connection.cursor()

    def check_card_balance(self, card_number, expiration, cvc, holder):
        query = "SELECT balance FROM card WHERE card_number = %s AND expiration = %s AND cvc = %s AND holder = %s"
        self.cursor.execute(query, (card_number, expiration, cvc, holder))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def update_card_balance(self, card_number, new_balance):
        query = "UPDATE card SET balance = %s WHERE card_number = %s"
        self.cursor.execute(query, (new_balance, card_number))
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def check_restaurant_availability(self, restaurant_id):
        query = "SELECT name, city FROM restaurant WHERE id = %s"
        self.cursor.execute(query, (restaurant_id,))
        result = self.cursor.fetchone()
        if result:
            return True, result[0], result[1]  # (available, restaurant_name, city)
        else:
            return False, None, None

    def check_menu_item_availability(self, item_id):
        query = "SELECT name, price, available FROM menu WHERE id = %s"
        self.cursor.execute(query, (item_id,))
        result = self.cursor.fetchone()
        if result:
            available = result[2]
            if available > 0:
                return True, result[0], float(result[1])  # (available, item_name, price)
            else:
                print("This item is out of stock.")
                return False, None, None
        else:
            print("Menu item not found.")
            return False, None, None


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
            return items
        else:
            print("No menu items found for this restaurant.")

            
    def validate_credit_card(self, card_number, expiration, cvc, holder):
        if not (100 <= int(cvc) <= 999):
            return False, "Invalid CVC"
        
        # Check expiration date format
        if len(expiration) != 5 or not expiration[:2].isdigit() or not expiration[3:].isdigit():
            return False, "Invalid expiration date format"

        month, year = map(int, expiration.split('/'))
        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year - 2000  #current year's last two digits

        if year < current_year or (year == current_year and month < current_month):
            return False, "Card expired"

        query = "SELECT holder FROM card WHERE number = %s AND expiration = %s AND cvc = %s"
        self.cursor.execute(query, (card_number, expiration, cvc))
        result = self.cursor.fetchone()
        if result:
            return True, result[0]  # (valid, card_holder)
        else:
            query = "INSERT INTO card (number, expiration, cvc, holder) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (card_number, expiration, cvc, holder))
            self.connection.commit()
            return True, holder  