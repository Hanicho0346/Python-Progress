
# question 5:temprature converter

def temperature_converter(temp, unit):
    unit = unit.lower()
    if unit =="c":
        return  round((temp * 9/5) + 32,2)
    elif unit == "f":
        return round((temp - 32) * 5/9,2)
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."

temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C or F): ")

converted_temp = temperature_converter(temp, unit)
print(f"The converted temperature is: {converted_temp}")
