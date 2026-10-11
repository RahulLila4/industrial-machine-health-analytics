import sqlite3
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# File paths
csv_path = PROJECT_ROOT / "data" / "processed" / "ai4i2020_processed.csv"
db_path = PROJECT_ROOT / "sql" / "machine_health.db"

# Load processed CSV
df_sql = pd.read_csv(csv_path)

# Connect to SQLite database
conn = sqlite3.connect(db_path)

# Load data into SQLite table
df_sql.to_sql(
    "machine_health",
    conn,
    if_exists="replace",
    index=False
)

# Close connection
conn.close()

print("Data loaded successfully.")
print("Rows loaded:", len(df_sql))