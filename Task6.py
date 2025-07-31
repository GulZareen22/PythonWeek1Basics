# ----- GRADE CALCULATOR -----
marks = float(input("Enter your marks (out of 100): "))

if marks >= 90 and marks <= 100:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif 0<=marks<50:
    grade = "F"
else:
    grade = "Invalid input"

print(f"Your grade is: {grade}")

# ----- PASSWORD STRENGTH CLASSIFIER -----
password = input("Enter your password: ")

length = len(password)
lower = 0
upper = 0
digits = 0
special = 0

for char in password:
    if char.islower():
        lower += 1
    elif char.isupper():
        upper += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

if length >= 8 and lower > 0 and upper > 0 and digits > 0 and special > 0:
    strength = "Strong"
elif length >= 6 and lower > 0 and digits > 0:
    strength = "Moderate"
else:
    strength = "Weak"

print(f"Strength: {strength}")

