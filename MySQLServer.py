import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host='localhost:3306',  
            user='root',       
            password='awh4edg#35aW'  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Creating the database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as e:
        # Handle connection errors
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()