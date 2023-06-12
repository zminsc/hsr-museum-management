import numpy as np
import pygad

from globals import assistants, exhibition_areas
from typing import List


def fitness_func(ga_instance: pygad.GA, solution: List[int], solution_idx: int):
    losses = []

    for i in range(len(exhibition_areas)):
        cur_assistants = [
            assistants[solution[i * 3]],
            assistants[solution[i * 3 + 1]],
            assistants[solution[i * 3 + 2]],
        ]

        losses.append(exhibition_areas[i].calc_loss(cur_assistants))

    return 1.0 / (np.sum(losses) + 1)


def crossover_func(parents, offspring_size, ga_instance):
    offspring = []
    num_parents = parents.shape[0]
    num_genes = offspring_size[1]

    for i in range(num_parents):
        for j in range(i + 1, num_parents):
            parent1 = parents[i].copy()
            parent2 = parents[j].copy()

            idx1 = np.random.randint(0, num_genes)
            idx2 = np.random.randint(0, num_genes)

            indices = range(min(idx1, idx2), max(idx1, idx2))
            used_genes = set(np.take(parent1, indices, mode="wrap"))

            idx = indices.stop

            for gene in parent2:
                if idx % num_genes == indices.start:
                    break
                if gene in used_genes:
                    continue

                parent1[idx % num_genes] = gene
                used_genes.add(gene)
                idx += 1

            offspring.append(parent1)

    return np.array(offspring)


def print_solution(solution: List[int]) -> None:
    print()
    for i in range(len(exhibition_areas)):
        print(exhibition_areas[i].name + ":\n")
        print(
            f"\t{assistants[solution[i * 3]].name}, {assistants[solution[i * 3 + 1]].name}, {assistants[solution[i * 3 + 2]].name}\n"  # noqa: E501
        )


def check_solution_found(ga_instance: pygad.GA) -> None:
    if ga_instance.best_solution()[1] == 1.0:
        return "stop"
