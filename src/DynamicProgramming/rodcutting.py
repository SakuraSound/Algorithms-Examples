'''
Created on Oct 8, 2011

@author: Hanabi
'''


prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 34, 37, 37, 40, 42, 42, 44, 50, 60, 60]

length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

table = {0:(0, [])}

def memoized_rod_cutting(price, length):
    if table.has_key(length):
        return table[length]
    q = (0, [])
    for i in xrange(1, length+1):
        newval = memoized_rod_cutting(price, length -i)
        q = q if q[0] >= (price[i] + newval[0]) else new_val(price[i], i, newval)
    table[length] = q
    return q

def new_val(price, i, value):
    newlist = value[1] + [i]
    return (price + value[0], newlist)

print 1, memoized_rod_cutting(prices, 1)
print table
print 3, memoized_rod_cutting(prices, 3)
print table
print 8, memoized_rod_cutting(prices, 8)
print table
print 16, memoized_rod_cutting(prices, 16)
print table
print 17, memoized_rod_cutting(prices, 17)
print 18, memoized_rod_cutting(prices, 18)
print 19, memoized_rod_cutting(prices, 19)
print 20, memoized_rod_cutting(prices, 20)