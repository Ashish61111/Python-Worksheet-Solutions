def count_items(items_list):

    counts = {}

    for item in items_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


# Test case 1: Product sales
products = ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Laptop"]

result1 = count_items(products)

print("Product Sales Count:")
print(result1)


# Test case 2: Word frequency analysis
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

result2 = count_items(words)

print("\nWord Frequency Count:")
print(result2)