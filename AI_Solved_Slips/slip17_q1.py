import random

def objective_function(x):
    return -(x ** 2)

def hill_climbing(initial_x, step_size, max_iterations):
    current_x = initial_x

    for _ in range(max_iterations):
        current_value = objective_function(current_x)
        neighbor_x = current_x + random.uniform(-step_size, step_size)

        if objective_function(neighbor_x) > current_value:
            current_x = neighbor_x

    return current_x, objective_function(current_x)

if __name__ == "__main__":
    initial_x = random.uniform(-10, 10)
    result_x, result_value = hill_climbing(initial_x, 0.1, 100)

    print("Hill Climbing Algorithm:")
    print("Initial x:", initial_x)
    print("Maximum x found:", result_x)
    print("Maximum value found:", result_value)
