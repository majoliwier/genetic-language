import json
from AST.minilang_gp import MiniLangGP, generate_code


def main():
    path = "/Users/amika/Documents/projects-uni/genetic-language/fitness_tests/results/evolution_history_1_2A.json"

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku: {e}")
        return

    gp = MiniLangGP(max_depth=5)

    best_program_serial = data.get("best_program_serial")
    if not best_program_serial:
        print("Brak klucza 'best_program' w JSON.")
        return

    try:
        program_node = gp.deserialize(best_program_serial)
    except Exception as e:
        print(f"Błąd podczas deserializacji programu: {e}")
        return

    code = generate_code(program_node)

    print(f"Task: {data.get('task_name', 'Nieznane zadanie')}")
    print(f"Fitness score: {data.get('fitness_score', 'Brak danych')}")
    print("Best program:\n")
    print(code)


if __name__ == "__main__":
    main()
