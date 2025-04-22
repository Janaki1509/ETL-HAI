import psycopg2


def verify_load(table_name: str):
    conn = psycopg2.connect( 
        dbname="healthcare",
        user="admin",
        password="admin123",
        host="localhost",
        port="5432")
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    result = cursor.fetchone()
    print(f" Verification: {result[0]} rows loaded in table `{table_name}`\n")

    cursor.close()
    conn.close()
