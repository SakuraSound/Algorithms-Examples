'''
Created on Nov 8, 2011
Code for calculating the minimum cost and the chain for matrix multiplication

@author: Hanabi
'''


dim = ((30,35),(35,15),(15,5), (5,10), (10,20), (20,25))

table = {(1,):(0, (1,), (30,35)), (2,):(0, (2,), (35,15)), (3,):(0, (3,), (15,5)),
          (4,):(0, (4,), (5,10)), (5,):(0, (5,), (10,20)), (6,):(0, (6,), (20,25))}


COST = 0
CHAINS = 1
DIMS = 2

def matrix_mult_cost(mat):
    print mat
    if table.has_key(mat):
        #print "got cost", table[mat]
        return table[mat]
    else:
        #print "doesnt have key", mat
        min_cost = float('inf')
        min_chains = ()        
        min_dims = ()
        for i in xrange(1,len(mat)):
            #print mat[:i]
            opt_left = matrix_mult_cost(mat[:i])
            print opt_left
            #print mat[i:]
            opt_right = matrix_mult_cost(mat[i:])
            print opt_right
            p_b = opt_left[DIMS][0]
            p_k = opt_left[DIMS][1]
            p_j = opt_right[DIMS][1]
            cost = opt_left[COST] + opt_right[COST] + (p_b*p_k*p_j)
            if cost <= min_cost:
                min_cost = cost
                min_chains = (opt_left[CHAINS],opt_right[CHAINS])
                min_dims = (opt_left[DIMS][0], opt_right[DIMS][1])
        table[mat] = (min_cost, min_chains, min_dims)
        return table[mat]

#matrices = (1, 2, 3, 4, 5, 6)
matrices = (1, 2, 3)
print matrices
print matrix_mult_cost(matrices)
print table