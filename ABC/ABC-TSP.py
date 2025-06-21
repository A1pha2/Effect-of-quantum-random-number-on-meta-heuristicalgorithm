#!/usr/bin/env python
# coding: utf-8
from mealpy.swarm_based import ABC
import os
import numpy as np
from mealpy import PermutationVar, BinaryVar, FloatVar


# # <span style="color:blue; font-weight:bold;">TSP problem</span>
# 

# ### <span style="color:yellow; font-weight:bold;">berlin52.tsp</span>
# 
os.chdir("/home/user/quantum-project/quantum-project/ABC") 

import sys

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(parent_dir)

# Now import from TSP.py
from TSP import *
from run_function import *
from config import parameters, num_trials

filePath1 = os.path.join("..","TSP_problem","berlin52.tsp")
coordinates1 = load_tsplib_tsp(filePath1)
data, num_cities = prepare_tsp_data(coordinates1)

distance_matrix = create_distance_matrix(coordinates1)
print(distance_matrix)

# Create the problem instance
bounds = PermutationVar(valid_set=list(range(0, num_cities)), name="per_var")
problem = TspProblem(bounds=bounds, minmax="min", data=data, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Berlin52")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Berlin52", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=52,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Berlin52")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Berlin52", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=52,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Berlin52")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Berlin52", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=52,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Berlin52")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Berlin52", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=52,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# ### <span style="color:yellow; font-weight:bold;">Bier127.tsp</span>
# 
filePath1 = os.path.join("..","TSP_problem","bier127.tsp")
coordinates1 = load_tsplib_tsp(filePath1)
data, num_cities = prepare_tsp_data(coordinates1)

distance_matrix = create_distance_matrix(coordinates1)
print(distance_matrix)

# Create the problem instance
bounds = PermutationVar(valid_set=list(range(0, num_cities)), name="per_var")
problem = TspProblem(bounds=bounds, minmax="min", data=data, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Bier127")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Bier127", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=127,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Bier127")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Bier127", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=127,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Bier127")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Bier127", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=127,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Bier127")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Bier127", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=127,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# ### <span style="color:yellow; font-weight:bold;">Eil101.tsp</span>
# 
filePath1 = os.path.join("..","TSP_problem","eil101.tsp")
coordinates1 = load_tsplib_tsp(filePath1)
data, num_cities = prepare_tsp_data(coordinates1)

distance_matrix = create_distance_matrix(coordinates1)
print(distance_matrix)

# Create the problem instance
bounds = PermutationVar(valid_set=list(range(0, num_cities)), name="per_var")
problem = TspProblem(bounds=bounds, minmax="min", data=data, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Eil101")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Eil101", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=101,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Eil101")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Eil101", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=101,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Eil101")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Eil101", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=101,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Eil101")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Eil101", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=101,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# ### <span style="color:yellow; font-weight:bold;">Pr76.tsp</span>
# 
filePath1 = os.path.join("..","TSP_problem","pr76.tsp")
coordinates1 = load_tsplib_tsp(filePath1)
data, num_cities = prepare_tsp_data(coordinates1)

distance_matrix = create_distance_matrix(coordinates1)
print(distance_matrix)

# Create the problem instance
bounds = PermutationVar(valid_set=list(range(0, num_cities)), name="per_var")
problem = TspProblem(bounds=bounds, minmax="min", data=data, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Pr76")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Pr76", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=76,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Pr76")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Pr76", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=76,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Pr76")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Pr76", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=76,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "Pr76")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "Pr76", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=76,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# ### <span style="color:yellow; font-weight:bold;">St70.tsp</span>
# 
filePath1 = os.path.join("..","TSP_problem","st70.tsp")
coordinates1 = load_tsplib_tsp(filePath1)
data, num_cities = prepare_tsp_data(coordinates1)

distance_matrix = create_distance_matrix(coordinates1)
print(distance_matrix)

# Create the problem instance
bounds = PermutationVar(valid_set=list(range(0, num_cities)), name="per_var")
problem = TspProblem(bounds=bounds, minmax="min", data=data, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "St70")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "St70", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=70,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "St70")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "St70", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=70,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "St70")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "St70", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=70,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "TSP", "St70")
base_history_dir = os.path.join("..", "history", "ABC", "tsp", "St70", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=70,
    mod=ABC,
    mod_ver="OriginalABC",
    problem=problem,
)

