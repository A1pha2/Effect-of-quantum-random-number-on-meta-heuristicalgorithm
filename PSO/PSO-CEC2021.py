#!/usr/bin/env python
# coding: utf-


from mealpy.swarm_based import PSO
import os
import numpy as np
from mealpy import PermutationVar, BinaryVar, FloatVar


os.chdir("/home/user/quantum-project/quantum-project/PSO") 


# # <span style="color:blue; font-weight:bold;">F12021</span>
#


import sys

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(parent_dir)
from run_function import *
from config import parameters, num_trials


from opfunu.cec_based.cec2021 import F12021

f1 = F12021(10, f_bias=0)


p1 = {
    "bounds": FloatVar(lb=f1.lb, ub=f1.ub),
    "obj_func": f1.evaluate,
    "minmax": "min",
    "name": "F1",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f1.lb, ub=f1.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F12021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F12021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p1,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F12021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F12021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p1,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F12021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F12021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p1,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F12021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F12021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p1,
)


# # <span style="color:blue; font-weight:bold;">F22021</span>
#


from opfunu.cec_based.cec2021 import F22021

f2 = F22021(10, f_bias=0)


p2 = {
    "bounds": FloatVar(lb=f2.lb, ub=f2.ub),
    "obj_func": f2.evaluate,
    "minmax": "min",
    "name": "F2",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f2.lb, ub=f2.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F22021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F22021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p2,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F22021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F22021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p2,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F22021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F22021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p2,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F22021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F22021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p2,
)


# # <span style="color:blue; font-weight:bold;">F32021</span>
#


from opfunu.cec_based.cec2021 import F32021

f3 = F32021(10, f_bias=0)


p3 = {
    "bounds": FloatVar(lb=f3.lb, ub=f3.ub),
    "obj_func": f3.evaluate,
    "minmax": "min",
    "name": "F3",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f3.lb, ub=f3.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F32021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F32021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p3,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F32021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F32021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p3,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F32021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F32021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p3,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F32021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F32021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p3,
)


# # <span style="color:blue; font-weight:bold;">F42021</span>
#


from opfunu.cec_based.cec2021 import F42021

f4 = F42021(10, f_bias=0)


p4 = {
    "bounds": FloatVar(lb=f4.lb, ub=f4.ub),
    "obj_func": f4.evaluate,
    "minmax": "min",
    "name": "F4",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f4.lb, ub=f4.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F42021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F42021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p4,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F42021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F42021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p4,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F42021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F42021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p4,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F42021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F42021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p4,
)


# # <span style="color:blue; font-weight:bold;">F52021</span>
#


from opfunu.cec_based.cec2021 import F52021

f5 = F52021(10, f_bias=0)


p5 = {
    "bounds": FloatVar(lb=f5.lb, ub=f5.ub),
    "obj_func": f5.evaluate,
    "minmax": "min",
    "name": "F5",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f5.lb, ub=f5.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F52021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F52021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p5,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F52021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F52021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p5,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F52021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F52021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p5,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F52021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F52021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p5,
)


# # <span style="color:blue; font-weight:bold;">F62021</span>
#


from opfunu.cec_based.cec2021 import F62021

f6 = F62021(10, f_bias=0)


p6 = {
    "bounds": FloatVar(lb=f6.lb, ub=f6.ub),
    "obj_func": f6.evaluate,
    "minmax": "min",
    "name": "F6",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f6.lb, ub=f6.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F62021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F62021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p6,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F62021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F62021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p6,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F62021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F62021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p6,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F62021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F62021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p6,
)


# # <span style="color:blue; font-weight:bold;">F72021</span>
#


from opfunu.cec_based.cec2021 import F72021

f7 = F72021(10, f_bias=0)


p7 = {
    "bounds": FloatVar(lb=f7.lb, ub=f7.ub),
    "obj_func": f7.evaluate,
    "minmax": "min",
    "name": "F7",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f7.lb, ub=f7.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F72021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F72021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p7,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F72021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F72021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p7,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F72021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F72021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p7,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F72021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F72021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p7,
)


# # <span style="color:blue; font-weight:bold;">F82021</span>
#


from opfunu.cec_based.cec2021 import F82021

f8 = F82021(10, f_bias=0)


p8 = {
    "bounds": FloatVar(lb=f8.lb, ub=f8.ub),
    "obj_func": f8.evaluate,
    "minmax": "min",
    "name": "F8",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f8.lb, ub=f8.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F82021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F82021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p8,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F82021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F82021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p8,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F82021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F82021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p8,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F82021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F82021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p8,
)


# # <span style="color:blue; font-weight:bold;">F92021</span>
#


from opfunu.cec_based.cec2021 import F92021

f9 = F92021(10, f_bias=0)


p9 = {
    "bounds": FloatVar(lb=f9.lb, ub=f9.ub),
    "obj_func": f9.evaluate,
    "minmax": "min",
    "name": "F9",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f9.lb, ub=f9.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F92021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F92021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p9,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F92021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F92021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p9,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F92021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F92021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p9,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F92021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F92021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p9,
)


# # <span style="color:blue; font-weight:bold;">F102021</span>
#


from opfunu.cec_based.cec2021 import F102021

f10 = F102021(10, f_bias=0)


p10 = {
    "bounds": FloatVar(lb=f10.lb, ub=f10.ub),
    "obj_func": f10.evaluate,
    "minmax": "min",
    "name": "F10",
    "save_population": True,
}


# Create the problem instance
bounds = FloatVar(lb=f10.lb, ub=f10.ub)


# #### <span style="color:green; font-weight:bold;">-Mersene Twister</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F102021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F102021", "Mt19937")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Mt19937",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p10,
)


# #### <span style="color:green; font-weight:bold;">-Quasirandom</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F102021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F102021", "QuasiRandom")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="QuasiRandom",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p10,
)


# #### <span style="color:green; font-weight:bold;">-Ibm qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F102021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F102021", "Ibm")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="Ibm",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p10,
)


# #### <span style="color:green; font-weight:bold;">-Beam splitter qrng</span>
#


# Base directories
base_starting_solution_dir = os.path.join("..", "starting_solution", "CEC2021", "F102021")
base_history_dir = os.path.join("..", "history", "PSO", "CEC2021", "F102021", "BeamSplitter")

run_optimization_trials(
    base_starting_solution_dir=base_starting_solution_dir,
    base_history_dir=base_history_dir,
    num_trials=num_trials,
    rng_type="BeamSplitter",
    parameters=parameters,
    num_city=10,
    mod=PSO,
    mod_ver="OriginalPSO",
    problem=p10,
)

