

def run():
    aggr = 0
    first, second = 0, 1
    while first < 4000000:
        # print a
        if first % 2:
            aggr = aggr + first
        temp = first
        first = first + second
        second = temp
    print aggr

run()
