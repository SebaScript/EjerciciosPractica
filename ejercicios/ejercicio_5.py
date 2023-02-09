def convert_fahrenheit_to_celsius(degrees_fahrenheit):
    return (degrees_fahrenheit - 32) * 5 / 9


degrees_fahrenheit = float(input("Please enter the number of degrees fahrenheit: "))
print(f"{degrees_fahrenheit} degrees fahrenheit = {convert_fahrenheit_to_celsius(degrees_fahrenheit)} degrees celsius.")
