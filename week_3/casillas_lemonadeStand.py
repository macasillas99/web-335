"""
Author: Maxine Casillas
Date: June 21, 2026
File Name: casillas_lemonadeStand.py
Description: This program calculates the cost and profit for a lemonade stand.
"""

# Defining a function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost # Adding the lemon and sugar costs together
    return total_cost # Returning the total cost


# Defining a function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = lemons_cost + sugar_cost # Adding the lemon and sugar costs together
    profit = selling_price - total_cost # Subtracting the total cost from the selling price
    return profit # Returning the profit


# Creating variables to test the calculate_cost function
lemons_cost = 5
sugar_cost = 3
total_cost = calculate_cost(lemons_cost, sugar_cost)

# Building a string for the cost result using string concatenation
cost_output = str(lemons_cost) + " + " + str(sugar_cost) + " = " + str(total_cost)

# Printing the cost result to the console
print(cost_output)


# Creating variables to test the calculate_profit function
selling_price = 12
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

# Building a string for the profit result using string concatenation
profit_output = str(selling_price) + " - " + str(total_cost) + " = " + str(profit)

# Printing the profit result to the console
print(profit_output)
