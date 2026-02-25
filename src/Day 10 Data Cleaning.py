# Task 1: The Integrity Audit (Missing Values & Duplicates)

import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Shape before cleaning
print("Shape before cleaning:", df.shape)

# Missing values report
print("\nMissing values report:")
print(df.isna().sum())

# Fill missing numeric values with median
for col in df.select_dtypes(include='number'):
    df[col] = df[col].fillna(df[col].median())

# Remove duplicate rows
df = df.drop_duplicates()

# Shape after cleaning
print("\nShape after cleaning:", df.shape)

# Final cleaned data
print("\nCleaned Data:")
print(df)

# Task 2: The Type Fixer (Data Type Conversion)

import pandas as pd

# Sample data
df = pd.DataFrame({
    "Product": ["Fridges", "Ovens", "Television", "Mixer Grinder"],
    "Price": ["$1000", "$500", "$700", "$250"],
    "Date": ["2026-01-10", "2026-01-12", "2026-02-15", "2026-02-18"]
})

# 1. Check initial data types
print("Before conversion:")
print(df.dtypes)

# 2. Clean Price and convert to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# 3. Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check final data types
print("\nAfter conversion:")
print(df.dtypes)

# Now data is mathematically usable
print("\nAverage Price:", df["Price"].mean())

# Task 3: The Categorical Standardizer (String Cleaning)

import pandas as pd

df = pd.DataFrame({"Location": [" New York", "new york","NEW YORK "]})
print("Before normalization:")
print(df["Location"].unique())

# Normalize text
df["Location"] = df["Location"].str.strip().str.title()

# OR you can use .str.lower() instead of .str.title()
print("\nAfter normalization:")
print(df["Location"].unique())
