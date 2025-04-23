from extract import extract_data
from transform import transform_data
from load import load_data
from verify_load import verify_load
import psycopg2

def run_etl():
    df = extract_data()
    df_clean = transform_data(df)
    
    # Save the cleaned data as a CSV file
    df_clean.to_csv("data/clean_data.csv", index=False)
    print("[Main] Cleaned CSV file saved at: data/clean_data.csv")

    load_data(df_clean)
    verify_load("infection_data")
    

if __name__ == "__main__":
    run_etl()
