# Write a Python program that asks the user for their age and tells them whether they are a minor (under 18), an adult (18-65), or a senior (over 65)
# Ask for their age
age = int(input("Please enter your age: "))
# Checking the age category
if age < 18:
    category = "Minor"
elif 18 <= age <= 65:
    category = "Adult"
else:
    category = "Senior"
# Printing the age category
print("You are categorized as:", category)
