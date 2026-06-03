def calculate_bmi(weight_kg, height_m):

    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    result = {
        "bmi": bmi,
        "category": category
    }

    return result

# Test cases
person1 = calculate_bmi(50, 1.70)
person2 = calculate_bmi(70, 1.75)
person3 = calculate_bmi(85, 1.75)
person4 = calculate_bmi(100, 1.70)

print("Person 1:", person1)
print("Person 2:", person2)
print("Person 3:", person3)
print("Person 4:", person4)