import sys, random, json, os

# Dodanie katalogu głównego projektu do sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from AST.minilang_gp import generate_code, MiniLangGP
from fitness_tests import fitness_functions

# Mapowanie nazw testów na funkcje przystosowania oraz docelowe liczby dla kontekstu
TEST_MAPPING = {
    "1_1A": (fitness_functions.fitness_1_1A_gradual, 1),
    "1_1B": (fitness_functions.fitness_1_1B_gradual, 789),
    "1_1C": (fitness_functions.fitness_1_1C_gradual, 31415),
    "1_1D": (fitness_functions.fitness_1_1D_gradual, 1),
    "1_1E": (fitness_functions.fitness_1_1E_gradual, 789),
    "1_1F": (fitness_functions.fitness_1_1F_gradual, 1),
    "1_2A": (fitness_functions.fitness_1_2A, None),
    "1_2B": (fitness_functions.fitness_1_2B, None),
    # Dodaj inne testy, jeśli potrzebne
}

# Konfiguracje ewolucji
MAX_GENERATIONS = 200
POPULATION_SIZE = 2000
TOURNAMENT_SIZE = 5


def main():
    if len(sys.argv) < 2:
        print("Użycie: python run_evolution_for_target.py <TEST_NAME>")
        print("Dostępne testy: " + ", ".join(TEST_MAPPING.keys()))
        sys.exit(1)

    test_name = sys.argv[1]
    if test_name not in TEST_MAPPING:
        print(f"Nieznany test: {test_name}")
        sys.exit(1)

    fitness_function, target_number = TEST_MAPPING[test_name]
    output_json = f"evolution_history_{test_name}.json"

    gp = MiniLangGP(max_depth=3)
    population = gp.generate_initial_population(POPULATION_SIZE)
    history = []

    best_overall_program = None
    best_overall_fitness = -float('inf')

    stagnation_threshold = 10
    initial_mutation_prob = 0.2
    high_mutation_prob = 0.5

    last_best_fitness = -float('inf')
    stagnation_count = 0
    mutation_prob = initial_mutation_prob

    for generation in range(MAX_GENERATIONS + 1):
        print(f"Pokolenie {generation}")
        fitness_scores = [fitness_function(prog) for prog in population]
        best_fitness = max(fitness_scores)
        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        print(f"  Najlepsze przystosowanie: {best_fitness:.5f}")
        print(f"  Średnie przystosowanie: {avg_fitness:.5f}")

        history.append({
            "generation": generation,
            "best_fitness": best_fitness,
            "avg_fitness": avg_fitness
        })

        # Aktualizacja najlepszego ogólnego programu, jeśli znaleziono lepszy
        if best_fitness > last_best_fitness:
            last_best_fitness = best_fitness
            stagnation_count = 0
            mutation_prob = initial_mutation_prob  # resetowanie prawdopodobieństwa

            # Aktualizacja najlepszych globalnych wartości
            best_overall_fitness = best_fitness
            best_index = fitness_scores.index(best_fitness)
            best_overall_program = population[best_index]

            # Dodane: Wypisz kod najlepszego programu w bieżącym pokoleniu
            best_program_code = generate_code(best_overall_program)
            print(f"  Najlepszy program w pokoleniu {generation}:\n{best_program_code}\n")

        else:
            stagnation_count += 1
            if stagnation_count >= stagnation_threshold:
                mutation_prob = high_mutation_prob
                print(
                    f"Stagnacja wykryta w pokoleniu {generation}. Zwiększono prawdopodobieństwo mutacji do {mutation_prob}.")

        if generation != 0 and best_fitness == 1.0:
            print("Znaleziono idealny program spełniający warunki!")
            break

        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = gp.tournament_selection(population, fitness_function, TOURNAMENT_SIZE)
            parent2 = gp.tournament_selection(population, fitness_function, TOURNAMENT_SIZE)

            chance = random.random()
            if chance < 0.2:
                offspring1 = gp.mutate(parent1)
                offspring2 = gp.mutate(parent2)
            elif chance < 0.8:
                offspring1, offspring2 = gp.crossover(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2

            new_population.extend([offspring1, offspring2])

        population = new_population[:POPULATION_SIZE]

    # Zapisywanie wyników po zakończeniu pętli, niezależnie od znalezienia idealnego programu
    result = {
        "test_name": test_name,
        "target_number": target_number,
        "found_generation": None if best_overall_fitness < 1.0 else generation,
        "best_program_code": generate_code(best_overall_program) if best_overall_program else None,
        "best_program_serial": gp.serialize(best_overall_program) if best_overall_program else None,
        "best_fitness": best_overall_fitness,
        "evolution_history": history
    }
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    print(f"Wyniki zapisane w pliku: {output_json}")


if __name__ == "__main__":
    main()
