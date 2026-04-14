#Remove duplicates
s = "Hello World"
c = ""
for i in s[::-1]:
    if i not in c:
        c += i
print(c)

#count the vowels in string
n = "Bharathi"
c = 0
v = "aeiouAEIOU"
for i in n:
    for i in v:
        c+=1
print("count of vowels:", c)
    
#string functions
s1 = "Hello World I am Bharathi"
print(s1.find('e'))
print(s1.find('l'))
print(s1.rfind('B'))
print(s1.rfind('t'))
print(s1.find('e'))
print(s1.replace('H','h'))
print(s1)
s2 = s1.replace('H', 'h')
s2 = s1.replace('B', 'b')
print(s2)
print("HEllo world".endswith("d"))#true
print("HEllo world".endswith("l"))#false
print("HEllo world".startswith("HE")) #true
print("Hello{}, I am {}".format("Annapoorani", "Bharathi"))
 #1.
c = "Hello {},  I am {}"
print(c.format("Annapoorani", "Bharathi"))
print(c)

#2.
a, b ="Annapoorani", "Bharathi"
print(f"Name :{a}")
print("                  Bharathi                                        ")
print("                       Bharathi                                 ".strip())
print("Kumar S".split())
print("hello i am Bharathi, Full Stack developer in HCL".split())
n = "hello i am Bharathi, Full Stack developer in HCL"
print(n.split(','))
n1 = n.split()
print(n1)
j = ' '.join(n1)
print(j)


#Encode nd DEcode

n= "hello I am Bharathi Full Stack Developer in HCL"
print(n)
e = n.encode('UTF-32')
print(e)
d = e.decode('UTF-32')
print(d)

#Escape Sequence -> /n -> new line /t new tab

print("Hello /ni am Bharathi /nI am Worked at Chennai /tand full stack developer in HCL")
print("Bharathi is a Python Deveoper in /n2026".splitlines())


#Build in functions
print("Bharathi".islower())
print("Bharathi".isupper())
print("Bharathi".istitle())
print("Bharathi".isalpha())
print("Bharathi1".isalpha())
print("123456".isdigit())
print("43562Bharathi".isalnum())
print("ab".isidentifier())
print("Hello #$%^&&*!#$, ghtyurndghe        yturh".isascii())
print("Hello #$%^&&*!#$, ghtyurndghe        வணக்கம்yturh".isascii())


#remove h in specifc string
s = "Bharathi"
v = ' '
for i in s:
    if i not in 'h':
        v+=i
print(v)
#remove h in specifc string
s = "praveen"
v = ' '
for i in s:
    if i not in 'e':
        v+=i
print(v)

#To get the specific value in string -e
s = "Praveen"
v = " "
for i in s:
    if i == 'e':
        v += i
        break
print(v)

      
