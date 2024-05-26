# import mysql.connector
import datetime
from Helpers_Folder import connection as conn

class CreditCardValidator:
    
    def __init__(self):
        pass
        # self.connection = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     password='Amal1234',
        #     database='course'
        # )
        # self.cursor = self.connection.cursor()

    def CreditCardValidator(prompt):
        user_input = input(prompt)
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            exit()
        return user_input


    def validate_credit_card(self, card_number, expiration, cvc, holder):
        # Check Valid informations for variables
        if len(card_number) == 16 and len(expiration) == 5 and len(cvc) == 3 and holder.isalpha():
            #   Check CVC
            if not (100 <= int(cvc) <= 999):
                return False, "Invalid CVC"

            # Check expiration date
            if not expiration[:2].isdigit() or not expiration[3:].isdigit():
                return False, "Invalid expiration date format"

            month, year = map(int, expiration.split('/'))
            current_month = datetime.datetime.now().month
            current_year = datetime.datetime.now().year % 100  # Last 2 number of the year

            if year < current_year or (year == current_year and month < current_month):
                return False, "The card has expired"
            return True, holder  # Card accepted

        else:
            return False, None  # Invalid Card informations
