# Python Average Calculation with Robustness Improvements
This repository demonstrates a simple Python function to calculate the average of a list of numbers.  The original version was improved to handle various edge cases and potential errors more gracefully.

## Original Bug
The initial `calculate_average` function correctly handles empty lists.  However, it lacks robustness against non-numeric input. If the list contains strings or other non-numeric data types, it raises a `TypeError`. 

## Solution
The improved function includes error handling to check for non-numeric data types and provide a more informative error message.  This makes the function more robust and reliable.