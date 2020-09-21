"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        #always check first to see if it exists, represent as set
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #get alls are most common question for interviews/tests
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        return set()

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = []
        checked = set()
        queue.append(starting_vertex)
        while queue:
            cur_node = queue.pop(0)
            if cur_node not in checked:
                checked.add(cur_node)
                print(cur_node)
                for e in self.get_neighbors(cur_node):
                    queue.append(e)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = []
        stack.append(starting_vertex)
        checked = set()
        while stack:
            current = stack.pop()
            if current not in checked:
                checked.add(current)
                print(current)
                for e in self.get_neighbors(current):
                    stack.append(e)

    def dft_recursive(self, starting_vertex, checked=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex in checked:
            return
        checked.add(starting_vertex)
        print(starting_vertex)
        for e in self.get_neighbors(starting_vertex):
            self.dft_recursive(e, checked)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = []
        checked = set()
        queue.append([starting_vertex])
        while queue:
            cur_path = queue.pop(0)
            cur_node = cur_path[-1]
            if cur_node == destination_vertex:
                return cur_path
            if cur_node not in checked:
                checked.add(cur_node)
                for e in self.get_neighbors(cur_node):
                    new_path = list(cur_path)
                    new_path.append(e)
                    queue.append(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = []
        stack.append([starting_vertex])
        checked = set()
        while stack:
            cur_path = stack.pop()
            cur_node = cur_path[-1]
            if cur_node == destination_vertex:
                return cur_path
            if cur_node not in checked:
                checked.add(cur_node)
                print(cur_path)
                for e in self.get_neighbors(cur_node):
                    new_path = list(cur_path)
                    new_path.append(e)
                    stack.append(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def recurse(vert, destination_vertex, checked=set()):
            cur_node = vert[-1]
            if cur_node in checked:
                return
            if cur_node == destination_vertex:
                return vert
            checked.add(cur_node)
            for e in self.get_neighbors(cur_node):
                new_path = list(vert)
                new_path.append(e)
                res = recurse(new_path, destination_vertex, checked)
                if res:
                    return res
        return recurse([starting_vertex], destination_vertex)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
