numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [num ** 2 for num in numbers]

even_numbers = list(filter(lambda num: num % 2 == 0, numbers))

print("Original List:", numbers)
print("Squares List:", squares)
print("Even Numbers:", even_numbers)