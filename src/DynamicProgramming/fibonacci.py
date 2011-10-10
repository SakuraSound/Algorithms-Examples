'''
Created on Oct 9, 2011

@author: Hanabi

Memoization top-down of Fibonacci sequencing
'''



table = {0:0, 1:1, 2:1, 3:2, 4:3}

def fibonacci(position):
    if table.has_key(position):
        return table[position]
    else:
        ret = fibonacci(position - 1) + fibonacci(position - 2)
        table[position] = ret
        return ret
    

print fibonacci(5)
print table
print fibonacci(8)
print table
print fibonacci(12)
print table
print fibonacci(18)
print table
print fibonacci(27)
print table
print fibonacci(40)
print table