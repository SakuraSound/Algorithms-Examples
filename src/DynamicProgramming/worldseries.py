'''
Created on Oct 10, 2011

@author: Hanabi
'''

table = {(1, 0): 0, (0, 1): 1}


def right(a, b, p, q):
    r = (a, max(b-1, 0))
    print r
    if table.has_key(r):
        print "Found table entry"
        return table[r]
    else:  
        if r[1] == 0:
            table[r] = right(a-1, 0, p, q)
        else:
            table[r] = worldseries(a, r[1], p, q)
        return table[r]

def worldseries(a, b, p, q):
    left = (max(a - 1, 0), b)
    print left, a, b
    if table.has_key(left):
        print "Found table entry"
        Pp = table[left]
    else:
        if left[0] == 0:
            table[left] = right(a, b, p, q)
            return table[left]
        else:
            Pp = worldseries(left[0], b, p, q)   
    Pq = right(a, b, p, q)
    ret = (p * Pp) + (q * Pq)
    table[(a, b)] = ret
    return ret

print table
print worldseries(6, 6, .3, .7)
print table