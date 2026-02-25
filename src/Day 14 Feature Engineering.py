# Task 1
import pandas as pd

# Sample dataset
df = pd.read_csv("Car_datasets.csv")
print("Original Data:")
print(df)

# 1. Label Encoding (Binary)
df["Transmission"] = df["Transmission"].map({"Automatic": 1, "Manual": 0})

# 2. One-Hot Encoding (Nominal)
df_encoded = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nEncoded Data:")
print(df_encoded)

# Task 2

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load dataset
df = pd.read_csv("employee_salary.csv")
print(df)

# Select numeric features
features = df[["Age","Salary"]]

# --------------------
# Standardization
# --------------------
std_scaler = StandardScaler()
standardized = std_scaler.fit_transform(features)
df_std = pd.DataFrame(standardized, columns=["Age_std","Salary_std"])

print("\nStandardized Data:\n", df_std)

# --------------------
# Normalization
# --------------------
mm_scaler = MinMaxScaler()
normalized = mm_scaler.fit_transform(features)
df_norm = pd.DataFrame(normalized, columns=["Age_norm","Salary_norm"])

print("\nNormalized Data:\n", df_norm)

# --------------------
# Histograms
# --------------------
plt.figure(figsize=(12,4))

# Original Salary
plt.subplot(1,3,1)
plt.hist(df["Salary"])
plt.title("Original Salary")

# Standardized Salary
plt.subplot(1,3,2)
plt.hist(df_std["Salary_std"])
plt.title("Standardized Salary")

# Normalized Salary
plt.subplot(1,3,3)
plt.hist(df_norm["Salary_norm"])
plt.title("Normalized Salary")

plt.tight_layout()
plt.show()

# Task 3

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("employee_salary.csv")

# Feature & Target
X = df[["Experience"]]   # Non-linear feature
y = df["Salary"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 1. Simple Linear Model

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_pred_lin = lin_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_lin)

# 2. Polynomial Model

poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)
y_pred_poly = poly_model.predict(X_poly_test)
r2_poly = r2_score(y_test, y_pred_poly)

# Output

print("R2 Score (Linear):", r2_linear)
print("R2 Score (Polynomial):", r2_poly)