from grammar.minilang_gp import Node
from minilang_gp import MiniLangGP
import random


def example_fitness_function(program: 'Node') -> float:
    return random.random()


def generate_code(node: 'Node', indent: int = 0) -> str:
    indent_str = "    " * indent
    code = ""

    if node.type == 'block':
        code += indent_str + "{\n"
        for child in node.children:
            code += generate_code(child, indent + 1)
        code += indent_str + "}\n"
    elif node.type == 'assign':
        lhs = node.children[0].value
        rhs = generate_code(node.children[1])
        code += indent_str + f"{lhs} = {rhs};\n"
    elif node.type == 'while':
        condition = generate_code(node.children[0])
        body = generate_code(node.children[1], indent)
        code += indent_str + f"while ({condition}) {body}"
    elif node.type == 'if':
        condition = generate_code(node.children[0])
        if_body = generate_code(node.children[1], indent)
        code += indent_str + f"if ({condition}) {if_body}"
        if len(node.children) > 2:
            else_body = generate_code(node.children[2], indent)
            code += indent_str + f"else {else_body}"
    elif node.type == 'io':
        if node.value == 'input':
            var_name = node.children[0].value
            code += indent_str + f"input({var_name});\n"
        else:
            expr = generate_code(node.children[0])
            code += indent_str + f"output({expr});\n"
    elif node.type == 'break':
        code += indent_str + "break;\n"
    elif node.type == 'continue':
        code += indent_str + "continue;\n"
    elif node.type == 'expression':
        left = generate_code(node.children[0])
        right = generate_code(node.children[1])
        code += f"({left} {node.value} {right})"
    elif node.type == 'int' or node.type == 'float':
        code += node.value
    elif node.type == 'id':
        code += node.value
    else:
        for child in node.children:
            code += generate_code(child, indent)
    return code


def main():
    gp = MiniLangGP(max_depth=5, min_depth=2)

    population_size = 10
    generations = 10
    tournament_size = 2

    population = [gp.generate_random_program() for _ in range(population_size)]

    print("\nPrzykład generowanego programu:")
    for i in range(generations):
        print(f"Generacja {i}:")
        program = population[i]
        code = generate_code(program)
        print(code)


if __name__ == "__main__":
    main()
