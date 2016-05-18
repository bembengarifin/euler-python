
import datetime

def run():
    """Just a runner"""
    max_triangle_number = 12799270
    max_divisor = 500
    index = 1
    while True:
        triangle_number = sum(xrange(1, index + 1))

        #divisor = get_divisor_brute_force(triangle_number)
        divisor = get_divisor_by_div(triangle_number)

        # do something with s
        #print triangle_number  
        #if triangle_number >= max_triangle_number:
        if divisor >= max_divisor:
            break
        index += 1
    print triangle_number


def get_divisor_brute_force(number):
    """This is to get the factorial"""
    lst = []
    
    for index in xrange(number, 0, -1):
        #print index
        if number % index == 0:
            lst.append(str(index))
    
    #print str(number) + ": " + ",".join(lst) + " (" + str(len(lst)) + ")"
    return len(lst)

def get_divisor_by_div(number):
    """This is to get the factorial"""
    lst = []
    
    #add 1 and self as always
    lst.append(str(1))
    lst.append(str(number))
    
    d = 2
    upper = number - 1
    while True:
        if d >= upper:
            break    
            
        if number % d == 0:
            lst.append(str(d))
            upper = number / d
            lst.append(str(upper))

        d += 1

    #print str(number) + ": " + ",".join(lst) + " (" + str(len(lst)) + ")"
    return len(lst)

print datetime.datetime.now()
run()
print datetime.datetime.now()
#print get_divisor_by_div(12799270)
#print get_divisor_brute_force(12799270)
