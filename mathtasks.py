#ex1
import math
degree = float(input("Input degree: "))
rad = degree * math.pi / 180
print("Output radiant:", rad)

#ex2
import math
height = float(input("Height: "))
firstVal = float(input("Base, first value: "))
secondVal = float(input("Base, second value: "))
area = ((firstVal + secondVal)/2) * height
print("Area: ", area)

#ex3 
import math
n = int(input("number of the sides: "))
l = float(input("length of the side: "))
a = l / 2 * (math.tan(math.pi /n))
area = (n * l * a) / 2
print("Area: ", area)

#ex4 
import math
l = float(input("length of base: "))
h = float(input("height of parrallelogram: "))
area = l * h
print("Area: ", area)