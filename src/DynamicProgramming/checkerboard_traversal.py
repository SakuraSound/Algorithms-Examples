'''
Created on Nov 8, 2011
HANABI and SAKURASOUND are code names for Joir-dan Gumbs
@author: Hanabi
'''


costs = [[1, 3, 4, 1, 8],
         [3, 5, 3, 9, 2],
         [4, 5, 1, 8, 6],
         [12, 4, 1, 7, 2],
         [1, 2, 4, 2, 3]]

COST = 0
CHAIN = 1

table = {(0,0):(1, ((0,0),)), (0,1):(3, ((0,1),)), (0,2):(4, ((0,2),)), (0,3):(1, ((0,3),)), (0,4):(8, ((0,4),))}

def test_min(optimal, min_cost, min_chain, node_cost):
    new_optimal = (optimal[COST] + node_cost, optimal[CHAIN])
    return new_optimal if new_optimal[COST] <= min_cost else (min_cost, min_chain)
    

def simple_board_traverse(row,COL = None):
    if table.has_key((row, COL)):
        return table[(row, COL)]
    else:
        min_cost = float('Inf')
        min_chain = ()
        if COL == None:
            crange = range(len(costs))
            for col in crange:
                optimal = simple_board_traverse(row, col)
                min_cost, min_chain = test_min(optimal, min_cost, min_chain, 0)
        else:
            trange = [-1, 0, 1]
            crange = range(len(costs))
            for col in trange:
                if (COL + col) in crange:
                    optimal = simple_board_traverse(row - 1, COL + col)
                    min_cost, min_chain = test_min(optimal, min_cost, min_chain, costs[row][COL])
        table[(row, COL)] = (min_cost, tuple([cel for cel in min_chain] + [(row, COL)]))
        return table[(row, COL)]

"""
# Forgot the top case... 
def board_traverse(row, tcol=None):
    if table.has_key((row, tcol)):
        #print "found", (row, tcol), table[(row, tcol)]
        return table[(row, tcol)]
    else:
        tcol = 0 if tcol == None else tcol
        min_cost = float('Inf')
        min_chain = ()
        nrange = range(len(costs[row-1]))
        trange = nrange if row == len(costs) else range(tcol - 1, tcol + 2)
        #print trange
        print "*"*(len(costs) - row),(row, tcol)
        for col in trange:
            if (col - 1) in nrange:
                print "*"*(len(costs) - row),(row -1, col -1),   
                optimal = board_traverse(row -1, col -1)
                #print row, col, costs[row][tcol]
                min_cost, min_chain = test_min(optimal, min_cost, min_chain, costs[row][col - 1])
            if (col) in nrange:
                print "*"*(len(costs) - row),(row-1, col),
                optimal = board_traverse(row-1, col)
                min_cost, min_chain = test_min(optimal, min_cost, min_chain, costs[row][col])
            if (col + 1) in nrange:
                print "*"*(len(costs) - row),(row-1, col + 1), "----",
                optimal = board_traverse(row -1, col +1)
                min_cost, min_chain = test_min(optimal, min_cost, min_chain, costs[row][col + 1])
        table[(row, tcol)] = (min_cost , tuple([cel for cel in min_chain] + [(row, tcol)]))
        print "*"*(len(costs) - row),[table[(row, tcol)]]
        return table[(row, tcol)]
        
"""
print simple_board_traverse(4)    