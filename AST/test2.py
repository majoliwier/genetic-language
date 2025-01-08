from AST.MiniLangInterpreter import MiniLangInterpreter
from AST.minilang_gp import generate_code, MiniLangGP


def main():
    gp = MiniLangGP(max_depth=3)

    example_program = gp.generate_random_program()

    interpreter = MiniLangInterpreter(max_loop_iterations=1000, max_execution_time=3)

    interpreter.execute_program(example_program)

    print("Output buffer:", interpreter.output_buffer)

    print("Variables:", interpreter.variables)

    print("\nGenerated Code:")
    print(generate_code(example_program))


if __name__ == "__main__":
    main()
