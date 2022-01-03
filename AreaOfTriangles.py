#Calculates the area of an triangle
a = input("Add the lenght for side 1: ")
a = float(a)

b = input("Add the lenght for side 2: ")
b = float(b)

c = input("Add the lenght for side 3: ")
c = float(c)

#Formula for finding the area with 3 sides
s = (a + b + c)/2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  #the ** and 0.5 make it square root

print("The area is %0.2f" %area) #the %0.2f only lets 2 points after the decimal print


