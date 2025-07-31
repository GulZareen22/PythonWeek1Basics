#------Task3 partA-----
A=float(input("Enter first number: "))
B=float(input("Enter second number: "))
C=float(input("Enter third number: "))
D=(A+B+C)/3
print(f"The average of {A} , {B} and {C} is {D:.3f}")

#------Task3 partB-----
Minutes=int(input("Enter the total minutes: "))
Hours=Minutes/60
Minutes_Remaining=Minutes%60
print(f"{Minutes} minutes can be written as {Hours:.0f} hours and {Minutes_Remaining} minutes")