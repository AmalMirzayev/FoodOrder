import mysql.connector

def add_card(card_number, expiration, cvc, holder, balance):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Amal1234',
        database='Course'
    )
    cursor = connection.cursor()

    query = "INSERT INTO card (card_number, expiration, cvc, holder, balance) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (card_number, expiration, cvc, holder, balance))

    connection.commit()
    cursor.close()
    connection.close()
    print("The card has been successfully added!")

def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == 'exit':
        print("Exiting the program...")
        exit()
    return user_input

if __name__ == "__main__":
    while True:
        card_number = get_input("Enter your card number: ( type 'exit' to quit): ")
        expiration = get_input("Expiration Date (MM/YY): ( type 'exit' to quit): ")
        cvc = get_input("CVC: ( type 'exit' to quit): ")
        holder = get_input("Cardholder: ( type 'exit' to quit): ")
        balance_input = get_input("Balance: ( type 'exit' to quit): ")

        if balance_input.lower() == 'exit':
            print("Exiting the program...")
            break

        try:
            balance = float(balance_input)
        except ValueError:
            print("Invalid input for balance. Please enter a valid number.")
            continue

        add_card(card_number, expiration, cvc, holder, balance)
