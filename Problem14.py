'''
n = n/2 (n is even)
n = 3n + 1 (n is odd)
'''

import datetime


def generate(sequence):
    counter = 0
    while sequence != 1:
        # print c
        # print s
        if sequence % 2 == 1:
            sequence = sequence * 3 + 1
        else:
            sequence = sequence / 2
        counter += 1
    return counter

def run(start_sequence):
    largest = 0
    largest_sequence = start_sequence
    while start_sequence > 0:
        current = generate(start_sequence)
        if current > largest:
            largest = current
            largest_sequence = start_sequence
        start_sequence -= 1
    return (largest, largest_sequence)

#print generate(1000000)
#print generate(9000000)
#print generate(13)

start_time = datetime.datetime.now()
print run(1000000)

end_time = datetime.datetime.now()

duration = end_time - start_time
print duration
