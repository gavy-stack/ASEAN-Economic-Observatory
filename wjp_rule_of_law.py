import pandas as pd

# 1. Load the historical WJP dataset
file_path = "data/raw/wjp_historical.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Historical Data",
    header=1
)

# 2. Inspect the dataset
print("--- ORIGINAL DATASET ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- FIRST FIVE ROWS ---")
print(df.head())

print("\n--- COLUMN NAMES ---")
for column in df.columns:
    print(column)