from AST.minilang_gp import MiniLangGP, generate_code, example_fitness_function
import random

def main():
    gp = MiniLangGP(max_depth=3)

    population_size = 100
    generations = 100
    tournament_size = 2

    population = [gp.generate_random_program() for _ in range(population_size)]

    print("\nPrzykład ewolucji:")
    for generation in range(generations):

        fitness_scores = [example_fitness_function(prog) for prog in population]
        best_fitness = max(fitness_scores)
        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        print(f"Generacja {generation}:")
        print(f"Najlepsze przystosowanie: {best_fitness:.4f}")
        print(f"Średnie przystosowanie: {avg_fitness:.4f}")
        print("Najlepszy program:")
        print(generate_code(max(population, key=example_fitness_function)))

        new_population = []

        while len(new_population) < population_size * 2:
            parent1 = gp.tournament_selection(population, example_fitness_function, tournament_size)
            parent2 = gp.tournament_selection(population, example_fitness_function, tournament_size)

            chances = random.random()
            if chances < 0.2:
                offspring1 = gp.mutate(parent1)
                offspring2 = gp.mutate(parent2)
            elif chances < 0.8:
                offspring1, offspring2 = gp.crossover(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2

            new_population.extend([offspring1, offspring2])

        fitness_scores = [example_fitness_function(prog) for prog in new_population]

        fitness_program_pairs = list(zip(fitness_scores, new_population))

        fitness_program_pairs.sort(reverse=True, key=lambda x: x[0])

        sorted_population = [prog for fitness, prog in fitness_program_pairs]

        population = sorted_population[:population_size]

    best_program = max(population, key=example_fitness_function)
    print("\nNajlepszy znaleziony program:")
    print(generate_code(best_program))


if __name__ == "__main__":
    main()
