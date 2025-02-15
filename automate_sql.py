import mysql.connector
from mysql.connector import Error

# Database connection details
db_host = "database-1.cyvg56cxbepj.us-east-1.rds.amazonaws.com"  # RDS endpoint
db_user = "admin"  # Database username
db_password = "12345678"  # Database password
db_name = "companydb"  # Database name

# SQL script to create the departments table
sql_script = """
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);
"""

def execute_sql_script():
    try:
        # Establishing the connection to the database
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        if connection.is_connected():
            print("Connected to the database")

            cursor = connection.cursor()
            cursor.execute(sql_script)  # Execute the SQL script
            connection.commit()  # Commit the changes
            print("Departments table created successfully")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()  # Close cursor
            connection.close()  # Close connection
            print("Database connection closed")

if __name__ == "__main__":
    execute_sql_script()
