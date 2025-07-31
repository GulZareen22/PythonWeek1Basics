# ----- CLI UNIT CONVERTER -----
while True:
    print("\n----- UNIT CONVERTER MENU -----")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
   # ----- LENGTH -----
    if choice == "1":
        print("\n--- Length Converter ---")
        value = float(input("Enter length: "))
        unit = input("Is this in (m)eters or (km)? ").lower()

        if unit == "m":
            print(f"{value} meters = {value / 1000:.3f} kilometers")
        elif unit == "km":
            print(f"{value} kilometers = {value * 1000:.2f} meters")
        else:
            print("Invalid unit!")
 # ----- WEIGHT -----
    elif choice == "2":
        print("\n--- Weight Converter ---")
        value = float(input("Enter weight: "))
        unit = input("Is this in (kg) or (lb)? ").lower()

        if unit == "kg":
            print(f"{value} kg = {value * 2.20462:.2f} pounds")
        elif unit == "lb":
            print(f"{value} pounds = {value / 2.20462:.2f} kg")
        else:
            print("Invalid unit!")
 # ----- TEMPERATURE -----
    elif choice == "3":
        print("\n--- Temperature Converter ---")
        temp = float(input("Enter temperature: "))
        unit = input("Is this in (C), (F), or (K)? ").upper()

        if unit == "C":
            print(f"{temp}°C = {(temp * 9/5) + 32:.2f}°F")
            print(f"{temp}°C = {temp + 273.15:.2f} K")
        elif unit == "F":
            print(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
            print(f"{temp}°F = {((temp - 32) * 5/9) + 273.15:.2f} K")
        elif unit == "K":
            print(f"{temp} K = {temp - 273.15:.2f}°C")
            print(f"{temp} K = {((temp - 273.15) * 9/5) + 32:.2f}°F")
        else:
            print("Invalid unit!")
 # ----- EXIT -----
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option! Please choose between 1–4.")
