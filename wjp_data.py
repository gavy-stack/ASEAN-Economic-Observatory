
import pandas as pd

# 1. Read the Excel workbook
file_path = "data/raw/wjp_historical.xlsx"

excel = pd.ExcelFile(file_path)

# 2. Display all sheet names
print("--- WORKSHEET NAMES ---")
print(excel.sheet_names)

# 3. Inspect the first worksheet
df = pd.read_excel(file_path, sheet_name=0)

# 4. Display its dimensions
print("\n--- DATASET DIMENSIONS ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 5. Display column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# 6. Display the first five rows
print("\n--- FIRST FIVE ROWS ---")
print(df.head())

# 7. Display dataset information
print("\n--- DATASET INFORMATION ---")
df.info()
