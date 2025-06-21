import re
import numpy as np
from mealpy import Problem

# Load the Max-Cut problem from a .clq file
def load_maxcut_file(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('e'):
                parts = line.strip().split()
                node1, node2 = int(parts[1]), int(parts[2])
                edges.append((node1 - 1, node2 - 1, 1))  # Convert to 0-based indexing with weight 1
    return edges

def prepare_maxcut_data(edges):
    """
    Prepare Max-Cut data from a list of edges.
    """
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    num_nodes = len(nodes)
    adjacency_matrix = np.zeros((num_nodes, num_nodes))
    for edge in edges:
        node1, node2, weight = edge
        adjacency_matrix[node1, node2] = weight
        adjacency_matrix[node2, node1] = weight  # Undirected graph

    # Prepare the data dictionary
    data = {
        "adjacency_matrix": adjacency_matrix
    }
    return data, adjacency_matrix.shape[0]

#class for the Max-Cut problem
class MaxCutProblem(Problem):
    def __init__(self, bounds, minmax="max", data=None, **kwargs):
        """
        Initialize the Max-Cut Problem.
        :param bounds: Bounds for the optimization variables.
        :param minmax: Optimization goal ("max" for maximization).
        :param data: Dictionary containing the adjacency matrix.
        """
        self.adj_matrix = data["adjacency_matrix"]
        self.num_nodes = self.adj_matrix.shape[0]
        super().__init__(bounds=bounds, minmax=minmax, **kwargs)

    def calculate_cut_value(self, binary_solution):
        """
        Calculate the cut value of a binary solution.
        :param binary_solution: List of binary values (0 or 1) for each node.
        :return: Total cut value.
        """
        cut_value = 0
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):  # Iterate only over upper triangle
                if binary_solution[i] != binary_solution[j]:  # Nodes in different sets
                    cut_value += self.adj_matrix[i, j]
        return cut_value

    def obj_func(self, x):
        """
        Objective function to maximize the cut value.
        :param x: Solution vector (raw continuous values).
        :return: Cut value for the solution.
        """
        binary_solution = [int(round(val)) for val in x]  # Convert to binary
        cut_value = self.calculate_cut_value(binary_solution)
        return cut_value
