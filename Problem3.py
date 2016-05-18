primes = []


def generatePrimes():

    #    numbers = ((x, False) for x in xrange(2, 10));
    #        if x[0] == 2:
    #            x[1] = True
    #        print x

    numbers = xrange(1, 10)

    for idx, val in enumerate(numbers):
        print idx

print generatePrimes()
