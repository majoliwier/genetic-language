from grammar.minilang_gp import MiniLangGP, generate_code


gp = MiniLangGP(max_depth=3, min_depth=1)

population_size = 100

population = [gp.generate_random_program() for _ in range(population_size)]

for individual in range(population_size):
    print("Program numer: ", individual+1)
    print(generate_code(population[individual]))
