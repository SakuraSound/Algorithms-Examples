'''
Created on Oct 9, 2011

@author: Hanabi

memoization of binomial coefficients
'''

table = {(0,0): 1, (1, 1): 1, (1, 0): 1 }

def binomialcoeff(n, k):
    if k == n or k == 0:
        return 1
    key = (n, k)
    if table.has_key(key):
        return table[key]
    else:
        ret = binomialcoeff(n-1, k-1) + binomialcoeff(n-1, k)
        table[key] = ret
        return ret
    

for i in xrange(12):
    print i, " ",  
    for j in xrange(i+1):
        print binomialcoeff(i, j), " ", 
    print


    
