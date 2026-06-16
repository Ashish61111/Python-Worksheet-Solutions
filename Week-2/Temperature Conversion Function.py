def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius1 = 0
celsius2 = 25
celsius3 = 100

fahrenheit1 = celsius_to_fahrenheit(celsius1)
fahrenheit2 = celsius_to_fahrenheit(celsius2)
fahrenheit3 = celsius_to_fahrenheit(celsius3)

print(celsius1, "degrees Celsius =", fahrenheit1, "degrees Fahrenheit")
print(celsius2, "degrees Celsius =", fahrenheit2, "degrees Fahrenheit")
print(celsius3, "degrees Celsius =", fahrenheit3, "degrees Fahrenheit")