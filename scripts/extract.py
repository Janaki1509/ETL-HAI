import pandas as pd

def extract_data():
    file_path = "data/Healthcare_Associated_Infections-Hospital.csv"
    df = pd.read_csv(file_path)
    print("[Extract] Data shape:", df.shape)
    return df
