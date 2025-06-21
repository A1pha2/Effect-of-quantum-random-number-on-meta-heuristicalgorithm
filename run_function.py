import os
import numpy as np


def read_sets(file_path, pop_size, num_city):
    """
    Reads a file containing ranked sets and returns them as a list of lists.

    Parameters:
    - file_path (str): Path to the file containing the ranked sets.
    - pop_size (int): Expected population size (number of sets).
    - num_city (int): Expected number of cities (elements per set).

    Returns:
    - list: A list of ranked sets, where each set is a list of integers.

    Raises:
    - ValueError: If the file content does not match the expected dimensions.
    """
    sets = []
    with open(file_path, "r") as file:
        for line in file:
            set = list(map(int, line.strip().split()))
            sets.append(set)

    # Validate the dimensions of the ranked sets
    if len(sets) != pop_size:
        raise ValueError(
            f"Expected {pop_size} sets, but found {len(sets)} in the file."
        )

    for set in sets:
        if len(set) != num_city:
            raise ValueError(
                f"Each set must have {num_city} elements. Found a set with {len(set)} elements."
            )

    return np.array(sets)


def save_history_file(model, file_dir, file_prefix, num_epochs):
    """
    :param model: The optimization model containing the history
    :param file_dir: The directory where the history file will be saved
    :param file_prefix: Prefix for the history filename
    """
    history_file = os.path.join(file_dir, f"{file_prefix}_history.txt")

    with open(history_file, "w") as f:

        # for epoch in enumerate(model.history.list_global_best):
        for epoch in range(0, num_epochs):
            # fitness = agent.target.fitness, Global Fitness: {fitness}
            # solution = agent.solution, Solution: {solution}

            # Fetch additional metrics
            diversity = model.history.list_diversity[epoch]
            exploration = model.history.list_exploration[epoch]
            exploitation = model.history.list_exploitation[epoch]
            local_fitness = model.history.list_current_best_fit[epoch]
            global_fitness = model.history.list_global_best_fit[epoch]
            runtime = model.history.list_epoch_time[epoch]

            f.write(
                f"Epoch: {epoch+1}, Local Fitness: {local_fitness}, Global Fitness: {global_fitness}, Diversity: {diversity}, \
Exploration: {exploration}, Exploitation: {exploitation}, Runtime: {runtime}\n"
            )

    print(f"History saved to {history_file}")


import os

def run_optimization_trials(
    base_starting_solution_dir,
    base_history_dir,
    num_trials,
    rng_type,
    parameters,  # No need for pop_size as a separate argument
    num_city,
    mod,
    mod_ver,
    problem,
):
    """
    Run optimization trials using a specified algorithm and store history.

    :param base_starting_solution_dir: Base directory of starting solutions
    :param base_history_dir: Base directory to store history results
    :param num_trials: Number of trials to execute
    :param rng_type: Type of RNG used (e.g., MT19937)
    :param parameters: List of dictionaries containing epoch and pop_size
    :param num_city: Number of cities for reading sets
    :param mod: Module containing the optimization algorithm
    :param mod_ver: Version of the optimization algorithm used
    :param problem: Problem instance to be solved
    """
    # Ensure the base history directory exists
    os.makedirs(base_history_dir, exist_ok=True)

    # Loop through each trial directory (trial_1 to trial_n)
    for trial_num in range(1, num_trials + 1):
        trial_name = f"trial_{trial_num}"
        file_path_rng = os.path.join(
            base_starting_solution_dir, trial_name, f"{rng_type}.txt"
        )

        if not os.path.exists(file_path_rng):
            print(f"Skipping {file_path_rng} (File not found)")
            continue

        # Loop through parameter sets
        for idx, params in enumerate(parameters, start=1):
            pop_size = params["pop_size"]  # Dynamically get pop_size from parameters
            
            # Read the corresponding starting solution
            starting_solutions = read_sets(file_path_rng, pop_size, num_city)

            # Define the history directory for this trial
            trial_history_dir = os.path.join(base_history_dir, trial_name)
            os.makedirs(trial_history_dir, exist_ok=True)

            if not os.path.exists(trial_history_dir):
                print(f"Skipping {trial_history_dir} (File not found)")
                continue

            # Create unique directory name based on parameters
            file_prefix = f"e={params['epoch']}p={params['pop_size']}"
            file_dir = os.path.join(trial_history_dir, file_prefix)
            os.makedirs(file_dir, exist_ok=True)

            # Initialize and solve the model
            model_class = getattr(mod, mod_ver)  # Dynamically get the class from the module
            model = model_class(epoch=params["epoch"], pop_size=params["pop_size"])
            history = model.solve(problem, starting_solutions=starting_solutions)

            # Save history
            save_history_file(model, file_dir, file_prefix, params["epoch"])

            # Print the best results for each run
            print(
                f"Trial {trial_num} - Run {idx}: Epoch={params['epoch']}, Pop Size={params['pop_size']}"
            )
            print(f"Best fitness: {model.g_best.target.fitness}")
            print(
                f"Best solution: {model.problem.decode_solution(model.g_best.solution)}"
            )

