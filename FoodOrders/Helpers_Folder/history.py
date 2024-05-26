class OrderHistory:
    def __init__(self):
        self.order_history = []

    def add_order(self, restaurant_name, city, items, total_cost, date):
        order = {
            'restaurant_name': restaurant_name,
            'city': city,
            'items': items,
            'total_cost': total_cost,
            'date': date
        }
        self.order_history.append(order)

    def show_order_history(self):
        if not self.order_history:
            print("No orders have been made yet.")
        else:
            print("Order History:")
            for i, order in enumerate(self.order_history, 1):
                print(f"Order {i}:")
                print(f"  Restaurant: {order['restaurant_name']}")
                print(f"  City: {order['city']}")
                print(f"  Items: {', '.join(order['items'])}")
                print(f"  Total Cost: {order['total_cost']}")
                print(f"  Date: {order['date']}")
                print()
