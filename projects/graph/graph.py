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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else: 
            raise IndexError("That vertex does not exist!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit queue is not empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit stack and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit stack is not empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex on the queue
            current_vertex = plan_to_visit.pop()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex, visited_vertices=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # add the currently checked vertex to visited
        visited_vertices.append(starting_vertex)
        print(starting_vertex)
        # for every neighbor of the current vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # if the vertice's neighbor has not been visited yet 
            if neighbor not in visited_vertices:
                # run the recursive function on it
                self.dft_recursive(neighbor)

    # Understand: Get a starting vertex from and go through all the existing
    # vertices only printing each one once. 
    # Plan: Print the current vertex and run the function on all it's neighbors
    # if the vertice has not been visited yet.

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue, and enqueue a PATH with the starting vertex
        path_queue = Queue()
        path_queue.enqueue([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while the queue is not empty
        while path_queue.size() > 0:
            # dequeue the first PATH
            current_path = path_queue.dequeue()
            # grab the last vertex in the PATH
            current_vertex = current_path[-1]
            # if it hasn't been visited
            if current_vertex not in visited_vertices:
                # check if it's the target
                if current_vertex == destination_vertex:
                    # return the path
                    return current_path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # make new versions of the current path, with each neighbor added to them
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        # duplicate the path
                        new_path = current_path.copy()
                        # add the neighbor
                        new_path.append(neighbor)
                        # add the new path to the queue
                        path_queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # stack rather than a queue
        # create an empty stack, and push a PATH with the starting vertex
        path_stack = Stack()
        path_stack.push([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while the stack is not empty
        while path_stack.size() > 0:
            # pop the first PATH
            current_path = path_stack.pop()
            # grab the last vertex in the PATH
            current_vertex = current_path[-1]
            # if it hasn't been visited
            if current_vertex not in visited_vertices:
                # check if it's the target
                if current_vertex == destination_vertex:
                    # return the path
                    return current_path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # make new versions of the current path, with each neighbor added to them
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        # duplicate the path
                        new_path = current_path.copy()
                        # add the neighbor
                        new_path.append(neighbor)
                        # add the new path to the stack
                        path_stack.push(new_path)

    def dfs_recursive(self, current_path, destination_vertex, visited_vertices = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create an empty list to hold the final working path
        working_path = []
        # if the given start is not a list
        if False == isinstance(current_path, list):
            # turn it into a list
            current_path = [current_path]

        # grab the last element of the list as the current vertex
        current_vertex = current_path[-1]

        # if the current vertex is equal to the destination vertex
        if current_vertex == destination_vertex:
            # return the current path as we have a resolution
            return current_path

        # if the current vertex has not been visited yet
        if current_vertex not in visited_vertices:
            # add the current vertex to the visited list
            visited_vertices.append(current_vertex)
            # print(f'current vertex {current_vertex}, destination vertex {destination_vertex}')

            # for every neighbor of the current vertex
            for neighbor in self.get_neighbors(current_vertex):
                # if the neighbor has not been visited yet
                if neighbor not in visited_vertices:
                    # copy the current path
                    new_path = current_path.copy()
                    # add the neighbor to the new path
                    new_path.append(neighbor)
                    # run the recursive function on the new path
                    working_path = self.dfs_recursive(new_path, destination_vertex)
        return working_path

    # Understand: return a depth-first path from starting vertex to the
    # destination vertex. 
    # Plan: get the last vertex of the current path and check if it is the
    # destination vertex. If not then run the function on the neighbor

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
