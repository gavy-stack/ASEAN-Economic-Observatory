
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


# 4. Investigate historical coverage

print("\n--- YEAR DISTRIBUTION ---")
print(df["Year"].value_counts())

print("\n--- UNIQUE YEARS ---")
print(df["Year"].unique())

print("\n--- YEAR DATA TYPES ---")
print(df["Year"].apply(type).value_counts())

# 5. Investigate country coverage

print("\n--- COUNTRY COVERAGE ---")
print("Number of countries:", df["Country"].nunique())

# 6. List ASEAN countries in the dataset

asean_countries = [
    "Singapore",
    "Malaysia",
    "Philippines",
    "Thailand",
    "Indonesia",
    "Vietnam",
    "Myanmar",
    "Cambodia"
]

asean_df = df[df["Country"].isin(asean_countries)]

print("\n--- ASEAN COUNTRY COVERAGE ---")
print(asean_df["Country"].value_counts())

# 7. Investigate the years available for each ASEAN country

print("\n--- ASEAN HISTORICAL COVERAGE ---")

# Preserve the original Year column and create a text version
asean_df = asean_df.copy()
asean_df["Year_label"] = asean_df["Year"].astype(str)

# Extract the starting year from each observation period
asean_df["Year_start"] = pd.to_numeric(
    asean_df["Year_label"].str[:4]
)

# Summarise coverage for each country
coverage = (
    asean_df.groupby("Country")
    .agg(
        first_period=("Year_start", "min"),
        last_period=("Year_start", "max"),
        periods_available=("Year_label", "nunique")
    )
)

print(coverage)

# Show the actual observation periods for each country
print("\n--- AVAILABLE PERIODS BY COUNTRY ---")

periods_by_country = (
    asean_df.sort_values("Year_start")
    .groupby("Country")["Year_label"]
    .agg(lambda periods: ", ".join(periods))
)

print(periods_by_country)

# 8. Check duplicate country-year observations

print("\n--- DUPLICATE COUNTRY-YEAR PAIRS ---")

duplicates = df.duplicated(
    subset=["Country", "Year"]
).sum()

print("Duplicate observations:", duplicates)

# 9. Identify missing observation periods

print("\n--- MISSING PERIODS BY ASEAN COUNTRY ---")

expected_periods = [
    "2012-2013",
    "2014",
    "2015",
    "2016",
    "2017-2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023",
    "2024",
    "2025",
    "2026"
]

for country in asean_countries:

    available = asean_df.loc[
        asean_df["Country"] == country,
        "Year_label"
    ].tolist()

    missing = [
        period for period in expected_periods
        if period not in available
    ]

    print(country, ":", missing if missing else "No missing periods")

# 10. Inspect historical indicator names

historical_sheets = [
    "WJP ROL Index 2012-2013 Scores",
    "WJP ROL Index 2014 Scores",
    "WJP ROL Index 2015 Scores"
]

for sheet in historical_sheets:

    print(f"\n--- {sheet} ---")

    historical_df = pd.read_excel(
        file_path,
        sheet_name=sheet,
        header=None
    )

    # Extract non-empty labels from the first column
    labels = (
        historical_df.iloc[:, 0]
        .dropna()
        .astype(str)
        .str.strip()
    )

    for label in labels:
        print(label)

# 11. Compare original 2012-2013 scores with consolidated historical data

# First, inspect Indonesia in the consolidated dataset

print("\n--- INDONESIA: CONSOLIDATED HISTORICAL DATA ---")

indonesia_historical = df[
    (df["Country"] == "Indonesia") &
    (df["Year"].astype(str) == "2012-2013")
]

selected_columns = [
    "Country",
    "Year",
    "WJP Rule of Law Index: Overall Score",
    "Factor 1: Constraints on Government Powers",
    "Factor 2: Absence of Corruption",
    "Factor 3: Open Government ",
    "Factor 5: Order and Security",
    "Factor 7: Civil Justice",
    "Factor 8: Criminal Justice"
]

print(indonesia_historical[selected_columns].to_string(index=False))


# Now, inspect Indonesia in the original 2012-2013 worksheet

print("\n--- INDONESIA: ORIGINAL 2012-2013 WORKSHEET ---")

original_df = pd.read_excel(
    file_path,
    sheet_name="WJP ROL Index 2012-2013 Scores",
    header=None
)

# Find the row containing country names
country_row = original_df[
    original_df.eq("Country").any(axis=1)
].index[0]

# Find Indonesia's column
indonesia_column = original_df.iloc[country_row].eq("Indonesia").idxmax()

# Print indicator labels and Indonesia's scores
for index, label in original_df.iloc[:, 0].items():

    if pd.notna(label):

        score = original_df.iloc[index, indonesia_column]

        print(label, ":", score)

# 12. Inspect consolidated subfactor scores for Indonesia, 2012-2013

print("\n--- CONSOLIDATED SUBFACTOR SCORES ---")

for column in df.columns:

    if column.startswith(("1.", "3.", "5.", "7.", "8.")):

        score = indonesia_historical.iloc[0][column]

        print(f"{column}: {score:.6f}")

# 13. Check coverage of selected Rule of Law indicators

rule_of_law_columns = [
    "Factor 7: Civil Justice",
    "7.1 People can access and afford civil justice",
    "7.3 Civil justice is free of corruption",
    "7.4 Civil justice is free of improper government influence",
    "7.5 Civil justice is not subject to unreasonable delay",
    "7.6. Civil justice is effectively enforced",
    "Factor 8: Criminal Justice",
    "8.1 Criminal investigation system is effective",
    "8.2 Criminal adjudication system is timely and effective",
    "8.3 Correctional system is effective in reducing criminal behavior",
    "8.4 Criminal system is impartial",
    "8.6 Criminal system is free of improper government influence",
    "8.7. Due process of the law and rights of the accused"
]

# Limit the observations to our research period
wjp_research = asean_df[
    asean_df["Year_start"].between(2012, 2024)
].copy()

print("\n--- RULE OF LAW INDICATOR COVERAGE ---")

print(
    wjp_research[rule_of_law_columns]
    .isna()
    .sum()
    .to_string()
)

print("\n--- NON-MISSING OBSERVATIONS ---")

print(
    wjp_research[rule_of_law_columns]
    .count()
    .to_string()
)