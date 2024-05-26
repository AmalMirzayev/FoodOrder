from Entities_Folder.food_ordering_system import FoodOrderSystem  
from Entities_Folder.CreditCardValidator import CreditCardValidator
from Entities_Folder.input_handler import get_input
from Helpers_Folder.search import search_menu_item 
from Entities_Folder.card import Card
from Entities_Folder.update import Update
from datetime import datetime
from Helpers_Folder.history import OrderHistory  # Order history sınıfını import ediyoruz

# MySQL connection configuration
config = {
    'user': 'root',
    'password': 'Amal1234',
    'host': 'localhost',
    'database': 'course'
}

def show_menu():
    print("1 - Add order")
    print("2 - Search menu item")
    print("3 - Show All restaurants")
    print("4 - Exit")
    print("5 - Add Your Card")
    print("6 - Show Order History")

def main():
    ordering_system = FoodOrderSystem()
    validator = CreditCardValidator()
    order_history = OrderHistory()

    while True:
        show_menu()
        choice = get_input("Choose an option: ")

        if choice == '1':
            ordering_system.show_all_restaurants()
            restaurant_id = get_input("Enter the ID of the restaurant you want to order from: ")
            available, restaurant_name, city = ordering_system.check_restaurant_availability(restaurant_id)
            if available:
                print(f"'{restaurant_name}' restaurant in {city} is available for ordering.")
                menu_items = ordering_system.show_all_menu_items(restaurant_id)
                if menu_items is None:
                    print("No menu items available for this restaurant.")
                    continue
                valid_item_ids = [item[0] for item in menu_items]  # Valid id 
                
                item_ids = []
                item_names = []
                total_cost = 0.0

                # Loop for Menu items choosing
                while True:
                    item_id = get_input("Enter the ID of the menu item you want to order (type 'done' to finish): ")
                    if item_id.lower() == 'done':
                        break
                    if not item_id.isdigit() or int(item_id) not in valid_item_ids:
                        print(f"Invalid menu item ID. Please select a valid ID from the restaurant's menu: {valid_item_ids}")
                        continue
                    item_available, item_name, price = ordering_system.check_menu_item_availability(item_id)
                    if item_available:
                        print(f"'{item_name}' menu item is available for {price}.")
                        item_ids.append(item_id)
                        item_names.append(item_name)
                        total_cost += price
                    else:
                        print("Menu item is not available for ordering in this restaurant.")
                
                if item_ids:
                    print(f"Total cost of selected items: {total_cost}")
                    confirm = get_input("Do you want to complete the order? (yes/no): ")
                    if confirm.lower() == 'yes':
                        while True:
                            card_number = get_input("Enter your credit card number: ").replace(" ", "")
                            if card_number.isdigit() and len(card_number) == 16:
                                break
                            else:
                                print("Invalid card number. Please enter a 16-digit card number without any letters or spaces.")
                        while True:
                            expiration = get_input("Enter the expiration date (MM/YY): ")
                            if len(expiration) != 5 or not expiration[:2].isdigit() or not expiration[3:].isdigit():
                                print("Invalid expiration date format. Please enter in MM/YY format.")
                            else:
                                month, year = map(int, expiration.split('/'))
                                current_month = datetime.now().month
                                current_year = datetime.now().year % 100  
                                if year < current_year or (year == current_year and month < current_month):
                                    print("Card has expired or invalid expiration date. Please enter a valid expiration date.")
                                else:
                                    break
                        while True:
                            cvc = get_input("Enter the CVV/CVC: ")
                            if cvc.isdigit() and len(cvc) == 3:
                                break
                            else:
                                print("Invalid CVV/CVC. Please enter a 3-digit CVV/CVC number.")
                        while True:
                            holder = get_input("Enter the cardholder's name: ")
                            if holder.replace(" ", "").isalpha():
                                break
                            else:
                                print("Invalid cardholder name. Please enter alphabetic characters only.")
                        valid, card_holder = validator.validate_credit_card(card_number, expiration, cvc, holder)
                        if valid:
                            has_balance, balance = Card.check_card_balance(card_number, total_cost, config)
                            if has_balance:
                                print(f"Credit card validation for {card_holder} successful and sufficient balance available. Placing orders...")
                                for item_id in item_ids:
                                    ordering_system.place_order(item_id)
                                    Update.update_menu_item_availability(item_id, config)  # Decrease the 'available' value of ordered menu item
                                    Update.update_restaurant_availability(restaurant_id, config)  # Decrease the 'available' value of the restaurant
                                
                                # Save order history
                                order_history.add_order(
                                    restaurant_name=restaurant_name,
                                    city=city,
                                    items=item_names,
                                    total_cost=total_cost,
                                    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                )
                                
                                print("Orders placed successfully! Enjoy your meal.")
                            else:
                                print(f"Insufficient balance. Current balance: {balance}, required balance: {total_cost}.")
                        else:
                            print("Invalid credit card information.")
                    else:
                        print("Order canceled.")
                else:
                    print("No menu items selected for ordering.")
            else:
                print("Restaurant not available for ordering.")
        
        elif choice == '2':
            item_name = get_input("Enter the name of the menu item you want to search for: ")
            search_menu_item(item_name)
        
        elif choice == '3':
            ordering_system.show_all_restaurants()
        
        elif choice == '4':
            print("Exiting the program...")
            break
        
        elif choice == '5':
            card_number = input("Card Number: ")
            while len(card_number) != 16 or not card_number.isdigit():
                print("Invalid card number. Please enter a 16-digit numeric card number.")
                card_number = input("Card Number: ")
            
            expiration = input("Expiration Date (MM/YY): ")
            while True:
                try:
                    expiration_date = datetime.strptime(expiration, '%m/%y')
                    if expiration_date < datetime.now():
                        print("Invalid expiration date. Please enter a date after the current month.")
                        expiration = input("Expiration Date (MM/YY): ")
                        continue
                    break
                except ValueError:
                    print("Invalid expiration date format. Please enter in MM/YY format.")
                    expiration = input("Expiration Date (MM/YY): ")

            cvc = input("CVC: ")
            while not cvc.isdigit() or len(cvc) != 3:
                print("Invalid CVC. Please enter a 3-digit numeric CVC.")
                cvc = input("CVC: ")

            holder = input("Card Holder: ")
            while not holder.replace(" ", "").isalpha():
                print("Invalid holder name. Please enter alphabetic characters only.")
                holder = input("Card Holder: ")
            
            balance_input = input("Balance: ")
            while True:
                if not balance_input.isdigit():
                    print("Invalid balance format. Please enter numeric values only.")
                    balance_input = input("Balance: ")
                else:
                    balance = balance_input 
                    break
            
            CD = Card()
            CD.add_card(card_number, expiration, cvc, holder, balance, config)

        elif choice == '6':
            order_history.show_order_history()

        else:
            print("Invalid option. Please choose an option between 1 and 6.")

if __name__ == "__main__":
    main()
