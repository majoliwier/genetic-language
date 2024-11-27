from minilang_gp import MiniLangGP
import random


# ocena fitess na razie randomowa
def example_fitness_function(program: 'Node') -> float:
    return random.random()


def print_program(node: 'Node', indent: int = 0) -> None:
    indent_str = "  " * indent
    print(f"{indent_str}{node.type}: {node.value}")
    for child in node.children:
        print_program(child, indent + 1)


def main():
    gp = MiniLangGP(max_depth=5, min_depth=2)

    population_size = 100
    generations = 100
    tournament_size = 2

    population = [gp.generate_random_program() for _ in range(population_size)]

    # program zapisany jako json
    # serial_program = gp.serialize(population[0])
    # print(serial_program)

    print("\nPrzykład ewolucji:")
    for generation in range(generations):

        fitness_scores = [example_fitness_function(prog) for prog in population]
        best_fitness = max(fitness_scores)
        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        print(f"Generacja {generation}:")
        print(f"Najlepsze przystosowanie: {best_fitness:.4f}")
        print(f"Średnie przystosowanie: {avg_fitness:.4f}")
        print("Najlepszy program:")
        print_program(max(population, key=example_fitness_function))

        new_population = []

        while len(new_population) < population_size * 2:
            parent1 = gp.tournament_selection(population, example_fitness_function, tournament_size)
            parent2 = gp.tournament_selection(population, example_fitness_function, tournament_size)

            if random.random() < 0.8:
                offspring1, offspring2 = gp.crossover(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2

            if random.random() < 0.1:
                offspring1 = gp.mutate(offspring1)
            if random.random() < 0.1:
                offspring2 = gp.mutate(offspring2)

            new_population.extend([offspring1, offspring2])

        fitness_scores = [example_fitness_function(prog) for prog in new_population]

        fitness_program_pairs = list(zip(fitness_scores, new_population))

        fitness_program_pairs.sort(reverse=True, key=lambda x: x[0])

        sorted_population = [prog for fitness, prog in fitness_program_pairs]

        population = sorted_population[:population_size]

    best_program = max(population, key=example_fitness_function)
    print("\nNajlepszy znaleziony program:")
    print_program(best_program)


if __name__ == "__main__":
    main()
