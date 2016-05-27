import datetime


def generate_primes(number):
    index = 2
    upper = number - 1
    largest_prime = index
    while True:
        if index >= upper:
            break
        if number % index == 0:
            upper = number / index
            if is_prime(upper) and upper > largest_prime:
                #print "Set upper"
                largest_prime = upper
            if is_prime(index) and index > largest_prime:
                #print "Set index"
                largest_prime = index
        index += 1

    print largest_prime


def is_prime(number):
    index = 2
    while index < number:
        if number % index == 0:
            return False
        index += 1
    return True

#print is_prime(10)
#print is_prime(600851475143)

start_time = datetime.datetime.now()
generate_primes(600851475143)
end_time = datetime.datetime.now()

duration = end_time - start_time
print duration
