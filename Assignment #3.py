import math



# create input code for the number of polygon points
n = int(input("Please enter the number of polygon (greater than 3) points): "))




#the points Coordinates are
x = []
y = []

print("Please enter both x and y coordinates for polygon points: ")
for r in range(n):
    xcoord = float(input("Please enter the X Coordinate for the point " + str(r + 1) + ": "))
    x.append(xcoord)
    ycoord = float(input("Please enter the Y Coordinate for the point " + str(r + 1) + ": "))
    y.append(ycoord)
print(" ")




#To print the coordinates into a Table
print("The Coordinates Table")
print(f"{'Point':>3} {'X':>8} {'Y':>10}")
print("-" *35)
for r in range(n):
    print(f"{r+1:>3} {x[r]:>12} {y[r]:>10}")
print(" ")





#Using the formular to calculate the cross sectional area
TAx = []
for r in range(n):
    Ax = (x[r]+x[r-1])*(y[r]-y[r-1])
    TAx.append(Ax)
SumAx = 0.5*sum(TAx)

#Using the formular to calculate the static cross sectional moments 
TSx =[]
for r in range(n):
    Sx = (x[r]-x[r-1])*((y[r]**2)+(y[r-1]*y[r])+(y[r-1]**2))
    TSx.append(Sx)
TSumx = (-1/6)*sum(TSx)
TSy =[]
for r in range(n):
    Sy = (y[r]-y[r-1])*((x[r]**2)+(x[r]*x[r-1])+(x[r-1]**2))
    TSy.append(Sy)
TSumy = (1/6)*sum(TSy)
#Using the formular to calculate the axial moments of interia of the transmission
INx =[]
for r in range(n):
    Ix = (x[r]-x[r-1])*((y[r]**3)+((y[r]**2)*y[r-1])+(y[r]*(y[r-1]**2))+(y[r-1]**3))
    INx.append(Ix)
INx1 = (-1/12)*sum(INx)
INy =[]
for r in range(n):
    Iy = (y[r]-y[r-1])*((x[r]**3)+((x[r]**2)*x[r-1])+(x[r]*(x[r-1]**2)+(x[r-1]**3)))
    INy.append(Iy)
INy1 = ((1/12)*sum(INy))

INxy = []
for r in range(n):
    INxy1 = (y[r]-y[r-1])*(y[r]*((3*(x[r]**2))+(2*x[r]*x[r-1])+(x[r-1]**2))+(y[r-1]*((3*x[r-1]**2)+(2*x[r]*x[r-1])+(x[r]**2))))
    INxy.append(INxy1)
    INxyT = (-1/24)*sum(INxy)

# Using the formular to calculate the coordinates of the cross section centroid
xt = TSumy/SumAx
yt = TSumx/SumAx

#Using the formular to calculate the moments of interia with respect to the axes in parallel of points gravity
Txt = INx1 - ((yt**2)*SumAx)
Tyt = INxy1 -((xt**2)*SumAx)
Txyt = INxyT + (xt*yt*SumAx)


print("Geometric characteristics: ")
print("Ax  is:", TSumx)
print("Sx  is:", round(TSumx, 2))
print("Sy  is:", round(TSumy, 2))
print("Ix  is:", round(INx1, 2))
print("Iy  is:", round(INy1, 2))
if TIxy >=0: print("Ixy is:  ", round(INxyT, 2))
else: print("Ixy is: ", round(INxyT, 2))
print("xt  is:", round(xt, 2))
print("yt  is:", round(yt, 2))
print("Ixt is:", round(Txt, 2))
print("Iyt is:", round(Tyt, 2))
if Txyt >=0: print("Ixyt is: ", round(Txyt, 2))
else: print("Ixyt: ", round(Txyt, 2))


#End of Program - Assignment #3 - Olaoluwa Osundare