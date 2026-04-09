#1.
s = "madam"
print(s == s[::-1])  #s[::-1] ->reverse string =madam-> madam

#2. Vowels
s = "education"
vowels = "aeiouAEIOU"
count = 0

for char in s:
    if char in vowels:
        count += 1
print(count)

#3.Reverse a string without using built-in functions

n = "Bharathi "
print(n[::-1])
print(n[::1])

#4
s = "Hello World"
upper = 0
lower = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

#5.
s = "programming"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

#6.frequent charecter in  string

print("banana".count('a'))

#7.  Anagrams

s1 = "listen"
s2 = "silent"
print(sorted(s1) == sorted(s2))


#8.
s = "I am bharathi and I am a software developer"
print(len(s))#number of letters
print(len(s.split()))#number of words

#9.
s = "abc123"
print(s.isdigit())

s = "abc123"
total = 0

for ch in s:
    if '0' <= ch <= '9':
        total += int(ch)

print(total)

# 10.

s = "hello world"
print(s.replace(" ", "-"))

#11.

s ="welcome to python"
print(s.title())

#12.
s = "abcdef"
print(s[1::2])

#13.
s = "hello world"
prefix = "hello"
suffix = "world"
print(s[:len(prefix)] == prefix)
print(s[-len(suffix):] == suffix)


'''
#HCF of given two numbers

def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example
num1 = 48
num2 = 18
print("HCF is:", hcf(num1, num2))

#Hcf second format
num1 = int(input("Enter the first  number: "))
num2 = int(input("Enter the second number: "))

print("HCF is:", hcf(num1, num2))


#HCF third format

num1 = 48
num2 = 18
print("HCF is:", hcf(num1, num2))
'''
