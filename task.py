'''
# Sum of n odd and even numbers
n = int(input("Enter a number: "))

sum_even = 0
sum_odd = 0

for i in range(1, n + 1):
    if i % 2 == 0: #remainder value
        sum_even += i
    else:
        sum_odd += i

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)


#Square of the number

n = int(input("Enter a number: "))

for i in range(1, n + 1):  
    print("Square of", i, "is", i * i) #1=1,2=4,3=9, 4=16,5=25

#Positive divisors of intger

n = int(input("Enter a number: "))

print("Positive divisors are:")
for i in range(1, n + 1): #remainder value
    if n % i == 0:
        print(i)


# Print the Prime numbers of 0 to 100
n = 0

for a in range(1, 100):
    if a > 1:
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0: #remainder
                break
        else:
            print(a, end=" ")
            n += 1

print("Total prime numbers:", n)
'''
#HCF of given two numbers

def hcf(a, b):
    while b != 0:
        a, b = b, a % b   # a=18-> b=12-> a%b=18%12=6
    return a

num1 = int(input("Enter the first  number: "))
num2 = int(input("Enter the second number: "))

print("HCF is:", hcf(num1, num2))

#

for i in range(1, 51):
    if(i % 3 == 0 and i % 5 == 0):
        print("hihello")
    elif(i % 3 == 0):
        print("hi")
    elif(i % 5 == 0):
        print("hello")
    else:
        print(i)
