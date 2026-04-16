#List an Tuple

# sum of all list
num = [5, 10, 15]
total = 0

for i in num:
    total += i

print(f"{total}")

#get the largest number form a list
num = [5, 10, 15, 34, 56, 76]
largest_num=max(num)
print(largest_num)

#get the smallest number form a list
num = [5, 10, 15, 34, 56, 76]
smallest_num=min(num)
print(smallest_num)

#remove Duplicates from  list

l = [54, 67, 89, 76.98, 90, "Bye"]
ans = [ ]
for i in l:
    if i not in ans:
        ans.append
    print(ans)

#clone or copy alist in ython
a = [10, 20, 30, 40, 50]
b = a.copy()
a = b.copy()
print(b)
print(a)

#REverse alist in python

a = [10, 20, 30, 40, 50]
a.reverse()
print(a)

#Random items in a list
import random
n = 5  
li = random.sample(range(1, 101), n)

print(li)


#remove empty element form  list
a = [10,"Bharathi", "Dhanusha", 234, [ ], ["hello",True], [ ], 44.87]
res = [b for b in a if b]
print(res)

#appending value

a =["Bharathi"]
print(a)
a.append("John")
print(a)
a.insert(3,"johny")
print(a)

b = [34 ,45.67 , "Bye"]
a.extend(b)
print(a)


#random datatypes in a list
import random
list = [10, "Hello", 3.14, True, [1, 2], {"key": "value"}]
random_item = random.choice(list)
random_type = type(random_item)
print(f"Item: {random_item}")
print(f"datatype : {random_type}")


#odd and even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
evens, odds = [ ], [ ]
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

#sorting a number in ascending order

list = [78.32, 89, 67, 90, 45, 67]
print(list)
list.sort()
print(list)


#TUPLE
#revrse the given tuple
t = (1, 2, 3, 4, 5) 
rev = t[::-1]

print(rev)

#Access value 20 form the tuple
t = (11, 20, 37, 40, 50)
print(t)
print(t[1])

#one tuple to another tuple
t = (10, 20, 30, 40, 50)
print(t)
new_tuple = (t[1], t[3])
print(new_tuple)
new_tuple = t[1:4]
print(new_tuple)
new_tuple = t[::2]
print(new_tuple)

#create  tuple single in 50
tuple = (50)
print(tuple)

#Swapping two tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1, t2 = t2, t1

print("t1:", t1)
print("t2:", t2)

#Unpack the tuple into foru variables
# four variales are storred in a,b,c,d
t = (10, 20, 30, 40)
a, b, c, d = t
print(a)
print(b)
print(c)
print(d)




