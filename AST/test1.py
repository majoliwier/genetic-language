from AST.minilang_gp import MiniLangGP, generate_code
from utilities.graph import draw_tree

gp = MiniLangGP(max_depth=1)

population_size = 2

population = gp.generate_initial_population(population_size)

for individual in range(population_size):
    print("Program numer: ", individual+1)
    print(generate_code(population[individual]))
    draw_tree(population[individual])

# code = """{"type": "program", "value": "", "children": [{"type": "ioStatement", "value": "output", "children": [{"type": "expression", "value": "&&", "children": [{"type": "INT", "value": "22", "children": []}, {"type": "INT", "value": "28", "children": []}]}]}, {"type": "assignStatement", "value": "=", "children": [{"type": "ID", "value": "var_3", "children": []}, {"type": "expression", "value": "||", "children": [{"type": "expression", "value": "*", "children": [{"type": "ID", "value": "var_3", "children": []}, {"type": "FLOAT", "value": "29.65", "children": []}]}, {"type": "FLOAT", "value": "97.86", "children": []}]}]}, {"type": "assignStatement", "value": "=", "children": [{"type": "ID", "value": "var_5", "children": []}, {"type": "ID", "value": "var_8", "children": []}]}, {"type": "assignStatement", "value": "=", "children": [{"type": "ID", "value": "var_6", "children": []}, {"type": "FLOAT", "value": "66.41", "children": []}]}, {"type": "assignStatement", "value": "=", "children": [{"type": "ID", "value": "var_8", "children": []}, {"type": "expression", "value": "<=", "children": [{"type": "expression", "value": "*", "children": [{"type": "INT", "value": "93", "children": []}, {"type": "ID", "value": "var_5", "children": []}]}, {"type": "INT", "value": "17", "children": []}]}]}, {"type": "ioStatement", "value": "input", "children": [{"type": "ID", "value": "var_6", "children": []}]}]}"""

# programm = gp.deserialize(code)
# print(generate_code(programm))
# draw_tree(programm)


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