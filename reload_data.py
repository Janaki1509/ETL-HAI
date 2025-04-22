import pandas as pd
from sqlalchemy import create_engine

# DB Configuration
DB_NAME = "healthcare"
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5432"
TABLE_NAME = "hospital_data"

# Load and Clean CSV
print("Reading CSV data...")
df = pd.read_csv("data/Healthcare_Associated_Infections-Hospital.csv")

# Strip whitespace from column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Expected clean columns: infection_type, number_of_infections, number_of_patients
print("Cleaning data...")

# Convert columns to numeric, forcing errors to NaN
df["number_of_infections"] = pd.to_numeric(df["number_of_infections"], errors="coerce")
df["number_of_patients"] = pd.to_numeric(df["number_of_patients"], errors="coerce")

# Drop rows with missing critical fields
df.dropna(subset=["infection_type", "number_of_infections", "number_of_patients"], inplace=True)

# Recalculate infection_rate
df["infection_rate"] = df["number_of_infections"] / df["number_of_patients"]

# Replace inf values from divide-by-zero
df["infection_rate"].replace([float('inf'), -float('inf')], pd.NA, inplace=True)

# Connect to PostgreSQL
print("🔌 Connecting to database...")
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Drop all existing data from the table
with engine.begin() as conn:
    print(f"Clearing table {TABLE_NAME}...")
    conn.execute(f"DELETE FROM {TABLE_NAME};")

# Insert cleaned data
print(f"Inserting {len(df)} cleaned records into {TABLE_NAME}...")
df.to_sql(TABLE_NAME, con=engine, if_exists="append", index=False)

print("Reload complete! Cleaned data inserted.")