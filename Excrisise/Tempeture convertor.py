
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
Temperature = float(input("Enter temperature: "))
if unit == "C":
    Temperature_Fahrenheit = (Temperature * 9/5) + 32
    print(f"The temperature in fahrenheit is: {round(Temperature_Fahrenheit,1)}°F")
elif unit == "F":
    Temperature_Celsius = (Temperature - 32) * 5/9
    print(f"The temperature in Celsius is: {round(Temperature_Celsius,1)}°C")
else:
    print(f"{unit} is invalid, Please enter a valid temperature scale C or F")