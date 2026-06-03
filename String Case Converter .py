def convert_case(text, case_type):

    if case_type == "upper":
        return text.upper()

    elif case_type == "lower":
        return text.lower()

    elif case_type == "title":
        return text.title()

    else:
        return "Error: Invalid case type"

# Test cases
text = "hello world from python"

print("Original Text:", text)
print("Upper Case :", convert_case(text, "upper"))
print("Lower Case :", convert_case(text, "lower"))
print("Title Case :", convert_case(text, "title"))
print("Invalid Case :", convert_case(text, "capital"))