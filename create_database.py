import mysql.connector

# Connect to MySQL Server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

# Create a new database
cursor = connection.cursor()
cursor.execute("CREATE DATABASE linky_db")
connection.commit()
print("Database created successfully")

# Create a new user and grant privileges
cursor.execute("CREATE USER 'linky'@'localhost' IDENTIFIED BY 'linky_JUNE2023'")
cursor.execute("GRANT ALL PRIVILEGES ON linky_db.* TO 'linky'@'localhost'")
cursor.execute("FLUSH PRIVILEGES")
connection.commit()
print("User created and privileges granted successfully")

# Close the connection
cursor.close()
connection.close()

