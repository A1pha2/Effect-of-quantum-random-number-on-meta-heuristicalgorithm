
import re
import math
import numpy as np
from mealpy import Problem

# Load the TSP file
def load_tsplib_tsp(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        start = False
        for line in lines:
            if line.strip() == "NODE_COORD_SECTION":
                start = True
                continue
            if line.strip() == "EOF":
                break
            if start:
                parts = re.split(r'\s+', line.strip())
                x, y = float(parts[1]), float(parts[2])  # Extract x and y coordinates
                coordinates.append((x, y))  # Add tuple to the list
    return coordinates

def calculate_distance(coord1, coord2):
    """
    Calculate Euclidean distance between two coordinates.
    """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def create_distance_matrix(coordinates):
    """
    Create a distance matrix from a list of coordinates.
    """
    num_cities = len(coordinates)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]  # Initialize a square matrix with zeros
    
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])
            else:
                distance_matrix[i][j] = 0  # Distance from a city to itself is 0
    return distance_matrix

def prepare_tsp_data(coordinates):
    """
    Prepare TSP data from a list of coordinates.
    """
    coordinates = np.array(coordinates)
    num_cities = len(coordinates)
    data = {
        "city_positions": coordinates,
        "num_cities": num_cities,
    }
    return data, num_cities

# class for the TSP problem
class TspProblem(Problem):
    def __init__(self, bounds=None, minmax="min", data=None, **kwargs):
        self.data = data
        super().__init__(bounds, minmax, **kwargs)

    @staticmethod
    def calculate_distance(city_a, city_b):
        # Calculate Euclidean distance between two cities
        return np.linalg.norm(city_a - city_b)

    @staticmethod
    def calculate_total_distance(route, city_positions):
        # Calculate total distance of a route
        total_distance = 0
        num_cities = len(route)
        for idx in range(num_cities):
            current_city = route[idx]
            next_city = route[(idx + 1) % num_cities]  # Wrap around to the first city
            total_distance += TspProblem.calculate_distance(city_positions[current_city], city_positions[next_city])
        return total_distance

    def obj_func(self, x):
        x_decoded = self.decode_solution(x)
        route = x_decoded["per_var"]
        fitness = self.calculate_total_distance(route, self.data["city_positions"])
        return fitness