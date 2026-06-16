def is_palindrome(text):

    cleaned_text = text.replace(" ", "").lower()

    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False


# Test cases
text1 = "Madam"
text2 = "Race Car"
text3 = "Hello"

print(text1, "->", is_palindrome(text1))
print(text2, "->", is_palindrome(text2))
print(text3, "->", is_palindrome(text3))