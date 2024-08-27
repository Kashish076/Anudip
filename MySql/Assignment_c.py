import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='food_ordering_system',
            user='root',
            password='Kash@123'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def fetch_foods(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM foods")
    return cursor.fetchall()

def fetch_drinks(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM drinks")
    return cursor.fetchall()

def place_order(connection, food_id, drink_id, quantity):
    cursor = connection.cursor()
    sql = "INSERT INTO orders (food_id, drink_id, quantity) VALUES (%s, %s, %s)"
    cursor.execute(sql, (food_id, drink_id, quantity))
    connection.commit()
    print("Order placed successfully")

def display_menu():
    print("1. View Foods")
    print("2. View Drinks")
    print("3. Place Order")
    print("4. Exit")

def main():
    connection = create_connection()
    if not connection:
        return

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            foods = fetch_foods(connection)
            print("Foods:")
            for food in foods:
                print(f"{food[0]}: {food[1]} - ${food[2]}")

        elif choice == '2':
            drinks = fetch_drinks(connection)
            print("Drinks:")
            for drink in drinks:
                print(f"{drink[0]}: {drink[1]} - ${drink[2]}")

        elif choice == '3':
            food_id = int(input("Enter food ID: "))
            drink_id = int(input("Enter drink ID: "))
            quantity = int(input("Enter quantity: "))
            place_order(connection, food_id, drink_id, quantity)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

    connection.close()

if __name__ == "__main__":
    main()
