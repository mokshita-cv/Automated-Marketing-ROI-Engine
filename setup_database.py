import mysql.connector
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

try:
    # 1. Connect to your local MySQL server
    conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
    cursor = conn.cursor()
    print(" Connected to MySQL Server successfully!")

    # 2. Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS marketing_roi_db")
    print("📁 Database 'marketing_roi_db' verified/created.")

    # 3. Switch to our new database
    cursor.execute("USE marketing_roi_db")

    # 4. Create our tracking table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS marketing_logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(100),
            segment VARCHAR(50),
            action_executed VARCHAR(255),
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("📋 Table 'marketing_logs' verified/created successfully!")

    # Commit changes and close
    conn.commit()
    cursor.close()
    conn.close()
    print("✨ Database setup complete!")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")