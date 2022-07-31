import math
import unittest
from graph import Graph
import queue

def findWaterContainerPath(a, b, c):
    # Variable, graph, and lists setup
    starting_state = (0, 0)
    final_path = list()
    state_graph = Graph()
    vertices = list()
    vertices.append(state_graph.addVertex(starting_state))
    current_vert = vertices[0]
    current_vert.setDistance(0)
    current_vert.setPred(None)
    states = list(current_vert.getId())

    # Adds a solution path to graph and all vertices to
    # the list of vertices
    while states[0] != c and  states[1] != c:
        states = list(current_vert.getId())
        
        if a < b:
            temp = min(states[0], b - states[1])
            states[0] = states[0] - temp
            states[1] = states[1] + temp
            current_state = tuple(states)
            if current_state not in state_graph:
                new_vertex = state_graph.addVertex(current_state)
                current_vert.addNeighbor(new_vertex)
            if states[0] == 0:
                states[0] = a
                current_state = tuple(states)
                if current_state not in state_graph:
                    new_vertex = state_graph.addVertex(current_state)
                    current_vert.addNeighbor(new_vertex)
            if states[1] == b:
                states[1] = 0
                current_state = tuple(states)
                if current_state not in state_graph:
                    new_vertex = state_graph.addVertex(current_state)
                    current_vert.addNeighbor(new_vertex)
        
        if a > b:
            temp = min(states[1], a - states[0])
            states[1] = states[1] - temp
            states[0] = states[0] + temp
            current_state = tuple(states)
            if current_state not in state_graph:
                new_vertex = state_graph.addVertex(current_state)
                current_vert.addNeighbor(new_vertex)
            if states[1] == 0:
                states[1] = b
                current_state = tuple(states)
                if current_state not in state_graph:
                    new_vertex = state_graph.addVertex(current_state)
                    current_vert.addNeighbor(new_vertex)
            if states[0] == a:
                states[0] = 0
                current_state = tuple(states)
                if current_state not in state_graph:
                    new_vertex = state_graph.addVertex(current_state)
                    current_vert.addNeighbor(new_vertex)

        # Breadth first search
        for vertex in current_vert.getConnections():
            if vertex.getColor() == 'white':
                vertex.setColor('gray')
                vertex.setDistance(current_vert.getDistance() + 1)
                vertex.setPred(current_vert)
                vertices.append(vertex)
                current_vert.setColor('black')
        current_vert = vertices.pop(0)
    
    # Traverse the graph and add solution to final path list
    while current_vert.getPred():
        final_path.insert(0, current_vert.getId())
        current_vert = current_vert.getPred()     
    final_path.insert(0, starting_state)

    return final_path

# Unittests
class TestWaterContainerGraphSearch(unittest.TestCase):

    def testFindWaterContainerPathLessThan(self):
        capacity_a = 5
        capacity_b = 3
        goal_amount = 4
        expected_path = [(0, 0), (0, 3), (3, 3), (0, 1), (1, 3), (4, 0)]
        self.assertEqual(expected_path, findWaterContainerPath(capacity_a, capacity_b, goal_amount))

    def testFindWaterContainerPathGreaterThan(self):
        capacity_a = 3
        capacity_b = 5
        goal_amount = 4
        expected_path = [(0, 0), (3, 0), (3, 3), (1, 0), (3, 1), (0, 4)]
        self.assertEqual(expected_path, findWaterContainerPath(capacity_a, capacity_b, goal_amount))

def main():
   
    capacity_a = input("Enter the capacity of container A: ")
    capacity_b = input("Enter the capacity of container B: ")
    goal_amount = input("Enter the goal quantity: ")
    # ADD SOME TYPE/VALUE CHECKING FOR THE INPUTS (OR INSIDE YOUR FUNCTION)
    if max(capacity_a, capacity_b) < goal_amount:
        print('Invalid input')

    elif int(goal_amount) % math.gcd(int(capacity_a), int(capacity_b)) == 0:
        path = findWaterContainerPath(int(capacity_a), int(capacity_b), int(goal_amount))
        print(path)

    else:
        print("No solution for containers with these sizes and with this final goal amount")

# unittest_main() - run all of TestWaterContainerGraphSearch's methods (i.e. test cases)
def unittest_main():
    unittest.main()

# evaluates to true if run as standalone program
if __name__ == '__main__':
    main()
    unittest_main()