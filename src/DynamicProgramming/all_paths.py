'''
Created on Nov 11, 2011

@author: Hanabi
'''

weights = [[0, 1, 1, 0, 0, 0],
           [0, 0, 1, 1, 1, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0]]


def make_matrix():
    x = [[[0 for i in xrange(len(weights))] for j in xrange(len(weights))] for k in xrange(len(weights))]
    return x



def floyd_warshall():
    for k in xrange(1, len(steps)):
        print  k
        for i in xrange(0, len(steps[0]) ):
            for j in xrange(0, len(steps[0]) ):
                steps[k][i][j] =  steps[k-1][i][j] +  (steps[k-1][i][k-1] and steps[k-1][k-1][j] )
                
    
    
steps = [weights] + make_matrix() 
print steps
floyd_warshall()
for i in xrange(len(steps)):
    for item in steps[i]:
        print item
    print "\n\n"