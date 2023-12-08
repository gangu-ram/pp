import numpy as np

def objective_function(x):
    return -x**2 + 4*x

def hill_climbing(initial_x, step_size, max_iterations):
    for _ in range(max_iterations):
        current_value = objective_function(initial_x)
        neighbors = [initial_x + step_size, initial_x - step_size]
        best_neighbor = max(neighbors, key=objective_function)

        if objective_function(best_neighbor) <= current_value:
            break

        initial_x = best_neighbor

    return initial_x, objective_function(initial_x)

if __name__ == "__main__":
    # Initial values
    initial_x, step_size, max_iterations = 0.0, 0.1, 100

    # Run hill climbing algorithm
    result_x, result_value = hill_climbing(initial_x, step_size, max_iterations)

    # Print results
    print("Optimal x:", result_x)
    print("Optimal value:", result_value)
