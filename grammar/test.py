from grammar.minilang_gp import MiniLangGP, generate_code

gp = MiniLangGP(max_depth=2)

population_size = 2

population = [gp.generate_random_program() for _ in range(population_size)]

for individual in range(population_size):
    print("Program numer: ", individual+1)
    print(generate_code(population[individual]))

child1, child2 = gp.crossover(population[0], population[1])
print("child1")
print(generate_code(child1))
print("child2")
print(generate_code(child2))

# child123 = gp.serialize(child1)
# print(child123)
