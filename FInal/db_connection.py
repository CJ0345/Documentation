import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'kakanin_hub'
        self.user = 'root'  
        self.password = ''  

    def get_db_connection(self):
        """Create and return a MySQL connection."""
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                print("Connection successful!")
                return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def execute_query(self, query, params=None):
        """
        Execute a query with optional parameters.
        Returns:
            - For SELECT queries: list of rows.
            - For non-SELECT queries: the number of affected rows.
        """
        conn = self.get_db_connection()  
        if not conn:
            return None 
        
        try:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
      
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                return result
                 
            conn.commit()
            return cursor.rowcount  
        except Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def create_tables(self):
        """Create necessary tables for the application."""
        conn = self.get_db_connection()
        if not conn:
            print("Failed to connect to the database. Tables not created.")
            return
        
        try:
            cursor = conn.cursor()
            
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        price DECIMAL(10, 2) NOT NULL,
                        size VARCHAR(100) NOT NULL
                    );
                """)
                print("Products table created successfully.")
            except Error as e:
                print(f"Error creating products table: {e}")

            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS orders (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        customer_name VARCHAR(255) NOT NULL,
                        customer_email VARCHAR(255) NOT NULL,
                        address VARCHAR(255) NOT NULL,
                        product_id INT NOT NULL,
                        quantity INT NOT NULL,
                        total_price DECIMAL(10, 2) NOT NULL,
                        order_status VARCHAR(50) DEFAULT 'Pending',
                        FOREIGN KEY (product_id) REFERENCES products(id)
                    );
                """)
                print("Orders table created successfully.")
            except Error as e:
                print(f"Error creating orders table: {e}")
            
            conn.commit()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
                
if __name__ == "__main__":
    db = Database()
    conn = db.get_db_connection()  
    if conn:
        print("Database connection established.")
