'''
#1.
# Cube of number
def cube(b):
    print(b * b * b)
cube(4)#64
cube(10) #100
cube (6) #216
cube(5) #125


#2.
# Square of number
def square(a):
    print(a * a)
square(5)#5*5 =25
square(10)#100
square (2) #4
square(12)#144


#3.
#series1()
#for i in range(start, stop, inc/dec)

def series1():
    for i in range(2, 17, 2):
        print(i, end=",")
series1()


#4. 
#Series2()
def series2():
    series = ["10, 50, 40, 20, 30, 0"]
    for i in reversed(series):
         print(i)
series2()

#5.
#split_numbers

def split_num():
    number = "4,3,2,7"
    digits = number.split(",")
    for i in reversed (digits):
        print(i)
       
    split_num()


#Armstrong Number

def armstrong_num():
    a = int(input("Enter the Number: "))
    b = 0
    t = a

    power = len(str(a))  

    while t > 0:
        d = t % 10
        b += d ** power
        t = t // 10

    if b == a:
        print(b, "is an Armstrong number")
    else:
        print(b, "is not an Armstrong number")
armstrong_num()

#spy number
def spy_num():
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
spy_num()

#number 0f digits

def count_digits():
    a = int(input("Enter a number: "))
    t = a
    total = 0

    while t > 0:
        t = t // 10
        total += 1

    print("Number of digits:", total)


count_digits()

#square of digits

def Square_of_digits():
    a = int(input("Enter a number: "))
    t = a

    print("Squares of digits:", end=" ")

    while t > 0:
        d = t % 10
        print(d ** 2, end=" ")
        t = t // 10


Square_of_digits()


#PRINT INT AND FLOAT VALUE
def addition():
    a = 10
    b = 34.90
    c = a+b
    print(c)
addition()

def input_price():
    price = float(input("Enter laptop price: "))
    return price


def calculate_charge(price):
    if price >= 50000:
        discount = price * 0.10
    elif price >= 30000:
        discount = price * 0.05
    else:
        discount = price * 0.02

    final_price = price - discount

    print("Original Price:", price)
    print("Discount:", discount)
    print("Final Price:", final_price)


# Main execution
price = input_price()
calculate_charge(price)

#capital letter
def is_capital(ch):
    
    if 'A' <= ch <= 'Z':
        return True
    else:
        return False
print(is_capital('A'))
print(is_capital('m'))

def to_small_letter(ch):
    
    if 'a' <= ch <= 'z':
        return True
    else:
        return False
print(to_small_letter('f'))
print(to_small_letter('s'))
print(to_small_letter('A'))
'''
 #vowel or consonant
def is_vowel(ch):
    ch = ch.lower()

    if ch in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"

print(is_vowel('A'))
print(is_vowel('a'))
print(is_vowel('i'))



