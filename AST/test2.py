from AST.MiniLangInterpreter import MiniLangInterpreter, advanced_fitness_function
from AST.minilang_gp import generate_code, MiniLangGP


def main():
    gp = MiniLangGP(max_depth=5)

    example_program = gp.generate_random_program()

    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)

    interpreter.execute_program(example_program)

    print("Output buffer:", interpreter.output_buffer)

    print("Variables:", interpreter.variables)

    print("\nGenerated Code:")
    print(generate_code(example_program))

    test_data = {
        "inputs": [
            {"var_0": 10, "var_1": 20},
            {"var_0": 5, "var_1": 15}
        ],
        "expected_outputs": [30, 20]
    }

    fitness_score = advanced_fitness_function(example_program, test_data)
    print(f"\nFitness Score: {fitness_score}")


if __name__ == "__main__":
    main()
