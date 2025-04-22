import pandas as pd

def transform_data(df):
    df = df.dropna(subset=['Score'])
    df = df[df['Score'].apply(lambda x: str(x).replace('.', '', 1).isdigit())]
    df = df.drop_duplicates()

    df['Score'] = df['Score'].astype(float)
    df['Year'] = pd.to_datetime(df['Start Date']).dt.year
    df['Infection_Category'] = df['Measure Name'].apply(lambda x: x.split(' ')[0] if pd.notnull(x) else 'Unknown')

    columns_to_keep = ['Facility Name', 'State', 'Measure ID', 'Measure Name', 'Score', 'Year', 'Infection_Category']
    df_cleaned = df[columns_to_keep].copy()

    print("[Transform] Transformed data shape:", df_cleaned.shape)
    return df_cleaned

