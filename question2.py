# Write a Python program that asks the user for a number and then prints whether the number is odd or even

number = int(input("Enter a number: "))
#checking if the numer is odd or even

if number % 2 == 0:
  print(f"{number} is even.")
else:
  print(f"{number} is odd.")