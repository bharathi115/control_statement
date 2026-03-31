#Bitwise Operators

a=64
b=88
print(a&b)
print(a|b)
print(a^b)
print(~4)
print(~-4)




a=98
b=63
# 98 and 63
print(a&b)
print(a|b)
print(a^b)
print(~6)
print(~-6)


a=145
b=168
# 145 and 168
print(a&b)
print(a|b)
print(a^b)
print(~8)
print(~-8)

        
         128   64   32   16   8   4   2   1  
          0     1    1    0   0   0   1   0  ->98
          0     0    1    1   1   1   1   1  ->63
98|63
(a|b)     0     1    1    1   1   1   1   1   -> 127
(a&b)     0     0    1    0   0   0   1   0   -> 34
(a^b)     0     1    0    1   1   1   0   1   -> 93


         128   64   32   16   8   4   2   1
          1     0    0    1   0   0   0   1   ->145
          1     0    1    0   1   0   0   0   ->168
          
145|168   1     0    1    1   1   0   0   1   ->185
(a|b)
(a&b)     1     0    0    0   0   0   0   0   ->128
(a^b)     0     0    1    1   1   0   0   1   ->57
