PI = 3.14
r = float(input("The radius of the circle : "))
Area = PI*r*r
print("Area of a circle = %.2f" %Area)

Filename = input("Input the Filename :")
f_extns = Filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))
