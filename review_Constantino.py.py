PI = 3.1416
#
# Function for Computing Surface Area
def Surface_Area():
    while True:
        print("Computing for Surface Area")
        r = float(input("Input Minor Radius:"))
        R = float(input("Input Major Radius:"))
        if r > R :
            print("Minor radius is Greater than the Major radius. Try Again.")
        elif r == 0 or R == 0:
            print("Minor and Major Radius cannot be Zero(0). Try Again.")
        else:
            Suf_area = (2 * PI * R) * (2 * PI * r )
            print("The Surface Area of the Torus:", Suf_area)
            break

# Function block for computing Volume
def Volume():
    while True:
        print("Computing for Volume")
        r = float(input("Input Minor Radius:"))
        R = float(input("Input Major Radius:"))
        if r > R:
            print("Minor radius is Greater than the Major radius. Try Again.")
        elif r == 0 or R == 0:
            print("Minor and Major Radii cannot be Zero(0). Try Again.")
        else:
            Volum = (2 * PI * R) * (PI * r **2)
            print("The Volume of the Torus:", Volum)
            break

# Function Block for choosing what to compute
def Computing():
    while True:
        ComputeWhat = input("What do you want to Compute?:  \n1.Surface \n2.Volume \nType 1 or 2:")
        if ComputeWhat == "1" :
                Surface_Area()
                break
        elif ComputeWhat == "2":
            Volume()
            break
        else:
            print("Choose between 1 0r 2")


print("Torus Calculator ")
Computing()

# For calling what to Compute & Computing again
while True:

    ComputeAnother = input("Do you want to compute Another set? \n1.Yes \n2.No \nType y or n:")
    if ComputeAnother == "y":
        Computing()
    elif ComputeAnother == "n":
        break
    else:
        print("Choose between 1 0r 2")



