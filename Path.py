'''
Python3 module containing the Path class.

@author: Trent Weatherman
@author: Nick Widener
@date: November 18, 2015
'''

class Path():
    '''
    Stores a path to the destination node.
    '''

    def __init__(self):
        '''
        Constructor for the Path class.

        Fields:
            path: A list of vertex IDs ordered by apperance in the path.
        '''
        self.path = []

    def add_vertex(self, vertex_ID):
        '''
        Adds a vertex ID to the path.
        '''
        self.path.append(vertex_ID)

    def add_vertices(self, vertex_list):
        '''
        Adds a list of vertex IDs to the path.
        '''
        self.path.extend(vertex_list)
