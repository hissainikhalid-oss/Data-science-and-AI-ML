# Topic 1: Introduction to Matplotlib & Line Plots
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x, y)
plt.show()

# Topic 2: Scatter Plots for Relationship Analysis

x = [1,2,3,4,5,6]
y = [6,5,4,3,2,1]

plt.scatter(x,y)
plt.show()

#to3
import matplotlib.pyplot as plt

catagories =['laptop','pc','mobile']
valuas = [75000,120000,80000]
plt.bar(catagories,valuas)
plt.show()

# Topic 3: Bar Charts for Categorical Data
import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.plot([1,2,3],[1,4,9])
plt.title("line plot")
plt.subplot(1,2,2)
plt.bar(['A','B','C'],[3,7,5])
plt.title("Bar Chart")
plt.show()

# Task 1: The Trend Tracker (Line Plots)

import matplotlib.pyplot as plt
# Data
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]
# Create line plot
plt.plot(months,revenue)
# Add title and labels
plt.title("Monthly Revenue Growth")
plt.xlabel("months")
plt.ylabel("revenue is USD")

plt.show() # Show plot