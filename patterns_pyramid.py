#Patterns of pyramid

#1.Half Pyramid of number
n = 6
for i in range(n):
    for j in range(i + 1):
        print(j, end="  ")
    print()
#inverted half Pyramid of number
n = 6
for i in range(n):
    for j in range(n - i):
        print(j, end="  ")
    print()

    #Half Pyramid  of *
n = 6
for i in range(n):
    for j in range(i + 1):
        print(" * ", end="  ")
    print()
#inverted half Pyramid of *
n = 6
for i in range(n):
    for j in range(n - i):
        print(" * ", end="  ")
    print()


#full pyramid of numbers
    n = 6
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    
    for j in range(i + 1):
        print(" n ", end=" ")
    
    print()

    
# full pyramid of *
n = 6
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i + 1):
        print(" * ", end=" ") 
    print()

#inverted ful pyramid of *
n = 8
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range( i - 1):
        print(" * ", end=" ")
    for j in range( i - 1):
        print("  ", end=" ")
    print()




#inverted full pyramid of numbers
n = 8
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range( i + 1):
        print(j, end=" ")
    for j in range(i - 1):
        print(j, end=" ")
    
    print()

# using *in  square pyramid
n = 8
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


#hollow pyramid in number
n=6
for i in range(n,0,-1):
    for j in range(i):
        if i==n or j==0 or j==i-1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()


#hollow pyramid in *
n=6
for i in range(n,0,-1):
    for j in range(i):
        if i==n or j==0 or j==i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
