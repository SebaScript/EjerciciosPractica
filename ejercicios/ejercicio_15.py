def determine_palindrome(text):
    text = str(text).lower().replace(' ', '')
    return text == text[::-1]


text = str(input("Please enter the string: "))
answer = determine_palindrome(text)

if answer:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome :(")
