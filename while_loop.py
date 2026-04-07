1.#Palindrome or not

a = int(input("Enter the Value:"))
b = 0
t = a

while t > 0:
    d = t % 10
    b = b * 10 + d
    t = t // 10
    
    if b == a:
        print(b,"is panlindrome")
    else:
       print(b,"is not a Palindrome")


#Armstrong number

a = int(input("Enter the Value:"))
b = 0
t = a

while t > 0:
    d = t % 10
    b += d ** 3
    t = t // 10
    
    if b == a:
        print(b,"is Armstrong Number")
    else:
       print(b,"is not a Armstrong Number")

#prime or not
a = int(input("Enter the number: "))

if a <= 1:
    print(a, "is not a Prime Number")
    
else:
    for i in range(2, a):
        if a % i == 0:
            print(a, "is not a Prime Number")
            break
    else:
        print(a, "is a Prime Number")

#Prime numbers
n = 0

for a in range(1, 100):
    if a > 1:
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                break
        else:
            print(a, end=" ")
            n += 1

print("Total prime numbers:", n)

#SPY number

a = int(input("Enter the Value: "))
b = 0
p = 1
t = a

while t > 0:
    d = t % 10
    b += d
    p *= d
    t = t // 10

if b == p:
    print(a, "is a Spy Number")
else:
    print(a, "is not a Spy Number")

#Hashard Number

a = int(input("Enter the number: "))
t = a
b = 0

while t > 0:
    d = t % 10
    b += d
    t = t // 10

if a % b == 0:
    print(a, "is a Harshad Number")
else:
    print(a, "is not a Harshad Number")

#number of digits

a = int(input("Enter a number: "))
t = a
total= 0

while t > 0:
    t = t // 10
    total += 1

print("Number of digits:", total)

#square of split

a = int(input("Enter a number: "))
t = a

print("Squares of digits:", end=" ")

while t > 0:
    d= t % 10
    print(d ** 2, end=" ")
    t = t // 10
#sum of  n odd  and numbers
    n = int(input("Enter Value: "))

# Sum of first n odd numbers
i = 1
total = 0
odd = 0

while total < n:
    odd += i
    i += 2
    total += 1

print("Sum of first odd numbers:", odd)

# Sum of first n even numbers
i = 2
total = 0
even = 0

while total < n:
    even += i
    i += 2
    total += 1

print("Sum of first even numbers:", even)


#factorial number

n= int(input("Enter value:"))
fact = 1
for i in range(1,n+1):
    fact*=i
    print("Factorial Value: " fact)
