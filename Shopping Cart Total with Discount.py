def calculate_total(prices, discount_percent=0):

    subtotal = sum(prices)

    discount_amount = subtotal * (discount_percent / 100)

    final_total = subtotal - discount_amount

    result = {
        "subtotal": round(subtotal, 2),
        "discount_amount": round(discount_amount, 2),
        "final_total": round(final_total, 2)
    }

    return result

# Test Case 1: No Discount
prices1 = [100, 200, 300]
print("Order 1:")
print(calculate_total(prices1))

# Test Case 2: 10% Discount
prices2 = [150, 250, 350]
print("\nOrder 2:")
print(calculate_total(prices2, 10))