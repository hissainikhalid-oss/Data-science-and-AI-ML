p_rain = 0.5
p_traffic = 0.2
p_both = p_rain * p_traffic
print("probability of Rain = ", p_rain)
print("probability of traffic = ", p_traffic)
print("probability of both Rain and trffic = ",p_both)
print("-" * 50)


# Task 1

import random

trials = 1000
count_sum_7 = 0

for i in range(trials):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_prob = count_sum_7 / trials
print("Experimental Probability of sum = 7:", experimental_prob)

# Task 2

import random

# Part 1: Independent Events
# Coin = Heads AND Die = 6

p_heads = 1/2
p_six = 1/6

p_independent = p_heads * p_six
print("Probability (Heads AND 6):", p_independent)


# Part 2: Dependent Events
# 5 Red, 5 Blue marbles
# Pick 2 Red without replacement

red = 5
total = 10

# First pick
p_first_red = red / total

# Second pick (after one red removed)
p_second_red = (red - 1) / (total - 1)

p_dependent = p_first_red * p_second_red
print("Probability (Both Red):", p_dependent)


# Part 3: Dice Simulation
# Experimental Probability

trials = 1000
count_sum_7 = 0

for i in range(trials):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    
    if d1 + d2 == 7:
        count_sum_7 += 1

experimental_prob = count_sum_7 / trials
print("Experimental Probability (Sum = 7):", experimental_prob)

# Task 3

# Given probabilities
p_spam = 0.1
p_ham = 0.9

p_free_given_spam = 0.9
p_free_given_ham = 0.05

# Step 1: Total probability of "Free"
p_free = (p_free_given_spam * p_spam) + (p_free_given_ham * p_ham)

# Step 2: Bayes Theorem
p_spam_given_free = (p_free_given_spam * p_spam) / p_free

# Output
print("P(Spam) =", p_spam)
print("P(Free | Spam) =", p_free_given_spam)
print("P(Free | Ham) =", p_free_given_ham)
print("Total P(Free) =", p_free)
print("Final Answer -> P(Spam | Free) =", p_spam_given_free)
