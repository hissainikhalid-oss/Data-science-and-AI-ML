#Topic 1: Introduction to Pandas Series
import pandas as pd

s1=pd.Series([1,2,3,4,5])
print(s1)

s2=pd.Series([10,20,30,40,50],index=['p','q','r','s','t'])
print(s2)

#Topic 2: Indexing and Selection in Series
marks= pd.Series([50,60,70,80],index=['math','ph','ch','bio'])
print(marks['math'])
print(marks[['math','ch']])

# topice 3 Boolean Masking in Series
scores = pd.Series([50,63,69,70.5,90])
passed1 = scores[scores>70] #passed gerater than 70
print(passed1)

passed2 = scores[scores<70] #passed lass than 70
print(passed2)

#Topic 4: Handling Missing Data in Series

import numpy as np
import pandas as pd

data = pd.Series([10, None, 30,None])
data = pd.Series([10, None, 30,np.nan])

print(data.isnull())
print(data.fillna(40))

# Task 1: The Product Catalog (Series Creation & Indexing)

import pandas as pd

products = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])

print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(products['Laptop'])

print("\nFirst two products:")
print(products[:2])

# Task 2: The Grade Filter (Boolean Masking & Missing Data)

name = pd.Series( [' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
data = pd.Series([ 85, None, 92, 45, None, 78, 55]) 
print(data.isnull()) # Identify missing values
print(data.fillna(0)) # Fill missing values with 0

passed = data[data>60] # Boolean masking: scores greater than 60
print(passed)

# Task 3: The Username Formatter (Vectorized String Operations)

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Remove spaces and convert to lowercase
cleaned = usernames.str.strip().str.lower()
print(cleaned)

# Check which names contain letter 'a'
contains_a = cleaned.str.contains('a')
print(contains_a)
