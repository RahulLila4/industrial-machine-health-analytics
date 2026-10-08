import sqlite3

# File paths
db_path = "E:/Industrial_Machine_Health_Analytics/sql/machine_health.db"
sql_path = "E:/Industrial_Machine_Health_Analytics/sql/01_basic_analysis.sql"

# Connect to database
conn = sqlite3.connect(db_path)

# Read SQL query
with open(sql_path, "r") as file:
    query = file.read()

# Execute query
cursor = conn.execute(query)

# Get column names
columns = [description[0] for description in cursor.description]

# Get results
results = cursor.fetchall()

# Display results
print("\nColumns:")
print(columns)

print("\nResults:")
for row in results:
    print(row)

# Close connection
conn.close()