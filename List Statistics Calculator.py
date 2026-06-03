def calculate_statistics(numbers):

    if len(numbers) == 0:
        return "List is empty"

    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    count = len(numbers)

    statistics = {
        "mean": mean,
        "max": maximum,
        "min": minimum,
        "count": count
    }

    return statistics

# Test case 1
numbers1 = [10, 20, 30, 40, 50]
result1 = calculate_statistics(numbers1)
print("Statistics for", numbers1)
print(result1)

# Test case 2 (empty list)
numbers2 = []
result2 = calculate_statistics(numbers2)
print("\nStatistics for", numbers2)
print(result2)