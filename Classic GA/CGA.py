import random
import time


def initialize_population(population_size, gene_length):
    population = []
    for _ in range(population_size):
        individual = [random.randint(0, 1) for _ in range(gene_length)]
        population.append(individual)
    return population


# Function to calculate the fitness of an individual (example fitness function)
def fitness_function(individual):
    return sum(individual)


# Function to select parents using tournament selection
def select_parents(population, num_parents):
    parents = []
    tournament_size = 3
    for _ in range(num_parents):
        tournament = random.sample(population, tournament_size)
        parents.append(max(tournament, key=fitness_function))
    return parents


# Function to perform crossover (single-point crossover)
def crossover(parents, num_offspring):
    offspring = []
    for _ in range(num_offspring):
        parent1, parent2 = random.sample(parents, 2)
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        offspring.append(child)
    return offspring


# Function to perform mutation (bit flip mutation)
def mutate(offspring, mutation_rate):
    for child in offspring:
        for i in range(len(child)):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]
    return offspring


# Main genetic algorithm function
def genetic_algorithm(population_size, gene_length, num_generations, mutation_rate):
    start_time = time.time()

    population = initialize_population(population_size, gene_length)
    for generation in range(num_generations):
        # Calculate fitness of each individual
        fitness_scores = [fitness_function(individual) for individual in population]
        # Select parents
        parents = select_parents(population, num_parents=2)
        # Perform crossover to create offspring
        offspring = crossover(parents, num_offspring=population_size - len(parents))
        # Perform mutation on offspring
        offspring = mutate(offspring, mutation_rate)
        # Replace old population with offspring
        population = parents + offspring
        # Print best individual in this generation
        best_individual = max(population, key=fitness_function)
        print(
            f"Generation {generation + 1}: Best Individual - {best_individual} Fitness - {fitness_function(best_individual)}"
        )

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Genetic Algorithm finished in {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    population_size = 100
    gene_length = 4
    num_generations = 50
    mutation_rate = 0.1
    genetic_algorithm(population_size, gene_length, num_generations, mutation_rate)
