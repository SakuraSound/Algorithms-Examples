'''
Created on Nov 8, 2011

Code to stack a set of boxes
@author: Hanabi
'''
import itertools

L = 0
W=1
H=2

boxes = ((1,3,2), (2,4,2), (4,1,3), (6,3,5))

# This setup runs in n * 3! time, or n time... 
def setup(boxes):
    all_boxes_rotation = []
    for box in boxes:
        perms = itertools.permutations(box) # Generates all full-length permutations
        all_boxes_rotation.extend(perms)
        
    return tuple([x for x in all_boxes_rotation])

def box_stacking():
    pass


print setup(boxes)