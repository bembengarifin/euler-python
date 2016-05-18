#print reduce ( lambda x, y : x + y, [x for x in range(100000000) if x % 3 == 0 or x % 5 == 0])

#sum = 0
#for x in xrange(3, 1000000000):
#    if x % 3 == 0 or x % 5 == 0:
#        sum += x
#print sum


sum = 0
index = 3
while index < 1000000000:
    if index % 3 == 0 or index % 5 == 0:
        sum += index
    index += 1
print sum
#
#print index


#print reduce ( lambda x, y : x + y, (x for x in xrange(1000000000) if x % 3 == 0 or x % 5 == 0))