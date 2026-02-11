#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    total_size = 1
    
    if v.left:
        total_size += calculate_sizes(v.left)
    if v.right:
        total_size += calculate_sizes(v.right)

    v.size = total_size
    return total_size


#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 2t+1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t-1 (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    current_v = v
    
    while True:
        l_size = 0
        if current_v.left is not None:
            l_size = current_v.left.size
        
        r_size = 0
        if current_v.right is not None:
            r_size = current_v.right.size
    

        if l_size >= t:
            current_v = current_v.left

        elif r_size >= t:
            current_v = current_v.right
        
        else:
            return current_v