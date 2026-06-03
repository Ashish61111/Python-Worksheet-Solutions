def separate_even_odd(numbers):

    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return (even_numbers, odd_numbers)


# Test case
numbers = [10, 15, 22, 33, 40, 51, 68, 79]

result = separate_even_odd(numbers)

print("Original List:", numbers)
print("Even Numbers:", result[0])
print("Odd Numbers:", result[1])