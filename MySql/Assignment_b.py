import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Kash@123',
            database='food_ordering_system'
        )
        if connection.is_connected():
            print("Connected to MySQL")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def insert_data(connection):
    """Insert data into the foods and drinks tables."""
    try:
        cursor = connection.cursor()

        foods_query = """
        INSERT INTO foods (name, price) VALUES
        ('Pizza', 8.99),
        ('Burger', 5.99),
        ('Pasta', 7.99);
        """
        cursor.execute(foods_query)

        drinks_query = """
        INSERT INTO drinks (name, price) VALUES
        ('Coke', 1.99),
        ('Water', 0.99),
        ('Juice', 2.99);
        """
        cursor.execute(drinks_query)

        connection.commit()
        print("Data inserted successfully")

    except Error as e:
        print(f"Error: '{e}'")
        connection.rollback()

def main():
    connection = create_connection()
    if connection:
        insert_data(connection)
        connection.close()

if __name__ == "__main__":
    main()
