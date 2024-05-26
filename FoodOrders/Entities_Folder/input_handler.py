import datetime
from Entities_Folder.food_ordering_system import FoodOrderSystem  
def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        exit()
    return user_input

def main():
    ordering_system = FoodOrderSystem() 

    # Tüm restoranları göster
    ordering_system.show_all_restaurants()

    restaurant_id = get_input("Enter the ID of the restaurant you want to order from: ")
    available, restaurant_name, city = ordering_system.check_restaurant_availability(restaurant_id)
    if available:
        print(f"Restaurant '{restaurant_name}' in {city} is available for ordering.")
        ordering_system.show_all_menu_items(restaurant_id)
        
        item_ids = []
        total_cost = 0.0
        while True:
            item_id = get_input("Enter the ID of the menu item you want to order (or 'done' to finish): ")
            if item_id.lower() == 'done':
                break
            item_available, item_name, price = ordering_system.check_menu_item_availability(item_id)
            if item_available:
                print(f"Menu item '{item_name}' is available for {price}.")
                item_ids.append(item_id)
                total_cost += price
            else:
                print("Menu item is not available for ordering.")
        
        if item_ids:
            print(f"Total cost for the selected items: {total_cost}")
            confirm = get_input("Do you want to proceed with the order? (yes/no): ")
            if confirm.lower() == 'yes':
                while True:
                    card_number = get_input("Enter your credit card number: ").replace(" ", "")
                    if card_number.isdigit() and len(card_number) == 16:
                        break
                    else:
                        print("Invalid card number. Please enter a 16-digit card number without any letters or spaces.")
                while True:
                    expiration = get_input("Enter the expiration date (MM/YY): ")
                    if len(expiration) != 5 or not expiration[:2].isdigit() or not expiration[3:].isdigit() or expiration[2] != '/':
                        print("Invalid expiration date format. Please enter MM/YY.")
                        continue
                    month, year = map(int, expiration.split('/'))
                    current_month = datetime.datetime.now().month
                    current_year = datetime.datetime.now().year % 100  # Last two digits of the current year
                    if year < current_year or (year == current_year and month < current_month):
                        print("Card expired or invalid expiration date. Please enter a valid expiration date.")
                    else:
                        break
                while True:
                    cvc = get_input("Enter the CVV/CVC: ")
                    if cvc.isdigit() and 100 <= int(cvc) <= 999:
                        break
                    else:
                        print("Invalid CVC. Please enter a 3-digit CVC number.")
                while True:
                    holder = get_input("Enter the card holder's name: ")
                    if holder.replace(" ", "").isalpha():
                        break
                    else:
                        print("Invalid holder name. Please enter only letters.")
                valid, card_holder = ordering_system.validate_credit_card(card_number, expiration, cvc, holder)
                if valid:
                    print(f"Credit card validation successful for card holder '{card_holder}'. Placing orders...")
                    for item_id in item_ids:
                        ordering_system.place_order(item_id)
                    print("Orders successful! Enjoy your meals.")
                else:
                    print("Invalid credit card details.")
            else:
                print("Order cancelled.")
    else:
        print("Restaurant is not available for ordering.")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
