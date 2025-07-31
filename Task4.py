#-----BMI CALCULATOR------
Height=float(input("Enter your height in meters: "))
Weight=int(input("Enter your weight in kilograms: "))

BMI=Weight/Height**2

if BMI<18.5:
    print("You are underweight")
elif 24.9<BMI<29.9:
    print("You are overweight")
elif 18.5<BMI<24.9:
    print("You are normal weight")
else:
    print("You are obese")

#-----SIMPLE INTEREST CALCULATOR----
Principal=int(input("Enter the initial amount(in Rs): "))
Rate=float(input("Enter the interest rate: "))
Time=int(input("Enter the time period(in years): "))
Simple_Interest=(Principal*Rate*Time)/100
Total_amount=Principal+Simple_Interest
print(f"Simple Interest earned after {Time} years with rate of {Rate} percent on amount of Rs{Principal} is: Rs{Simple_Interest:.2f}")
print(f"Total amount after {Time} years is: Rs{Total_amount:.2f}")
