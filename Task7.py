# ----- MULTIPLICATION TABLE -----
number = int(input("Enter a number to generate its multiplication table: "))

print(f"\nMultiplication Table of {number}:\n")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


    # ----- SUM OF NUMBERS DIVISIBLE BY 3-----
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
total = 0
ending_no=end-1

for i in range(start, end + 1):
    if i % 3 == 0:
        total += i

print(f"Sum of numbers divisible by 3 from {start} to {ending_no} is: {total}")





