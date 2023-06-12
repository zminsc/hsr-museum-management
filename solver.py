import numpy as np
import pygad

from globals import assistants, exhibition_areas
from ga_utils import fitness_func, crossover_func
from ga_utils import print_solution, check_solution_found

# arguments that can be changed
num_generations = 1000
num_parents_mating = 8
parent_selection_type = "rank"
mutation_type = "random"
mutation_probability = 0.05

# arguments that cannot be changed
sol_per_pop = (num_parents_mating * (num_parents_mating - 1)) // 2 + 1
num_genes = len(exhibition_areas) * 3
gene_space = np.arange(0, len(assistants), 1)

ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    gene_type=np.int32,
    parent_selection_type=parent_selection_type,
    crossover_type=crossover_func,
    mutation_type=mutation_type,
    mutation_probability=mutation_probability,
    gene_space=gene_space,
    on_generation=check_solution_found,
    allow_duplicate_genes=False,
)

ga_instance.run()

best_solution, best_solution_fitness, _ = ga_instance.best_solution()

print_solution(best_solution)
print(f"Fitness of best solution: {best_solution_fitness}")

ga_instance.plot_fitness()