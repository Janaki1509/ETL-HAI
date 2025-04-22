import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import numpy as np

# DB config
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'healthcare'
DB_USER = 'admin'
DB_PASSWORD = 'admin123'

# Connect to PostgreSQL
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load data
df = pd.read_sql("SELECT * FROM infection_data", engine)

# Clean and convert 'score'
df['score'] = pd.to_numeric(df['score'], errors='coerce')

# Log-transform to handle outliers
df['log_score'] = df['score'].apply(lambda x: np.log1p(x))  # log1p handles 0 values safely

# Statistic Analysis
print("🔍 Row count:", len(df))

print("\n📊 Numeric Column Statistics:")
print(df.describe())

print("\n🔤 Categorical Column Statistics:")
print(df.describe(include=['object']))

print("\n🧪 Missing values:")
print(df.isnull().sum())

print("\n🔢 Unique values per column:")
print(df.nunique())

print("\n📋 Column-wise summary:")
summary = pd.DataFrame({
    "Data Type": df.dtypes,
    "Missing Values": df.isnull().sum(),
    "Unique Values": df.nunique(),
    "Sample Values": df.apply(lambda x: x.unique()[:5])
})
print(summary)

# Plot 1: Top 15 Infection Types
grouped = df.groupby('measure_id')['log_score'].mean().sort_values(ascending=False).head(15)
plt.figure(figsize=(12, 8))
sns.barplot(x=grouped.values, y=grouped.index, hue=grouped.index, palette='mako', errorbar=None, legend=False)
plt.xlabel("Average log(Score + 1)")
plt.ylabel("Measure ID")
plt.title("Top 15 Infection Types by Avg log(Score)")
plt.tight_layout()
plt.savefig("outputs/top_15_avg_log_score_by_measure.png")
plt.show()

# Plot 2: Average Score by State
state_avg = df.groupby('state')['log_score'].mean().sort_values(ascending=False)
plt.figure(figsize=(14, 6))
sns.barplot(x=state_avg.index, y=state_avg.values, hue=state_avg.index, palette="rocket", errorbar=None, legend=False)
plt.title("Average log(Score + 1) by State")
plt.ylabel("Avg log(Score)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("outputs/avg_log_score_by_state.png")
plt.show()
