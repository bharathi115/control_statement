#swaping two numbers without temperary variables
a = 10
b=20
print(a)
print(b)
print("Before swap: a =", a, ", b =", b)

a, b = b, a

print("After swap: a =", a, ", b =", b)

#swaping two numbers using temperary variables
a= 40
b=2
print("Before swap: a =", a, ", b =", b)

temp = a
a = b
b = temp

print("After swap: a =", a, ", b =", b)

#Average find three Numbers
a=30
b=30
c=2
count=a+b+c
print("the number of count is:",count)
print(count/3)
print("the number of average is:",count/3)

#circle, Traingle, Square
#traingle

b=10
h=2
traingle=(1/2)*b*h
print("the area of traingle is:", traingle)


#square
number = 5
square = number ** 2
print("the area of square is:", square)

#circle
import math
radius=10
area=math.pi * (radius ** 2)
print("area of circle is:", area)

#Simple Interst 
p =100
t=2
r=5
si = (100 * 2 * 5) / 100
print("the Simple Interst is:", si )

#squre root of number
import math

a = 100
b = 20
num_sqrt1 = math.sqrt(a)
print("the number of square root is:", num_sqrt1)
num_sqrt2=math.sqrt(b)
print("the number of square root is:", num_sqrt2)

#last digit of a number

num= 7685781
last_digit = (num) % 10

print("the number oflast digit is:", last_digit)

#fahrenheit to centigrade    formula:  c=(f-32)*5/9

f = 80
c=(f-32)*5/9
print( "the centigrade value is :", c)


#centigrade to fahrenheit    formula : f=(c*9/5)+32
c = 26.66
f=(c*9/5)+32
print("the fahrenheit value is :", f)
