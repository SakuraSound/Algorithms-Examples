'''
Created on Nov 7, 2011

@author: Hanabi
'''


location = [0, 2, 3, 5, 7, 10, 12]

profit =   [5, 3, 0, 4, 8, -1, 10]

k  = 3

table = {0:(0, [])}

def memoized_gas_stations(locations, profit, k):
    

def new_val(total_profit, i, value):
    newlist = value[1] + [i]
    return (total_profit + value[0], newlist)