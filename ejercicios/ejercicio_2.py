def calculate_circle_area(radius):
    return float((radius ** 2) * 3.1416)


radius = float(input("Enter the circle radius(in meters): "))
if radius >= 0:
    print(f"The area of the circle is: {calculate_circle_area(radius)} meters.")
else:
    print("The radius of the circle can't be less than 0")
