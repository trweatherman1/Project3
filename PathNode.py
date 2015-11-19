'''
Python 3 module containing the PathNode class.

@author: Trent Weatherman
@author: Nick Widener
@date: November 18, 2015
'''
class PathNode():
    '''
    Class that containg a Path object and links to other PathNode obkects that
    are used to build a binary tree.
    '''

    def __init__(self, path):
        '''
        Constructor for the PathNode class.

        Fields:
            path: A reference to a Path object.
            parent: The node above this node in the tree.
            sibling: The next node on the same level of the tree.
            left_child: The left child of this node.
            right_child: The right child of this node.
        '''
        self.path = path
        self.parent = None
        self.sibling = None
        self.left_child = None
        self.right_child = None

    def set_parent(self, parent):
        '''
        Sets the node's parent field.
        '''
        self.parent = parent

    def set_sibling(self, sibling):
        '''
        Sets the node's sibling field.
        '''
        self.sibling = sibling

    def set_left_child(self, left_child):
        '''
        Sets the node's left_child field.
        '''
        self.left_child = left_child

    def set_right_child(self, right_child):
        '''
        Sets the node's right_child field.
        '''
        self.right_child = right_child
