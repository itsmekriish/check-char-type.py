print("📈 Character Type Checker 📈")
char = input("Enter a single character: ")

if char.isalpha():
    print("This is a letter")
elif char.isdigit():
    print("This is a number")
else:
    print("This is a Special Character!")
