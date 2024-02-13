Side1 = float(input("Enter First Side: "))
Side2 = float(input("Enter Second Side: "))
Side3 = float(input("Enter Third Side: "))

if Side1 == Side2 and Side2 == Side3:
    print("This is an equilateral triangle")

elif Side1 == Side2 or Side2 == Side3 or Side1 == Side3:
    print("This is a isoceles triangle")

else:
    print("This is a scalene triangle")
