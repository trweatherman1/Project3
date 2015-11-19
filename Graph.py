'''
Python3 module containing the Graph class.

@author: Trent Weatherman
@author: Nick Widener
@date: November 18, 2015
'''
import sys
from Vertex import Vertex
from Path import Path
from PathNode import PathNode

class Graph():
    '''
    An acyclic directed graph class with vertices and edges specified by an
    input file. Contains methods for populating and searching the graph.
    '''

    def __init__(self):
        '''
        Constructor fot the Graph class.

        Fields:
            dfs_paths: A list of Path objects that holds the currently discovered
                       paths in order of discovery.
            vertex_list: A dictionary, keys are vertex IDs and values are the
                         Vertex objects with those IDs.
            root: The root of the PathNode tree.
            last_node: The last node added to the PathNode tree.
        '''
        self.dfs_paths = [None]
        self.vertex_list = dict()
        self.root = None
        self.last_node = None

    def heap_hooray_dfs(self, graph_file, search_file):
        '''
        Calls all the method necessary to read the input files, create the
        vertices, find all the paths from the source to the destination vertex,
        and build and print a tree contining those paths.
        '''
        self.read_input_graph(graph_file)
        source_dest = self.read_source_dest(search_file)
        self.dfs_search(source_dest[0], source_dest[1])
        self.build_complete_tree()
        self.print_tree_levels()

    def read_input_graph(self, input_file):
        '''
        Reads the input file that is the first command line argument and builds
        the graph based on its contents.

        @param input_file: The name of a text file containing two integers per
                           line seperated by spaces. Each integer is a vertex
                           ID and each line represents an edge from the first
                           vertex to the second vertex.
        '''
        file = open(input_file)
        for line in file:
            if (len(line) != 1):
                start = int(line.split()[0])
                end = int(line.split()[1])
                if (start not in self.vertex_list.keys()):
                    self.vertex_list[start] = Vertex(start)
                if (end not in self.vertex_list.keys()):
                    self.vertex_list[end] = Vertex(end)
                self.vertex_list[start].add_adj_vertex(end)
        file.close()

    def read_source_dest(self, input_file):
        '''
        Reads the input file that is the second command line argument to get
        the vertex IDs of the source and destination vertices for the depth
        first search method.

        #param input_file: The name of a text file containing the vertex IDs of
                           the source and destination vertices seperated by spaces.
        @returns: A tuple. The first element is the source, the second element
                  is the destination.
        '''
        file = open(input_file)
        contents = file.read().split()
        file.close()
        return int(contents[0]),int(contents[1])

    def dfs_search(self, source, dest):
        '''
        Finds all paths from the source vertex to the dettination vertex,
        creates a Path object for each of these paths, and adds those Paths
        to dfs_paths in order of discovery.

        @param sourcs: The ID of the source vertex.
        @param dest: The ID of the destination vertex.
        '''
        stack = [source]
        while (len(stack) > 0):
            current_vertex = self.vertex_list[stack[len(stack)-1]]
            next = current_vertex.get_next()
            if (next == dest):
                path = Path()
                path.add_vertices(stack)
                path.add_vertex(next)
                self.dfs_paths.append(path)
            elif (next != -1):
                stack.append(next)
            else:
                self.vertex_list[stack.pop()].reset_visited()

    def build_complete_tree(self):
        '''
        Builds a binary tree with a PathNode object for each path from the
        source vertex to the destination vertex.
        '''
        if (len(self.dfs_paths) != 1):
            self.populate_tree()
            self.set_sibling_links(self.root)

    def populate_tree(self, index=1, new_parent=None):
        '''
        Creates a PathNode object for each Path in dfs_paths and sets their
        parent and child links.

        @param index: The index of the path in dfs_paths. Defaults to 1.
        @param new_parent: The PathNode that will be the parent of the node
                           created. Defaults to None.
        '''
        current_node = PathNode(self.dfs_paths[index])
        if (index == 1):
            self.root = current_node
        if (index == len(self.dfs_paths) - 1):
            self.last_node = current_node
        current_node.set_parent(new_parent)
        if (index*2 < len(self.dfs_paths)):
            current_node.set_left_child(self.populate_tree(index*2, current_node))
        if (index*2+1 < len(self.dfs_paths)):
            current_node.set_right_child(self.populate_tree(index*2+1, current_node))
        return current_node

    def set_sibling_links(self, root):
        '''
        Sets the sibling links for every PathNode in the tree.

        @param root: The root of the binary tree or a subtree.
        '''
        if (root == self.root and root.left_child != None and root.left_child != self.last_node):
            root.left_child.sibling = root.right_child
            self.set_sibling_links(root.left_child)
            self.set_sibling_links(root.right_child)
        else:
            if (root.left_child != None and root.left_child != self.last_node):
                root.left_child.sibling = root.right_child
                if (root.sibling != None):
                    root.right_child.sibling = root.sibling.left_child
                self.set_sibling_links(root.left_child)
                self.set_sibling_links(root.right_child)

    def print_tree_levels(self):
        '''
        Prints the lengths of the paths in each level of the tree.
        '''
        source_dest = self.read_source_dest(sys.argv[2])
        print('[' + str(source_dest[0]) + ', ' + str(source_dest[1]) + ']')
        if (len(self.dfs_paths) != 1):
            print('\tRoot: ' + str(len(self.root.path.path) - 1))
            end_node = self.root.left_child
            current_level = 1
            while end_node != None:
                string = '\tLevel ' + str(current_level) + ': '
                current_node = end_node
                while current_node != None:
                    string += str(len(current_node.path.path) - 1) + ' '
                    current_node = current_node.sibling
                print(string)
                current_level += 1
                end_node = end_node.left_child

if __name__ == '__main__':
    Graph().heap_hooray_dfs(sys.argv[1], sys.argv[2])
__author__ = 'Trent'
