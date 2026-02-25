# Task 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
df = pd.read_excel("Housing_with_City.xlsx")

# 1.Histogram with KDE

sns.histplot(df["price"], kde=True)
plt.title("Distribution of Housing prices")
plt.xlabel("price")
plt.ylabel("Frequency")
plt.show()

# 2.Skewness and Kurtosis
print("Skewness:", df["price"].skew())
print("Kurtosis:", df["price"].kurt())

# 3.Count Plot for categorical column
sns.countplot(x="City", data=df)
plt.title("City Frequency")
plt.show()

# Task2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1.Load dataset
df = pd.read_excel("Housing_with_City.xlsx")

# 2.Scatter Plot: Area vs Price
plt.scatter(df["area"], df["price"])
plt.title("House Area vs price")
plt.xlabel("Area (Square Footage)")
plt.ylabel("price")
plt.show()

# 3.Boxplot: City vs Price
sns.boxplot(x="City", y="price", data=df)
plt.title("Price Distribution by City")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()

#TASK 3: The Pattern Finder
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1.Load dataset
df = pd.read_excel("Housing_with_City.xlsx")

# 2.Correlation
plt.subplot(1,2,1)
corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
print("There are no two variables with correlation score higher than 0.8")
sns.heatmap(corr_matrix,annot=True)
plt.show()

# 3.Boxplot 
plt.subplot(1,2,2)
sns.boxplot(x=df ['price'])
plt.xlabel('Price')
plt.show()
plt.tight_layout()