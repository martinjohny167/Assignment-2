import mysql.connector

# Connection details
db_host = 'database-1.cyvg56cxbepj.us-east-1.rds.amazonaws.com'
db_user = 'admin'
db_password = '12345678'
db_name = 'companydb'

# SQL script to create table and add column
create_table_sql = """
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);
"""

add_column_sql = """
ALTER TABLE projects ADD COLUMN budget DECIMAL(10, 2);
"""

# Connect to MySQL
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = conn.cursor()

# Execute the CREATE TABLE statement
try:
    cursor.execute(create_table_sql)
    print("Table 'projects' created or already exists.")
    
    # Check if the 'budget' column exists
    cursor.execute("DESCRIBE projects")
    columns = [column[0] for column in cursor.fetchall()]
    
    if 'budget' not in columns:
        cursor.execute(add_column_sql)
        print("Column 'budget' added to the 'projects' table.")
    else:
        print("Column 'budget' already exists.")
    
    conn.commit()
    print("Database schema changes applied successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    conn.close()
