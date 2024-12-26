def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list or non-numeric input
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average is: {average}")

my_mixed_list = [1, 2, 'a', 4, 5]
average = calculate_average(my_mixed_list)
print(f"The average is: {average}")

my_string_list = ['a', 'b', 'c']
average = calculate_average(my_string_list)
print(f"The average is: {average}") #Handles non-numeric list