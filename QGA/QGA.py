from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
import numpy as np

# ALGORITHM PARAMETERS
N = 50  # Define here the population size
genome = 4  # Define here the chromosome length
generation_max = 450  # Define here the maximum number of generations/iterations

# Initialize quantum circuit and classical register
qc = QuantumCircuit(genome, genome)

# Example fitness function
def fitness_function(x):
    return sum(x)  # Calculate sum of x values

# Main loop for genetic algorithm
for generation in range(generation_max):
    print(f"= GENERATION: {generation} =")

    # Reset quantum circuit
    qc.reset(range(genome))

    # Randomize initial states using Hadamard gate
    for qubit in range(genome):
        if np.random.rand() < 0.5:
            qc.h(qubit)  # Apply Hadamard gate with 50% probability

    # Measure and evaluate fitness
    qc.measure(range(genome), range(genome))
    sim = Aer.get_backend("qasm_simulator")
    result = sim.run(transpile(qc, sim)).result()
    counts = result.get_counts()

    fitness_values = {
        binary_string: fitness_function([int(bit) for bit in binary_string])
        for binary_string in counts.keys()
    }
    # Select top N individuals based on fitness
    selected_strings = sorted(
        fitness_values.keys(), key=lambda x: fitness_values[x], reverse=True
    )[:N]

    # Update quantum circuit for selected individuals
    qc.reset(range(genome))
    for binary_string in selected_strings:
        for idx, bit in enumerate(binary_string):
            if bit == "1":
                qc.x(idx)  # Apply X-gate for '1' bits
        qc.h(range(genome))  # Apply Hadamard gate for randomization

    print("Selected Individuals:")
    for binary_string in selected_strings:
        print(
            "Binary String:", binary_string, "Fitness:", fitness_values[binary_string]
        )

# Execute the final circuit and plot the result
qc.measure(range(genome), range(genome))
simulator = Aer.get_backend("qasm_simulator")
compiled_qc = transpile(qc, simulator)
qobj = assemble(compiled_qc)
result = simulator.run(qobj).result()
counts = result.get_counts()
print("Final Results:")
print(counts)
plot_histogram(counts)
