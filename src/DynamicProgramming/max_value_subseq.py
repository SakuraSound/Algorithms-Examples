'''
Created on Nov 12, 2011

@author: Haruka
'''
'''
Created on Nov 10, 2011

@author: Hanabi
HANABI and SAKURASOUND are code names for Joir-dan Gumbs
'''

array = (1, 4, -3, 4, 9, 15, 14, -12, 5)


table = {(i,i):array[i] for i in xrange(len(array))}

def max_value(pos, start):
    if table.has_key((pos, start)):
        return table[(pos, start)]
    else:    
        maximum = max([max_value(pos-1, i) + array[pos] for i in range(pos) if i >= start])
        table[(pos, start)] = max(maximum, array[pos])
        return table[(pos, start)]  
            
        
print sum(array)
print max_value(len(array)-1, 0)
print max(table.items(), key=lambda x: x[1])
for key, val in sorted(table.items(), key=lambda (x,y): -y):
    print key, val
