import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate datasets

# Normal Distribution (Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-Skewed (Income)
income = np.random.exponential(scale=50000, size=1000)

# Left-Skewed (Easy Exam)
scores = 100 - np.random.exponential(scale=15, size=1000)

# Create DataFrame
df = pd.DataFrame({
    "Heights": heights,
    "Income": income,
    "Scores": scores
})

# Plot Histograms with KDE
plt.figure(figsize=(15,4))

plt.subplot(1,3,1)
sns.histplot(df["Heights"], kde=True)
plt.title("Normal Distribution (Heights)")

plt.subplot(1,3,2)
sns.histplot(df["Income"], kde=True)
plt.title("Right Skewed (Income)")

plt.subplot(1,3,3)
sns.histplot(df["Scores"], kde=True)
plt.title("Left Skewed (Scores)")

plt.tight_layout()
plt.show()

# Compare Mean & Median
for col in df.columns:
    print(f"{col}")
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("-"*30)

# Task 2
       
import pandas as pd
import numpy as np

# STEP 0: Create Your Dataset
data = {"value": [50, 52, 49, 51, 48, 200, 47, 53, 46, 54]}

df = pd.DataFrame(data)

# Step 1:Calculate Mean 
mean = df["value"].mean()

# Step 2:Calculate Standard Deviation 
std_dev = df["value"].std()

# Step 3:Calculate Z-Score
# Z = (x - μ) / σ
df["z_score"] = (df["value"] - mean) / std_dev

# Step 4:Identify Outliers
# |Z| > 3
outliers = df[np.abs(df["z_score"]) > 3]

# OUTPUT RESULTS
print("Mean (μ):", mean)
print("Standard Deviation (σ):", std_dev)

print("\nDataset with Z-Scores:")
print(df)

print("\nStatistical Outliers (|Z| > 3):")
print(outliers)

# Task 3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1️ Create a heavily skewed dataset (income-like using exponential distribution)
np.random.seed(42)
population = np.random.exponential(scale=50000, size=100000)

# 2️ Take 1,000 samples of size 30 and compute means
sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# 3️ Plot histogram of sample means
plt.figure(figsize=(8, 5))
sns.histplot(sample_means, bins=30, kde=True)

plt.title("Distribution of Sample Means (n=30, 1000 samples)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.show()