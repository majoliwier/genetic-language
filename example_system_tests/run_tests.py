from AST.minilang_gp import MiniLangGP, generate_code
from fitness_functions import (
    fitness_1_1_A,
    fitness_1_1_B,
    fitness_1_1_C,
    fitness_1_1_D,
    fitness_1_1_E,
    fitness_1_1_F,
    fitness_1_2_A,
    fitness_1_2_B,
    fitness_1_2_C,
    fitness_1_2_D,
    fitness_1_2_E,
    fitness_1_3_A,
    fitness_1_3_B,
    fitness_1_4_A,
    fitness_1_4_B
)
import random
import json
import os
from utilities.graph import draw_tree_to_file


def run_gp_test(gp, fitness_func, task_name, population_size=100, generations=100, tournament_size=3):
    population = gp.generate_initial_population(population_size)
    results = {
        "task_name": task_name,
        "best_program": None,
        "fitness_score": None,
        "generation_found": None,
        "generations": []
    }

    best_program_node = None

    for generation in range(generations):
        fitness_scores = [fitness_func(prog) for prog in population]
        best_fitness = max(fitness_scores)
        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        results["generations"].append({
            "generation": generation + 1,
            "best_fitness": best_fitness,
            "average_fitness": avg_fitness
        })

        print(f"Zadanie {task_name} - Generacja {generation + 1}:")
        print(f"  Najlepsze przystosowanie: {best_fitness:.4f}")
        print(f"  Średnie przystosowanie: {avg_fitness:.4f}")

        if best_fitness == 1.0:
            best_program = max(population, key=fitness_func)
            results["best_program"] = generate_code(best_program)
            results["fitness_score"] = best_fitness
            results["generation_found"] = generation + 1
            print(f"  Idealny program znaleziony w generacji {generation + 1}:")
            print(results["best_program"])
            best_program_node = best_program
            break

        new_population = []

        while len(new_population) < population_size * 2:
            parent1 = gp.tournament_selection(population, fitness_func, tournament_size)
            parent2 = gp.tournament_selection(population, fitness_func, tournament_size)

            chance = random.random()
            if chance < 0.2:
                offspring1 = gp.mutate(parent1)
                offspring2 = gp.mutate(parent2)
            elif chance < 0.8:
                offspring1, offspring2 = gp.crossover(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2

            new_population.extend([offspring1, offspring2])

        fitness_scores = [fitness_func(prog) for prog in new_population]
        fitness_program_pairs = list(zip(fitness_scores, new_population))
        fitness_program_pairs.sort(reverse=True, key=lambda x: x[0])
        sorted_population = [prog for fitness, prog in fitness_program_pairs]
        population = sorted_population[:population_size]

    if results["best_program"] is None:
        best_program = max(population, key=fitness_func)
        results["best_program"] = generate_code(best_program)
        results["fitness_score"] = max(fitness_scores)
        results["generation_found"] = generations
        print(f"  Najlepszy program po {generations} generacjach:")
        print(results["best_program"])
        best_program_node = best_program

    save_results_to_json(results, task_name)

    if best_program_node:
        graphs_dir = os.path.join("test_results", "graphs")
        if not os.path.exists(graphs_dir):
            os.makedirs(graphs_dir)
        graph_file = os.path.join(graphs_dir, f"{task_name.replace('.', '_')}.png")
        draw_tree_to_file(best_program_node, graph_file)
        print(f"  Graf AST zapisany w pliku: {graph_file}")

    return best_program


def save_results_to_json(results, task_name):
    output_dir = "test_results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = f"{task_name.replace('.', '_')}.json"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print(f"  Wyniki zapisane w pliku: {file_path}")


def main():
    gp = MiniLangGP(max_depth=10)

    test_cases = {
        "1.1.A": fitness_1_1_A,
        "1.1.B": fitness_1_1_B,
        "1.1.C": fitness_1_1_C,
        "1.1.D": fitness_1_1_D,
        "1.1.E": fitness_1_1_E,
        "1.1.F": fitness_1_1_F,
        "1.2.A": fitness_1_2_A,
        "1.2.B": fitness_1_2_B,
        "1.2.C": fitness_1_2_C,
        "1.2.D": fitness_1_2_D,
        "1.2.E": fitness_1_2_E,
        "1.3.A": fitness_1_3_A,
        "1.3.B": fitness_1_3_B,
        "1.4.A": fitness_1_4_A,
        "1.4.B": fitness_1_4_B
    }

    results_summary = {}

    for task_name, fitness_func in test_cases.items():
        print(f"\n--- Rozpoczynanie testu dla zadania {task_name} ---")
        best_program = run_gp_test(
            gp=gp,
            fitness_func=fitness_func,
            task_name=task_name,
            population_size=100,
            generations=100,
            tournament_size=3
        )
        results_summary[task_name] = best_program

    summary_path = os.path.join("test_results", "summary.json")
    with open(summary_path, 'w', encoding='utf-8') as f:
        summary_data = {task: generate_code(prog) for task, prog in results_summary.items()}
        json.dump(summary_data, f, indent=4, ensure_ascii=False)

    print("\n=== Podsumowanie Testów Zapisane w 'test_results/summary.json' ===")


if __name__ == "__main__":
    main()
