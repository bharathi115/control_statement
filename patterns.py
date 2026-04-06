#PREPARATION
#1.

n = 4

for i in range(n):          
    for j in range(n):     
        print("*", end=" ")
    print()
print("------------------------------------------------")    
#2.
n = 4
for i in range(n):
    for j in range(n):
        if i == 0 or i == 3 or j == 0 or j ==3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("------------------------------------------------")

#3.
n=6
for i in range(n): # i=1 nextly i++
    for j in range(i+1):
        print("*", end=" ")
    print()
print("------------------------------------------------")
#4.
n=6
for i in range(n):#n-i =6-1
    for j in range(n-i):
        print("*", end=" ")
    print()
print("------------------------------------------------")

#5.
n = 4

for i in range(n):    
    for j in range(n):
        if j < n - i - 1:#4-0-1=3 =0<3=true so space goes continue check 0-4-1=3
                         #3<3 = false comes print else part *
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
print("------------------------------------------------")
#6.
n = 4

for i in range(n):    
    for j in range(n):
        if j < i:#0<0
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
print("------------------------------------------------")
#7.
n = 6
 
for i in range(n):    
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
print("------------------------------------------------")
#8.
n = 6
for i in range(n):
    for j in range(n):
        if j ==n-i-1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    
    print()

print("------------------------------------------------")
#9.
n = 6

for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    
    for j in range(i):
        print("*", end=" ")
        
    print()


print("------------------------------------------------")

#10
n = 8
for i in range(n):
    for j in range(n):
        if i == 0 or j ==0 or i == 7 or j == 7:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("------------------------------------------------")

    
