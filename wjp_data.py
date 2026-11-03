
import pandas as pd

# 1. Read the historical dataset
file_path = "data/raw/wjp_historical.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Historical Data",
    header=1
)

# 2. Inspect the dataset
print("--- DATASET DIMENSIONS ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- FIRST FIVE ROWS ---")
print(df.head())

print("\n--- DATASET INFORMATION ---")
df.info()

# 3. Inspect the first five columns
print("\n--- FIRST FIVE COLUMNS ---")
print(df.iloc[:, :5].head(10))
