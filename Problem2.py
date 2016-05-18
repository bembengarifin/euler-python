sum = 0

#a, b = 0, 1
#while a < 4000000:
#    print a
#    sum += a
#    c = a + b
#    a = b + c
#    b = c + a

a, b = 0, 1
while a < 4000000:
    print a
    c = a 
    a += b 
    b = c 

print sum
    