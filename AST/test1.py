from AST.minilang_gp import MiniLangGP, generate_code
from utilities.graph import draw_tree

gp = MiniLangGP(max_depth=3)

population_size = 2

population = gp.generate_initial_population(population_size)

for individual in range(population_size):
    print("Program numer: ", individual+1)
    print(generate_code(population[individual]))
    draw_tree(population[individual])

newbaby1 = gp.mutate(population[0])
newbaby2 = gp.mutate(population[1])
print("mutant 1")
print(generate_code(newbaby1))
draw_tree(newbaby1)
print("mutant 2")
print(generate_code(newbaby2))
draw_tree(newbaby2)

# newbaby1,newbaby2 = gp.crossover(population[0], population[1])
# print("miks 1")
# print(generate_code(newbaby1))
# draw_tree(newbaby1)
# print("miks 2")
# print(generate_code(newbaby2))
# draw_tree(newbaby2)