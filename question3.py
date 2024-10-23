#Write a program that takes a score (0-100) as input and categorizes it into grades
# Ask for a score
score = int(input("Enter your score (0-100): "))

# Check the score and assign a grade
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = 'Invalid score! Please enter a score between 0 and 100.'
# Print the grade
print("Your grade:", grade)
