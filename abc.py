#Program to print area of circle
radius = float(input("Enter the radius:"))
area = 3.14 * radius * radius
print(area)

#Print file extension from file name
a=str(input("Input the Filename:"))
if(".py" in a):
    print("The extension of the file is: 'Python'")
else:
    print("Code will be extended")
