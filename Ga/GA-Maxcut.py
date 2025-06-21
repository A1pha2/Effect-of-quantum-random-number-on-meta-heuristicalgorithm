#!/usr/bin/env python
# coding: utf-8
from mealpy.evolutionary_based import GA
import os
import numpy as np
from mealpy import PermutationVar, BinaryVar, FloatVar


os.chdir("/home/user/quantum-project/quantum-project/Ga") 


# # <span style="color:blue; font-weight:bold;">brock200_2.clq</span>
# 
import sys

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(parent_dir)
from Maxcut import *
from run_function import *
from config import parameters, num_trials

filePath2 = os.path.join("..", "maxcut_problem", "brock200_2.clq.txt")
edges = load_maxcut_file(filePath2)

data1, num_nodes1 = prepare_maxcut_data(edges)
# print(data1)

# Create the problem instance
bounds = [BinaryVar(n_vars=num_nodes1, name="binary")]
problem = MaxCutProblem(bounds=bounds, minmax="max", data=data1, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Brock200_2")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Brock200_2", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Brock200_2")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Brock200_2", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Brock200_2")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Brock200_2", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=200,
    mod=GA,    
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Brock200_2")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Brock200_2", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=200,
    mod=GA,    
    mod_ver="BaseGA",
    problem=problem,
)


# # <span style="color:blue; font-weight:bold;">brock200_4.clq</span>
# 
filePath2 = os.path.join("..", "maxcut_problem", "brock200_4.clq.txt")
edges = load_maxcut_file(filePath2)

data1, num_nodes1 = prepare_maxcut_data(edges)
# print(data1)

# Create the problem instance
bounds = [BinaryVar(n_vars=num_nodes1, name="binary")]
problem = MaxCutProblem(bounds=bounds, minmax="max", data=data1, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Brock200_4")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Brock200_4", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Brock200_4")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Brock200_4", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Brock200_4")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Brock200_4", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Brock200_4")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Brock200_4", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# # <span style="color:blue; font-weight:bold;">C125.9.clq</span>
filePath2 = os.path.join("..", "maxcut_problem", "C125.9.clq.txt")
edges = load_maxcut_file(filePath2)

data1, num_nodes1 = prepare_maxcut_data(edges)
# print(data1)

# Create the problem instance
bounds = [BinaryVar(n_vars=num_nodes1, name="binary")]
problem = MaxCutProblem(bounds=bounds, minmax="max", data=data1, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "C125.9")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "C125.9", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=125,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "C125.9")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "C125.9", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=125,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "C125.9")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "C125.9", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=125,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "C125.9")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "C125.9", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=125,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# # <span style="color:blue; font-weight:bold;">gen200_p0.9_44.b.clq</span>
filePath2 = os.path.join("..", "maxcut_problem", "gen200_p0.9_44.b.clq.txt")
edges = load_maxcut_file(filePath2)

data1, num_nodes1 = prepare_maxcut_data(edges)
# print(data1)

# Create the problem instance
bounds = [BinaryVar(n_vars=num_nodes1, name="binary")]
problem = MaxCutProblem(bounds=bounds, minmax="max", data=data1, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "gen200_p0.9_44.b")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "gen200_p0.9_44.b", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "gen200_p0.9_44.b")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "gen200_p0.9_44.b", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "gen200_p0.9_44.b")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "gen200_p0.9_44.b", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "gen200_p0.9_44.b")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "gen200_p0.9_44.b", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=200,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# # <span style="color:blue; font-weight:bold;">keller4.clq</span>
filePath2 = os.path.join("..", "maxcut_problem", "keller4.clq.txt")
edges = load_maxcut_file(filePath2)

data1, num_nodes1 = prepare_maxcut_data(edges)
# print(data1)

# Create the problem instance
bounds = [BinaryVar(n_vars=num_nodes1, name="binary")]
problem = MaxCutProblem(bounds=bounds, minmax="max", data=data1, save_population=True)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Keller4")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Keller4", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=171,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Keller4")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Keller4", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=171,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Keller4")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Keller4", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=171,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
# 
# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "Maxcut", "Keller4")
base_history_dir = os.path.join("..", "history", "ga", "maxcut", "Keller4", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=171,
    mod=GA,
    mod_ver="BaseGA",
    problem=problem,
)

