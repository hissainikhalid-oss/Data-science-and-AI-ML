#Task 1: Correlation Checker (Scatter Plots)

import matplotlib.pyplot as plt
#Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

#Create Scatter plot
plt.scatter(study_hours, scores)

#Add Title & Labels
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")

#Show plot
plt.show()

#Task 2: The Comparison Dashboard (Bar Charts & Subplots)

import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line chart
months = [1, 2, 3, 4, 5]
revenue = [2000, 3500, 3000, 5000, 6500]

# Create first subplot (Bar Chart)
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

# Create second subplot (Line Plot)
plt.subplot(1, 2, 2)
plt.plot(months, revenue)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

# Adjust layout
plt.tight_layout()

plt.show()