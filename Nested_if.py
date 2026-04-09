'''
#nested_if Statement
#1.
email = input("Enter Email Id :")
if email == "abc@gmail.com":
    pas = int(input("Enter Password :"))
    if pas == 1234:
        print("Login Sucess!")
    else:
        print("Worng Password")
else:
    print("Invaild Email Id")

#2.

email = input("Enter Email Id :")
if email == "bharathi@gmail.com":
    pas = int(input("Enter Password :"))
    if pas == 123456:
        print("Login successfully")
    else:
        print("Wrong Password")
else:
    print("Invalid Email Id")

'''
#str(len) only prints start 1 2 3 4
#normal format start with 012345
#reversed strings are start to last 0 -1 -2 -3
#Strings
'''
a = "Hello,world"
b = "I am Bharathi"

print(a.index("World"))
print(a[0])
print(a[6])
print(a[8])
print(a.upper())
print(a.lower())
print(len(a))
print("He is called 'Balu'")
print('He is called "Balu"')
print(b[:5])
print(b[5:])
print(b[2:5])
print(a[3:])'
print(a[7:])
print(b[-5:-2]) #this prints reverse pattern
print(a[3:5])
print(a.replace("H", "J"))
print(a.strip())
print(a.title())
c = a.split(",")
print(c)
'''
txt ="Hello, welcome to my  world."
d = txt.index("world")
print(d)
txt.lower().index("world")



