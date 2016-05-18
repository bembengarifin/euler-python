

def run():
    aggr = 0
    index = 3
    while index < 1000:
        if index % 3 == 0 or index % 5 == 0:
            aggr += index
        index += 1
    print aggr

print reduce(lambda x, y: x + y, (x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0))

run()
