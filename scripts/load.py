import psycopg2

def load_data(df):
    conn = psycopg2.connect(
        dbname="healthcare",
        user="admin",
        password="admin123",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS infection_data (
            facility_name TEXT,
            state TEXT,
            measure_id TEXT,
            measure_name TEXT,
            score FLOAT,
            year INT,
            infection_category TEXT
        )
    """)

    # Wipe existing data before each run during development
    cur.execute("TRUNCATE TABLE infection_data")
    conn.commit()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO infection_data (facility_name, state, measure_id, measure_name, score, year, infection_category)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Facility Name'],
            row['State'],
            row['Measure ID'],
            row['Measure Name'],
            row['Score'],
            row['Year'],
            row['Infection_Category']
        ))

    conn.commit()
    print(f"[Load] Inserted {len(df)} rows into PostgreSQL.")
    cur.close()
    conn.close()