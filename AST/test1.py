from AST.minilang_gp import MiniLangGP, generate_code
from utilities.graph import draw_tree

gp = MiniLangGP(max_depth=4)

population_size = 10

population = [gp.generate_random_program() for _ in range(population_size)]

for individual in range(population_size):
    print("Program numer: ", individual+1)
    print(generate_code(population[individual]))
    draw_tree(population[individual])

