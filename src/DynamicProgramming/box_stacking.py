'''
Created on Nov 8, 2011

Code to stack a set of boxes
HANABI and SAKURASOUND are code names for Joir-dan Gumbs
@author: Hanabi

Performs in O(n^2) ignoring complexity to get all information presented in one algorithm.
'''
import itertools
# -- FOR BOXES DIMENSIONS
H = 0
W=1
L=2

# --- FOR THE BOX STACKING ALGO
HEIGHT = 0
BOX_TUPLE = 1
TOP_BOX = -1
R_BOX = 2
O_BOX = 3
AREA = 1
boxes = ((1,3,2), (2,4,2), (4,1,3), (6,3,5))

table = {}

# This setup runs in n*dim time, or n time... 
def setup(boxes):
    all_boxes_rotation = []
    for box in boxes:
        for dim in xrange(len(box)):
            pbox = [x for x in box]
            height = pbox[dim]
            pbox[H], pbox[dim] = pbox[dim], pbox[H]
            if pbox[W] > pbox[L]: 
                pbox[L], pbox[W] = pbox[W], pbox[L] 
            area = reduce(lambda x,y: x*y, [z for z in box if z != pbox[H]])
            fbox = tuple([x for x in pbox])
            all_boxes_rotation.append((height, area, fbox, box))
        
    return  tuple([x for x in sorted(all_boxes_rotation, key=lambda permbox: permbox[AREA])])

def box_stacking(permboxes):
    if table.has_key(permboxes):
        #print "Found", permboxes, table[permboxes] # I commented this because it would show a ton of memo messages
        return table[permboxes]
    else:
        if len(permboxes) == 1:
            print "found", permboxes[0]
            table[permboxes] = (permboxes[0][HEIGHT], (permboxes[0],))
            return table[permboxes]
        else:
            max_height = float('-Inf')
            max_boxes = ()
            
            for i in xrange(len(permboxes)):
                max_i = box_stacking(tuple([x for x in permboxes if x != permboxes[i]]))
                if max_i[HEIGHT] > max_height + permboxes[i][HEIGHT]:
                    b_top_w = max_i[BOX_TUPLE][TOP_BOX][W] #Width of the Top box in this chain
                    b_top_l = max_i[BOX_TUPLE][TOP_BOX][L] #Length of the Top box in this chain
                    if b_top_w > permboxes[i][R_BOX][W] and b_top_l > permboxes[i][R_BOX][L]:
                        max_height = max_i[HEIGHT] + permboxes[i][HEIGHT]
                        chain = [box for box in max_i[BOX_TUPLE]] + [permboxes[i]]
                        max_boxes = tuple([x for x in chain])
            table[permboxes] = (max_height, max_boxes)
            return table[permboxes]

#print setup(boxes)
print box_stacking(setup(boxes))