import json
from AST.minilang_gp import MiniLangGP, generate_code


def main():
    path = "../example_system_tests/test_results/1_3_A1.json"

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku: {e}")
        return

    gp = MiniLangGP(max_depth=5)

    best_program_serial = data.get("best_program")
    if not best_program_serial:
        print("Brak klucza 'best_program' w JSON.")
        return

    print("Best program:\n")
    print(best_program_serial)

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
