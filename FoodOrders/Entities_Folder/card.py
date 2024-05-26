import mysql.connector
import datetime
from datetime import datetime

class Card:
    def __init__(self) -> None:
        pass 

    def add_card(self, card_number, expiration, cvc, holder, balance, config):
        # Check card_number 16 digit 
        if len(card_number) != 16 or not card_number.isdigit():
            print("Invalid card number. Please enter a 16-digit numeric card number.")
            return
        
        # Valid expiration date
        try:
            expiration_date = datetime.strptime(expiration, '%m/%y')
            if expiration_date < datetime.now():
                print("Invalid expiration date. Please enter a date after the current month.")
                return
        except ValueError:
            print("Invalid expiration date format. Please enter in MM/YY format.")
            return

        # Valid format for cvc 3 digit code
        if not cvc.isdigit() or len(cvc) != 3:
            print("Invalid CVC. Please enter a 3-digit numeric CVC.")
            return

        # Holder contains only letters 
        if not holder.replace(" ", "").isalpha():
            print("Invalid holder name. Please enter alphabetic characters only.")
            return
        if not balance.isdigit():
            print("Invalid balance. Please enter numeric characters only.")
            return
        else:
            print("Balance is valid.")

        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        query = "INSERT INTO card (card_number, expiration, cvc, holder, balance) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (card_number, expiration, cvc, holder, balance))

        connection.commit()
        cursor.close()
        connection.close()
        print("Card successfully added!")
        

    def check_card_balance(card_number, total_cost, config):
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            query = "SELECT balance FROM card WHERE card_number = %s"
            cursor.execute(query, (card_number,))
            balance = cursor.fetchone()
            cursor.close()
            connection.close()
            if balance:
                if balance[0] >= total_cost:
                    return True, balance[0]
                else:
                    return False, balance[0]
            else:
                return False, 0.0
        except mysql.connector.Error as error:
            print("Error: ", error)
            return False, 0.0
        
    def check_card_existence(card_number, config):
            try:
                connection = mysql.connector.connect(**config)
                cursor = connection.cursor()
                query = "SELECT * FROM card WHERE card_number = %s"
                cursor.execute(query, (card_number,))
                card = cursor.fetchone()
                cursor.close()
                connection.close()
                if card:
                    return True
                else:
                    return False
            except mysql.connector.Error as error:
                print("Error: ", error)
                return False