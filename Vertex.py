'''
Python3 module containing the Vertex class.

@author: Trent Weatherman
@author: Nick Widener
@date: November 18, 2015
'''

class Vertex():
    '''
    Vertex class that is used by the Graph class.
    '''

    def __init__(self, ID):
        '''
        Constructor for the Vertex class.

        Fields:
            ID: A unique integer used to identify the vertex.
            visited: The number of times the vertex has been visited during a
                     depth first search.
            sdj_list: A list holding the IDs of all verticies that are adjacent
                      to the vertex.
        '''
        self.ID = ID
        self.visited = 0
        self.adj_list = []

    def add_adj_vertex(self, vertex_ID):
        '''
        Adds a new vertex id to the adj_list.
        '''
        self.adj_list.append(vertex_ID)

    def reset_visited(self):
        '''
        Resets visited to 0.
        '''
        self.visited = 0

    def get_next(self):
        '''
        Returns the next vertex ID in adj_list.
        '''
        if (self.visited < len(self.adj_list)):
            next = self.adj_list[self.visited]
            self.visited += 1
            return next
        else:
            return -1
