import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Kash@123'
        )
        if connection.is_connected():
            print("Connected to MySQL")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def create_database(connection):
    """Create the food_ordering_system database."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS food_ordering_system")
        print("Database created successfully")
    except Error as e:
        print(f"Error: '{e}'")

def create_tables(connection):
    """Create the foods, drinks, and orders tables."""
    try:
        cursor = connection.cursor()
        cursor.execute("USE food_ordering_system")
        
        foods_table = """
        CREATE TABLE IF NOT EXISTS foods (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(5,2) NOT NULL
        );
        """
        cursor.execute(foods_table)

        drinks_table = """
        CREATE TABLE IF NOT EXISTS drinks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(5,2) NOT NULL
        );
        """
        cursor.execute(drinks_table)

        orders_table = """
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            food_id INT,
            drink_id INT,
            quantity INT NOT NULL,
            order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (food_id) REFERENCES foods(id),
            FOREIGN KEY (drink_id) REFERENCES drinks(id)
        );
        """
        cursor.execute(orders_table)

        print("Tables created successfully")
    except Error as e:
        print(f"Error: '{e}'")

def main():
    connection = create_connection()
    if connection:
        create_database(connection)
        create_tables(connection)
        connection.close()

if __name__ == "__main__":
    main()

